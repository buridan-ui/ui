import reflex as rx

import src.routes as routes

from src.templates.drawer import drawer
from src.templates.search import site_search
from src.comps.ui.titles import site_title
from src.docs.library.base_ui.components.base.button import button
from src.comps.ui.buttons import site_github, site_theme


def main_navbar_nav_link(nav: str, url: str):
    return rx.el.a(
        button(nav, variant="ghost", size="sm", class_name="!text-sm cursor-pointer"),
        to=f"/{url}",
        class_name="",
    )


def main_navbar():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(drawer(), class_name="flex lg:hidden"),
                rx.el.a(button(site_title(), variant="ghost"), to="/"),
                rx.el.div(
                    main_navbar_nav_link("Docs", routes.GET_STARTED_URLS[0]["url"]),
                    main_navbar_nav_link(
                        "Components", routes.BASE_UI_COMPONENTS[0]["url"]
                    ),
                    main_navbar_nav_link("Charts", routes.CHARTS_URLS[0]["url"]),
                    main_navbar_nav_link(
                        "Wrapped React", routes.WRAPPED_COMPONENTS_URLS[0]["url"]
                    ),
                    main_navbar_nav_link(
                        "Integrations", routes.JS_INTEGRATIONS_URLS[0]["url"]
                    ),
                    class_name="hidden lg:flex flex-row items-center text-sm no-underline gap-x-2",
                ),
                class_name="flex flex-row items-baseline gap-x-2 lg:gap-x-4",
            ),
            rx.el.div(
                site_search(),
                rx.el.p(
                    "|", class_name="text-muted-foreground/50 font-thin hidden lg:flex"
                ),
                site_github(),
                rx.el.p("|", class_name="text-muted-foreground/50 font-thin"),
                site_theme(),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="xl:max-w-[80rem] 2xl:max-w-[85rem] w-full mx-auto flex flex-row items-center justify-between",
        ),
        class_name="bg-background w-full h-12 sticky top-0 left-0 px-0 py-7 items-center justify-between flex flex-row z-[99999]",
    )
