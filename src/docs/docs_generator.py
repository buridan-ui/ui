from pathlib import Path
from typing import List

from src.mdparser import DelimiterParser
from src.wrappers.base.main import base
from src.types import RouteConfig

# Path to the top-level docs directory
DOCS_BASE_DIR = Path("docs")
# Path to the components directory for the DelimiterParser
COMPONENTS_DIR = "src/docs/components"

# Instantiate the parser with the dynamic load directory
md_parser = DelimiterParser(dynamic_load_dir=COMPONENTS_DIR)


def generate_docs_routes() -> List[RouteConfig]:
    """
    Scans the DOCS_BASE_DIR for markdown files, parses them, and
    generates a list of RouteConfig objects for dynamic page creation.
    """
    docs_routes = []

    if not DOCS_BASE_DIR.exists():
        print(f"Warning: Docs base directory not found: {DOCS_BASE_DIR}")
        return []

    for md_file_path in DOCS_BASE_DIR.glob("**/*.md"):
        # Calculate the relative path from DOCS_BASE_DIR
        relative_path = md_file_path.relative_to(DOCS_BASE_DIR)

        # Convert to URL path: e.g., getting_started/charting.md -> /getting-started/charting
        # Replace underscores with hyphens, remove .md extension
        url_path_parts = [part.replace("_", "-") for part in relative_path.parts]
        url_path = "/" + "/".join(url_path_parts).replace(".md", "")

        # Read the markdown content
        with open(md_file_path, "r") as f:
            md_content = f.read()

        # Generate the page component using the DelimiterParser
        @base(url=url_path, page_name=relative_path.stem.replace("_", " ").title())
        def doc_page_component(content=md_content):  # Capture md_content in closure
            return md_parser.parse_and_render(content)

        # Create a RouteConfig object
        docs_routes.append(
            RouteConfig(
                path=url_path,
                component=doc_page_component,
                title=relative_path.stem.replace("_", " ").title(),
            )
        )
    return docs_routes
