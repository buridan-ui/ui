import reflex as rx


def breadcrumb(*children, **props):
    """Breadcrumb navigation container"""
    return rx.el.nav(
        *children, aria_label="breadcrumb", data_slot="breadcrumb", **props
    )


def breadcrumb_list(*children, class_name: str = "", **props):
    """Ordered list container for breadcrumb items"""
    base_classes = (
        "text-[var(--muted-foreground)] flex flex-wrap items-center gap-1 text-sm "
        "break-words sm:gap-2.5"
    )

    return rx.el.ol(
        *children,
        data_slot="breadcrumb-list",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_item(*children, class_name: str = "", **props):
    """Individual breadcrumb item"""
    base_classes = "inline-flex items-center gap-1.5"

    return rx.el.li(
        *children,
        data_slot="breadcrumb-item",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_link(*children, href: str = "#", class_name: str = "", **props):
    """Breadcrumb link (clickable)"""
    base_classes = "hover:text-[var(--foreground)] transition-colors no-underline"

    return rx.el.a(
        *children,
        href=href,
        data_slot="breadcrumb-link",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_page(*children, class_name: str = "", **props):
    """Current page breadcrumb (non-clickable)"""
    base_classes = "text-[var(--foreground)] font-normal"

    return rx.el.span(
        *children,
        role="link",
        aria_disabled="true",
        aria_current="page",
        data_slot="breadcrumb-page",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_separator(*children, class_name: str = "", **props):
    """Separator between breadcrumb items"""
    base_classes = "[&>svg]:size-3.5"

    # If no children provided, use chevron as default
    if not children:
        children = (rx.icon(tag="chevron-right", size=14),)

    return rx.el.li(
        *children,
        role="presentation",
        aria_hidden="true",
        data_slot="breadcrumb-separator",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_ellipsis(class_name: str = "", **props):
    """Ellipsis for collapsed breadcrumb items"""
    base_classes = "flex size-9 items-center justify-center"

    return rx.el.span(
        rx.icon(tag="ellipsis", size=16),
        rx.el.span("More", class_name="sr-only"),
        role="presentation",
        aria_hidden="true",
        data_slot="breadcrumb-ellipsis",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


# Example matching the shadcn BreadcrumbDemo


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
