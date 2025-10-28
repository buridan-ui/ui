import reflex as rx
from ..base_ui.components.base.card import card


def card_low_level():
    return rx.el.div(
        card.root(
            card.header(
                rx.el.div(
                    rx.el.p("Card Title", class_name="text-md"), class_name="w-full p-4"
                ),
            ),
            card.content(
                rx.el.div(
                    rx.el.p("Card Content", class_name="text-md"),
                    class_name="w-full p-4",
                ),
            ),
            card.footer(
                rx.el.div(
                    rx.el.p("Card Footer", class_name="text-md"),
                    class_name="w-full p-4",
                ),
            ),
            class_name="w-full max-w-[35em]",
        ),
        class_name="py-8 w-full max-w-[35em]",
    )
