from reflex.experimental import ClientStateVar

# Global state for selected page - default to docs overview
selected_page = ClientStateVar.create("selected_page", "docs/overview")

# Global state for switching theme of components/ui
current_theme = ClientStateVar.create("current_theme", "gray")
