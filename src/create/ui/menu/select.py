import reflex as rx

from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi


def __():
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p("Style", class_name="text-xs text-muted-foreground"),
                        rx.el.p("Moria", class_name="text-sm"),
                        class_name="flex flex-col items-start justify-start",
                    ),
                    hi(
                        "Add01Icon",
                        class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
                    ),
                    class_name="!w-full flex items-center justify-between p-2",
                ),
                variant="ghost",
                class_name="w-full max-w-[140px] !p-0 !shrink-none h-12 rounded-xl",
            )
            # select.value(),
            # hi(
            #     "Add01Icon",
            #     class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
            # ),
            # class_name="w-[180px] flex items-center justify-between group",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.group_label("Fruit"),
                        *[
                            select.item(
                                select.item_text(fruit.capitalize()),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=fruit.capitalize(),
                                class_name="w-full flex flex-row items-center justify-between",
                            )
                            for fruit in [
                                "apple",
                                "banana",
                                "orange",
                                "grape",
                                "blueberry",
                                "pineapple",
                            ]
                        ],
                    ),
                    class_name="w-[180px]",
                ),
                side_offset=4,
            ),
        ),
        name="example_select",
        default_value="Select a fruit",
    )
