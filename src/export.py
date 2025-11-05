import reflex as rx

import src.meta as meta
import src.routes as routes

from src.docs.generator import generate_docs_library
from src.views.landing.landing import site_landing_page
from src.templates.docpage import docpage
from src.templates.toc import table_of_content

# Define the landing page
landing = site_landing_page()

# Define redirects in one place
redirect_map = {
    "/docs": routes.GET_STARTED_URLS[0]["url"],
    "/docs/components": routes.BASE_UI_COMPONENTS[0]["url"],
    "/docs/charts": routes.CHARTS_URLS[0]["url"],
    "/docs/javascript-integrations": routes.JS_INTEGRATIONS_URLS[0]["url"],
    "/docs/wrapped-components": routes.WRAPPED_COMPONENTS_URLS[0]["url"],
}


# Main application export function
def export(app: rx.App):
    # Landing page
    app.add_page(
        landing,
        route="/",
        title="The UI Library for Reflex Developers - buridan/ui",
        meta=meta.SITE_META_TAGS,
    )

    # Create redirect pages dynamically
    for route, target in redirect_map.items():
        app.add_page(
            rx.fragment(),
            route=route,
            on_load=lambda target=target: rx.redirect(target),
        )

    # Add all the documentation pages
    for doc in generate_docs_library():
        main_content = rx.el.div(*doc.component, class_name="w-full")
        toc_content = table_of_content(doc.url, doc.table_of_content)

        title_s = doc.url.split("/")[-1].replace("-", " ").title()
        title = f"{title_s} – buridan/ui"

        app.add_page(
            docpage(main_content, toc_content),
            route=f"/{doc.url}",
            title=title,
            meta=meta.SITE_META_TAGS,
        )
