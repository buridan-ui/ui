from ...base_ui.components.base.select import select
from ...base_ui.icons.hugeicon import hi


def select_example():
    """A basic select example."""

    return select.root(
        select.trigger(
            select.value(),
            hi(
                "Add01Icon",
                class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
            ),
            class_name="w-[180px] flex items-center justify-between group",
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
