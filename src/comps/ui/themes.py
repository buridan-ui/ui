import reflex as rx

import src.hooks as hooks
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

THEME_OPTIONS = [
    ("Hematite", "فيْروز", "gray"),
    ("Feyrouz", "فيْروز", "blue"),
    ("Yaqout", "يَاقوت", "red"),
    ("Zumurrud", "زُمُرُّد", "green"),
    ("Kahraman", "كَهْرَمان", "amber"),
    ("Amethyst", "أَمِيثِسْت", "purple"),
]


def theme_buttons():
    return rx.el.div(
        rx.el.div(
            select.root(
                select.trigger(
                    select.value(),
                    hi(
                        "Add01Icon",
                        class_name="size-4 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
                    ),
                    class_name="w-[150px] flex items-center justify-between group rounded-lg px-2 py-1.5",
                ),
                select.portal(
                    select.positioner(
                        select.popup(
                            select.group(
                                select.group_label("Theme"),
                                *[
                                    select.item(
                                        select.item_text(theme_class.capitalize()),
                                        select.item_indicator(
                                            hi("Tick02Icon", class_name="size-4")
                                        ),
                                        value=theme_class.capitalize(),
                                        class_name="w-full flex flex-row items-center justify-between",
                                        on_click=hooks.current_theme.set_value(
                                            theme_class
                                        ),
                                    )
                                    for _, __, theme_class in THEME_OPTIONS
                                ],
                            ),
                            class_name="w-[150px]",
                        ),
                        side_offset=4,
                    ),
                ),
                name="theme_select",
                default_value=hooks.current_theme.value.to(str).capitalize(),
            ),
            class_name=(
                "w-full flex flex-row flex-wrap gap-4 items-center "
                "justify-center md:justify-end px-8"
            ),
        ),
    )
