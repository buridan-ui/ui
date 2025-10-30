import reflex as rx
from src.docs.library.base_ui.components.base.breadcrumb import (
    breadcrumb,
    breadcrumb_ellipsis,
    breadcrumb_item,
    breadcrumb_list,
    breadcrumb_link,
    breadcrumb_separator,
    breadcrumb_page,
)


def breadcrumb_demo():
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(),
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
                    breadcrumb_link("Components", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page("Breadcrumb"),
                ),
            ),
        ),
        class_name="p-8",
    )


def breadcrumb_simple():
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Products", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Electronics", href="#"),
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
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="home", size=14),
                        "Home",
                        href="#",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="folder", size=14),
                        "Documents",
                        href="#",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page(
                        rx.icon(tag="file-text", size=14),
                        "README.md",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
            ),
        ),
        class_name="p-8",
    )


def breadcrumb_custom_separator():
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(
                    rx.text("/", class_name="text-[var(--muted-foreground)]")
                ),
                breadcrumb_item(
                    breadcrumb_link("Blog", href="#"),
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
