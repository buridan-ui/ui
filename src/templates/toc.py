import reflex as rx
from typing import List, Dict


def _create_markdown_toc_links(toc_data: List[Dict]) -> rx.Component:
    """Create markdown TOC links."""
    if not toc_data:
        return rx.el.div()

    return rx.el.div(
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


def table_of_content(toc_data: List[Dict]):
    """
    Render table of contents.

    Args:
        toc_data: List of dicts with 'text', 'id', 'level' keys
    """
    return rx.el.div(
        rx.scroll_area(
            rx.el.div(
                rx.el.label(
                    "Table of Content",
                    color=rx.color("slate", 12),
                    class_name="text-sm font-bold pb-2",
                ),
                _create_markdown_toc_links(toc_data),
                class_name="flex flex-col w-full h-full p-4",
            ),
            class_name="flex flex-col items-center gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]",
        ),
        # class_name="hidden lg:flex max-w-[18rem] w-full sticky top-0 max-h-[100vh] z-[10] pb-5",
        class_name="hidden lg:block max-w-[18rem] w-full sticky top-12 h-[calc(100vh-3rem)] shrink-0",
    )
