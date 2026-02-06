import reflex as rx

from src.docs.library.javascript_integrations.fuse.fuse import (
    custom_search_script,
    fuse_cdn_script,
    load_json_file_and_initialize,
)
from src.docs.library.javascript_integrations.minisearch.minisearch import (
    custom_minisearch_search_script,
    load_json_file_and_initialize_minisearch,
    minisearch_cdn_script,
)
from src.docs.library.javascript_integrations.quill.quill import (
    quill_custom_font,
    quill_init,
    quill_lib,
    quill_stylesheet,
)
from src.export import export


def site_tracking_script() -> rx.Script:
    return rx.script(
        src="https://gc.zgo.at/count.js",
        custom_attrs={
            "data-goatcounter": "https://buridan-ui.goatcounter.com/count",
        },
    )


# --- Reflex app init ---
app = rx.App(
    stylesheets=["css/wrapper.css", "css/themes.css"],
    head_components=[
        site_tracking_script(),
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

# --- Main export entry function ---
export(app)
