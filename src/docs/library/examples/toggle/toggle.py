import reflex as rx
from ...base_ui.components.base.toggle import toggle


def toggle_example():
    return toggle(
        rx.icon("bookmark"),
        "Bookmark",
        class_name=(
            "data-[pressed]:bg-transparent "
            "data-[pressed]:[&_svg]:fill-blue-500 "
            "data-[pressed]:[&_svg]:stroke-blue-500"
        ),
    )


def toggle_pressed():
    """A toggle example with a default pressed state."""
    return toggle(rx.icon("italic"), default_pressed=True)


def toggle_disabled():
    """A disabled toggle example."""
    return toggle(rx.icon("underline"), disabled=True)
