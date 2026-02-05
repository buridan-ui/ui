from typing import Literal

import reflex as rx

import src.create.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

LibraryName = Literal["base-ui", "radix-ui"]


def library_svg(lib: LibraryName) -> rx.Component:
    return rx.image(
        src=rx.color_mode_cond(
            f"/svg/{lib}/light.svg",
            f"/svg/{lib}/dark.svg",
        ),
        class_name="size-4",
    )


def component_library_menu():
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Component Library",
                            class_name="text-xs text-muted-foreground",
                        ),
                        rx.el.p(select.value(), class_name="text-sm"),
                        class_name="flex flex-col items-start justify-start",
                    ),
                    rx.cond(
                        hooks.component_library.value == "Base UI",
                        library_svg(lib="base-ui"),
                        library_svg(lib="radix-ui"),
                    ),
                    class_name="!w-full flex items-center justify-between p-2",
                ),
                variant="ghost",
                class_name="w-full max-w-[180px] !p-0 !shrink-none h-12 rounded-xl",
            )
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.item(
                            rx.el.div(
                                library_svg(lib="radix-ui"),
                                select.item_text("Radix UI"),
                                class_name="flex flex-row gap-x-1 w-full items-center justify-start",
                            ),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Radix UI",
                            class_name="w-full flex flex-row items-center justify-between rounded-lg",
                            on_click=hooks.component_library.set_value("Radix UI"),
                        ),
                        select.item(
                            rx.el.div(
                                library_svg(lib="base-ui"),
                                select.item_text("Base UI"),
                                class_name="flex flex-row gap-x-1 w-full items-center justify-start",
                            ),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Base UI",
                            class_name="w-full flex flex-row items-center justify-between rounded-lg",
                            on_click=hooks.component_library.set_value("Base UI"),
                        ),
                        class_name="!w-[13rem]",
                    ),
                    class_name="!rounded-xl",
                ),
                side_offset=4,
            ),
        ),
        name="component_library",
        default_value="Base UI",
    )
