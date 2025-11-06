import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
import time
import argparse
import sys
from typing import Optional, Dict, Any, List
import io
import os
from datetime import datetime
import traceback
from rag_api_client import RAGApiClient

# Chunking configuration for MCP RAG
CHUNKER = 'recursive'
CHUNK_SIZE = 1024
CHUNK_OVERLAP_PERCENTAGE = 20.0

# Manifest file name (stored under docs/<product>/<version>/)
MANIFEST_FILENAME = 'manifest.json'
# Error log file name
ERROR_LOG_FILENAME = 'crawl_errors.log'

# Retry configuration
MAX_RETRIES = 10
# Retry delays: immediate, then 1m, 3m, 5m, 10m, then 15m max for remaining attempts
RETRY_DELAYS = [0, 60, 180, 300, 600, 900, 900, 900, 900, 900]


def _manifest_path(base_dir: Path) -> Path:
    return base_dir / MANIFEST_FILENAME


def _error_log_path(base_dir: Path) -> Path:
    return base_dir / ERROR_LOG_FILENAME


def log_error(base_dir: Path, url: str, error: Exception, context: str = "") -> None:
    """Log error to file with timestamp and full traceback."""
    log_path = _error_log_path(base_dir)
    timestamp = datetime.now().isoformat()
    
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*80}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"URL: {url}\n")
        if context:
            f.write(f"Context: {context}\n")
        f.write(f"Error Type: {type(error).__name__}\n")
        f.write(f"Error Message: {str(error)}\n")
        f.write(f"\nTraceback:\n")
        f.write(traceback.format_exc())
        f.write(f"{'='*80}\n")


def retry_request_with_backoff(
    url: str,
    base_dir: Optional[Path] = None,
    context: str = "",
    **kwargs
) -> requests.Response:
    """Make HTTP request with exponential backoff retry logic.
    
    Retry schedule:
    - Attempt 1: immediate (0s)
    - Attempt 2: 60s (1 minute)
    - Attempt 3: 180s (3 minutes)
    - Attempt 4: 300s (5 minutes)
    - Attempt 5: 600s (10 minutes)
    - Attempts 6-10: 900s (15 minutes max)
    
    Args:
        url: URL to request
        base_dir: Optional base directory for error logging
        context: Optional context string for error logging
        **kwargs: Additional arguments to pass to requests.get()
    
    Returns:
        requests.Response object
    
    Raises:
        requests.RequestException: If all retries are exhausted
    """
    last_exception = None
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, **kwargs)
            # Check for HTTP errors (4xx, 5xx) - these might be retryable too
            response.raise_for_status()
            return response
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
            last_exception = e
            
            # Log error
            if base_dir is not None:
                log_error(base_dir, url, e, f"{context} (Attempt {attempt + 1}/{MAX_RETRIES})")
            
            # If this was the last attempt, don't wait
            if attempt == MAX_RETRIES - 1:
                break
            
            # Get delay for this attempt
            delay = RETRY_DELAYS[attempt] if attempt < len(RETRY_DELAYS) else RETRY_DELAYS[-1]
            
            if delay > 0:
                delay_minutes = delay / 60
                print(f"    ⚠️ Connection error (attempt {attempt + 1}/{MAX_RETRIES}): {type(e).__name__}")
                print(f"    ⏳ Waiting {delay_minutes:.1f} minutes before retry...")
                time.sleep(delay)
            else:
                print(f"    ⚠️ Connection error (attempt {attempt + 1}/{MAX_RETRIES}): {type(e).__name__}")
                print(f"    🔄 Retrying immediately...")
    
    # All retries exhausted
    if base_dir is not None:
        log_error(base_dir, url, last_exception, f"{context} (All {MAX_RETRIES} attempts exhausted)")
    
    raise last_exception


def load_manifest(base_dir: Path, product: str, version: str) -> Dict[str, Any]:
    """Load or initialize a manifest JSON that tracks per-URL progress.

    The manifest structure:
    {
        "product": str,
        "version": str,
        "created_at": iso8601,
        "updated_at": iso8601,
        "items": {
            source_url: {
                "filename": str,
                "local_path": str,
                "section": str,
                "is_downloaded": bool,
                "is_uploaded": bool
            }
        }
    }
    """
    path = _manifest_path(base_dir)
    now_iso = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
            import json
            manifest = json.loads(data) if data else {}
            if not isinstance(manifest, dict):
                manifest = {}
        except Exception:
            manifest = {}
    else:
        manifest = {}

    if 'product' not in manifest:
        manifest['product'] = product
    if 'version' not in manifest:
        manifest['version'] = version
    if 'created_at' not in manifest:
        manifest['created_at'] = now_iso
    if 'items' not in manifest or not isinstance(manifest['items'], dict):
        manifest['items'] = {}
    manifest['updated_at'] = now_iso
    return manifest


def save_manifest_atomic(base_dir: Path, manifest: Dict[str, Any]) -> None:
    """Write manifest to disk atomically (write .tmp then rename)."""
    import json
    path = _manifest_path(base_dir)
    tmp_path = path.with_suffix(path.suffix + '.tmp')
    manifest['updated_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, path)


def update_manifest_entry(
    base_dir: Path,
    manifest: Dict[str, Any],
    *,
    source_url: str,
    filename: str,
    local_path: str,
    section: str,
    is_downloaded: Optional[bool] = None,
    is_uploaded: Optional[bool] = None,
) -> None:
    items = manifest.setdefault('items', {})
    entry = items.get(source_url, {})
    entry['filename'] = filename
    entry['local_path'] = local_path
    entry['section'] = section
    if is_downloaded is not None:
        entry['is_downloaded'] = bool(is_downloaded)
    if is_uploaded is not None:
        entry['is_uploaded'] = bool(is_uploaded)
    # Defaults
    if 'is_downloaded' not in entry:
        entry['is_downloaded'] = False
    if 'is_uploaded' not in entry:
        entry['is_uploaded'] = False
    items[source_url] = entry
    save_manifest_atomic(base_dir, manifest)


def _parse_front_matter(filepath: Path) -> Optional[Dict[str, str]]:
    """Parse YAML front matter from a markdown file. Returns dict with metadata or None."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        # Split on '---\n' delimiter
        parts = content.split('\n---\n', 1)
        if len(parts) < 2:
            return None
        
        front_matter_text = parts[0].lstrip('---').strip()
        metadata = {}
        
        # Simple YAML parser for key: value pairs
        for line in front_matter_text.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                metadata[key] = value
        
        return metadata if metadata else None
    except Exception:
        return None


def rebuild_manifest_from_existing_files(
    base_dir: Path,
    manifest: Dict[str, Any],
    *,
    client: Optional[RAGApiClient] = None,
    collection_id: Optional[int] = None,
) -> int:
    """Scan existing .md files in base_dir and add them to manifest.
    
    Returns the number of files added/updated in the manifest.
    """
    added_count = 0
    items = manifest.setdefault('items', {})
    
    # Find all .md files recursively
    for md_file in base_dir.rglob('*.md'):
        # Skip manifest itself if somehow it's a .md
        if md_file.name == MANIFEST_FILENAME.replace('.json', '.md'):
            continue
        
        # Parse front matter
        metadata = _parse_front_matter(md_file)
        if not metadata:
            continue
        
        source_url = metadata.get('source_url')
        if not source_url:
            continue
        
        # If already in manifest, skip (don't overwrite)
        if source_url in items:
            continue
        
        section = metadata.get('section', 'unknown')
        filename = md_file.name
        local_path = str(md_file)
        
        # Check if uploaded by querying server
        is_uploaded = False
        if client is not None and collection_id is not None:
            existing = find_document_in_collection_by_filename(client, collection_id, filename)
            if existing is not None:
                status = existing.get('status')
                if status == 'completed':
                    is_uploaded = True
        
        # Add to manifest
        items[source_url] = {
            'filename': filename,
            'local_path': local_path,
            'section': section,
            'is_downloaded': True,  # File exists, so it's downloaded
            'is_uploaded': is_uploaded,
        }
        added_count += 1
    
    # Save manifest if we added anything
    if added_count > 0:
        save_manifest_atomic(base_dir, manifest)
    
    return added_count


def get_or_create_collection(client: RAGApiClient, name: str) -> int:
    """Return collection id by name, creating it if missing."""
    # Try to find existing collection by name (paginate conservatively)
    skip = 0
    limit = 100
    while True:
        resp = client.list_collections(skip=skip, limit=limit)
        collections = resp.get('collections', []) if isinstance(resp, dict) else []
        for c in collections:
            if c.get('name') == name:
                return int(c['id'])
        total = resp.get('total', 0)
        skip += limit
        if skip >= total:
            break

    created = client.create_collection(name=name, description=f"Auto-created for {name}", is_public=True)
    return int(created['id'])


def find_document_in_collection_by_filename(
    client: RAGApiClient, collection_id: int, filename: str
) -> Optional[Dict[str, Any]]:
    """Return the document dict from a collection by filename if present, else None."""
    skip = 0
    limit = 100
    target = filename.strip().lower()
    while True:
        docs = client.get_collection_documents(collection_id=collection_id, skip=skip, limit=limit)
        if not isinstance(docs, list) or not docs:
            break
        for d in docs:
            fname = str(d.get('filename', '')).strip().lower()
            if fname == target:
                return d
        if len(docs) < limit:
            break
        skip += limit
    return None


def upload_markdown_and_assign(
    client: RAGApiClient,
    markdown_path: str,
    collection_id: int,
) -> Optional[int]:
    """Upload a markdown file, wait until processed, then assign to collection.

    Returns processed document_id. Raises RuntimeError on failure.
    """
    # Read file and strip front matter (YAML between leading '---' blocks)
    with open(markdown_path, 'r', encoding='utf-8') as f:
        text = f.read()

    def _strip_front_matter(s: str) -> str:
        if s.startswith('---'):
            parts = s.split('\n---\n', 1)
            if len(parts) == 2:
                # If it starts with '---', the first delimiter may be just '---\n...\n---\n'
                # Handle also a possible trailing newline
                remainder = parts[1]
                return remainder.lstrip('\n')
        return s

    cleaned = _strip_front_matter(text)

    # Prepare multipart upload with cleaned content
    filename = os.path.basename(markdown_path)
    files = {
        'file': (filename, io.BytesIO(cleaned.encode('utf-8')), 'text/markdown')
    }
    data: Dict[str, Any] = {
        'chunker': CHUNKER,
        'chunk_size': CHUNK_SIZE,
        'chunk_overlap_percentage': CHUNK_OVERLAP_PERCENTAGE,
        'process_immediately': True,
    }

    resp = client.session.post(
        url=f"{client.base_url}/documents/upload",
        data=data,
        files=files,
        timeout=client.timeout_seconds,
    )
    # If duplicate (already exists), skip gracefully
    if resp.status_code == 409:
        print("    ⊘ Skipping upload (duplicate on server)")
        return None

    upload = resp.json() if resp.content else {}
    if isinstance(upload, dict):
        detail = str(upload.get('detail', '')).lower()
        if '409' in detail or 'duplicate' in detail or 'already exists' in detail:
            print("    ⊘ Skipping upload (duplicate reported)")
            return None

    # Determine document_id from possible response shapes
    document_id: Optional[int] = None
    if isinstance(upload, dict):
        if 'id' in upload:  # DocumentResponse
            document_id = int(upload['id'])
        elif 'document_id' in upload:  # AsyncUploadResponse
            document_id = int(upload['document_id'])
        elif 'results' in upload:  # MultipleFileUploadResponse
            results: List[Dict[str, Any]] = upload.get('results', [])
            if results and results[0].get('document_id'):
                document_id = int(results[0]['document_id'])

    if document_id is None:
        raise RuntimeError(f"Upload did not return a document id: {upload}")

    # Poll until processed or failed
    max_wait_seconds = 600
    poll_interval = 2.0
    waited = 0.0
    last_status = None
    while waited <= max_wait_seconds:
        doc = client.get_document(document_id)
        last_status = doc.get('status') if isinstance(doc, dict) else None
        if last_status == 'completed':
            break
        if last_status == 'failed':
            raise RuntimeError(f"Document processing failed for id={document_id}")
        time.sleep(poll_interval)
        waited += poll_interval

    if last_status != 'completed':
        raise RuntimeError(f"Timeout waiting for processing document id={document_id}; last_status={last_status}")

    # Assign to collection
    client.assign_document_to_collections(document_id=document_id, collection_ids=[collection_id])
    return document_id

def extract_main_content(soup):
    """Extrae el contenido principal y lo convierte a markdown limpio"""
    content = soup.select_one('div.contentnode.parsys')
    
    if not content:
        return None
    
    # Eliminar la sección de links relacionados
    for related in content.select('div.linklist.relatedlinks'):
        related.decompose()
    
    # Limpiar divs innecesarios
    for div in content.find_all('div', style='display: inline;'):
        div.unwrap()
    
    markdown = md(
        str(content),
        heading_style="ATX",
        bullets="-",
        strip=['script', 'style']
    )
    
    return markdown

def extract_toc_from_json(base_url, toc_json_url=None, base_dir: Optional[Path] = None):
    """Extrae el TOC desde el JSON endpoint de Broadcom"""
    import json

    if not toc_json_url:
        # Construir URL del JSON TOC desde la base_url
        parsed = urlparse(base_url)
        path_parts = parsed.path.rstrip('.html').split('/')

        # Construir path del JSON TOC: /us/en/.../jcr:content.toc.html
        toc_path = '/'.join(path_parts) + '/jcr:content.toc.html'
        toc_json_url = urljoin(base_url, toc_path)

    try:
        response = retry_request_with_backoff(
            toc_json_url,
            base_dir=base_dir,
            context="Extracting TOC from JSON"
        )
        if response.status_code != 200:
            return []

        data = response.json()

        if not isinstance(data, list):
            return []

        # Aplanar la estructura jerárquica en una lista plana
        toc_items = []

        def flatten_toc(items, level=0):
            for item in items:
                title = item.get('title', '')
                link = item.get('link', '')

                if title and link:
                    full_url = urljoin(base_url, link)
                    toc_items.append({
                        'title': title,
                        'url': full_url,
                        'level': level,
                        'href': link
                    })

                # Procesar children recursivamente
                children = item.get('children', [])
                if children:
                    flatten_toc(children, level + 1)

        flatten_toc(data)
        return toc_items

    except Exception as e:
        print(f"    ⚠️ Error obteniendo TOC JSON: {e}")
        return []


def extract_toc_sidebar(soup, base_url, base_dir: Optional[Path] = None):
    """Extrae el TOC del sidebar (página de contenido)"""
    # Primero intentar obtener el TOC desde el JSON endpoint
    toc_items = extract_toc_from_json(base_url, base_dir=base_dir)

    if toc_items:
        return toc_items

    # Fallback: parsear HTML (código original)
    toc_div = soup.select_one('div.toc.tableofcontentsmod.tableofcontents')

    if not toc_div:
        return []

    toc_items = []

    # Buscar todos los links en el TOC
    for link in toc_div.find_all('a', class_='toc-title', href=True):
        title = link.get_text(strip=True)
        href = link['href']

        # Skip si no tiene título
        if not title:
            continue

        full_url = urljoin(base_url, href)

        # Determinar nivel de anidación
        level = 0
        parent = link.find_parent('li')
        while parent:
            parent = parent.find_parent('ul')
            if parent and 'tocList' not in parent.get('class', []):
                level += 1
                parent = parent.find_parent('li')
            else:
                break

        toc_items.append({
            'title': title,
            'url': full_url,
            'level': level,
            'href': href
        })

    return toc_items

def extract_landing_links(soup, base_url):
    """Extrae los links principales de una landing page"""
    landing_div = soup.select_one('div.toccontainer_landing')

    if not landing_div:
        return []

    landing_items = []

    # Buscar todos los tocitems
    for tocitem in landing_div.select('div.tocitem'):
        title_elem = tocitem.select_one('div.pagetitle')
        # Buscar el span.card-link con href en lugar de div.view-more a[href]
        link_elem = tocitem.select_one('span.card-link[href]')

        if title_elem and link_elem:
            title = title_elem.get_text(strip=True)
            href = link_elem.get('href', '')

            if href:
                full_url = urljoin(base_url, href)

                landing_items.append({
                    'title': title,
                    'url': full_url,
                    'href': href,
                    'type': 'landing_section'
                })

    return landing_items

def is_landing_page(soup):
    """Determina si es una landing page o página de contenido"""
    return soup.select_one('div.toccontainer_landing') is not None

def extract_metadata(soup, url):
    """Extrae producto, versión y sección de la página"""
    product = "unknown"
    version = "unknown"

    # Estrategia 1: Extraer del div.title-banner (más confiable)
    title_banner = soup.select_one('div.title-banner')
    if title_banner:
        title_text = title_banner.get_text(strip=True)
        print(f"  DEBUG: Title banner encontrado: '{title_text}'")

        # "VMware Tools 13.0.0.0" -> producto: VMware Tools, version: 13.0.0
        parts = title_text.split()
        version_found = False

        for i, part in enumerate(parts):
            if re.match(r'^\d+\.\d+', part):  # Detecta patrón de versión
                # Extraer nombre del producto (todas las palabras antes del número)
                product_words = parts[:i] if i > 0 else []
                if product_words:
                    # Convertir a formato slug: "VMware Tools" -> "vmware-tools"
                    product = '-'.join(product_words).lower()
                version = part
                version_found = True
                print(f"  DEBUG: Producto del banner: '{product}', Versión: '{version}'")
                break

        if not version_found and len(parts) >= 2:
            # Si no se encuentra versión, usar las primeras 2 palabras como producto
            product = '-'.join(parts[:2]).lower()
    
    # Estrategia 2: Extraer versión del URL si no se encontró en el banner
    if version == "unknown":
        url_parts = urlparse(url).path.split('/')
        print(f"  DEBUG: URL parts: {url_parts}")

        # /us/en/vmware-cis/vsphere/tools/13-0-0/...
        if len(url_parts) >= 7:
            url_version = url_parts[6] if len(url_parts) > 6 and url_parts[6] else "unknown"
            print(f"  DEBUG: Versión del URL: '{url_version}'")

            if url_version != "unknown" and url_version:
                version = url_version.replace('.html', '')
    
    # Estrategia 3: Breadcrumb como fallback
    if product == "unknown" or version == "unknown":
        breadcrumb = soup.select_one('nav.bc-nav')
        if breadcrumb:
            links = breadcrumb.find_all('a')
            print(f"  DEBUG: Breadcrumb links: {[l.get_text(strip=True) for l in links]}")
            
            if len(links) >= 2 and product == "unknown":
                product = links[0].get_text(strip=True).replace(' ', '_')
            if len(links) >= 3 and version == "unknown":
                version = links[2].get_text(strip=True).replace(' ', '_')
    
    # Limpiar nombres para filesystem (solo caracteres seguros)
    product = re.sub(r'[^\w\-]', '', product)  # Permitir guiones
    version = re.sub(r'[^\w\-\.]', '', version)  # Permitir guiones y puntos

    # Remover extensión .html del nombre de versión
    version = version.replace('.html', '').replace('html', '')

    print(f"  ✓ Metadata final - Producto: '{product}', Versión: '{version}'")

    return product, version

def get_base_path(url):
    """Extrae el path base del producto/versión para filtrar URLs"""
    parsed = urlparse(url)
    # Remover extensión .html antes de hacer el split
    path = parsed.path.rstrip('.html')
    parts = path.split('/')

    # Asumiendo estructura: /us/en/vmware-cis/vsphere/tools/13-0-0/...
    if len(parts) >= 7:
        return '/'.join(parts[:7])  # Incluye hasta la versión
    elif len(parts) >= 6:
        return '/'.join(parts[:6])
    elif len(parts) >= 5:
        return '/'.join(parts[:5])

    return path

def should_crawl_url(url, base_path):
    """Determina si una URL debe ser crawleada (mismo producto/versión)"""
    return base_path in url

def sanitize_filename(title):
    """Limpia el título para usarlo como nombre de archivo"""
    filename = re.sub(r'[^\w\s\-]', '', title)
    filename = re.sub(r'\s+', '_', filename)
    filename = filename.lower()
    filename = filename[:100]
    return filename + '.md'

def save_page(markdown_content, filepath, url="", product="", version="", section="", breadcrumb=None, *, client: Optional[RAGApiClient] = None, collection_id: Optional[int] = None, manifest: Optional[Dict[str, Any]] = None, base_dir_for_manifest: Optional[Path] = None):
    """Saves markdown content to a file with metadata and optionally uploads to MCP RAG.

    If `client` and `collection_id` are provided, the saved file is uploaded
    to the RAG server with configured chunking, waits until processed, and is
    assigned to the collection. Any failure raises and should stop the crawl.
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # If file exists locally, ensure it also exists remotely (in the target collection)
    if filepath.exists():
        print(f"    ⊘ Exists locally: {filepath.name} (verifying remote)")
        if client is not None and collection_id is not None:
            existing = find_document_in_collection_by_filename(client, collection_id, filepath.name)
            if existing is not None:
                status = existing.get('status')
                doc_id = int(existing.get('id')) if existing.get('id') is not None else None
                if status == 'completed':
                    print(f"    ⊘ Remote already ingested (doc_id={doc_id}), skipping upload")
                    return
                elif status == 'processing':
                    print("    … Remote processing in progress, waiting until completion")
                    # Poll by id until completed/failed
                    if doc_id is not None:
                        max_wait_seconds = 600
                        poll_interval = 2.0
                        waited = 0.0
                        last_status = status
                        while waited <= max_wait_seconds:
                            doc = client.get_document(doc_id)
                            last_status = doc.get('status') if isinstance(doc, dict) else None
                            if last_status == 'completed':
                                print(f"    ✓ Remote completed (doc_id={doc_id})")
                                return
                            if last_status == 'failed':
                                print("    ✗ Remote processing failed, will re-upload")
                                break
                            time.sleep(poll_interval)
                            waited += poll_interval
                        if last_status == 'completed':
                            return
                        # else fallthrough to re-upload
                else:
                    print("    … Remote not completed, will (re)upload")
            else:
                print("    … Not found remotely, will upload")
        else:
            # No client/collection context → skip to avoid duplicate local writes
            return

    # Build metadata header
    metadata_lines = []
    if url:
        metadata_lines.append(f"source_url: {url}")
    if product:
        metadata_lines.append(f"product: {product}")
    if version:
        metadata_lines.append(f"version: {version}")
    if section:
        metadata_lines.append(f"section: {section}")
    if breadcrumb and len(breadcrumb) > 0:
        # Create breadcrumb path
        breadcrumb_str = " > ".join(breadcrumb)
        metadata_lines.append(f"breadcrumb: {breadcrumb_str}")

    if metadata_lines:
        header = "---\n" + "\n".join(metadata_lines) + "\n---\n\n"
    else:
        header = ""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header + markdown_content)

    print(f"    ✓ Saved: {filepath.name}")

    # Update manifest: mark as downloaded
    if manifest is not None and base_dir_for_manifest is not None and url:
        update_manifest_entry(
            base_dir_for_manifest,
            manifest,
            source_url=url,
            filename=filepath.name,
            local_path=str(filepath),
            section=section,
            is_downloaded=True,
        )

    # Optional upload-and-assign step
    if client is not None and collection_id is not None:
        doc_id = upload_markdown_and_assign(client, str(filepath), collection_id)
        if doc_id is None:
            print("    ⊘ Skipped upload (duplicate)")
            if manifest is not None and base_dir_for_manifest is not None and url:
                update_manifest_entry(
                    base_dir_for_manifest,
                    manifest,
                    source_url=url,
                    filename=filepath.name,
                    local_path=str(filepath),
                    section=section,
                    is_uploaded=True,
                )
        else:
            print(f"    ✓ Uploaded and assigned document_id={doc_id}")
            if manifest is not None and base_dir_for_manifest is not None and url:
                update_manifest_entry(
                    base_dir_for_manifest,
                    manifest,
                    source_url=url,
                    filename=filepath.name,
                    local_path=str(filepath),
                    section=section,
                    is_uploaded=True,
                )

def crawl_section(section_url, base_dir, section_name, base_path, visited_urls, version_base_url=None, product="", version="", depth=0, *, client: Optional[RAGApiClient] = None, collection_id: Optional[int] = None, manifest: Optional[Dict[str, Any]] = None):
    """Crawls a specific section and all its sub-pages"""

    indent = "  " * depth

    if section_url in visited_urls:
        print(f"{indent}⊘ Already visited: {section_url}")
        return

    visited_urls.add(section_url)

    try:
        # Always download section page to get TOC (TOC might change)
        print(f"{indent}→ Downloading: {section_url}")
        response = retry_request_with_backoff(
            section_url,
            base_dir=base_dir,
            context=f"Downloading section: {section_name}"
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        # Clean section name
        clean_section_name = sanitize_filename(section_name).replace('.md', '')
        main_file = base_dir / f'{clean_section_name}.md'

        # Check if already downloaded (manifest + file exists) - skip saving but still extract TOC
        skip_save = False
        if manifest is not None:
            entry = manifest.get('items', {}).get(section_url)
            if entry and entry.get('is_downloaded') is True and main_file.exists():
                skip_save = True
                print(f"{indent}  ⊘ File already exists, skipping save (will check upload)")

        # Extract and save main section content (unless already saved)
        if not skip_save:
            content = extract_main_content(soup)
            if content:
                # Main section page - breadcrumb is just the section name
                save_page(
                    content,
                    main_file,
                    section_url,
                    product=product,
                    version=version,
                    section=section_name,
                    breadcrumb=[section_name],
                    client=client,
                    collection_id=collection_id,
                    manifest=manifest,
                    base_dir_for_manifest=base_dir,
                )
        else:
            # File exists but check if upload is needed
            if manifest is not None:
                entry = manifest.get('items', {}).get(section_url)
                if entry and entry.get('is_uploaded') is not True and client is not None and collection_id is not None:
                    # Re-read file and try to upload
                    with open(main_file, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    # Extract content without front matter for upload
                    if file_content.startswith('---'):
                        parts = file_content.split('\n---\n', 1)
                        if len(parts) == 2:
                            file_content = parts[1].lstrip('\n')
                    # Use save_page to handle upload (it will skip local write if exists)
                    save_page(
                        file_content,
                        main_file,
                        section_url,
                        product=product,
                        version=version,
                        section=section_name,
                        breadcrumb=[section_name],
                        client=client,
                        collection_id=collection_id,
                        manifest=manifest,
                        base_dir_for_manifest=base_dir,
                    )
        # Create subdirectory for sub-pages
        section_dir = base_dir / clean_section_name
        section_dir.mkdir(exist_ok=True)

        # Extract TOC from sidebar using version base URL
        # If not provided, use section URL
        toc_base_url = version_base_url if version_base_url else section_url
        toc_items = extract_toc_sidebar(soup, toc_base_url, base_dir=base_dir)
        print(f"{indent}  ✓ Found {len(toc_items)} pages in TOC")

        # Filter TOC to include only pages from this section
        # Extract section path (e.g., /release-notes/, /vmware-tools-administration/)
        section_path_parts = urlparse(section_url).path.split('/')
        section_identifier = None

        # Find section identifier (last part before .html)
        for part in reversed(section_path_parts):
            if part and part != '':
                # Remove .html if exists
                section_identifier = part.replace('.html', '')
                break

        # Filter toc_items for this section
        section_toc_items = []
        if section_identifier:
            for item in toc_items:
                item_path = urlparse(item['url']).path
                # Include if URL contains section identifier
                if f"/{section_identifier}/" in item_path or item_path.endswith(f"/{section_identifier}.html"):
                    section_toc_items.append(item)
        else:
            section_toc_items = toc_items

        print(f"{indent}  ✓ Filtered {len(section_toc_items)} pages for this section (out of {len(toc_items)} total)")

        # Process each page from filtered TOC
        for idx, item in enumerate(section_toc_items, 1):
            if item['url'] in visited_urls:
                continue

            if not should_crawl_url(item['url'], base_path):
                print(f"{indent}  ⊗ Out of scope: {item['title']}")
                continue

            print(f"{indent}  [{idx}/{len(section_toc_items)}] {item['title']}")

            visited_urls.add(item['url'])

            filename = sanitize_filename(item['title'])
            filepath = section_dir / filename

            # Check if already downloaded (manifest + file exists)
            skip_download = False
            if manifest is not None:
                entry = manifest.get('items', {}).get(item['url'])
                if entry and entry.get('is_downloaded') is True and filepath.exists():
                    skip_download = True
                    print(f"{indent}    ⊘ Already downloaded (manifest), skipping download")
                    # Check if upload is needed
                    if entry.get('is_uploaded') is not True and client is not None and collection_id is not None:
                        # Re-read file and try to upload
                        try:
                            with open(filepath, 'r', encoding='utf-8') as f:
                                file_content = f.read()
                            # Extract content without front matter for upload
                            if file_content.startswith('---'):
                                parts = file_content.split('\n---\n', 1)
                                if len(parts) == 2:
                                    file_content = parts[1].lstrip('\n')
                            # Build breadcrumb: Section > Page Title
                            page_breadcrumb = [section_name, item['title']]
                            save_page(
                                file_content,
                                filepath,
                                item['url'],
                                product=product,
                                version=version,
                                section=section_name,
                                breadcrumb=page_breadcrumb,
                                client=client,
                                collection_id=collection_id,
                                manifest=manifest,
                                base_dir_for_manifest=base_dir,
                            )
                        except Exception as e:
                            print(f"{indent}    ⚠️ Error re-uploading existing file: {e}")
                    else:
                        print(f"{indent}    ⊘ Already uploaded, skipping")
                elif entry and entry.get('is_uploaded') is True:
                    print(f"{indent}    ⊘ Already uploaded (manifest): {item['title']}")
                    continue

            if not skip_download:
                try:
                    page_response = retry_request_with_backoff(
                        item['url'],
                        base_dir=base_dir,
                        context=f"Downloading page: {item['title']} (section: {section_name})"
                    )
                    page_soup = BeautifulSoup(page_response.content, 'html.parser')

                    page_content = extract_main_content(page_soup)

                    if page_content:
                        # Save directly in section directory (flat)
                        # Build breadcrumb: Section > Page Title
                        page_breadcrumb = [section_name, item['title']]

                        save_page(
                            page_content,
                            filepath,
                            item['url'],
                            product=product,
                            version=version,
                            section=section_name,
                            breadcrumb=page_breadcrumb,
                            client=client,
                            collection_id=collection_id,
                            manifest=manifest,
                            base_dir_for_manifest=base_dir,
                        )

                    time.sleep(0.5)

                except Exception as e:
                    print(f"{indent}    ✗ Error: {e}")
                    # Stop on any failure to avoid partial ingestion
                    raise

    except Exception as e:
        print(f"{indent}✗ Error processing section {section_url}: {e}")
        raise

def print_toc_preview(start_url):
    """Shows a preview of what will be downloaded from the TOC"""
    print(f"\n{'='*70}")
    print(f"📋 TOC PREVIEW")
    print(f"{'='*70}")
    print(f"Fetching TOC from: {start_url}\n")

    try:
        # Download main page
        response = retry_request_with_backoff(
            start_url,
            base_dir=None,  # No base_dir in preview mode
            context="Preview: Downloading main page"
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract metadata
        product, version = extract_metadata(soup, start_url)
        base_path = get_base_path(start_url)

        print(f"\n{'='*70}")
        print(f"📦 Product: {product}")
        print(f"📌 Version: {version}")
        print(f"🔍 Base path: {base_path}")
        print(f"{'='*70}\n")

        # Check if landing page
        if not is_landing_page(soup):
            print("⚠️  This is a content page, not a landing page.")
            print("   Will extract TOC from sidebar...\n")

            toc_items = extract_toc_sidebar(soup, start_url, base_dir=None)

            print(f"📄 Found {len(toc_items)} pages in TOC:\n")
            for i, item in enumerate(toc_items[:20], 1):  # Show first 20
                indent = "  " * item.get('level', 0)
                print(f"  {i}. {indent}{item['title']}")

            if len(toc_items) > 20:
                print(f"\n  ... and {len(toc_items) - 20} more pages")

            print(f"\n{'='*70}")
            return

        # Landing page - extract sections
        landing_links = extract_landing_links(soup, start_url)

        if not landing_links:
            print("❌ No sections found on this landing page.")
            return

        print(f"📚 Found {len(landing_links)} main sections:\n")

        total_pages = 0

        # Get TOC for the whole documentation
        toc_items = extract_toc_from_json(start_url, base_dir=None)

        for idx, section in enumerate(landing_links, 1):
            print(f"\n{'─'*70}")
            print(f"📖 Section {idx}/{len(landing_links)}: {section['title']}")
            print(f"{'─'*70}")

            # Count pages for this section
            section_url = section['url']
            section_path_parts = urlparse(section_url).path.split('/')
            section_identifier = None

            for part in reversed(section_path_parts):
                if part and part != '':
                    section_identifier = part.replace('.html', '')
                    break

            # Filter TOC for this section
            section_pages = []
            if section_identifier and toc_items:
                for item in toc_items:
                    item_path = urlparse(item['url']).path
                    if f"/{section_identifier}/" in item_path or item_path.endswith(f"/{section_identifier}.html"):
                        section_pages.append(item)

            print(f"  📄 Pages to download: {len(section_pages)}")

            # Show first few pages as preview
            if section_pages:
                print(f"  Preview (first 5):")
                for i, page in enumerate(section_pages[:5], 1):
                    indent = "  " * page.get('level', 0)
                    print(f"    {i}. {indent}{page['title']}")

                if len(section_pages) > 5:
                    print(f"    ... and {len(section_pages) - 5} more")

            total_pages += len(section_pages)

        print(f"\n{'='*70}")
        print(f"📊 SUMMARY")
        print(f"{'='*70}")
        print(f"  Total sections: {len(landing_links)}")
        print(f"  Total pages to download: {total_pages}")
        print(f"  Estimated time: ~{total_pages * 0.5 / 60:.1f} minutes")
        print(f"  Output directory: docs/{product}/{version}/")
        print(f"{'='*70}\n")

    except Exception as e:
        print(f"\n❌ Error fetching TOC preview: {e}")
        import traceback
        traceback.print_exc()


def crawl_documentation(start_url, output_dir='docs', preview_only=False):
    """Main function that orchestrates the crawling process"""

    if preview_only:
        print_toc_preview(start_url)
        return

    print(f"\n{'='*70}")
    print(f"🕷️  BROADCOM DOCS CRAWLER")
    print(f"{'='*70}")
    print(f"Starting URL: {start_url}\n")

    visited_urls = set()

    # Create base directory first (needed for error logging)
    # We'll extract metadata after, but need base_dir for retry logging
    # So we'll do a preliminary download to get product/version
    print("📊 Extracting metadata...")
    try:
        response = retry_request_with_backoff(
            start_url,
            base_dir=None,  # Will be created after we know product/version
            context="Initial metadata extraction"
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        product, version = extract_metadata(soup, start_url)
    except Exception as e:
        # If we can't even get metadata, create a temp directory for error logging
        temp_base_dir = Path(output_dir) / "unknown" / "unknown"
        temp_base_dir.mkdir(parents=True, exist_ok=True)
        log_error(temp_base_dir, start_url, e, "Failed to extract metadata")
        raise

    base_path = get_base_path(start_url)

    print(f"\n{'='*70}")
    print(f"📦 Product: {product}")
    print(f"📌 Version: {version}")
    print(f"🔍 Base path: {base_path}")
    print(f"{'='*70}\n")

    # Create base directory
    base_dir = Path(output_dir) / product / version
    base_dir.mkdir(parents=True, exist_ok=True)

    # Re-download main page with proper base_dir for error logging
    response = retry_request_with_backoff(
        start_url,
        base_dir=base_dir,
        context="Downloading main page for crawling"
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    # Load or initialize manifest for this product/version
    manifest = load_manifest(base_dir, product, version)

    # Initialize RAG client and target collection
    api_key = os.environ.get('RAG_API_KEY', 'dev-secret-token')
    client = RAGApiClient(base_url='http://127.0.0.1:9000', api_key=api_key)
    collection_name = f"{product}-{version}"
    print(f"🔐 Using collection: {collection_name}")
    collection_id = get_or_create_collection(client, collection_name)
    print(f"✓ Collection id: {collection_id}")

    # Rebuild manifest from existing files (sync with what's already downloaded)
    print("📋 Scanning existing files to rebuild manifest...")
    added = rebuild_manifest_from_existing_files(base_dir, manifest, client=client, collection_id=collection_id)
    if added > 0:
        print(f"✓ Added {added} existing files to manifest")
    else:
        print("✓ Manifest is up to date")

    # Determine page type
    if is_landing_page(soup):
        print("✓ Page type: LANDING PAGE\n")

        # Extract main sections
        landing_links = extract_landing_links(soup, start_url)
        print(f"📚 Found {len(landing_links)} main sections:\n")

        for idx, section in enumerate(landing_links, 1):
            print(f"   {idx}. {section['title']}")

        print()

        # Crawl each section
        for idx, section in enumerate(landing_links, 1):
            print(f"\n{'─'*70}")
            print(f"📖 SECTION {idx}/{len(landing_links)}: {section['title']}")
            print(f"{'─'*70}")

            crawl_section(
                section['url'],
                base_dir,
                section['title'],
                base_path,
                visited_urls,
                version_base_url=start_url,
                product=product,
                version=version,
                depth=1,
                client=client,
                collection_id=collection_id,
                manifest=manifest,
            )

            time.sleep(1)
    else:
        print("✓ Page type: CONTENT PAGE\n")
        crawl_section(start_url, base_dir, "main", base_path, visited_urls, version_base_url=start_url, product=product, version=version, client=client, collection_id=collection_id, manifest=manifest)

    print(f"\n{'='*70}")
    print(f"✅ CRAWLING COMPLETED")
    print(f"{'='*70}")
    print(f"📊 Total pages downloaded: {len(visited_urls)}")
    print(f"📁 Files saved in: {base_dir}")
    print(f"{'='*70}\n")

def main():
    """Main entry point with argument parsing"""
    parser = argparse.ArgumentParser(
        description='Broadcom Documentation Crawler - Download and convert Broadcom docs to Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview TOC before downloading
  python broadcom_crawler.py https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html --preview

  # Download documentation
  python broadcom_crawler.py https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html

  # Download to custom directory
  python broadcom_crawler.py https://techdocs.broadcom.com/... --output my_docs

  # Interactive mode (preview + confirm)
  python broadcom_crawler.py https://techdocs.broadcom.com/... --interactive
        """
    )

    parser.add_argument(
        'url',
        help='URL of the Broadcom documentation page to crawl'
    )

    parser.add_argument(
        '-o', '--output',
        default='docs',
        help='Output directory for downloaded documentation (default: docs)'
    )

    parser.add_argument(
        '-p', '--preview',
        action='store_true',
        help='Show TOC preview without downloading'
    )

    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Show preview and ask for confirmation before downloading'
    )

    args = parser.parse_args()

    # Validate URL
    if not args.url.startswith('https://techdocs.broadcom.com/'):
        print("❌ Error: URL must be from techdocs.broadcom.com")
        sys.exit(1)

    # Preview only mode
    if args.preview:
        crawl_documentation(args.url, output_dir=args.output, preview_only=True)
        return

    # Interactive mode
    if args.interactive:
        crawl_documentation(args.url, output_dir=args.output, preview_only=True)

        print("\n" + "="*70)
        response = input("Do you want to proceed with the download? [y/N]: ")
        if response.lower() not in ['y', 'yes']:
            print("❌ Download cancelled.")
            return

        print("\n🚀 Starting download...\n")

    # Start crawling
    crawl_documentation(args.url, output_dir=args.output, preview_only=False)


if __name__ == "__main__":
    main()