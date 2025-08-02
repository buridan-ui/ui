import reflex as rx

from buridan_ui.templates.sidemenu.sidemenu import sidemenu


def drawer():
    return rx.drawer.root(
        rx.drawer.trigger(rx.el.button(rx.icon(tag="menu", size=13))),
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
            z_index="50",
        ),
        direction="left",
    )
