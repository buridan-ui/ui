import reflex as rx

from src.templates.sidebar import sidebar
from src.templates.navbar import docs_navbar


def docpage(main_content, toc_content):
    """The template for all documentation pages."""
    return rx.el.body(
        rx.el.div(
            rx.el.header(docs_navbar(), class_name="sticky top-0 z-50"),
            rx.el.main(
                rx.el.div(
                    rx.el.div(
                        rx.scroll_area(
                            sidebar(),
                            class_name="h-full",
                        ),
                        class_name="sticky top-12 h-[calc(100vh-3rem)] hidden xl:flex",
                    ),
                    rx.el.div(
                        rx.el.div(
                            main_content,
                            class_name="flex-1 min-w-0 py-6",
                        ),
                        toc_content,
                        class_name="flex items-start w-full flex-1 min-w-0",
                    ),
                    class_name="flex w-full gap-x-8 xl:max-w-[80rem] 2xl:max-w-[85rem] mx-auto",
                ),
                class_name="w-full",
            ),
            class_name="bg-background relative flex min-h-screen flex-col",
        ),
    )
