import os

# ------------------------ DO NOT EDIT ---------------------------- #
# Get the directory of the current script/module
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to your project root if needed
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

LOCAL_BASE_PRO_PATH = os.path.join(project_root, "buridan_ui", "buridan_ui", "pro")
LOCAL_BASE_CHART_PATH = os.path.join(project_root, "buridan_ui", "buridan_ui", "charts")
LOCAL_BASE_PANTRY_PATH = os.path.join(
    project_root, "buridan_ui", "buridan_ui", "pantry"
)

# ------------------------ DO NOT EDIT ---------------------------- #
VERSION = "v.0.6.3"


BASE_PANTRY_PATH = (
    "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/pantry/"
)

BASE_CHART_PATH = (
    "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/charts/"
)

SiteFont = "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap"

SiteTheme = "dark"

# original font family:  "IBM Plex Mono,ui-monospace,monospace"
FontFamily = "JetBrains Mono,ui-monospace,monospace"


SiteMetaTags = [
    {"name": "application-name", "content": "Buridan UI"},
    {
        "name": "keywords",
        "content": "buridan, ui, web apps, framework, open source, frontend, backend, full stack",
    },
    {
        "name": "description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    {"property": "og:url", "content": "https://buridan-ui.reflex.run/"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Buridan UI"},
    {
        "property": "og:description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    {
        "property": "og:image",
        "content": "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
    },
    {"property": "og:image:width", "content": "1200"},
    {"property": "og:image:height", "content": "630"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": "https://buridan-ui.reflex.run/"},
    {
        "property": "twitter:url",
        "content": "https://buridan-ui.reflex.run/",
    },
    {"name": "twitter:title", "content": "Buridan UI"},
    {
        "name": "twitter:description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    {
        "name": "twitter:image",
        "content": "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
    },
]
