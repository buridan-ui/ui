import reflex as rx
from ...base_ui.components.base.toggle_group import toggle_group
from ...base_ui.components.base.toggle import toggle


def toggle_group_example():
    """A basic toggle group example."""
    return toggle_group(
        toggle(
            rx.icon("bold"),
            value="bold",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        toggle(
            rx.icon("italic"),
            value="italic",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        toggle(
            rx.icon("underline"),
            value="underline",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        default_value=["bold"],
        class_name="flex gap-px rounded-md border border-input bg-background p-0.5",
    )


def toggle_group_multiple():
    """A toggle group example allowing multiple selections."""
    return toggle_group(
        toggle(
            rx.icon("align-left"),
            value="left",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        toggle(
            rx.icon("align-center"),
            value="center",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        toggle(
            rx.icon("align-right"),
            value="right",
            class_name="flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground",
        ),
        default_value=["left", "right"],
        multiple=True,
        class_name="flex gap-px rounded-md border border-input bg-background p-0.5",
    )


def toggle_group_disabled():
    """A disabled toggle group example."""
    return toggle_group(
        toggle(rx.icon("bold"), value="bold"),
        toggle(rx.icon("italic"), value="italic"),
        toggle(rx.icon("underline"), value="underline"),
        disabled=True,
    )
