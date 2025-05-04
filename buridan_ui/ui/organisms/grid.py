import reflex as rx


def responsive_grid(
    *children: rx.Component,
    lg: int = 1,
    md: int = 1,
    sm: int = 1,
    gap: int = 14,
    padding: int = 4,
) -> rx.Component:
    # Generate Tailwind classes for each breakpoint
    breakpoint_classes = (
        f"sm:grid-cols-{sm} "  # Small screens
        f"md:grid-cols-{md} "  # Medium screens
        f"lg:grid-cols-{lg} "  # Large screens
    )

    return rx.grid(
        *children,
        class_name=f"grid grid-cols-1 {breakpoint_classes} gap-{gap} p-{padding} size-full",
    )
