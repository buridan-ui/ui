import reflex as rx

from src.export import export
from src.docs.library.javascript_integrations.fuse.fuse import (
    fuse_cdn_script,
    load_json_file_and_initialize,
    custom_search_script,
)
from src.docs.library.javascript_integrations.minisearch.minisearch import (
    minisearch_cdn_script,
    custom_minisearch_search_script,
    load_json_file_and_initialize_minisearch,
)
from src.docs.library.javascript_integrations.quill.quill import (
    quill_stylesheet,
    quill_custom_font,
    quill_init,
    quill_lib,
)

# --- Reflex app init ---
app = rx.App(
    stylesheets=["css/wrapper.css"],
    head_components=[
        fuse_cdn_script(),
        custom_search_script(),
        minisearch_cdn_script(),
        custom_minisearch_search_script(),
        load_json_file_and_initialize(),
        load_json_file_and_initialize_minisearch(),
        quill_lib(),
        quill_stylesheet(),
        quill_custom_font(),
        quill_init(),
    ],
)

# --- Main export entry ---
export(app)
