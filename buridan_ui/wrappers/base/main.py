from functools import wraps
from typing import Callable, List, Optional

import reflex as rx
from reflex.experimental import ClientStateVar

from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import desktop_footer, footer
from buridan_ui.templates.sidemenu.sidemenu import sidemenu

from buridan_ui.wrappers.base.utils.routes import base_content_path_ui


Chart_Theme = ClientStateVar.create("chart_theme", "")


def create_responsive_display(
    small_screens: str, large_screens: str, breakpoint: int = 3
):
    """Create a responsive display list for different screen sizes.

    Args:
        small_screens: Display value for small screens
        large_screens: Display value for large screens
        breakpoint: Index where display changes (default: 3)

    Returns:
        List of display values for different breakpoints
    """
    return [small_screens if i <= breakpoint else large_screens for i in range(6)]


def create_border(
    color_name: str = "gray",
    shade: int = 5,
    style: str = "dashed",
    width: str = "1.25px",
):
    """Create a consistent border style.

    Args:
        color_name: Color name from the theme
        shade: Color shade from 1-12
        style: Border style (solid, dashed, etc.)
        width: Border width

    Returns:
        Formatted border string
    """
    return f"{width} {style} {rx.color(color_name, shade)}"


def create_icon(tag: str, size: int = 13):
    """Create a consistently styled icon.

    Args:
        tag: Icon name
        size: Icon size

    Returns:
        Icon component
    """
    return rx.icon(tag=tag, size=size, color=rx.color("slate", 11))


def base_footer_responsive(
    component: rx.Component, small_screens: str, large_screens: str
):
    """Create a responsive footer component.

    Args:
        component: Footer component to display
        small_screens: Display value for small screens
        large_screens: Display value for large screens

    Returns:
        Responsive footer component
    """
    return rx.box(
        component,
        display=create_responsive_display(small_screens, large_screens),
        width="100%",
    )


def create_meta_item(icon_tag: str, label_text: str, title: Optional[str] = None):
    """Create a metadata item with icon and label.

    Args:
        icon_tag: Icon name
        label_text: Text to display
        title: Optional title attribute

    Returns:
        Metadata item component
    """
    return rx.el.div(
        create_icon(icon_tag),
        rx.el.label(
            label_text,
            class_name="text-sm",
        ),
        class_name="flex flex-row items-center justify-start gap-x-2",
        title=title,
    )


def page_meta(created: str, updated: str, dir_count: int):
    """Create page metadata component showing creation date, update date, and component count.

    Args:
        created: Creation date string
        updated: Last update date string
        dir_count: Number of components

    Returns:
        Page metadata component
    """
    return rx.el.div(
        create_meta_item("file-plus-2", created, "Created On"),
        create_meta_item("file-pen-line", updated, "Last Update"),
        create_meta_item("cuboid", f"{dir_count} Component(s)"),
        class_name="flex flex-row flex-wrap items-center gap-x-6 gap-y-4",
    )


def create_pattern_background():
    """Create a patterned background element.

    Returns:
        Patterned background component
    """
    return rx.box(
        border_left=create_border(),
        border_right=create_border(),
        color=rx.color("gray", 3),
        class_name="h-full p-3 col-start-2 row-span-full row-start-1 max-sm:hidden bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
    )


ActiveTab = ClientStateVar.create("active_tab", 0)


def tab_selector(tabs=["Preview", "Code"]):
    return rx.box(
        rx.hstack(
            *[
                rx.button(
                    rx.icon(
                        tag=tab,
                        color=rx.cond(
                            ActiveTab.value == i,
                            rx.color("slate", 12),  # Active text color
                            rx.color("slate", 10),  # Inactive text color
                        ),
                    ),
                    on_click=[
                        rx.call_function(ActiveTab.set_value(i)),
                    ],
                    aria_disabled="false",
                    background=rx.cond(
                        ActiveTab.value == i,
                        rx.color("gray", 3),  # Active background color
                        "transparent",  # Inactive background (transparent)
                    ),
                    cursor="pointer",
                    class_name=rx.cond(
                        ActiveTab.value == i,
                        # Active tab styling (without color references)
                        "group inline-flex items-center justify-center whitespace-nowrap py-2 align-middle font-semibold "
                        "transition-all duration-300 ease-in-out min-w-[32px] "
                        "gap-1.5 text-xs "
                        "h-6 w-full rounded-md px-3 drop-shadow sm:w-auto",
                        # Inactive tab styling (without color references)
                        "group inline-flex items-center justify-center whitespace-nowrap rounded-lg py-2 align-middle "
                        "font-semibold transition-all duration-300 ease-in-out "
                        "min-w-[32px] gap-1.5 text-xs "
                        "h-6 w-full bg-transparent px-3 sm:w-auto",
                    ),
                )
                for i, tab in enumerate(tabs)
            ],
            class_name="inline-flex h-8.5 w-full items-baseline justify-start rounded-lg p-1 sm:w-auto",
            border=create_border(),
        )
    )


def theme_option(
    name: str, arabic_name: str, color_class: str, color_var: str
) -> rx.Component:
    return rx.popover.close(
        rx.el.div(
            rx.el.button(
                f"{name} {arabic_name}",
                class_name="w-full text-left",
                type="button",
            ),
            rx.el.div(
                style={"backgroundColor": f"var(--{color_var})"},
                class_name=f"h-2 w-2 rounded {color_class}",
            ),
            on_click=[
                rx.call_function(Chart_Theme.set_value(color_class).to(str)),
                rx.call_script(
                    """
                    document.querySelectorAll('.recharts-wrapper').forEach(chart => {
                      chart.style.display = 'none';
                      void chart.offsetHeight;
                      chart.style.display = '';
                    });
                    """
                ),
            ],
            class_name="flex flex-row gap-x-2 items-center px-3 py-2 w-full justify-between hover:px-4 transition-[padding] duration-200 ease-out cursor-pointer",
        )
    )


def theme_select_menu():
    return rx.box(
        rx.popover.root(
            rx.popover.trigger(
                rx.el.button(
                    "Chart Theme",
                    rx.el.div(
                        style={"backgroundColor": "var(--chart-2)"},
                        class_name=f"h-2 w-2 rounded-full {Chart_Theme.value.to(str)}",
                    ),
                    class_name="text-sm px-2 font-semibold flex flex-row justify-between items-center gap-x-4 rounded-md",
                    type="button",
                    color=rx.color("slate", 11),
                ),
            ),
            rx.popover.content(
                rx.box(
                    theme_option("Feyrouz", "فيْروز", "theme-blue", "chart-2"),
                    rx.divider(
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        bg="transparent",
                    ),
                    theme_option("Yaqout", "يَاقوت", "theme-red", "chart-2"),
                    rx.divider(
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        bg="transparent",
                    ),
                    theme_option("Zumurrud", "زُمُرُّد", "theme-green", "chart-2"),
                    rx.divider(
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        bg="transparent",
                    ),
                    theme_option("Kahraman", "كَهْرَمان", "theme-amber", "chart-2"),
                    rx.divider(
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        bg="transparent",
                    ),
                    theme_option("Amethyst", "أَمِيثِسْت", "theme-purple", "chart-2"),
                    class_name="bg-background w-[160px] flex flex-col text-sm rounded-md shadow-md",
                    border=f"1.25px dashed {rx.color('gray', 4)}",
                ),
                side="left",
                side_offset=15,
                class_name="items-center bg-transparent !shadow-none !p-0 border-none w-auto overflow-visible font-sans pointer-events-auto",
            ),
        ),
        style={
            "display": "inline-flex",
            "height": "1.925rem",
            "align_items": "baseline",
            "justify_content": "flex-start",
            "padding": "0.25rem",
            "border": f"1.25px dashed {rx.color('gray', 4)}",
        },
        class_name="rounded-md",
    )


def create_header(url: str):
    """Create the page header component.

    Args:
        url: Current page URL

    Returns:
        Header component
    """

    return rx.el.div(
        rx.el.label(
            base_content_path_ui(url),
            class_name="text-sm font-bold font-sans flex items-center align-center gap-x-2",
            display=create_responsive_display("none", "flex"),
        ),
        rx.el.label(
            "buridan/ui",
            class_name="text-sm font-bold font-sans flex items-center align-center gap-x-2",
            display=create_responsive_display("flex", "none"),
        ),
        rx.el.div(
            theme_select_menu()
            if url.startswith("/charts/")
            else rx.box(class_name="hidden"),
            rx.box(
                drawer(),
                display=create_responsive_display("flex", "none"),
            ),
            class_name="flex flex-row gap-x-2",
        ),
        border_bottom=create_border(),
        class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[20] flex flex-row justify-between align-center items-center gap-x-2 bg-background",
    )


def create_title_section(page_name: str, meta_component: rx.Component):
    """Create the title section component.

    Args:
        page_name: Page title
        meta_component: Metadata component

    Returns:
        Title section component
    """
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                page_name,
                class_name="text-4xl sm:4xl font-bold py-6",
            ),
            meta_component,
            class_name="w-full justify-start flex flex-col pb-9 pl-4",
        ),
        class_name="flex flex-col p-0 gap-y-2 min-h-[100vh] w-full",
    )


def create_footer_section():
    """Create the footer section component.

    Returns:
        Footer section component
    """
    return rx.el.div(
        base_footer_responsive(desktop_footer(), "none", "flex"),
        base_footer_responsive(footer(), "flex", "none"),
        class_name="flex flex-col w-full lg:px-4 xl:px-4 px-1 py-2",
        border_top=create_border(),
    )


def generate_reference_links(chart_data, name):
    return [
        rx.el.a(
            "Installation",
            href=f"{chart_data['url']}#{chart_data['id_prefix']}-installation",
            id=f"{chart_data['id_prefix']}-installation",  # Add ID here
            color=rx.color("slate", 11),
            class_name="cursor-pointer text-sm font-regular hover:underline",
        ),
        rx.el.a(
            "Chart Theme",
            href=f"{chart_data['url']}#{chart_data['id_prefix']}-theme",
            id=f"{chart_data['id_prefix']}-theme",  # Add ID here
            color=rx.color("slate", 11),
            class_name="cursor-pointer text-sm font-regular hover:underline",
        ),
        rx.el.a(
            "API Reference",
            href=f"{chart_data['url']}#{chart_data['id_prefix']}-reference",
            id=f"{chart_data['id_prefix']}-reference",  # Add ID here
            color=rx.color("slate", 11),
            class_name="cursor-pointer text-sm font-regular hover:underline",
        ),
    ]


def table_of_content(name: str):
    charts = {
        "Bar Charts": {
            "url": "/charts/bar-charts",
            "id_prefix": "bar",
            "quantity": 10,
        },
        "Area Charts": {
            "url": "/charts/area-charts",
            "id_prefix": "area",
            "quantity": 8,
        },
    }

    if name in charts:
        chart_data = charts[name]
        links = [
            rx.el.a(
                f"{name} v{i + 1}",
                href=f"{chart_data['url']}#{chart_data['id_prefix']}-v{i + 1}",
                id=f"{chart_data['id_prefix']}-v{i + 1}",  # Add ID here
                color=rx.color("slate", 11),
                class_name="cursor-pointer text-sm font-regular hover:underline",
            )
            for i in range(chart_data["quantity"])
        ]
        refs = generate_reference_links(chart_data, name)
    else:
        links = []
        refs = []

    return rx.scroll_area(
        rx.el.div(
            border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
            class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[99] bg-background",
        ),
        rx.box(
            rx.el.label(
                f"{name} Examples",
                color=rx.color("slate", 12),
                class_name="text-sm font-bold",
            ),
            *links,
            rx.el.label(
                "API", color=rx.color("slate", 12), class_name="text-sm font-bold pt-6"
            ),
            *refs,
            class_name="flex flex-col w-full gap-y-2 p-4",
        ),
        height="100vh",
        class_name="flex flex-col max-w-[260px] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[4rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[1rem] pt-12",
        # on_mount=rx.call_script(TableOfContentScript),  # Make sure to call the highlight script
    )


def base(url: str, page_name: str, dir_meta: List[str | int] = []):
    """Create a base page template.

    Args:
        url: Current page URL
        page_name: Page title
        dir_meta: List containing [created_date, updated_date, dir_count]

    Returns:
        Decorated function that returns the template
    """

    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        def template():
            # Get the page content
            contents = content()

            # Create metadata component or hidden div
            if dir_meta:
                created, updated, dir_count = dir_meta
                meta = page_meta(created, updated, dir_count)
            else:
                meta = rx.el.div(class_name="hidden")

            # Create title section with content items
            content_section = create_title_section(page_name, meta)

            # Add content items to the content section
            for item in contents:
                content_section.children.append(item)

            # Create the main layout
            return rx.hstack(
                sidemenu(),
                create_pattern_background(),
                rx.scroll_area(
                    create_header(url),
                    content_section,
                    create_footer_section(),
                    class_name="flex flex-col w-full gap-y-2 align-start z-[10] pt-14 [&_.rt-ScrollAreaScrollbar]:mt-[4rem] [&_.rt-ScrollAreaScrollbar]:mb-[1rem]",
                    height=["100%" if i == 0 else "100vh" for i in range(6)],
                ),
                create_pattern_background(),
                # sidemenu_right(),
                table_of_content(name=page_name),
                class_name="w-[100%] h-[100vh] gap-x-0 bg-background",
            )

        return template

    return decorator
