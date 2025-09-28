from src.wrappers.base.main import base
from src.mdparser import DelimiterParser

# Instantiate the parser, pointing it to the directory with the component examples.
# It will automatically find and register them.
md_parser = DelimiterParser(dynamic_load_dir="src/start/components")

# Read the markdown content from the file.
with open("src/start/content/charting.md") as f:
    md_content = f.read()


@base("/getting-started/charting", "Charting Walkthrough")
def charting():
    # Parse the markdown content to render the page with injected components.
    return md_parser.parse_and_render(md_content)
