from __future__ import annotations

from reflex.experimental import ClientStateVar

from buridan_ui.config import VERSION
from buridan_ui.static.scripts import count_python_files_in_folder
from buridan_ui.templates.sidemenu.scripts import SideBarScript
from buridan_ui.static.routes import (
    ChartRoutes,
    PantryRoutes,
    GettingStartedRoutes,
    BuridanProRoutes,
)

import reflex as rx


# Centralized state variables with localStorage persistence
SIDEBAR_STATES = {
    "site_settings": ClientStateVar.create("site_settings", False),
    "getting_started": ClientStateVar.create("getting_started", False),
    "chart": ClientStateVar.create("chart", False),
    "pantry": ClientStateVar.create("pantry", False),
    "pro": ClientStateVar.create("pro", False),
}


def get_icon_box_style():
    """Generate consistent icon box styling."""
    return {
        "_hover": {"background": rx.color("gray", 3)},
        "border": f"0.81px solid {rx.color('gray', 5)}",
        "class_name": "flex flex-row cursor-pointer rounded-md flex items-center justify-center align-center py-1 px-2",
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
            rx.box(
                rx.el.div(
                    rx.icon(
                        "github",
                        size=11,
                        color=rx.color("slate", 12),
                    ),
                    rx.el.p(
                        "GitHub",
                        class_name="text-sm",
                        color=rx.color("slate", 12),
                    ),
                    class_name="flex flex-row items-center gap-x-2",
                ),
                **icon_box_style,
            ),
            href="https://github.com/buridan-ui/ui",
            is_external=True,
        )

    else:
        icon_component = rx.box(
            rx.color_mode.icon(
                light_component=rx.el.div(
                    rx.icon(
                        "moon",
                        size=11,
                        color=rx.color("slate", 12),
                    ),
                    rx.el.p(
                        "Dark",
                        class_name="text-sm",
                        color=rx.color("slate", 12),
                    ),
                    class_name="flex flex-row items-center gap-x-2",
                ),
                dark_component=rx.el.div(
                    rx.icon(
                        "sun",
                        size=11,
                        color=rx.color("slate", 12),
                    ),
                    rx.el.p(
                        "Light",
                        class_name="text-sm",
                        color=rx.color("slate", 12),
                    ),
                    class_name="flex flex-row items-center gap-x-2",
                ),
            ),
            title="Toggle theme",
            on_click=rx.toggle_color_mode,
            **icon_box_style,
        )

    return rx.el.div(
        rx.el.label(title, class_name="text-sm font-regular"),
        rx.el.div(icon_component),
        class_name="w-full flex flex-row justify-between align-center items-center",
    )


def side_bar_wrapper(title: str, component, state_key: str):
    """Create a sidebar section with toggle functionality."""
    state = SIDEBAR_STATES[state_key]

    return rx.el.div(
        state,
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    title, color=rx.color("slate", 12), class_name="text-sm font-bold"
                ),
                (
                    rx.hover_card.root(
                        rx.hover_card.trigger(
                            rx.icon(
                                tag="info",
                                class_name="size-4 cursor-pointer",
                                color=rx.color("slate", 11),
                            ),
                        ),
                        rx.hover_card.content(
                            rx.el.div(
                                rx.el.label(
                                    "Buridan Pro (coming soon)",
                                    class_name="text-xs font-bold",
                                ),
                                rx.el.label(
                                    "Unlock advanced components and features with a Pro subscription.",
                                    class_name="text-xs",
                                ),
                                class_name="flex flex-col gap-y-2",
                            ),
                            size="1",
                            width="250px",
                        ),
                    )
                    if state_key == "pro"
                    else rx.spacer()
                ),
                class_name="flex flex-row items-center gap-x-2",
            ),
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


def create_section_description(text_parts):
    """Create a consistent section description."""
    return rx.el.label(
        *text_parts,
        color=rx.color("gray", 12),
        class_name="text-sm font-light pt-1 pb-2",
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
        # download_site_source(),
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

    pro_count = count_python_files_in_folder("buridan_ui/pro")
    pro_components_content = rx.el.div(
        create_section_description(
            [
                "Get access to ",
                rx.el.span(
                    f"{pro_count} ",
                    class_name="text-sm font-bold",
                    color=rx.color("slate", 12),
                ),
                "carefully designed block to build dashboards and data apps even faster.",
            ]
        ),
        rx.el.div(
            create_sidebar_menu_items(BuridanProRoutes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )

    pantry_count = count_python_files_in_folder("buridan_ui/pantry")
    pantry_components_content = rx.el.div(
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

    # Header component
    header = rx.el.div(
        rx.el.div(
            rx.link(
                rx.el.label(
                    "buridan/ui",
                    class_name="text-sm font-bold flex items-center align-center gap-x-2 cursor-pointer",
                    color=rx.color("slate", 12),
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
        side_bar_wrapper("Data App Components", pro_components_content, "pro"),
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
        on_mount=rx.call_script(SideBarScript),
    )


def sidemenu_right():
    from buridan_ui.wrappers.base.main import create_responsive_display

    return rx.scroll_area(
        rx.el.div(
            border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
            class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[99] bg-background",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.el.label(
                        "Reflex Build",
                        class_name="text-sm font-bold",
                        color=rx.color("slate", 12),
                    ),
                    rx.el.label(
                        "Build smarter, faster, and more efficiently with Reflex's AI builder.",
                        class_name="text-sm font-light pt-1 pb-2",
                        color=rx.color("gray", 12),
                    ),
                    rx.el.label(
                        "Reflex streamlines Python app development with powerful AI tools and seamless deployment.",
                        class_name="text-sm font-light pt-1 pb-2",
                        color=rx.color("gray", 12),
                    ),
                    rx.link(
                        rx.el.div(
                            rx.el.label(
                                "Start Building",
                                class_name="text-sm underline hover:cursor-pointer",
                            ),
                            class_name="flex felx-row items-center justify-between gap-x-2",
                        ),
                        href="https://reflex.build/",
                        is_external=True,
                    ),
                    class_name="flex flex-col w-full h-full p-2 gap-y-2",
                ),
                color=rx.color("gray", 4),
                class_name="flex flex-col gap-y-2 w-full",
            ),
            class_name=" w-full px-1 py-2 " + "border-l border-dashed border-slate-500",
        ),
        rx.divider(class_name="h-[10px] opacity-0"),
        rx.box(
            rx.box(
                rx.box(
                    rx.el.label(
                        "Notice",
                        class_name="text-sm font-bold",
                        color=rx.color("slate", 12),
                    ),
                    rx.el.label(
                        "We’re upgrading our UI library with Tailwind CSS for faster, cleaner, and more customizable designs.",
                        class_name="text-sm font-light pt-1 pb-2",
                        color=rx.color("gray", 12),
                    ),
                    rx.el.label(
                        "You may notice styling updates as we roll out improvements.",
                        class_name="text-sm font-light pt-1 pb-2",
                        color=rx.color("gray", 12),
                    ),
                    rx.el.label(
                        "Thanks for being part of the journey!",
                        class_name="text-sm font-light pt-1 pb-2",
                        color=rx.color("gray", 12),
                    ),
                    class_name="flex flex-col px-2 gap-y-2",
                ),
                color=rx.color("amber", 5),
                class_name="flex flex-col gap-y-2 w-full" + "",
            ),
            class_name="w-full px-1 py-2 " + "border-l border-dashed border-orange-500",
        ),
        height="100vh",
        class_name="flex flex-col max-w-[280px] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[4rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[1rem] pt-12",
        display=create_responsive_display("none", "flex"),
    )
