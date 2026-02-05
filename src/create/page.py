import reflex as rx

from .ui.menu.library import component_library_menu


def create_page():
    """The main page layout for buridan-ui/create feature"""
    return rx.el.body(
        rx.el.div(
            # rx.el.header(main_navbar(), class_name="sticky top-0 z-50"),
            rx.el.main(
                rx.el.div(
                    # sidebar(),
                    rx.el.div(
                        rx.el.div(
                            # main_content,
                            component_library_menu(),
                            class_name="flex-1 min-w-0 pt-6",
                        ),
                        # toc_content,
                        class_name="flex items-start w-full flex-1 min-w-0",
                    ),
                    class_name="flex w-full gap-x-0 xl:max-w-[80rem] 2xl:max-w-[85rem] mx-auto",
                ),
                class_name="w-full",
            ),
            class_name="bg-background relative flex min-h-screen flex-col",
        ),
    )
