import reflex as rx

import src.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.icons.hugeicon import hi
from src.templates.sidebar import sidebar


def drawer():
    return rx.drawer.root(
        rx.drawer.trigger(
            button(
                hi(
                    "Add01Icon",
                    class_name=(
                        "size-5 transition-transform duration-75 ease-in-out "
                        + rx.cond(hooks.menu_icon.value, "rotate-45", "").to(str)
                    ),
                ),
                rx.el.p("Menu", class_name="text-lg font-medium"),
                size="sm",
                variant="ghost",
                on_click=hooks.menu_icon.set_value(~hooks.menu_icon.value),
                class_name="flex flex-row items-center justify-between",
            ),
            class_name="px-2",
        ),
        rx.drawer.portal(
            rx.drawer.content(
                sidebar(in_drawer=True),
                width="100%",
                top="3.5rem",
                right="0",
                background=rx.color_mode_cond(
                    "oklch(1 0 0 / 0.99)", "oklch(0.145 0 0 / 0.99)"
                ),
                on_escape_key_down=hooks.menu_icon.set_value(~hooks.menu_icon.value),
                on_interact_outside=hooks.menu_icon.set_value(~hooks.menu_icon.value),
            ),
            class_name="z-[9999]",
        ),
        direction="left",
    )
