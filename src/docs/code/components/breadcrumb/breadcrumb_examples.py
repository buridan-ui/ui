import reflex as rx
from .breadcrumb_installation import (
    breadcrumb,
    breadcrumb_ellipsis,
    breadcrumb_item,
    breadcrumb_list,
    breadcrumb_link,
    breadcrumb_separator,
    breadcrumb_page,
)


def breadcrumb_demo():
    """
    Example matching the shadcn BreadcrumbDemo component.
    Shows breadcrumb with links, ellipsis dropdown, and current page.
    """
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(),
                # Dropdown menu for collapsed items
                breadcrumb_item(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.box(
                                breadcrumb_ellipsis(class_name="size-4"),
                                rx.el.span("Toggle menu", class_name="sr-only"),
                                class_name="flex items-center gap-1",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Documentation"),
                            rx.menu.item("Themes"),
                            rx.menu.item("GitHub"),
                            class_name="min-w-[8rem]",
                        ),
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Components", href="/docs/components"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page("Breadcrumb"),
                ),
            ),
        ),
        class_name="p-8",
    )


# Additional examples


def breadcrumb_simple():
    """Simple breadcrumb without dropdown"""
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="/"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Products", href="/products"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Electronics", href="/products/electronics"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page("Laptop"),
                ),
            ),
        ),
        class_name="p-8",
    )


def breadcrumb_with_icons():
    """Breadcrumb with icons"""
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="home", size=14),
                        "Home",
                        href="/",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="folder", size=14),
                        "Documents",
                        href="/documents",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page(
                        rx.icon(tag="file-text", size=14),
                        "README.md",
                    ),
                ),
            ),
        ),
        class_name="p-8",
    )


def breadcrumb_custom_separator():
    """Breadcrumb with custom separator"""
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="/"),
                ),
                breadcrumb_separator(
                    rx.text("/", class_name="text-[var(--muted-foreground)]")
                ),
                breadcrumb_item(
                    breadcrumb_link("Blog", href="/blog"),
                ),
                breadcrumb_separator(
                    rx.text("/", class_name="text-[var(--muted-foreground)]")
                ),
                breadcrumb_item(
                    breadcrumb_page("Article"),
                ),
            ),
        ),
        class_name="p-8",
    )
