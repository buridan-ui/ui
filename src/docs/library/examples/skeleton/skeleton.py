import reflex as rx
from ...base_ui.components.base.skeleton import skeleton_component


def skeleton_example():
    """A basic skeleton example."""
    return skeleton_component(class_name="h-8 w-32 rounded-md")


def skeleton_card_example():
    """A skeleton example simulating a loading card."""
    return rx.box(
        rx.flex(
            skeleton_component(class_name="h-12 w-12 rounded-full"),
            rx.flex(
                skeleton_component(class_name="h-4 w-[250px] rounded-md"),
                skeleton_component(class_name="h-4 w-[200px] rounded-md"),
                direction="column",
                spacing="2",
            ),
            spacing="4",
        ),
        class_name="flex items-center space-x-4 rounded-md border border-input p-4 w-96",
    )
