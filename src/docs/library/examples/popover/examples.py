import reflex as rx

from ...base_ui.components.base.popover import popover
from ...base_ui.components.base.button import button


def popover_demo():
    return rx.el.div(
        popover.root(
            popover.trigger(render_=button("Click Me", variant="outline")),
            popover.portal(
                popover.positioner(
                    popover.popup(
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
                    ),
                    side="top",
                ),
            ),
        ),
        class_name="p-8",
    )
