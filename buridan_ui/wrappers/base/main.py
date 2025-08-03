from functools import wraps
from typing import Callable, List, Optional

import reflex as rx
from reflex.experimental import ClientStateVar

from buridan_ui.templates.search.search import search
from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import desktop_footer, footer
from buridan_ui.templates.sidemenu.sidemenu import sidemenu
from buridan_ui.wrappers.base.utils.routes import base_content_path_ui
from buridan_ui.landing.hero import doc_icon_svg


# ============================================================================
# CLIENT STATE VARIABLES
# ============================================================================

Chart_Theme = ClientStateVar.create("chart_theme", "")

# ============================================================================
# CONSTANTS & CONFIGURATION
# ============================================================================

CHART_CONFIGS = {
    "Bar Charts": {"url": "/charts/bar-charts", "id_prefix": "bar", "quantity": 10},
    "Area Charts": {"url": "/charts/area-charts", "id_prefix": "area", "quantity": 8},
    "Line Charts": {"url": "/charts/line-charts", "id_prefix": "line", "quantity": 8},
    "Pie Charts": {"url": "/charts/pie-charts", "id_prefix": "pie", "quantity": 6},
}

THEME_OPTIONS = [
    ("Feyrouz", "فيْروز", "theme-blue"),
    ("Yaqout", "يَاقوت", "theme-red"),
    ("Zumurrud", "زُمُرُّد", "theme-green"),
    ("Kahraman", "كَهْرَمان", "theme-amber"),
    ("Amethyst", "أَمِيثِسْت", "theme-purple"),
]

# Common CSS classes
SIDEBAR_TOC_CLASSES = "flex flex-col max-w-[300px] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[4rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[1rem]"


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def create_responsive_display(
    small_screens: str, large_screens: str, breakpoint: int = 3
):
    """Create a responsive display list for different screen sizes."""
    return [small_screens if i <= breakpoint else large_screens for i in range(6)]


def create_border(
    color_name: str = "gray",
    shade: int = 5,
    style: str = "dashed",
    width: str = "1.25px",
):
    """Create a consistent border style."""
    return f"{width} {style} {rx.color(color_name, shade)}"


def create_icon(tag: str, size: int = 13):
    """Create a consistently styled icon."""
    return rx.icon(tag=tag, size=size, color=rx.color("slate", 11))


def create_divider():
    """Create a consistent divider."""
    return rx.divider(border_bottom=create_border(), bg="transparent")


# ============================================================================
# COMPONENT BUILDERS
# ============================================================================


def create_meta_item(icon_tag: str, label_text: str, title: Optional[str] = None):
    """Create a metadata item with icon and label."""
    return rx.el.div(
        create_icon(icon_tag),
        rx.el.label(label_text, class_name="text-sm"),
        class_name="flex flex-row items-center justify-start gap-x-2",
        title=title,
    )


def page_meta(created: str, updated: str, dir_count: int):
    """Create page metadata component showing creation date, update date, and component count."""
    return rx.el.div(
        create_meta_item("file-plus-2", created, "Created On"),
        create_meta_item("file-pen-line", updated, "Last Update"),
        create_meta_item("cuboid", f"{dir_count} Component(s)"),
        class_name="flex flex-row flex-wrap items-center gap-x-6 gap-y-4",
    )


def base_footer_responsive(
    component: rx.Component, small_screens: str, large_screens: str
):
    """Create a responsive footer component."""
    return rx.box(
        component,
        display=create_responsive_display(small_screens, large_screens),
        width="100%",
    )


# ============================================================================
# THEME COMPONENTS
# ============================================================================


def _create_theme_option(name: str, arabic_name: str, color_class: str):
    """Create a single theme option."""
    return rx.popover.close(
        rx.el.div(
            rx.el.button(
                f"{name} {arabic_name}",
                class_name="w-full text-left",
                type="button",
            ),
            rx.el.div(
                style={"backgroundColor": "var(--chart-2)"},
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


def _create_theme_content():
    """Create theme selection content."""
    content_items = []
    for i, (name, arabic_name, color_class) in enumerate(THEME_OPTIONS):
        content_items.append(_create_theme_option(name, arabic_name, color_class))

    return rx.box(
        *content_items,
        class_name="bg-background w-[160px] flex flex-col text-sm rounded-md shadow-md",
    )


def theme_select_menu():
    """Create theme selection menu."""
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
                _create_theme_content(),
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
        },
        border=f"1px solid {rx.color('gray', 3)}",
        class_name="rounded-md",
    )


# ============================================================================
# HEADER COMPONENTS
# ============================================================================


def _create_logo():
    """Create the buridan.UI logo."""
    return rx.link(
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
        display=create_responsive_display("flex", "none"),
        text_decoration="none",
        href="/",
    )


def _create_header_actions(url: str):
    """Create header action components."""
    return rx.el.div(
        search(),
        theme_select_menu()
        if url.startswith("/charts/")
        else rx.box(class_name="hidden"),
        rx.box(drawer(), class_name="flex md:hidden"),
        class_name="flex flex-row gap-x-2",
    )


def create_header(url: str):
    """Create the page header component."""
    return rx.el.div(
        rx.el.label(
            base_content_path_ui(url),
            class_name="text-sm font-bold font-sans flex items-center align-center gap-x-2",
            display=create_responsive_display("none", "flex"),
        ),
        _create_logo(),
        _create_header_actions(url),
        class_name="w-full h-12 px-4 py-3 sticky top-0 left-0 z-[20] flex flex-row justify-between align-center items-center gap-x-2 backdrop-blur-md",
    )


# ============================================================================
# LAYOUT COMPONENTS
# ============================================================================


def create_title_section(page_name: str, meta_component: rx.Component):
    """Create the title section component."""
    return rx.el.div(
        rx.el.div(
            rx.el.label(page_name, class_name="text-4xl sm:4xl font-bold py-6"),
            meta_component,
            class_name="w-full justify-start flex flex-col pb-9 pl-4",
        ),
        class_name="flex flex-col p-0 gap-y-2 min-h-[100vh] w-full",
    )


def create_footer_section():
    """Create the footer section component."""
    return rx.el.div(
        base_footer_responsive(desktop_footer(), "none", "flex"),
        base_footer_responsive(footer(), "flex", "none"),
        class_name="flex flex-col w-full lg:px-4 xl:px-4 px-1 py-2",
        border_top=create_border(),
    )


# ============================================================================
# TABLE OF CONTENTS COMPONENTS
# ============================================================================


def _generate_chart_links(chart_data: dict, name: str):
    """Generate chart variant links."""
    return [
        rx.el.a(
            f"{name} v{i + 1}",
            href=f"{chart_data['url']}#{chart_data['id_prefix']}-v{i + 1}",
            id=f"{chart_data['id_prefix']}-v{i + 1}",
            color=rx.color("slate", 11),
            class_name="cursor-pointer text-sm font-regular hover:underline",
        )
        for i in range(chart_data["quantity"])
    ]


def _create_reflex_build_link():
    return rx.link(
        rx.el.button(
            rx.vstack(
                rx.hstack(
                    rx.color_mode_cond(
                        doc_icon_svg(fill="white", background="black"),
                        doc_icon_svg(fill="black", background="white"),
                    ),
                    rx.el.strong(
                        "AI Builder",
                        class_name="text-sm",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    rx.fragment(
                        rx.el.strong("Reflex Build"),
                        " is your ",
                        rx.el.strong("AI-powered assistant"),
                        " for building ",
                        rx.el.strong("beautiful, production-ready apps"),
                        " — directly from text prompts, in seconds.",
                    ),
                    class_name="text-sm text-left text-slate-11",
                    width="100%",
                ),
                rx.text(
                    "No boilerplate. Just results.",
                    class_name="text-sm font-medium text-slate-11 pt-1",
                ),
                spacing="2",
                align="start",
                class_name="w-full",
            ),
            class_name="rounded-lg w-full text-left p-3",
            border=f"1px solid {rx.color('gray', 3)}",
            _hover={"background": rx.color("gray", 3)},
        ),
        href="https://build.reflex.dev/",
        text_decoration="none",
        width="100%",
        color=rx.color("slate", 12),
        _hover={"color": rx.color("slate", 12)},
        class_name="-translate-x-3",
        is_external=True,
    )


def _create_toc_content(chart_links: List):
    """Create table of contents content."""
    return rx.box(
        rx.el.label(
            "Examples", color=rx.color("slate", 12), class_name="text-sm font-bold"
        ),
        *chart_links,
        _create_reflex_build_link(),
        class_name="flex flex-col w-full gap-y-2 p-4",
    )


def _create_empty_toc():
    """Create empty table of contents for non-chart pages."""
    return rx.box(
        _create_reflex_build_link(),
        height="100vh",
        class_name=f"hidden xl:flex {SIDEBAR_TOC_CLASSES} pt-12 p-4",
    )


def table_of_content(name: str):
    """Create table of contents component."""
    if name not in CHART_CONFIGS:
        return _create_empty_toc()

    chart_data = CHART_CONFIGS[name]
    chart_links = _generate_chart_links(chart_data, name)

    return rx.box(
        rx.el.div(class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[99]"),
        _create_toc_content(chart_links),
        height="100vh",
        class_name=f"hidden xl:flex {SIDEBAR_TOC_CLASSES} self-start top-8",
    )


# ============================================================================
# MAIN TEMPLATE DECORATOR
# ============================================================================


def base(url: str, page_name: str, dir_meta: List[str | int] = []):
    """Create a base page template decorator."""

    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        def template():
            # Get the page content
            contents = content()

            # Create metadata component or hidden div
            meta = page_meta(*dir_meta) if dir_meta else rx.el.div(class_name="hidden")

            # Create title section with content items
            content_section = create_title_section(page_name, meta)
            content_section.children.extend(contents)

            # Create the main layout
            return rx.box(
                sidemenu(),
                rx.scroll_area(
                    create_header(url),
                    rx.box(
                        rx.box(
                            content_section,
                            create_footer_section(),
                            class_name="flex flex-col w-full max-lg:max-w-[60rem] mx-auto",
                        ),
                        table_of_content(name=page_name),
                        class_name="items-start relative flex flex-row gap-x-0",
                    ),
                    class_name="h-screen w-full overflow-y-auto [&_.rt-ScrollAreaScrollbar]:mt-[4rem] [&_.rt-ScrollAreaScrollbar]:mb-[1rem]",
                ),
                class_name="w-full h-screen flex flex-row gap-x-0",
            )

        return template

    return decorator
