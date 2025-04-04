from functools import wraps
from typing import Callable

import reflex as rx
from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import desktop_footer, footer
from buridan_ui.templates.sidemenu.sidemenu import sidemenu

from .utils.routes import base_content_path_ui
from ...templates.settings.settings import app_settings


def base_footer_responsive(component: rx.Component, start: str, end: str):
    return rx.box(
        component,
        display=[start if i <= 3 else end for i in range(6)],
        width="100%",
    )


def page_meta(created, updated, dir_count):
    return rx.el.div(
        rx.el.div(
            rx.icon(
                tag="file-plus-2",
                size=13,
                color=rx.color("slate", 11),
            ),
            rx.el.label(
                created,
                class_name="text-sm",
            ),
            class_name="flex flex-row items-center justify-start gap-x-2",
            title="Created On",
        ),
        rx.el.div(
            rx.icon(
                tag="file-pen-line",
                size=13,
                color=rx.color("slate", 11),
            ),
            rx.el.label(
                updated,
                class_name="text-sm",
            ),
            class_name="flex flex-row items-center justify-start gap-x-2",
            title="Last Update",
        ),
        rx.el.div(
            rx.icon(
                tag="cuboid",
                size=13,
                color=rx.color("slate", 11),
            ),
            rx.el.label(
                f"{dir_count} Component(s)",
                class_name="text-sm",
            ),
            class_name="flex flex-row items-center justify-start gap-x-2",
        ),
        class_name="flex flex-row flex-wrap items-center gap-x-6 gap-y-4",
    )


def base(url: str, page_name: str, dir_meta: list[str | int] = []):
    def decorator(content: Callable[[], list[rx.Component]]):
        @wraps(content)
        def template():
            contents = content()

            # Properly handle the conditional
            if dir_meta:
                created, updated, dir_count = dir_meta
                meta = page_meta(created, updated, dir_count)

            else:
                meta = rx.el.div(class_name="hidden")

            return rx.hstack(
                sidemenu(),
                rx.box(
                    border_left=f"1.25px dashed {rx.color('gray', 5)}",
                    border_right=f"1.25px dashed {rx.color('gray', 5)}",
                    color=rx.color("gray", 3),
                    class_name="h-full p-4 col-start-2 row-span-full row-start-1 max-sm:hidden bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
                ),
                rx.scroll_area(
                    # absolute navbar ...
                    rx.el.div(
                        rx.el.label(
                            base_content_path_ui(url),
                            class_name="text-sm font-bold font-sans flex items-center align-center gap-x-2",
                            display=["none" if i <= 3 else "flex" for i in range(6)],
                        ),
                        rx.el.label(
                            "buridan/ui",
                            class_name="text-sm font-bold font-sans flex items-center align-center gap-x-2",
                            display=["flex" if i <= 3 else "none" for i in range(6)],
                        ),
                        rx.el.div(
                            app_settings(),
                            rx.box(
                                drawer(),
                                display=[
                                    "flex" if i <= 3 else "none" for i in range(6)
                                ],
                            ),
                            class_name="flex flex-row gap-x-2",
                        ),
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        class_name="w-full h-12 px-4 py-3 absolute top-0 left-0 z-[999] flex flex-row justify-between align-center items-center gap-x-2",
                    ),
                    # ... title
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                page_name,
                                class_name="text-4xl sm:4xl font-bold py-6",
                            ),
                            meta,
                            class_name="w-full justify-start flex flex-col pb-9 pl-4",
                        ),
                        *contents,
                        class_name="flex flex-col p-0 gap-y-2 min-h-[100vh] w-full",
                    ),
                    rx.box(
                        border_top=f"1.25px dashed {rx.color('gray', 5)}",
                        border_bottom=f"1.25px dashed {rx.color('gray', 5)}",
                        color=rx.color("gray", 3),
                        class_name="w-full p-4 col-start-2 row-span-full row-start-1 bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
                    ),
                    rx.el.div(
                        base_footer_responsive(desktop_footer(), "none", "flex"),
                        base_footer_responsive(footer(), "flex", "none"),
                        class_name="flex flex-col w-full lg:px-8 xl:px-8 px-1",
                        # border_top=f"1px solid {rx.color('gray', 3)}",
                    ),
                    # ...fix scrollbar scroller appearance?? original 0.1something
                    class_name="flex flex-col w-full gap-y-2 align-start [&_.rt-ScrollAreaScrollbar]:mr-[-0.2875rem] z-[10] pt-14",
                ),
                rx.box(
                    border_left=f"1.25px dashed {rx.color('gray', 5)}",
                    border_right=f"1.25px dashed {rx.color('gray', 5)}",
                    color=rx.color("gray", 3),
                    class_name="h-full p-4 col-start-2 row-span-full row-start-1 max-sm:hidden bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)]",
                ),
                class_name="w-[100%] h-[100vh] gap-x-0 bg-background",
            )

        return template

    return decorator
