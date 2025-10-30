from ...base_ui.components.base.tooltip import tooltip
from ...base_ui.components.base.button import button

import reflex as rx


def tooltip_group_example():
    """A group of icon buttons with tooltips using the Tooltip API."""

    return rx.el.div(
        tooltip.provider(
            *[
                tooltip.root(
                    tooltip.trigger(
                        rx.icon(tag=icon),
                        class_name="flex size-8 items-center justify-center rounded-sm",
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(label),
                            side_offset=10,
                        )
                    ),
                )
                for icon, label in [
                    ("bold", "Bold"),
                    ("italic", "Italic"),
                    ("underline", "Underline"),
                    ("strikethrough", "Strikethrough"),
                ]
            ],
        ),
        class_name="flex !flex-row gap-px rounded-md border border-input bg-background p-0.5",
    )


def tooltip_example():
    """A basic tooltip example."""
    return tooltip(
        trigger=button("i", variant="outline"),
        content="This is a tooltip!",
    )


def tooltip_with_long_content():
    """Tooltip with longer content."""
    return tooltip(
        trigger=button("i", variant="outline"),
        content="This is a much longer tooltip content that provides more detailed information.",
    )


def tooltip_with_custom_placement():
    """Tooltip with custom placement (e.g., bottom)."""
    return tooltip(
        trigger=button("i", variant="outline"),
        content="This tooltip appears at the bottom.",
        side="bottom",
    )
