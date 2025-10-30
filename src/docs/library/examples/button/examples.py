import reflex as rx

from ...base_ui.components.base.button import button


def button_size_examples():
    return rx.el.div(
        button("Small", size="sm"),
        button("Default", size="default"),
        button("Large", size="lg"),
        class_name="flex items-center gap-3",
    )


def button_default_example():
    return button("Default", variant="default")


def button_outline_example():
    return button("Outline", variant="outline")


def button_secondary_example():
    return button("Secondary", variant="secondary")


def button_ghost_example():
    return button("Ghost", variant="ghost")


def button_destructive_example():
    return button("Destructive", variant="destructive")


def button_link_example():
    return button("Link", variant="link")


def button_icon_examples():
    return (
        button(rx.icon("mail", class_name="size-4"), variant="outline", size="icon-sm"),
    )
