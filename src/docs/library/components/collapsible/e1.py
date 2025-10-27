import reflex as rx

from ...base_ui.components.base.collapsible import collapsible
from ...base_ui.components.base.button import button


def collapsible_example():
    return collapsible(
        trigger=button(
            "Trigger",
            varient="outline",
            class_name="w-full",
        ),
        content=rx.el.p(
            "This is the collapsible content. You can put anything here!",
            class_name="py-2 text-center",
        ),
        default_open=False,
        class_name="w-full max-w-xs",
    )
