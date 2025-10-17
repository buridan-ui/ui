import reflex as rx

import src.meta as meta
import src.routes as routes

from src.docs.generator import generate_docs_library
from src.views.landing.landing import site_landing_page
from src.templates.docpage import docpage
from src.templates.toc import table_of_content


landing = site_landing_page()


def export(app: rx.App):
    # landing page
    app.add_page(
        landing,
        route="/",
        title="The UI Library for Reflex Developers - buridan/ui",
        meta=meta.SITE_META_TAGS,
    )

    # redirect if wrong url
    app.add_page(
        rx.fragment(),
        route="/docs",
        on_load=lambda: rx.redirect(routes.GET_STARTED_URLS[0]["url"]),
    )

    # Add all the documentation pages.
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
            # on_load=rx.call_script(selected_page.set_value(doc.url))
        )
