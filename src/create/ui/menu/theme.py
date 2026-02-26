import reflex as rx

import src.create.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

THEMES = [
    "amber",
    "blue",
    "cyan",
    "emerald",
    "fuchsia",
    "gray",
    "green",
    "indigo",
    "lime",
    "neutral",
    "orange",
    "pink",
    "purple",
    "red",
    "rose",
    "sky",
    "stone",
    "teal",
    "violet",
    "yellow",
    "zinc",
]


def theme_options(theme: str):
    return select.item(
        rx.el.div(
            rx.el.div(
                class_name="size-4 bg-primary rounded-full "
                + rx.color_mode_cond(
                    f"{theme}",
                    f"{theme}-dark",
                ).to(str),
            ),
            select.item_text(theme),
            class_name="flex gap-x-2 w-full items-center capitalize",
        ),
        select.item_indicator(
            hi("Tick02Icon", class_name="size-4"),
        ),
        value=theme,
        class_name="w-full flex items-center justify-between rounded-lg",
        on_click=hooks.theme.set_value(theme),
    )


def theme_menu():
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Theme",
                            class_name="text-xs text-muted-foreground",
                        ),
                        rx.el.p(
                            select.value(),
                            class_name="text-md font-medium capitalize",
                        ),
                        class_name="flex flex-col items-start",
                    ),
                    rx.el.div(
                        class_name="size-4 bg-primary rounded-full "
                        + rx.color_mode_cond(
                            f"{hooks.theme.value}",
                            f"{hooks.theme.value}-dark",
                        ).to(str),
                    ),
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
                        *[theme_options(theme) for theme in THEMES],
                        class_name="!w-[13rem]",
                    ),
                    class_name="!rounded-xl h-[50vh] overflow-scroll scrollbar-none",
                ),
                side_offset=4,
                side="left",
            ),
        ),
        name="component_library",
        default_value="neutral",
    )
