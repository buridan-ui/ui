import reflex as rx

import src.routes as routes

from src.templates.drawer import drawer
from src.components.ui.titles import site_title
from src.docs.library.components.button.button import button
from src.components.ui.buttons import site_github, site_theme, site_reflex_build


def docs_navbar():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(drawer(), class_name="flex lg:hidden"),
                rx.el.a(button(site_title(), variant="ghost"), to="/"),
                class_name="max-w-[18rem] w-full flex flex-row gap-x-2 xl:gap-x-0 items-center justify-start",
            ),
            rx.el.div(
                site_github(),
                site_theme(),
                class_name="w-full flex flex-row gap-x-0 items-center justify-end",
            ),
            class_name="xl:max-w-[80rem] 2xl:max-w-[75rem] w-full mx-auto flex flex-row items-center",
        ),
        class_name="bg-background w-full h-12 py-1",
    )


def main_navbar_nav_link(nav: str, url: str):
    return rx.el.a(
        button(nav, variant="ghost", size="sm", class_name="!text-sm cursor-pointer"),
        to=url,
        class_name="",
    )


def main_navbar():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(drawer(), class_name="flex lg:hidden"),
                button(site_title(), variant="ghost"),
                rx.el.div(
                    main_navbar_nav_link(
                        "Getting Started", routes.GET_STARTED_URLS[0]["url"]
                    ),
                    main_navbar_nav_link(
                        "Wrapped Components", routes.WRAPPED_COMPONENTS_URLS[0]["url"]
                    ),
                    main_navbar_nav_link(
                        "JS Integrations", routes.JS_INTEGRATIONS_URLS[0]["url"]
                    ),
                    main_navbar_nav_link("Chart UI", routes.CHARTS_URLS[0]["url"]),
                    main_navbar_nav_link(
                        "Components", routes.COMPONENTS_URLS[0]["url"]
                    ),
                    class_name="hidden lg:flex flex-row items-center text-sm no-underline gap-x-2",
                ),
                class_name="flex flex-row items-baseline gap-x-2 lg:gap-x-4",
            ),
            rx.el.div(
                site_reflex_build(),
                site_github(),
                site_theme(),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="xl:max-w-[90rem] 2xl:max-w-[85rem] w-full mx-auto flex flex-row items-center justify-between",
        ),
        class_name="bg-background w-full h-10 sticky top-0 left-0 px-4 py-6 items-center justify-between flex flex-row z-[15]",
    )
