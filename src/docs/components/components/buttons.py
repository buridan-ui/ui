import reflex as rx
from typing import Literal


def button(
    *children,
    variant: Literal[
        "default", "destructive", "outline", "secondary", "ghost", "link"
    ] = "default",
    size: Literal["default", "sm", "lg", "icon", "icon-sm", "icon-lg"] = "default",
    type: str = "button",
    class_name: str = "",
    **props,
):
    """
    Button component matching shadcn/ui styling.
    Uses CSS variables from your theme for colors.

    Args:
        *children: Button content (text, icons, etc.)
        variant: Button style variant
        size: Button size
        type: HTML button type
        class_name: Additional classes
        **props: Additional props for the button element
    """

    # Base classes that apply to all buttons
    base_classes = (
        "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium "
        "transition-all disabled:pointer-events-none disabled:opacity-50 "
        "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 "
        "outline-none focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 aria-invalid:border-[var(--destructive)]"
    )

    # Variant styles
    variant_classes = {
        "default": "bg-primary text-[var(--primary-foreground)] hover:bg-[var(--primary)]/90",
        "destructive": (
            "bg-[var(--destructive)] text-white hover:bg-[var(--destructive)]/90 "
            "focus-visible:ring-[var(--destructive)]/20 dark:focus-visible:ring-[var(--destructive)]/40 "
            "dark:bg-[var(--destructive)]/60"
        ),
        "outline": (
            "border bg-[var(--background)] shadow-xs hover:bg-[var(--accent)] hover:text-[var(--accent-foreground)] "
            "dark:bg-[var(--input)]/30 dark:border-[var(--input)] dark:hover:bg-[var(--input)]/50"
        ),
        "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        "ghost": "hover:bg-[var(--accent)] hover:text-[var(--accent-foreground)] dark:hover:bg-[var(--accent)]/50",
        "link": "text-[var(--primary)] underline-offset-4 hover:underline",
    }

    # Size styles
    size_classes = {
        "default": "h-9 px-4 py-2 has-[>svg]:px-3",
        "sm": "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        "lg": "h-10 rounded-md px-6 has-[>svg]:px-4",
        "icon": "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
    }

    # Combine all classes
    combined_classes = f"{base_classes} {variant_classes[variant]} {size_classes[size]} {class_name}".strip()

    return rx.el.button(
        *children, type=type, data_slot="button", class_name=combined_classes, **props
    )


# Example usage


def button_examples():
    """Examples showing all button variants and sizes"""
    return rx.box(
        # Variants
        rx.box(
            rx.text("Variants", class_name="text-lg font-semibold mb-3"),
            rx.box(
                button("Default", variant="default"),
                button("Destructive", variant="destructive"),
                button("Outline", variant="outline"),
                button("Secondary", variant="secondary"),
                button("Ghost", variant="ghost"),
                button("Link", variant="link"),
                class_name="flex flex-wrap gap-3",
            ),
            class_name="mb-8",
        ),
        # Sizes
        rx.box(
            rx.text("Sizes", class_name="text-lg font-semibold mb-3"),
            rx.box(
                button("Small", size="sm"),
                button("Default", size="default"),
                button("Large", size="lg"),
                class_name="flex items-center gap-3",
            ),
            class_name="mb-8",
        ),
        # Icon buttons
        rx.box(
            rx.text("Icon Buttons", class_name="text-lg font-semibold mb-3"),
            rx.box(
                button(rx.icon("mail"), variant="outline", size="icon-sm"),
                button("✓", variant="default", size="icon"),
                button("✕", variant="destructive", size="icon-lg"),
                class_name="flex items-center gap-3",
            ),
            class_name="mb-8",
        ),
        # Buttons with icons
        rx.box(
            rx.text("With Icons", class_name="text-lg font-semibold mb-3"),
            rx.box(
                button(
                    rx.html("✉"),
                    "Email me",
                    variant="outline",
                ),
                button(
                    "Continue",
                    rx.html("→"),
                    variant="default",
                ),
                class_name="flex gap-3",
            ),
        ),
        class_name="w-full max-w-2xl p-8",
    )
