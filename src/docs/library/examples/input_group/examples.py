import reflex as rx
from src.docs.library.base_ui.components.base.input_group import (
    input_with_addons,
    textarea_with_footer,
)


def input_price():
    return rx.el.div(
        input_with_addons(
            placeholder="0.00",
            prefix="$",
            suffix="USD",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )


def input_url():
    return rx.el.div(
        input_with_addons(
            placeholder="example.com",
            prefix="https://",
            suffix=".com",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )


def input_email():
    return rx.el.div(
        input_with_addons(
            placeholder="Enter your username",
            suffix="@company.com",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )


def input_textarea():
    return rx.el.div(
        textarea_with_footer(
            placeholder="Enter your message",
            footer_text="120 characters left",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
