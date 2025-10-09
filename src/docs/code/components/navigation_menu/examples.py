import reflex as rx
from .navigation_menu import (
    navigation_menu_item,
    navigation_menu_trigger,
    navigation_menu_list,
    navigation_menu,
    navigation_menu_link,
    navigation_menu_content,
)


def list_item(title: str, href: str):
    """Helper for list items with icon."""
    return rx.el.li(
        rx.link(title, href=href, class_name="text-sm font-medium"),
        class_name="p-2",
    )


def navigation_example():
    """Clean navigation menu example."""

    products = [
        {
            "title": "Analytics",
            "href": "/products/analytics",
            "description": "Track user behavior and gain insights",
        },
        {
            "title": "Marketing",
            "href": "/products/marketing",
            "description": "Create and manage campaigns",
        },
        {
            "title": "Commerce",
            "href": "/products/commerce",
            "description": "Sell products online with ease",
        },
        {
            "title": "Insights",
            "href": "/products/insights",
            "description": "Make data-driven decisions",
        },
    ]

    resources = [
        {
            "title": "Documentation",
            "href": "/docs",
            "description": "Learn how to integrate our products",
        },
        {
            "title": "API Reference",
            "href": "/docs/api",
            "description": "Complete API documentation",
        },
        {"title": "Guides", "href": "/guides", "description": "Step-by-step tutorials"},
        {"title": "Blog", "href": "/blog", "description": "Latest news and updates"},
    ]

    company = [
        {
            "title": "About",
            "href": "/about",
            "description": "Learn about our mission and values",
        },
        {
            "title": "Careers",
            "href": "/careers",
            "description": "Join our growing team",
        },
        {
            "title": "Contact",
            "href": "/contact",
            "description": "Get in touch with our team",
        },
    ]

    def create_dropdown(title: str, items: list):
        """Create a navigation dropdown menu."""
        return navigation_menu_item(
            navigation_menu_trigger(rx.el.button(title)),
            navigation_menu_content(
                rx.el.ul(
                    *[
                        list_item(title=item["title"], href=item["href"])
                        for item in items
                    ],
                    class_name="flex flex-col w-[240px] px-2 py-0 bg-[var(--popover)] border border-[var(--input)] rounded-md shadow-lg mt-10",
                ),
            ),
        )

    return rx.box(
        navigation_menu(
            navigation_menu_list(
                create_dropdown("Products", products),
                create_dropdown("Resources", resources),
                create_dropdown("Company", company),
                # Simple link
                navigation_menu_item(
                    navigation_menu_link(
                        "Pricing",
                        href="/pricing",
                        class_name=(
                            "text-sm font-medium h-8 px-2 py-0 rounded-md bg-transparent "
                            "hover:bg-[var(--muted)] inline-flex items-center transition-colors"
                        ),
                    ),
                ),
                class_name="flex flex-row items-center gap-0.5",
            ),
            viewport=True,
            delay_duration=200,
            skip_delay_duration=300,
            class_name="relative",
        ),
        class_name="flex justify-center w-full py-6",
    )
