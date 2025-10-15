import reflex as rx

from src.templates.sidebar import sidebar
from src.docs.library.components.button.button import button


def drawer():
    return rx.drawer.root(
        rx.drawer.trigger(
            button(rx.icon(tag="menu", size=13), variant="ghost", size="sm"),
        ),
        rx.drawer.overlay(z_index="9999"),
        rx.drawer.portal(
            rx.drawer.content(
                sidebar(in_drawer=True),
                width="18rem",
                top="0",
                right="0",
                height="100%",
                class_name="bg-background",
            ),
        ),
        direction="left",
    )
