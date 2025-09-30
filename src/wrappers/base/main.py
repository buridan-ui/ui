from functools import wraps
from typing import Callable, List, Optional, Dict

import reflex as rx

from src.templates.search.search import search
from src.templates.drawer.drawer import drawer
from src.templates.footer.footer import desktop_footer, footer
from src.templates.sidemenu.sidemenu import sidemenu
from src.wrappers.base.utils.routes import base_content_path_ui
from src.landing.hero import doc_icon_svg
from src.components.github import github_link
from src.components.theme import theme_button
from src.config_generator import get_component_config
from src.templates.navbar import doc_navbar


COMPONENT_CONFIGS = get_component_config()

# Common CSS classes
SIDEBAR_TOC_CLASSES = "flex flex-col max-w-[18rem] w-full gap-y-2 align-start sticky top-0 left-0 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] z-[10] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]"


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
        # rx.box(theme_select_menu(), class_name="hidden md:flex")
        # if url.startswith("/charts/")
        # else rx.box(class_name="hidden"),
        search(),
        github_link(),
        theme_button(),
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
        class_name="w-full h-12 px-4 py-3 sticky top-0 left-0 z-[99] flex flex-row justify-between align-center items-center gap-x-2 backdrop-blur-md",
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


def _generate_component_links(component_data: dict, name: str):
    """Generate component variant links."""
    base_name = name.replace(" Charts", "")
    return [
        rx.el.a(
            f"{base_name} v{i + 1}",
            href=f"#{component_data['id_prefix']}-v{i + 1}",
            color=rx.color("slate", 11),
            class_name="cursor-pointer text-sm font-regular hover:underline",
        )
        for i in range(component_data["quantity"])
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
            class_name="rounded-lg w-full text-left p-3 cursor-pointer",
            border=f"1px solid {rx.color('gray', 3)}",
            _hover={"background": rx.color("gray", 3)},
        ),
        href="https://build.reflex.dev/",
        text_decoration="none",
        width="100%",
        color=rx.color("slate", 12),
        _hover={"color": rx.color("slate", 12)},
        is_external=True,
    )


def _create_toc_content(component_links: List):
    """Create table of contents content."""
    return rx.box(
        rx.el.label(
            "Table of Content",
            color=rx.color("slate", 12),
            class_name="text-sm font-bold",
        ),
        *component_links,
        # _create_reflex_build_link(),
        class_name="flex flex-col w-full gap-y-2 p-4",
    )


def _create_empty_toc():
    """Create empty table of contents for non-chart pages."""
    return rx.box(
        _create_reflex_build_link(),
        height="100vh",
        class_name=f"hidden xl:flex {SIDEBAR_TOC_CLASSES} pt-12 p-4",
    )


def _create_markdown_toc_links(toc_data: List[Dict[str, str]]) -> rx.Component:
    """Create markdown TOC links."""
    return rx.box(
        *[
            rx.el.a(
                entry["text"],
                href=f"#{entry['id']}",
                class_name=f"cursor-pointer text-sm font-regular hover:underline no-underline{' pl-4' if entry['level'] > 1 else ''}",
            )
            for entry in toc_data
        ],
        class_name="flex flex-col w-full gap-y-2",
    )


def table_of_content(name: str, toc_data: Optional[List[Dict[str, str]]] = None):
    """Create table of contents component."""
    if toc_data:  # Markdown TOC
        return rx.box(
            rx.scroll_area(
                rx.box(  # New wrapper box for consistency
                    rx.el.label(
                        "Table of Content",
                        color=rx.color("slate", 12),
                        class_name="text-sm font-bold pb-2",
                    ),
                    _create_markdown_toc_links(toc_data),
                    # _create_reflex_build_link(),
                    # class_name="flex flex-col w-full gap-y-2 p-4",
                    class_name="flex flex-col w-full h-full p-4",
                ),
                class_name="flex flex-col items-center gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]",
            ),
            # height="100vh",
            # class_name=f"{SIDEBAR_TOC_CLASSES} self-start",
            class_name="hidden lg:flex max-w-[18rem] w-full sticky top-0 max-h-[100vh] z-[10] pb-5",
        )

    if name not in COMPONENT_CONFIGS:
        return _create_empty_toc()

    component_data = COMPONENT_CONFIGS[name]
    component_links = _generate_component_links(component_data, name)

    return rx.box(
        _create_toc_content(component_links),
        height="100vh",
        class_name=f"hidden xl:flex {SIDEBAR_TOC_CLASSES} self-start",
    )


def base(
    url: str,
    page_name: str,
    dir_meta: List[str | int] = [],
    toc_data: Optional[List[Dict[str, str]]] = None,
):
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

            return rx.box(
                doc_navbar(url=url),
                rx.scroll_area(
                    rx.box(
                        sidemenu(),
                        rx.box(
                            content_section,
                            class_name="flex w-full min-h-screen",
                        ),
                        table_of_content(name=page_name, toc_data=toc_data),
                        class_name="xl:max-w-[80rem] 2xl:max-w-[75rem] w-full mx-auto h-full flex flex-row gap-x-0",
                    ),
                    class_name="px-4 xl:px-0 pt-12 h-screen w-full overflow-y-auto",
                    style={"scroll-padding-top": "4rem"},
                ),
                bg=rx.color("slate", 2),
                class_name="w-full h-screen flex flex-col gap-y-0",
            )

        return template

    return decorator
