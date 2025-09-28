import reflex as rx
from src.config import VERSION
from src.static.scripts import count_python_files_in_folder
from src.templates.sidemenu.scripts import SideBarScript
from src.static.routes import (
    ChartRoutes,
    PantryRoutes,
    GettingStartedRoutes,
)

ICON_BOX_STYLE = {
    "_hover": {"background": rx.color("gray", 3)},
    "border": f"0.81px solid {rx.color('gray', 5)}",
    "class_name": "flex flex-row cursor-pointer rounded-md flex items-center justify-center align-center py-1 px-1",
}

SIDEBAR_CLASSES = "hidden xl:flex flex-col max-w-[300px] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[4rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[1rem]"


def create_section_description(text_parts):
    """Create a consistent section description."""
    return rx.el.label(
        *text_parts,
        color=rx.color("gray", 12),
        class_name="text-sm font-light pt-1 pb-2",
    )


def create_sidebar_menu_items(routes: list[dict[str, str]]):
    """Create menu items from routes."""

    def item(data):
        return rx.el.div(
            rx.link(
                rx.el.label(
                    data["name"],
                    color=rx.color("slate", 12),
                    class_name="cursor-pointer text-sm font-regular",
                ),
                href=data["path"],
                text_decoration="none",
            ),
            class_name="w-full",
            id=data["path"],
        )

    return rx.box(
        rx.foreach(routes, item),
        class_name="w-full flex flex-col gap-y-0",
    )


def _create_github_link():
    """Create GitHub link component."""
    return rx.link(
        rx.box(
            rx.el.div(
                rx.icon("github", size=11, color=rx.color("slate", 12)),
                rx.el.p("GitHub", class_name="text-sm", color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
            **ICON_BOX_STYLE,
        ),
        href="https://github.com/buridan-ui/ui",
        is_external=True,
    )


def _create_theme_toggle():
    """Create theme toggle component."""
    return rx.box(
        rx.color_mode.icon(
            light_component=rx.el.div(
                rx.icon("moon", size=11, color=rx.color("slate", 12)),
                rx.el.p("Dark", class_name="text-sm", color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
            dark_component=rx.el.div(
                rx.icon("sun", size=11, color=rx.color("slate", 12)),
                rx.el.p("Light", class_name="text-sm", color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
        ),
        title="Toggle theme",
        on_click=rx.toggle_color_mode,
        **ICON_BOX_STYLE,
    )


def _menu_settings(title: str, icon: str, is_theme=False):
    """Create a menu settings item."""
    icon_component = _create_theme_toggle() if is_theme else _create_github_link()

    return rx.el.div(
        rx.el.label(title, class_name="text-sm font-regular"),
        rx.el.div(icon_component),
        class_name="w-full flex flex-row justify-between align-center items-center",
    )


def side_bar_wrapper(title: str, component: rx.Component):
    """Create a sidebar section with toggle functionality."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    title, color=rx.color("slate", 12), class_name="text-sm font-bold"
                ),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="w-full flex flex-row justify-between align-center items-center",
        ),
        component,
        class_name="flex flex-col w-full gap-y-2 p-4",
    )


def _create_header():
    """Create the sidebar header."""
    return rx.el.div(
        rx.el.div(
            rx.link(
                rx.box(
                    rx.text(
                        "buridan",
                        font_weight="700",
                        font_size="1rem",
                        letter_spacing="-0.04em",
                    ),
                    rx.text(
                        ".UI",
                        font_size="0.6rem",
                        position="relative",
                        font_weight="600",
                    ),
                    color=rx.color("slate", 12),
                    class_name="flex flex-row items-baseline gap-x-[1px]",
                ),
                text_decoration="none",
                href="/",
            ),
            rx.el.label(
                VERSION,
                class_name="text-xs font-medium",
                color=rx.color("slate", 11),
            ),
            class_name="w-full flex flex-row justify-between items-baseline",
        ),
        class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[99] backdrop-blur-md",
    )


def _create_site_settings_content():
    """Create site settings section content."""
    return rx.vstack(
        create_section_description(
            [
                "The visual appearance of the site can be customized using the theme settings."
            ]
        ),
        _menu_settings("Light/Dark Mode", "", True),
        _menu_settings("Source", "github"),
        spacing="2",
    )


def _create_getting_started_content():
    """Create getting started section content."""
    return rx.el.div(
        create_section_description(
            ["Quickly set up and get started with the basics of buridan/ui."]
        ),
        rx.el.div(
            create_sidebar_menu_items(GettingStartedRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def _create_chart_components_content():
    """Create chart components section content."""
    chart_count = count_python_files_in_folder("src/charts")
    return rx.el.div(
        create_section_description(
            [
                "A collection of ",
                rx.el.span(
                    f"{chart_count} ",
                    class_name="text-sm font-bold",
                    color=rx.color("slate", 12),
                ),
                "chart components to help visualize data, build dashboards, and more.",
            ]
        ),
        rx.el.div(
            create_sidebar_menu_items(ChartRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def _create_pantry_components_content():
    """Create pantry components section content."""
    pantry_count = count_python_files_in_folder("src/pantry")
    return rx.el.div(
        create_section_description(
            [
                "A set of ",
                rx.el.span(
                    f"{pantry_count} ",
                    class_name="text-sm font-bold",
                    color=rx.color("slate", 12),
                ),
                "components to help build and customize your interface with ease.",
            ]
        ),
        rx.el.div(
            create_sidebar_menu_items(PantryRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def sidemenu(in_drawer=False):
    """Main sidemenu component."""

    # Main content
    content = rx.el.div(
        # _create_header(),
        side_bar_wrapper("Getting Started", _create_getting_started_content()),
        side_bar_wrapper("Chart Components", _create_chart_components_content()),
        side_bar_wrapper("Pantry Components", _create_pantry_components_content()),
        class_name="flex flex-col w-full h-full",
    )

    # Wrap in scroll area
    return rx.box(
        rx.scroll_area(
            content,
            # height="100vh",
            # class_name=SIDEBAR_CLASSES,
            on_mount=rx.call_script(SideBarScript),
            class_name="flex flex-col items-center gap-y-4",
        ),
        # class_name="sticky top-0 left-0 h-screen",
        class_name="hidden xl:flex max-w-[18rem] w-full sticky top-0 max-h-[100vh] z-[10] pb-5",
    )
