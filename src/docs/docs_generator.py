from pathlib import Path
from typing import List
import re
import os

from src.mdparser import DelimiterParser
from src.wrappers.base.main import base
from src.types import RouteConfig
from src.utils.text_helpers import slugify


# Path to the top-level docs directory
DOCS_BASE_DIR = Path("docs")
# Path to the components directory for the DelimiterParser
DOCS_COMPONENTS_ROOT = "src/docs/components"


def get_all_subdirectories(path: str) -> List[str]:
    """Returns a list of all subdirectories in a given path."""
    if not os.path.isdir(path):
        return []
    return [dirpath for dirpath, _, _ in os.walk(path)]


# Instantiate the parser with the dynamic load directory
md_parser = DelimiterParser(
    dynamic_load_dirs=get_all_subdirectories(DOCS_COMPONENTS_ROOT)
)


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """A simple frontmatter parser."""
    metadata = {}
    if not content.startswith("---"):
        return metadata, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return metadata, content

    frontmatter = parts[1]
    rest_of_content = parts[2]

    for line in frontmatter.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]

            if key == "order" and value.isdigit():
                value = int(value)

            metadata[key] = value

    return metadata, rest_of_content.lstrip()


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

        metadata, md_content = _parse_frontmatter(md_content)
        page_name = metadata.get("name", relative_path.stem.replace("_", " ").title())

        # Extract headings for TOC
        toc_data = []

        # Store original heading lines and their corresponding slug_ids for replacement
        heading_replacements = []

        # Match markdown headings: one or more #, followed by space, then the heading text
        heading_pattern = r"^(#{1,2})\s+(.+)$"

        for match in re.finditer(heading_pattern, md_content, re.MULTILINE):
            level = len(match.group(1))  # Count the # characters (1-6)
            heading_text = match.group(2).strip()  # Get the heading text
            slug_id = slugify(heading_text)  # Generate slug from heading text

            toc_data.append(
                {
                    "text": heading_text,
                    "id": heading_text,
                    # "id": slug_id,
                    "level": level,
                }
            )

            # Store the original heading line for replacement
            original_heading_line = match.group(0)
            heading_replacements.append((original_heading_line, slug_id))

        # # Pre-process md_content to inject IDs into headings

        # processed_md_content = md_content

        # # Apply replacements from bottom up to avoid issues with changing string length

        # for original_heading_line, slug_id in reversed(heading_replacements):

        #     # Inject {id="slug_id"} after the heading text

        #     # This assumes the heading doesn't already have an ID or other attributes

        #     new_heading_line = f"{original_heading_line} {{id=\"{slug_id}\"}}"

        #     processed_md_content = processed_md_content.replace(original_heading_line, new_heading_line, 1) # Replace only first occurrence
        # Generate the page component using the DelimiterParser
        @base(
            url=url_path,
            page_name=page_name,
            toc_data=toc_data,  # Pass toc_data here
        )
        def doc_page_component(content=md_content):  # Use processed_md_content
            return md_parser.parse_and_render(content)

        # Create a RouteConfig object
        docs_routes.append(
            RouteConfig(
                path=url_path,
                component=doc_page_component,
                title=page_name,
                toc_data=toc_data,  # Pass toc_data here
            )
        )
    return docs_routes
