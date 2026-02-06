import reflex as rx

import src.create.hooks as hooks
from src.docs.library.base_ui.components.base.button import button
from src.docs.library.base_ui.components.base.select import select
from src.docs.library.base_ui.icons.hugeicon import hi

RADIUS_OPTIONS = ["none", "small", "medium", "large"]

RADIUS_CLASSES = {
    "none": "rounded-none",
    "small": "rounded-sm",
    "medium": "rounded-md",
    "large": "rounded-lg",
}


def radius_option_item(radius: str):
    radius_class = RADIUS_CLASSES[radius]

    return select.item(
        rx.el.div(
            rx.el.p(radius.capitalize(), class_name="text-sm text-muted-foreground"),
            class_name=f"flex flex-col gap-y-1 w-full justify-start items-start {radius_class}",
        ),
        select.item_indicator(
            hi("Tick02Icon", class_name="size-4"),
        ),
        value=radius,
        class_name="w-full flex items-center justify-between rounded-lg",
        on_click=rx.call_script(hooks.radius.set_value(radius)),
    )


def radius_menu():
    return select.root(
        select.trigger(
            render_=button(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Radius",
                            class_name="text-xs text-muted-foreground",
                        ),
                        rx.el.p(
                            select.value(), class_name="text-md font-medium capitalize"
                        ),
                        class_name="flex flex-col items-start",
                    ),
                    hi("BorderRight02Icon", class_name="size-4"),
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
                        *[radius_option_item(r) for r in RADIUS_OPTIONS],
                        class_name="!w-[13rem]",
                    ),
                    class_name="!rounded-xl",
                ),
                side_offset=4,
                side="left",
            ),
        ),
        name="component_radius",
        default_value="none",
    )
