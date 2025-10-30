import reflex as rx
from ...base_ui.components.base.textarea import textarea


def textarea_demo():
    return rx.el.div(
        rx.el.p("Textarea", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="Enter your message here...",
        ),
        class_name="w-full max-w-md p-8",
    )


def textarea_disabled():
    return rx.el.div(
        rx.el.p("Disabled Textarea", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="This is disabled",
            disabled=True,
        ),
        class_name="w-full max-w-md p-8",
    )


def textarea_custom():
    return rx.el.div(
        rx.el.p("Custom Height", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="Taller textarea",
            class_name="min-h-32",
        ),
        class_name="w-full max-w-md p-8",
    )
