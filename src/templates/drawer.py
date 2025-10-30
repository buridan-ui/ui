import reflex as rx

from src.templates.sidebar import sidebar
from src.docs.library.base_ui.components.base.button import button


def drawer():
    return rx.drawer.root(
        rx.drawer.trigger(
            button(rx.icon(tag="menu", size=13), variant="ghost", size="sm"),
        ),
        rx.drawer.portal(
            rx.drawer.content(
                sidebar(in_drawer=True),
                width="100%",
                top="3.5rem",
                right="0",
                height="calc(100% - 3.5rem)",
                background=rx.color_mode_cond(
                    "oklch(1 0 0 / 0.95)", "oklch(0.145 0 0 / 0.95)"
                ),
            ),
        ),
        direction="left",
    )
