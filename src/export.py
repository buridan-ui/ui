import reflex as rx

from src.docs.generator import generate_docs_library
from src.views.landing.landing import site_landing_page
from src.templates.docpage import docpage

landing = site_landing_page()


def export_docs_match_cases():
    cases = [
        (doc.url, rx.box(*doc.component, class_name="w-full"))
        for doc in generate_docs_library()
    ]

    return cases


def export_docs_table_of_content():
    toc_mapping = {doc.url: doc.table_of_content for doc in generate_docs_library()}

    return toc_mapping


def export(app: rx.App):
    app.add_page(landing, "/")

    app.add_page(
        rx.fragment(),
        route="/docs",
        on_load=lambda: rx.redirect("/docs/get-started/overview"),
    )

    app.add_page(
        lambda: docpage(
            export_docs_match_cases(),
            export_docs_table_of_content(),
        ),
        route="/docs/[[...splat]]",
    )
