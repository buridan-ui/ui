import reflex as rx

import src.create.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

FONTS = [
    "Inter",
    "JetBrains Mono",
    "Geist",
    "Geist Mono",
    "Noto Sans",
    "Nunito Sans",
    "Figtree",
    "Roboto",
    "Raleway",
    "DM Sans",
    "Public Sans",
    "Outfit",
]


def font_options(font: str):
    font_var = f"--font-{font.lower().replace(' ', '-')}"

    return select.item(
        rx.el.div(
            rx.el.p(font, class_name="!text-xs text-muted-foreground capitalize"),
            select.item_text(
                "Every test phrase hides a parade of playful symbols.",
                class_name=f"line-clamp-2 !text-sm font-(family-name:{font_var})",
            ),
            class_name="flex flex-col gap-y-1 w-full justify-start items-start",
        ),
        select.item_indicator(
            hi("Tick02Icon", class_name="size-4"),
        ),
        value=font,
        class_name="w-full flex items-center justify-between rounded-lg",
        on_click=rx.call_script(hooks.font_family.set_value(font)),
    )


def font_menu():
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Font",
                            class_name="text-xs text-muted-foreground",
                        ),
                        rx.el.p(
                            select.value(),
                            class_name="text-md font-medium capitalize",
                        ),
                        class_name="flex flex-col items-start",
                    ),
                    hi(
                        "TextFontIcon",
                        class_name="size-4",
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
                        *[font_options(font) for font in FONTS],
                        class_name="!w-[18rem]",
                    ),
                    class_name="!rounded-xl h-[50vh] overflow-scroll scrollbar-none",
                ),
                side_offset=4,
                side="left",
            ),
        ),
        name="font_selector",
        default_value="Inter",
    )
