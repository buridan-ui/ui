import reflex as rx
from src.config import VERSION
from src.templates.search.search import search


def buridan_doc_navbar_header():
    return (
        rx.el.div(
            rx.link(
                rx.box(
                    rx.text(
                        "buridan",
                        font_weight="700",
                        font_size="1rem",
                        letter_spacing="-0.04em",
                    ),
                    rx.text(
                        ".UI",
                        font_size="0.6rem",
                        position="relative",
                        font_weight="600",
                    ),
                    color=rx.color("slate", 12),
                    class_name="flex flex-row items-baseline gap-x-[1px]",
                ),
                text_decoration="none",
                href="/",
            ),
            rx.badge(VERSION, color_scheme="gray", size="1", variant="outline"),
            class_name="flex flex-row w-full items-end gap-x-2",
        ),
    )


def site_theme() -> rx.Component:
    return rx.el.button(
        rx.color_mode.icon(
            light_component=rx.el.div(
                rx.icon("moon", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
            dark_component=rx.el.div(
                rx.icon("sun", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
        ),
        class_name=(
            "inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
            "cursor-pointer h-[1.625rem] w-[1.625rem]"
        ),
        border=f"1px solid {rx.color('gray', 5)}",
        on_click=rx.toggle_color_mode,
    )


def site_github() -> rx.Component:
    return rx.link(
        rx.el.button(rx.icon("github", size=14), class_name="cursor-pointer"),
        color=f"{rx.color('slate', 12)} !important",
        href="https://github.com/buridan-ui",
        text_decoration="none",
        border=f"1px solid {rx.color('gray', 5)}",
        class_name=(
            "inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
            "cursor-pointer h-[1.625rem] w-[1.625rem] cursor-pointer"
        ),
    )


def doc_navbar():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                buridan_doc_navbar_header(),
                class_name="max-w-[18rem] w-full flex items-center justify-start px-4",
            ),
            # rx.el.div(
            #     class_name="w-full flex items-center justify-start px-4"
            # ),
            rx.el.div(
                search(),
                site_github(),
                site_theme(),
                class_name="w-full flex flex-row gap-x-2 items-center justify-end px-4",
            ),
            class_name="xl:max-w-[80rem] 2xl:max-w-[75rem] w-full mx-auto flex flex-row items-center",
        ),
        border_bottom=f"0.90px solid {rx.color('gray', 5)}",
        class_name="w-full h-12 flex items-enter justify-center absolute top-0 z-[99]",
    )
