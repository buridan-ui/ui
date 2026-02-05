from typing import List, Literal

import reflex as rx

from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

IconType = Literal["icon", "swatch"]


def select_title_and_value(title: str, value: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.p(title, class_name="text-xs text-muted-foreground"),
        rx.el.p(value, class_name="text-sm"),
        class_name="flex flex-col items-start justify-start",
    )


def select_menu(
    title: str,
    default_value: str,
    display_icon: str,
    options: List[rx.Component],
):
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    select_title_and_value(title, select.value()),
                    hi(
                        display_icon,
                        class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
                    ),
                    class_name="!w-full flex items-center justify-between p-2",
                ),
                variant="ghost",
                class_name="w-full max-w-[140px] !p-0 !shrink-none h-12 rounded-xl",
            )
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        *options,
                        # *[
                        #     select.item(
                        #         select.item_text(fruit.capitalize()),
                        #         select.item_indicator(
                        #             hi("Tick02Icon", class_name="size-4")
                        #         ),
                        #         value=fruit.capitalize(),
                        #         class_name="w-full flex flex-row items-center justify-between",
                        #     )
                        #     for fruit in [
                        #         "apple",
                        #         "banana",
                        #         "orange",
                        #         "grape",
                        #         "blueberry",
                        #         "pineapple",
                        #     ]
                        # ],
                    ),
                ),
                side_offset=4,
            ),
        ),
        name="example_select",
        default_value=default_value,
    )
