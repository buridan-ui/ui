import reflex as rx

from src.templates.sidemenu.sidemenu import sidemenu


def drawer():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.el.button(
                rx.icon(tag="menu", size=13),
                class_name="rounded-md flex items-center gap-x-2 text-sm font-semibold cursor-pointer",
                border=f"1px solid {rx.color('gray', 3)}",
                _hover={"background": rx.color("gray", 3)},
                style={
                    "display": "inline-flex",
                    "height": "1.925rem",
                    "padding": "0.25rem 0.50rem",
                },
            )
        ),
        rx.drawer.overlay(z_index="999"),
        rx.drawer.portal(
            rx.drawer.content(
                sidemenu(True),
                **{
                    "top": "auto",
                    "right": "auto",
                    "height": "100%",
                    "background": "var(--background)",
                },
            ),
        ),
        direction="left",
    )
