import os
import re
import src.docs.constants as constants


from typing import List
from src.docs.parser import DocParser
from src.utils.frontmatter import parse_frontmatter


def get_all_subdirectories(path: str) -> List[str]:
    """Returns a list of all subdirectories in a given path."""
    if not os.path.isdir(path):
        return []
    return [dirpath for dirpath, _, _ in os.walk(path)]


parser = DocParser(
    dynamic_load_dirs=get_all_subdirectories(constants.DOCS_LIBRARY_ROOT)
)


def generate_docs_library() -> List[constants.DocDataStruct]:
    docs = []

    if not constants.DOCS_BASE_DIR.exists():
        print(f"Warning: Docs base directory not found: {constants.DOCS_BASE_DIR}")
        return []

    for md_file_path in constants.DOCS_BASE_DIR.glob("**/*.md"):
        relative_path = md_file_path.relative_to(constants.DOCS_BASE_DIR)
        url_path_parts = [part.replace("_", "-") for part in relative_path.parts]
        url_path = "docs/" + "/".join(url_path_parts).replace(".md", "")

        # Read the markdown content
        with open(md_file_path, "r") as f:
            md_content = f.read()

        __, md_content = parse_frontmatter(md_content)

        # Extract headings for TOC from THIS file's content
        toc_data = []
        for match in re.finditer(r"^(#{1,2})\s+(.+)$", md_content, re.MULTILINE):
            level = len(match.group(1))  # Count the # characters (1-2)
            heading_text = match.group(2).strip()  # Get the heading text

            toc_data.append(
                {
                    "text": heading_text,
                    "id": heading_text,
                    "level": level,
                }
            )

        # Create the doc component (no need for inner function)
        doc = constants.DocDataStruct(
            url=url_path,
            component=parser.parse_and_render(md_content),
            table_of_content=toc_data,
        )

        docs.append(doc)

    return docs
