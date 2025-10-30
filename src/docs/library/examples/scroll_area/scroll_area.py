import reflex as rx
from ...base_ui.components.base.scroll_area import scroll_area


def scroll_area_example():
    """A basic scroll area example."""
    return scroll_area(
        rx.box(
            *[rx.text(f"Item {i}", class_name="p-2") for i in range(50)],
        ),
        class_name="h-72 w-48 rounded-md border",
    )
