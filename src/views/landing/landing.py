import reflex as rx

from src.docs.library.base_ui.components.base.button import button
from src.templates.navbar import main_navbar
from src.views.examples.examples import examples_page
from src.comps.ui.themes import theme_buttons
import src.routes as routes


def header():
    return rx.text(
        "The UI Library for Reflex Developers",
        font_size="max(36px,min(4.5vw,60px))",
        font_weight="800",
        letter_spacing="-0.05em",
        line_height="1",
        class_name="text-center",
    )


def sub_header():
    return rx.box(
        rx.el.p(
            rx.fragment(
                rx.el.strong("Buridan UI"),
                " gives you ",
                rx.el.strong("composable, themeable components"),
                " designed for Reflex. ",
                rx.el.strong("Extend, override, and ship"),
                " without fighting the framework.",
            ),
            font_size="max(15px,min(2vw,20px))",
            font_weight="400",
            letter_spacing="-0.01em",
            line_height="1.8",
        ),
        class_name="w-full max-w-[750px] flex text-center px-2",
    )


def landing_buttons():
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                button("Get Started", size="sm"), to=routes.GET_STARTED_URLS[0]["url"]
            ),
            rx.el.a(
                button("View Components", variant="ghost", size="sm"),
                to=routes.BASE_UI_COMPONENTS[0]["url"],
            ),
            class_name="w-full max-w-[5rem] flex flex-row items-center justify-center gap-x-4",
        ),
        class_name="w-full flex justify-center",
    )


def site_landing_page():
    return rx.el.div(
        rx.el.div(
            main_navbar(),
            rx.el.div(
                header(),
                sub_header(),
                landing_buttons(),
                rx.el.div(
                    theme_buttons(),
                    examples_page(),
                    class_name="flex flex-col gap-y-0 w-full pt-[7rem]",
                ),
                class_name="w-full min-h-screen flex flex-col gap-y-6 items-center justify-start pt-[7rem]",
            ),
            class_name="xl:max-w-[90rem] 2xl:max-w-[85rem] w-full mx-auto flex-col",
        ),
        class_name="bg-background w-full min-h-screen flex flex-col gap-y-6 items-center justify-center",
    )
