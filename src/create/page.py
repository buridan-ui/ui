import reflex as rx

from src.create.layout.sidebars import component_sidebar, menu_option_sidebar
from src.docs.library.examples.accordion.accordion import accordion_example
from src.templates.navbar import navbar


def create_page():
    """The main page layout for buridan-ui/create feature"""
    return rx.el.body(
        rx.el.div(
            rx.el.header(navbar(), class_name="sticky top-0 z-50"),
            rx.el.main(
                rx.el.div(
                    menu_option_sidebar(),
                    rx.el.div(
                        rx.el.div(
                            # main_content,
                            # font-(family-name:--font-jetbrains-mono)
                            rx.el.div(
                                accordion_example(),
                                class_name="style-mira border border-input w-full p-4",
                            ),
                            rx.el.div(
                                accordion_example(),
                                class_name="style-maia w-full border border-input p-4",
                            ),
                            class_name="flex-1 min-w-0 pt-6",
                        ),
                        component_sidebar(),
                        class_name="flex items-start w-full flex-1 min-w-0",
                    ),
                    class_name="flex w-full gap-x-0 xl:max-w-[80rem] 2xl:max-w-[85rem] mx-auto",
                ),
                class_name="w-full",
            ),
            class_name="bg-background relative flex h-screen flex-col",
        ),
    )
