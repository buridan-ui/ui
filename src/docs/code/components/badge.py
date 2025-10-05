import reflex as rx
from typing import Literal


def badge(
    *children,
    variant: Literal["default", "secondary", "destructive", "outline"] = "default",
    class_name: str = "",
    **props,
):
    """
    Badge component matching shadcn/ui styling.
    Uses CSS variables from your theme for colors.

    Args:
        *children: Badge content (text, icons, etc.)
        variant: Badge style variant
        class_name: Additional classes
        **props: Additional props for the badge element
    """

    # Base classes that apply to all badges
    base_classes = (
        "inline-flex items-center justify-center rounded-md border px-2 py-0.5 text-xs font-medium "
        "w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none "
        "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
        "aria-invalid:border-[var(--destructive)] transition-[color,box-shadow] overflow-hidden"
    )

    # Variant styles
    variant_classes = {
        "default": (
            "border-transparent bg-[var(--primary)] text-[var(--primary-foreground)] "
            "[a&]:hover:bg-[var(--primary)]/90"
        ),
        "secondary": (
            "border-transparent bg-[var(--secondary)] text-[var(--secondary-foreground)] "
            "[a&]:hover:bg-[var(--secondary)]/90"
        ),
        "destructive": (
            "border-transparent bg-[var(--destructive)] text-white "
            "[a&]:hover:bg-[var(--destructive)]/90 "
            "focus-visible:ring-[var(--destructive)]/20 dark:focus-visible:ring-[var(--destructive)]/40 dark:bg-[var(--destructive)]/60"
        ),
        "outline": (
            "text-[var(--foreground)] border-[var(--input)] "
            "[a&]:hover:bg-[var(--accent)] [a&]:hover:text-[var(--accent-foreground)]"
        ),
    }

    # Combine all classes
    combined_classes = f"{base_classes} {variant_classes[variant]} {class_name}".strip()

    return rx.el.span(
        *children, data_slot="badge", class_name=combined_classes, **props
    )


# Example matching the shadcn BadgeDemo


def badge_demo():
    """
    Example matching the shadcn BadgeDemo component.
    Shows all badge variants and custom styles.
    """
    return rx.box(
        # Basic variants
        rx.box(
            badge("Badge"),
            badge("Secondary", variant="secondary"),
            badge("Destructive", variant="destructive"),
            badge("Outline", variant="outline"),
            class_name="flex w-full flex-wrap gap-2",
        ),
        # Custom styled badges
        rx.box(
            # Verified badge with icon
            badge(
                rx.icon(tag="badge-check"),
                "Verified",
                variant="secondary",
                class_name="bg-blue-500 text-white dark:bg-blue-600",
            ),
            # Circular number badges
            badge(
                "8",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "99",
                variant="destructive",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "20+",
                variant="outline",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            class_name="flex w-full flex-wrap gap-2",
        ),
        class_name="flex flex-col items-center gap-2 p-8",
    )


# Additional examples


def badge_with_icons():
    """Examples of badges with various icons"""
    return rx.box(
        badge(
            rx.icon(tag="check"),
            "Success",
            variant="secondary",
            class_name="bg-green-500 text-white dark:bg-green-600",
        ),
        badge(
            rx.icon(tag="x"),
            "Error",
            variant="destructive",
        ),
        badge(
            rx.icon(tag="alert-circle"),
            "Warning",
            variant="secondary",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        badge(
            rx.icon(tag="info"),
            "Info",
            variant="secondary",
            class_name="bg-blue-500 text-white dark:bg-blue-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )


def badge_status_examples():
    """Status badge examples"""
    return rx.box(
        badge("New", variant="default"),
        badge("Popular", variant="secondary"),
        badge("Sale", variant="destructive"),
        badge("Draft", variant="outline"),
        badge(
            rx.icon(tag="star"),
            "Featured",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )


def badge_notification_count():
    """Notification count badges (like the circular ones)"""
    return rx.box(
        # Simple counts
        badge(
            "1",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "5",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "10",
            variant="secondary",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "99+",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        class_name="flex items-center gap-2 p-8",
    )
