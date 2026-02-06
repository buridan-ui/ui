from typing import Literal, TypedDict

import reflex as rx

import src.create.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

LibraryName = Literal["base-ui", "radix-ui"]
LibraryValue = Literal["Base UI", "Radix UI"]


class Library(TypedDict):
    value: LibraryValue
    svg: LibraryName


LIBRARIES: list[Library] = [
    {"value": "Radix UI", "svg": "radix-ui"},
    {"value": "Base UI", "svg": "base-ui"},
]


def library_svg(lib: LibraryName) -> rx.Component:
    return rx.image(
        src=rx.color_mode_cond(
            f"/svg/{lib}/light.svg",
            f"/svg/{lib}/dark.svg",
        ),
        class_name="size-4",
    )


def library_item(lib: Library) -> rx.Component:
    return select.item(
        rx.el.div(
            library_svg(lib["svg"]),
            select.item_text(lib["value"]),
            class_name="flex gap-x-1 w-full items-center",
        ),
        select.item_indicator(
            hi("Tick02Icon", class_name="size-4"),
        ),
        value=lib["value"],
        class_name="w-full flex items-center justify-between rounded-lg",
        on_click=hooks.component_library.set_value(lib["value"]),
    )


def current_library_icon() -> rx.Component:
    return rx.cond(
        hooks.component_library.value == "Base UI",
        library_svg("base-ui"),
        library_svg("radix-ui"),
    )


def component_library_menu() -> rx.Component:
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Component Library",
                            class_name="text-xs text-muted-foreground",
                        ),
                        rx.el.p(select.value(), class_name="text-md font-medium"),
                        class_name="flex flex-col items-start",
                    ),
                    current_library_icon(),
                    class_name="!w-full flex items-center justify-between p-2",
                ),
                variant="ghost",
                class_name="w-full !p-0 h-12 rounded-xl",
            ),
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        *[library_item(lib) for lib in LIBRARIES],
                        class_name="!w-[13rem]",
                    ),
                    class_name="!rounded-xl",
                ),
                side_offset=4,
                side="left",
            ),
        ),
        name="component_library",
        default_value="Base UI",
    )
