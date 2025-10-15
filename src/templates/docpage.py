import reflex as rx

from src.templates.sidebar import sidebar
from src.templates.navbar import docs_navbar
from src.templates.toc import table_of_content
from src.hooks import selected_page


def docpage(match_cases, toc_mapping):
    toc_cases = [
        (url, table_of_content(toc_data)) for url, toc_data in toc_mapping.items()
    ]

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
                            rx.match(
                                selected_page.value,
                                *match_cases,
                                rx.box(
                                    rx.heading("Page not found", size="9"),
                                    rx.text(
                                        "The page you're looking for doesn't exist."
                                    ),
                                    class_name="p-4",
                                ),
                            ),
                            class_name="flex-1 min-w-0 py-6",
                        ),
                        rx.match(
                            selected_page.value,
                            *toc_cases,
                            rx.el.div(),
                        ),
                        class_name="flex items-start w-full flex-1 min-w-0",
                    ),
                    class_name="flex w-full gap-x-8 xl:max-w-[80rem] 2xl:max-w-[85rem] mx-auto",
                ),
                class_name="w-full",
            ),
            class_name="bg-background relative flex min-h-screen flex-col",
        ),
    )
