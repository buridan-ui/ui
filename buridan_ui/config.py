import os

VERSION = "v0.7.0-beta.2"
NAME = "buridan_ui"

BURIDAN_URL = "https://buridan-ui.reflex.run/"
BURIDAN_SLOGAN = (
    "Beautifully designed Reflex components to build your web apps faster. Open source."
)
BURIDAN_KEY_WORDS = (
    "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
)


BASE_GITHUB_URL = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/"
SITE_LOGO_URL = "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG"

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

LOCAL_BASE_PRO_PATH = os.path.join(project_root, NAME, NAME, "pro")
LOCAL_BASE_CHART_PATH = os.path.join(project_root, NAME, NAME, "charts")
LOCAL_BASE_PANTRY_PATH = os.path.join(project_root, NAME, NAME, "pantry")

BASE_PANTRY_PATH = BASE_GITHUB_URL + "pantry/"
BASE_CHART_PATH = BASE_GITHUB_URL + "charts/"


SITE_THEME = "dark"
FONT_FAMILY = "JetBrains Mono,ui-monospace,monospace"

SITE_META_TAGS = [
    {"name": "application-name", "content": "Buridan UI"},
    {"name": "keywords", "content": BURIDAN_KEY_WORDS},
    {"name": "description", "content": BURIDAN_SLOGAN},
    {"property": "og:url", "content": BURIDAN_URL},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Buridan UI"},
    {"property": "og:description", "content": BURIDAN_SLOGAN},
    {"property": "og:image", "content": SITE_LOGO_URL},
    {"property": "og:image:width", "content": "1200"},
    {"property": "og:image:height", "content": "630"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": BURIDAN_URL},
    {"property": "twitter:url", "content": BURIDAN_URL},
    {"name": "twitter:title", "content": "Buridan UI"},
    {"name": "twitter:description", "content": BURIDAN_SLOGAN},
    {"name": "twitter:image", "content": SITE_LOGO_URL},
]
