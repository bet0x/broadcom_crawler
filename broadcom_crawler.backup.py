import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
import time
import argparse
import sys

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

def extract_toc_from_json(base_url, toc_json_url=None):
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
        response = requests.get(toc_json_url)
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


def extract_toc_sidebar(soup, base_url):
    """Extrae el TOC del sidebar (página de contenido)"""
    # Primero intentar obtener el TOC desde el JSON endpoint
    toc_items = extract_toc_from_json(base_url)

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

def save_page(markdown_content, filepath, url="", product="", version="", section="", breadcrumb=None):
    """Saves markdown content to a file with metadata"""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

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

def crawl_section(section_url, base_dir, section_name, base_path, visited_urls, version_base_url=None, product="", version="", depth=0):
    """Crawls a specific section and all its sub-pages"""

    indent = "  " * depth

    if section_url in visited_urls:
        print(f"{indent}⊘ Already visited: {section_url}")
        return

    visited_urls.add(section_url)

    try:
        print(f"{indent}→ Downloading: {section_url}")
        response = requests.get(section_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Clean section name
        clean_section_name = sanitize_filename(section_name).replace('.md', '')

        # Extract and save main section content
        # Saved as <section_name>.md in the base directory
        content = extract_main_content(soup)
        if content:
            main_file = base_dir / f'{clean_section_name}.md'
            # Main section page - breadcrumb is just the section name
            save_page(content, main_file, section_url, product=product, version=version, section=section_name, breadcrumb=[section_name])
            # TODO: Chunk the content into smaller files via MCP RAG
        # Create subdirectory for sub-pages
        section_dir = base_dir / clean_section_name
        section_dir.mkdir(exist_ok=True)

        # Extract TOC from sidebar using version base URL
        # If not provided, use section URL
        toc_base_url = version_base_url if version_base_url else section_url
        toc_items = extract_toc_sidebar(soup, toc_base_url)
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

            try:
                page_response = requests.get(item['url'])
                page_soup = BeautifulSoup(page_response.content, 'html.parser')

                page_content = extract_main_content(page_soup)

                if page_content:
                    filename = sanitize_filename(item['title'])

                    # Save directly in section directory
                    # If you want to maintain hierarchy with subdirectories, add prefix based on level
                    # For now we save flat in the section folder
                    filepath = section_dir / filename

                    # Build breadcrumb: Section > Page Title
                    page_breadcrumb = [section_name, item['title']]

                    save_page(page_content, filepath, item['url'], product=product, version=version, section=section_name, breadcrumb=page_breadcrumb)

                time.sleep(0.5)

            except Exception as e:
                print(f"{indent}    ✗ Error: {e}")
                continue

    except Exception as e:
        print(f"{indent}✗ Error processing section {section_url}: {e}")

def print_toc_preview(start_url):
    """Shows a preview of what will be downloaded from the TOC"""
    print(f"\n{'='*70}")
    print(f"📋 TOC PREVIEW")
    print(f"{'='*70}")
    print(f"Fetching TOC from: {start_url}\n")

    try:
        # Download main page
        response = requests.get(start_url)
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

            toc_items = extract_toc_sidebar(soup, start_url)

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
        toc_items = extract_toc_from_json(start_url)

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

    # Download main page
    response = requests.get(start_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract metadata
    print("📊 Extracting metadata...")
    product, version = extract_metadata(soup, start_url)

    base_path = get_base_path(start_url)

    print(f"\n{'='*70}")
    print(f"📦 Product: {product}")
    print(f"📌 Version: {version}")
    print(f"🔍 Base path: {base_path}")
    print(f"{'='*70}\n")

    # Create base directory
    base_dir = Path(output_dir) / product / version
    base_dir.mkdir(parents=True, exist_ok=True)

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
                depth=1
            )

            time.sleep(1)
    else:
        print("✓ Page type: CONTENT PAGE\n")
        crawl_section(start_url, base_dir, "main", base_path, visited_urls, version_base_url=start_url, product=product, version=version)

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