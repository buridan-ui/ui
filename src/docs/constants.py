from enum import Enum
from typing import List, Dict
from pathlib import Path
from dataclasses import dataclass

import reflex as rx


# --- Markdown Command Constants ---
class DocParserCommands(str, Enum):
    DEMO_AND_CODE_SINGLE_FILE = "demo_and_code_single_file"
    SHOW_CODE_WITH_LANGUAGE = "show_code_with_language"
    DEMO_AND_SINGLE_FUNCTION = "demo_and_single_function"
    FULL_SOURCE_PAGE_OF_COMPONENT = "full_source_page_of_component"
    CLI_AND_MANUAL_INSTALLATION = "cli_and_manual_installation"


# --- Generated Doc Type ---
@dataclass
class DocDataStruct:
    """The data structure for the generated doc page"""

    url: str
    component: List[rx.Component]
    table_of_content: List[Dict]


# --- Docs Path Constants ---
DOCS_BASE_DIR = Path("docs")
DOCS_LIBRARY_ROOT = "src/docs/library"
