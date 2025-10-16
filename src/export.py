import reflex as rx

import src.meta as meta
import src.routes as routes

from src.docs.generator import generate_docs_library
from src.views.landing.landing import site_landing_page
from src.templates.docpage import docpage


landing = site_landing_page()


def export_docs_match_cases():
    cases = [
        (doc.url, rx.el.div(*doc.component, class_name="w-full"))
        for doc in generate_docs_library()
    ]

    return cases


def export_docs_table_of_content():
    toc_mapping = {doc.url: doc.table_of_content for doc in generate_docs_library()}

    return toc_mapping


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

    # SPA app for buridan/ui
    app.add_page(
        lambda: docpage(
            export_docs_match_cases(),
            export_docs_table_of_content(),
        ),
        route="/docs/[[...splat]]",
        meta=meta.SITE_META_TAGS,
        on_load=rx.call_script(
            r"""
            function updateDocTitle() {
                const path = window.location.pathname.replace(/^\/docs\//, '');
                const segments = path.split('/').filter(Boolean);
                const lastSegment = segments[segments.length - 1] || 'Docs';
                const title = lastSegment
                    .replace(/-/g, ' ')
                    .replace(/\b\w/g, c => c.toUpperCase());
                document.title = title + ' – buridan/ui';
            }

            // Run once on page load
            updateDocTitle();

            // Monkey-patch history methods to detect route changes
            const _pushState = history.pushState;
            history.pushState = function() {
                _pushState.apply(this, arguments);
                updateDocTitle();
            };

            const _replaceState = history.replaceState;
            history.replaceState = function() {
                _replaceState.apply(this, arguments);
                updateDocTitle();
            };

            // Handle back/forward navigation
            window.addEventListener('popstate', updateDocTitle);
        """
        ),
    )
