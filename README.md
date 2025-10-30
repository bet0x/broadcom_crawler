# Broadcom Documentation Crawler

A Python-based web crawler designed to download and convert Broadcom technical documentation into clean, organized Markdown files.

## Features

- 🕷️ **Automated Crawling**: Recursively crawls Broadcom documentation pages
- 📄 **Markdown Conversion**: Converts HTML content to clean Markdown format
- 📁 **Organized Structure**: Creates hierarchical folder structure: `<PRODUCT>/<VERSION>/<CONTENT>`
- 🎯 **Smart Section Filtering**: Automatically detects and filters content by section
- 🔄 **TOC Extraction**: Extracts table of contents from dynamic JSON endpoints
- ⚡ **Rate Limiting**: Built-in delays to avoid overwhelming servers
- 📊 **Progress Tracking**: Real-time progress indicators during crawling

## Directory Structure

The crawler generates the following structure:

```
docs/
└── <product-name>/              # e.g., vmware-tools
    └── <version>/               # e.g., 13.0.0.0
        ├── section_name.md      # Main section page
        ├── section_name/        # Section sub-pages
        │   ├── page1.md
        │   ├── page2.md
        │   └── page3.md
        └── ...
```

### Example Output

```
docs/
└── vmware-tools/
    └── 13.0.0.0/
        ├── release_notes.md
        ├── release_notes/
        │   ├── vmware_tools_13050_release_notes.md
        │   ├── vmware_tools_13010_release_notes.md
        │   └── vmware_tools_13000_release_notes.md
        ├── vmware_tools_administration.md
        ├── vmware_tools_administration/
        │   ├── introduction_to_vmware_tools.md
        │   ├── installing_vmware_tools.md
        │   └── ... (60+ files)
        └── ...
```

## Requirements

- Python 3.7+
- Dependencies:
  - `requests` - HTTP library
  - `beautifulsoup4` - HTML parsing
  - `markdownify` - HTML to Markdown conversion
  - `lxml` - XML/HTML processing

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd broad-docs-crawler
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies using `uv` (recommended):
```bash
uv pip install requests beautifulsoup4 markdownify lxml
```

Or using standard pip:
```bash
pip install requests beautifulsoup4 markdownify lxml
```

## Usage

### Quick Start

```bash
# Show help
python broadcom_crawler.py --help

# Preview what will be downloaded (recommended first step)
python broadcom_crawler.py "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html" --preview

# Download documentation
python broadcom_crawler.py "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html"

# Interactive mode (preview + confirm before download)
python broadcom_crawler.py "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html" --interactive

# Download to custom directory
python broadcom_crawler.py "https://techdocs.broadcom.com/..." --output my_docs
```

### Command Line Options

```
usage: broadcom_crawler.py [-h] [-o OUTPUT] [-p] [-i] url

positional arguments:
  url                  URL of the Broadcom documentation page to crawl

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Output directory (default: docs)
  -p, --preview        Show TOC preview without downloading
  -i, --interactive    Show preview and ask for confirmation
```

### TOC Preview Feature

The `--preview` flag shows you exactly what will be downloaded **before** starting:

```bash
python broadcom_crawler.py "URL" --preview
```

**Preview Output:**
```
📦 Product: vmware-tools
📌 Version: 13.0.0.0

📚 Found 4 main sections:

📖 Section 1/4: Release Notes
  📄 Pages to download: 4
  Preview (first 5):
    1. Release Notes
    2.   VMware Tools 13.0.5.0 Release Notes
    ...

📊 SUMMARY
  Total sections: 4
  Total pages to download: 71
  Estimated time: ~0.6 minutes
  Output directory: docs/vmware-tools/13.0.0.0/
```

### Interactive Mode

Use `--interactive` to preview and confirm before downloading:

```bash
python broadcom_crawler.py "URL" --interactive
```

This will show the preview and ask:
```
Do you want to proceed with the download? [y/N]:
```

### Advanced Usage

You can also import and use the crawler programmatically:

```python
from broadcom_crawler import crawl_documentation

# Crawl a specific documentation URL
url = "https://techdocs.broadcom.com/us/en/<product>/<version>.html"
crawl_documentation(url, output_dir='my_docs')

# Preview only
crawl_documentation(url, preview_only=True)
```

### Example URLs

```bash
# VMware Tools 13.0.0
python broadcom_crawler.py "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0.html" --preview

# VMware vSphere 8.0
python broadcom_crawler.py "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-install/8-0.html" --preview
```

## How It Works

1. **Metadata Extraction**: Extracts product name and version from `div.title-banner`
2. **Page Type Detection**: Identifies landing pages vs. content pages
3. **Section Discovery**: Finds all main sections via `div.tocitem` elements
4. **TOC Retrieval**: Fetches dynamic table of contents from JSON endpoint
5. **Content Extraction**: Extracts main content from `div.contentnode.parsys`
6. **Markdown Conversion**: Converts HTML to clean Markdown format
7. **File Organization**: Saves files in organized directory structure

### Key Selectors

- **Product/Version**: `div.title-banner`
- **Landing Page**: `div.toccontainer_landing`
- **Section Links**: `span.card-link[href]`
- **Main Content**: `div.contentnode.parsys`
- **TOC JSON**: `/jcr:content.toc.html` endpoint

## Output Format

Each Markdown file includes rich metadata for RAG (Retrieval Augmented Generation) applications:

```yaml
---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html
product: vmware-tools
version: 13.0.0.0
section: Release Notes
breadcrumb: Release Notes > VMware Tools 13.0.5.0 Release Notes
---

# VMware Tools 13.0.5.0 Release Notes

Page content in clean Markdown format...
```

### Metadata Fields

- **source_url**: Original URL of the documentation page
- **product**: Product name extracted from page title (e.g., `vmware-tools`)
- **version**: Version number (e.g., `13.0.0.0`)
- **section**: Main section name (e.g., `Release Notes`)
- **breadcrumb**: Hierarchical path with `>` separator for context

### Benefits for RAG

- **Filter by product/version**: Easily scope your queries to specific products
- **Contextual understanding**: Breadcrumb provides hierarchical context
- **Source traceability**: Original URL for verification
- **Clean separation**: Section field for coarse filtering, breadcrumb for fine-grained context

### Example RAG Usage

When ingesting into a vector database (Pinecone, Weaviate, etc.):

```python
# Parse markdown frontmatter
import yaml

with open('docs/vmware-tools/13.0.0.0/release_notes/page.md', 'r') as f:
    content = f.read()
    # Extract frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        metadata = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()

# Use metadata for filtering/routing
doc_embedding = {
    'text': markdown_content,
    'metadata': {
        'product': metadata['product'],      # vmware-tools
        'version': metadata['version'],      # 13.0.0.0
        'section': metadata['section'],      # Release Notes
        'breadcrumb': metadata['breadcrumb'], # Full context
        'source_url': metadata['source_url']
    }
}

# Query with filters
# "Show me installation steps for VMware Tools 13.0"
results = vector_db.query(
    query_embedding,
    filter={
        'product': 'vmware-tools',
        'version': '13.0.0.0'
    }
)
```

## Configuration

### Rate Limiting

Adjust the delay between requests (default: 0.5 seconds):
```python
time.sleep(0.5)  # Line 367
```

Between sections (default: 1 second):
```python
time.sleep(1)  # Line 434
```

### Output Directory

Change the default output directory:
```python
crawl_documentation(url, output_dir='custom_output')
```

### Content Filtering

Modify `should_crawl_url()` to customize URL filtering:
```python
def should_crawl_url(url, base_path):
    """Determines if a URL should be crawled (same product/version)"""
    return base_path in url
```

## Limitations

- Only works with Broadcom techdocs.broadcom.com structure
- Requires JavaScript-generated TOC to be accessible via JSON endpoint
- Does not download images or other media files
- Rate limiting means large documentation sets take time to download

## Troubleshooting

### "No sections found"

- Verify the URL is a valid Broadcom documentation landing page
- Check if `div.toccontainer_landing` exists on the page

### "Out of scope" warnings

- The crawler filters URLs to stay within the same product/version
- Check `base_path` matches your expected URL pattern

### Missing content

- Verify `div.contentnode.parsys` selector matches the page structure
- Check if content is loaded dynamically via JavaScript

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - Feel free to use and modify as needed.

## Author

Built with ❤️ for easier access to Broadcom documentation.

---

**Note**: This tool is for personal/educational use. Please respect Broadcom's terms of service and rate limits when using this crawler.
# broadcom_crawler
