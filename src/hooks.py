import src.routes as routes
from reflex.experimental import ClientStateVar

# Global state for selected page - default to docs overview
selected_page = ClientStateVar.create("selected_page", "docs/overview")

# Global state for switching theme of components/ui
current_theme = ClientStateVar.create("current_theme", "gray")

# Global state for search query
search_query = ClientStateVar.create("search_query", "")

# Global state for Getting Started Routes
getting_started_cs = ClientStateVar.create(
    "getting_started_cs",
    routes.GET_STARTED_URLS
    + routes.COMPONENTS_URLS
    + routes.CHARTS_URLS
    + routes.JS_INTEGRATIONS_URLS
    + routes.WRAPPED_COMPONENTS_URLS,
)
