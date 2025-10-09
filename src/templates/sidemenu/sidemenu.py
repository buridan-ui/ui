import reflex as rx
from reflex.experimental import ClientStateVar
from dataclasses import dataclass
from src.static.routes import (
    ChartRoutes,
    PantryRoutes,
    GettingStartedRoutes,
    ComponentRoutes,
)

selected_page = ClientStateVar.create("selected_page", "")


@dataclass
class SidebarSection:
    """Configuration for a sidebar section."""

    title: str
    description: str
    routes: list[dict[str, str]]


SIDEBAR_SECTIONS = [
    SidebarSection(
        title="Getting Started",
        description="Quickly set up and get started with the basics of buridan/ui.",
        routes=GettingStartedRoutes,
    ),
    SidebarSection(
        title="Components",
        description="Core components to help you build interactive, responsive, and visually consistent applications.",
        routes=ComponentRoutes,
    ),
    SidebarSection(
        title="Chart Components",
        description="A collection of chart components to help visualize data, build dashboards, and more.",
        routes=ChartRoutes,
    ),
    SidebarSection(
        title="Pantry Components",
        description="A set of components to help build and customize your interface with ease.",
        routes=PantryRoutes,
    ),
]


def create_section_description(text: str):
    """Create a consistent section description."""
    return rx.el.label(
        text,
        color=rx.color("gray", 12),
        class_name="text-sm font-medium pt-1 pb-2",
    )


def create_menu_item(data: dict[str, str]):
    """Create a single menu item."""
    return rx.el.div(
        rx.link(
            rx.el.label(
                data["name"],
                color=rx.color("slate", 12),
                class_name="cursor-pointer text-sm "
                + rx.cond(
                    selected_page.value == data["path"], "font-bold", "font-regular"
                ).to(str),
            ),
            href=data["path"],
            text_decoration="none",
        ),
        class_name="w-full "
        + rx.cond(selected_page.value == data["path"], "border-r", "").to(str),
        id=data["path"],
    )


def create_sidebar_menu_items(routes: list[dict[str, str]]):
    """Create menu items from routes."""
    return rx.box(
        rx.foreach(routes, create_menu_item),
        class_name="w-full flex flex-col gap-y-0",
    )


def create_section_content(section: SidebarSection):
    """Create content for a sidebar section."""
    return rx.el.div(
        create_section_description(section.description),
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


def sidemenu(in_drawer=False):
    """Main sidemenu component."""
    content = rx.el.div(
        *[sidebar_section(section) for section in SIDEBAR_SECTIONS],
        class_name="flex flex-col w-full h-full",
    )

    drawer_classes = "flex flex-col max-w-[18rem] h-full"
    default_classes = (
        "hidden xl:flex max-w-[18rem] w-full sticky top-0 max-h-[100vh] z-[10] pb-5"
    )

    return rx.box(
        rx.scroll_area(
            content,
            class_name="flex flex-col items-center gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]",
        ),
        class_name=drawer_classes if in_drawer else default_classes,
        on_mount=rx.call_script(
            """
            const url = window.location.pathname.replace(/\/$/, "");
            refs._client_state_setSelected_page(url);
            """
        ),
    )
