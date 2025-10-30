import reflex as rx

from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.input_group import input_with_addons
from src.docs.library.base_ui.components.base.kbd import kbd_group, kbd

import src.hooks as hooks


def icon_for_url(url: str):
    """UI helper for picking an icon — logic unchanged."""
    return rx.cond(
        url.startswith("docs/getting-started/"),
        rx.icon("file", size=15, class_name="!text-muted-foreground"),
        rx.cond(
            url.startswith("docs/components/"),
            rx.icon("blocks", size=15, class_name="!text-muted-foreground"),
            rx.cond(
                url.startswith("docs/wrapped-components/"),
                rx.icon("cuboid", size=15, class_name="!text-muted-foreground"),
                rx.cond(
                    url.startswith("docs/js-integrations/"),
                    rx.icon("workflow", size=15, class_name="!text-muted-foreground"),
                    rx.icon("chart-area", size=15, class_name="!text-muted-foreground"),
                ),
            ),
        ),
    )


def result_row(value: dict):
    """Reusable UI fragment for each search result row."""
    return rx.el.a(
        rx.el.div(
            icon_for_url(value["url"]),
            rx.el.p(value["title"], class_name="text-sm font-medium"),
            class_name="w-full flex flex-row gap-x-2 items-center",
        ),
        to=f"/{value['url']}",
        class_name=(
            "w-full flex px-2 py-1.5 rounded-lg hover:bg-input/40 "
            "hover:ring-1 hover:ring-input hover:ring-offset-0"
        ),
    )


def result_list(items, condition_fn=None):
    """List container with optional condition logic (logic unchanged)."""
    return rx.el.div(
        rx.foreach(
            items,
            lambda value: rx.cond(
                condition_fn(value) if condition_fn else True,
                result_row(value),
            ),
        ),
        class_name="w-full h-full flex flex-col px-1 py-1 gap-y-2",
    )


def search_trigger():
    return button(
        "Search documentation...",
        kbd_group(kbd("⌘"), kbd("K")),
        variant="outline",
        size="sm",
        class_name="!text-sm flex flex-row items-center justify-between mr-2",
    )


def search_input():
    return rx.el.div(
        input_with_addons(
            prefix=rx.icon("search", size=16, class_name="!text-muted-foreground"),
            placeholder="Search documentation...",
            class_name="pl-2 rounded-radius",
            on_change=lambda value: hooks.search_query.set_value(value),
        ),
        class_name="w-full h-10 absolute top-0 left-0 flex z-[99] px-3 py-2",
    )


def search_content():
    """Scrollable content, UI only refactored."""
    return rx.el.div(
        rx.scroll_area(
            rx.cond(
                hooks.search_query.value,
                result_list(
                    hooks.search_items_cs.value.to(list[dict[str, str]]),
                    lambda v: v["title"]
                    .lower()
                    .contains(hooks.search_query.value.to(str).lower()),
                ),
                result_list(
                    hooks.search_items_cs.value.to(list[dict[str, str]]),
                ),
            ),
            class_name=(
                "w-full h-full pt-10.5 "
                "[&_.rt-ScrollAreaScrollbar]:mt-[3rem] "
                "[&_.rt-ScrollAreaScrollbar]:mb-[1rem]"
            ),
        ),
        class_name="w-full h-full",
    )


def site_search():
    """Full dialog container."""
    return rx.dialog.root(
        rx.dialog.trigger(search_trigger(), class_name="hidden lg:flex"),
        rx.dialog.content(
            search_input(),
            search_content(),
            class_name="outline-2 outline-input h-[25rem] w-[32rem] rounded-radius p-2 relative",
        ),
    )
