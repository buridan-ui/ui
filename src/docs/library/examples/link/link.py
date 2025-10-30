import reflex as rx
from ...base_ui.components.base.link import link


def link_example():
    """A basic link example."""
    return link("This is a link", href="#")


def link_sizes():
    """Link examples with different sizes."""
    return rx.box(
        link("X-Small Link", href="#", size="xs"),
        link("Small Link", href="#", size="sm"),
        link("Medium Link", href="#", size="md"),
        link("Large Link", href="#", size="lg"),
        link("X-Large Link", href="#", size="xl"),
        class_name="flex flex-col items-start gap-4",
    )


def link_variants():
    """Link examples with different variants."""
    return rx.box(
        link("Primary Link", href="#", variant="primary"),
        link("Secondary Link", href="#", variant="secondary"),
        class_name="flex flex-col items-start gap-4",
    )


def link_with_icon():
    """Link example with an icon."""
    return link("Link with icon", href="#", show_icon=True)
