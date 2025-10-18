import reflex as rx

from src.docs.library.components.button.button import button
from src.docs.library.wrapped_components.simple_icon.simple_icon import simple_icon


def site_theme() -> rx.Component:
    return button(
        rx.color_mode.icon(
            light_component=rx.image(
                "/svg/theme/theme_light.svg",
                class_name="size-4 !shrink-0",
            ),
            dark_component=rx.image(
                "/svg/theme/theme_dark.svg",
                class_name="size-4 !shrink-0",
            ),
        ),
        on_click=rx.toggle_color_mode,
        variant="ghost",
        size="sm",
        class_name="cursor-pointer",
    )


def site_github() -> rx.Component:
    return rx.el.a(
        button(
            simple_icon("SiGithub"),
            rx.el.p("204", class_name="text-xs font-semibold text-muted-foreground"),
            class_name="cursor-pointer flex flex-row items-center gap-x-2",
            variant="ghost",
            size="sm",
        ),
        href="https://github.com/buridan-ui",
        class_name="no-underline",
    )


def site_reflex_build():
    return rx.el.a(
        button(
            rx.el.image(
                rx.color_mode_cond(
                    "/svg/reflex/reflex_light.svg",
                    "/svg/reflex/reflex_dark.svg",
                ),
            ),
            "Build",
            variant="ghost",
        ),
        href="https://build.reflex.dev/",
    )
