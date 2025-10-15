

# Popover

Displays rich content in a portal, triggered by a button.

# Installation

Copy the following code into your app directory.


```python
import reflex as rx


def popover_root(*children, **props):
    """
    Root popover container.
    Uses Reflex's built-in popover component.
    """
    return rx.popover.root(*children, data_slot="popover", **props)


def popover_trigger(*children, **props):
    """Trigger element for the popover"""
    return rx.popover.trigger(*children, data_slot="popover-trigger", **props)


def popover_content(*children, class_name: str = "", **props):
    """
    Popover content container.
    Uses CSS variables from your shadcn theme.
    """
    base_classes = (
        "bg-[var(--popover)] text-[var(--popover-foreground)] "
        "data-[state=open]:animate-in data-[state=closed]:animate-out "
        "data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 "
        "data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 "
        "data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 "
        "data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 "
        "z-50 w-72 rounded-md border border-input dark:border-[var(--input)] p-4 shadow-md outline-none"
    )

    return rx.popover.content(
        *children,
        data_slot="popover-content",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
```


# Example
A basic popover that appears when the user clicks the trigger button.


```python
def popover_demo():
    return rx.el.div(
        popover_root(
            popover_trigger(button("Click Me", variant="outline")),
            popover_content(
                rx.el.div(
                    # Header section
                    rx.el.div(
                        rx.el.h4(
                            "Dimensions",
                            class_name="leading-none font-medium",
                        ),
                        rx.el.p(
                            "Set the dimensions for the layer.",
                            class_name="text-[var(--muted-foreground)] text-sm",
                        ),
                        class_name="space-y-2",
                    ),
                    # Input fields section
                    rx.el.div(
                        # Width input
                        rx.el.div(
                            rx.el.label(
                                "Width",
                                html_for="width",
                                class_name="text-sm font-medium",
                            ),
                            rx.el.input(
                                type="text",
                                id="width",
                                value="100%",
                                placeholder="100%",
                                class_name=(
                                    "col-span-2 h-8 w-full rounded-md border border-[var(--input)] "
                                    "bg-transparent px-3 py-1 text-sm shadow-xs "
                                    "transition-[color,box-shadow] outline-none "
                                    "placeholder:text-[var(--muted-foreground)] "
                                    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
                                    "dark:bg-[var(--input)]/30"
                                ),
                            ),
                            class_name="grid grid-cols-3 items-center gap-4",
                        ),
                        # Max width input
                        rx.el.div(
                            rx.el.label(
                                "Max. width",
                                html_for="maxWidth",
                                class_name="text-sm font-medium",
                            ),
                            rx.el.input(
                                type="text",
                                id="maxWidth",
                                value="300px",
                                placeholder="300px",
                                class_name=(
                                    "col-span-2 h-8 w-full rounded-md border border-[var(--input)] "
                                    "bg-transparent px-3 py-1 text-sm shadow-xs "
                                    "transition-[color,box-shadow] outline-none "
                                    "placeholder:text-[var(--muted-foreground)] "
                                    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
                                    "dark:bg-[var(--input)]/30"
                                ),
                            ),
                            class_name="grid grid-cols-3 items-center gap-4",
                        ),
                        # Height input
                        rx.el.div(
                            rx.el.label(
                                "Height",
                                html_for="height",
                                class_name="text-sm font-medium",
                            ),
                            rx.el.input(
                                type="text",
                                id="height",
                                value="25px",
                                placeholder="25px",
                                class_name=(
                                    "col-span-2 h-8 w-full rounded-md border border-[var(--input)] "
                                    "bg-transparent px-3 py-1 text-sm shadow-xs "
                                    "transition-[color,box-shadow] outline-none "
                                    "placeholder:text-[var(--muted-foreground)] "
                                    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
                                    "dark:bg-[var(--input)]/30"
                                ),
                            ),
                            class_name="grid grid-cols-3 items-center gap-4",
                        ),
                        # Max height input
                        rx.el.div(
                            rx.el.label(
                                "Max. height",
                                html_for="maxHeight",
                                class_name="text-sm font-medium",
                            ),
                            rx.el.input(
                                type="text",
                                id="maxHeight",
                                value="none",
                                placeholder="none",
                                class_name=(
                                    "col-span-2 h-8 w-full rounded-md border border-[var(--input)] "
                                    "bg-transparent px-3 py-1 text-sm shadow-xs "
                                    "transition-[color,box-shadow] outline-none "
                                    "placeholder:text-[var(--muted-foreground)] "
                                    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
                                    "dark:bg-[var(--input)]/30"
                                ),
                            ),
                            class_name="grid grid-cols-3 items-center gap-4",
                        ),
                        class_name="grid gap-2",
                    ),
                    class_name="grid gap-4",
                ),
                class_name="w-80",
                side="top",
            ),
        ),
        class_name="p-8",
    )
```

