import reflex as rx
import src.routes as routes

from typing import List
from dataclasses import dataclass

from src.hooks import selected_page


@dataclass
class SidebarSection:
    """Configuration for a sidebar section."""

    title: str
    description: str
    routes: list[dict]


SIDEBAR_SECTIONS = [
    SidebarSection(
        title="Getting Started",
        description="Quickly set up and get started with the basics of buridan/ui.",
        routes=routes.GET_STARTED_URLS,
    ),
    SidebarSection(
        title="Wrapped React Components",
        description="Explore React components elegantly wrapped for Reflex",
        routes=routes.WRAPPED_COMPONENTS_URLS,
    ),
    SidebarSection(
        title="JavaScript Integrations",
        description="Learn how to extend Reflex apps with native JavaScript libraries.",
        routes=routes.JS_INTEGRATIONS_URLS,
    ),
    SidebarSection(
        title="Charts",
        description="A collection of chart components to help visualize data, build dashboards, and more.",
        routes=routes.CHARTS_URLS,
    ),
    SidebarSection(
        title="Components",
        description="Core components to help you build beautiful and visually consistent applications.",
        routes=routes.BASE_UI_COMPONENTS,
    ),
    # SidebarSection(
    #     title="Components",
    #     description="Core components to help you build beautiful and visually consistent applications.",
    #     routes=routes.COMPONENTS_URLS,
    # ),
]


def create_section_description(text: str):
    """Create a consistent section description."""
    return rx.el.label(
        text,
        class_name="text-sm font-medium pt-1 pb-2 text-muted-foreground",
    )


def create_menu_item(data: dict):
    """Create a single menu item."""
    return rx.el.div(
        rx.el.a(
            rx.el.label(
                data["title"],
                color=rx.color("slate", 12),
                class_name="cursor-pointer text-sm "
                + rx.cond(
                    selected_page.value == data["url"], "font-bold", "font-regular"
                ).to(str),
            ),
            to=f"/{data['url']}",
            text_decoration="none",
        ),
        class_name="w-full",
        id=data["url"],
    )


def create_sidebar_menu_items(routes: List[dict]):
    """Create menu items from routes."""
    return rx.box(
        *[create_menu_item(route) for route in routes],
        class_name="w-full flex flex-col gap-y-0",
    )


def create_section_content(section: SidebarSection):
    """Create content for a sidebar section."""
    return rx.el.div(
        # create_section_description(section.description),
        rx.el.div(
            create_sidebar_menu_items(section.routes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def sidebar_section(section: SidebarSection):
    """Create a complete sidebar section with title and content."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    section.title,
                    color=rx.color("slate", 12),
                    class_name="text-sm font-bold",
                ),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="w-full flex flex-row justify-between align-center items-center",
        ),
        create_section_content(section),
        class_name="flex flex-col w-full gap-y-2 p-4",
    )


def sidebar(in_drawer=False):
    """Main sidebar component."""
    content = rx.el.div(
        *[sidebar_section(section) for section in SIDEBAR_SECTIONS],
        class_name="flex flex-col max-w-[18rem] w-full h-full",
    )

    drawer_classes = "flex flex-col w-full h-full"
    default_classes = (
        "hidden xl:flex max-w-[18rem] w-full sticky top-12 max-h-[100vh] z-[10] pb-5"
    )

    return rx.el.div(
        rx.scroll_area(
            content,
            class_name="flex flex-col items-center gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]",
        ),
        class_name=drawer_classes if in_drawer else default_classes,
    )
