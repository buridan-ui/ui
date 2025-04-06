from __future__ import annotations

from reflex.constants.colors import Color
from reflex.experimental import ClientStateVar

from buridan_ui.config import VERSION
from buridan_ui.static.scripts import count_python_files_in_folder
from buridan_ui.templates.sidemenu.download import download_site_source
from buridan_ui.static.routes import ChartRoutes, PantryRoutes, GettingStartedRoutes

import reflex as rx

# Centralized state variables
SIDEBAR_STATES = {
    "site_settings": ClientStateVar.create("site_settings", False),
    "getting_started": ClientStateVar.create("getting_started", False),
    "chart": ClientStateVar.create("chart", False),
    "pantry": ClientStateVar.create("pantry", False),
}


# Common styling functions
def get_text_style(is_bold=False, additional_classes=""):
    """Generate consistent text styling."""
    weight = "font-bold" if is_bold else "font-regular"
    return f"text-sm {weight} {additional_classes} " + rx.color_mode_cond(
        "text-slate-700", "text-slate-200"
    ).to(str)


def get_icon_box_style():
    """Generate consistent icon box styling."""
    return {
        "_hover": {"background": rx.color("gray", 3)},
        "border": f"0.81px solid {rx.color('gray', 5)}",
        "class_name": "flex flex-row cursor-pointer rounded-md flex items-center justify-center align-center p-1",
    }


def create_icon(tag, size=11):
    """Create a consistently styled icon."""
    return rx.icon(
        tag=tag,
        size=size,
        color=rx.color("slate", 11),
        _hover={"color": rx.color("slate", 12)},
    )


def _menu_settings(title: str, icon: str, is_theme=False):
    """Create a menu settings item."""
    icon_box_style = get_icon_box_style()

    if not is_theme:
        icon_component = rx.link(
            rx.box(create_icon(icon), **icon_box_style),
            href="https://github.com/buridan-ui/ui",
            is_external=True,
        )
    else:
        icon_component = rx.box(
            rx.color_mode.icon(
                light_component=rx.icon("moon", size=11, color=rx.color("slate", 11)),
                dark_component=rx.icon("sun", size=11, color=rx.color("slate", 11)),
            ),
            title="Toggle theme",
            on_click=rx.toggle_color_mode,
            **icon_box_style,
        )

    return rx.el.div(
        rx.el.label(title, class_name=get_text_style()),
        rx.el.div(icon_component),
        class_name="w-full flex flex-row justify-between align-center items-center",
    )


def side_bar_wrapper(title: str, component, state_key: str):
    """Create a sidebar section with toggle functionality."""
    state = SIDEBAR_STATES[state_key]

    return rx.el.div(
        state,
        rx.el.div(
            rx.el.label(title, class_name=get_text_style(is_bold=True)),
            rx.el.div(
                rx.box(
                    rx.cond(
                        state.value,
                        create_icon("plus"),
                        create_icon("minus"),
                    ),
                    **get_icon_box_style(),
                    on_click=rx.call_function(state.set_value(~state.value)),
                ),
            ),
            class_name="w-full flex flex-row justify-between align-center items-center",
        ),
        rx.cond(
            state.value,
            rx.el.div(class_name="hidden"),
            component,
        ),
        class_name="flex flex-col w-full gap-y-2 p-4",
    )


def create_sidebar_menu_items(routes: list[dict[str, str | Color]]):
    """Create menu items from routes."""

    def item(data):
        return rx.el.div(
            rx.link(
                rx.el.label(
                    data["name"],
                    _hover={"color": rx.color("slate", 12)},
                    class_name=get_text_style(additional_classes="cursor-pointer"),
                ),
                href=data["path"],
                text_decoration="none",
            ),
            class_name="w-full",
        )

    return rx.vstack(
        rx.foreach(routes, item),
        spacing="0",
        width="100%",
    )


def create_section_description(text_parts):
    """Create a consistent section description."""
    return rx.el.label(
        *text_parts,
        class_name="text-sm font-light pt-1 pb-2 "
        + rx.color_mode_cond("text-slate-700", "text-slate-200").to(str),
    )


def create_divider():
    """Create a consistent divider."""
    return rx.divider(
        border_bottom=f"1.25px dashed {rx.color('gray', 5)}", bg="transparent"
    )


def sidemenu(in_drawer=False):
    """Main sidemenu component."""
    # Display logic for responsive design
    sidebar_display = (
        ["none" if i <= 3 else "flex" for i in range(6)] if not in_drawer else "flex"
    )

    # Content for each section
    site_settings_content = rx.vstack(
        create_section_description(
            [
                "The visual appearance of the site can be customized using the theme settings."
            ]
        ),
        _menu_settings("Light/Dark Mode", "", True),
        download_site_source(),
        _menu_settings("Source", "github"),
        spacing="2",
    )

    getting_started_content = rx.el.div(
        create_section_description(
            ["Quickly set up and get started with the basics of buridan/ui."]
        ),
        rx.el.div(
            create_sidebar_menu_items(GettingStartedRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )

    chart_count = count_python_files_in_folder("buridan_ui/charts")
    chart_components_content = rx.el.div(
        create_section_description(
            [
                "A collection of ",
                rx.el.span(f"{chart_count} ", class_name="text-sm font-bold"),
                "chart components to help visualize data, build dashboards, and more.",
            ]
        ),
        rx.el.div(
            create_sidebar_menu_items(ChartRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )

    pantry_count = count_python_files_in_folder("buridan_ui/pantry")
    pantry_components_content = rx.el.div(
        create_section_description(
            [
                "A set of ",
                rx.el.span(f"{pantry_count} ", class_name="text-sm font-bold"),
                "components to help build and customize your interface with ease.",
            ]
        ),
        rx.el.div(
            create_sidebar_menu_items(PantryRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )

    # Header component
    header = rx.el.div(
        rx.el.div(
            rx.link(
                rx.el.label(
                    "buridan/ui",
                    class_name=get_text_style(
                        is_bold=True,
                        additional_classes="font-sans flex items-center align-center gap-x-2 cursor-pointer",
                    ),
                ),
                text_decoration="none",
                href="/",
            ),
            rx.el.label(
                VERSION,
                class_name="text-xs font-medium",
                color=rx.color("slate", 11),
            ),
            class_name="w-full flex flex-row justify-between align-end items-end",
        ),
        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
        class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[99] bg-background",
    )

    # Main content
    content = rx.el.div(
        header,
        side_bar_wrapper("Site Settings", site_settings_content, "site_settings"),
        create_divider(),
        side_bar_wrapper("Getting Started", getting_started_content, "getting_started"),
        create_divider(),
        side_bar_wrapper("Chart Components", chart_components_content, "chart"),
        create_divider(),
        side_bar_wrapper("Pantry Components", pantry_components_content, "pantry"),
        class_name="flex flex-col w-full h-full pt-12",
    )

    # Wrap in scroll area
    return rx.scroll_area(
        content,
        height="100vh",
        class_name="flex flex-col max-w-[300px] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[4rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[1rem]",
        display=sidebar_display,
    )
