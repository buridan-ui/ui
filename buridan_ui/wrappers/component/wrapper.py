from __future__ import annotations

from functools import wraps
from typing import Callable

import reflex as rx
from reflex.components.datadisplay.code import Theme
from reflex.experimental import ClientStateVar

import random
import string


def extract_chart_info(path):
    import re

    # Regex pattern to match both 'charts' and 'pantry' base paths
    match = re.search(r"(charts|pantry)/([a-zA-Z]+)/v(\d+)", path)
    if match:
        # category = match.group(1)  # 'charts' or 'pantry'
        chart_name = match.group(2)  # 'area', 'animations', etc.
        version = match.group(3)  # Version number

        # Use rx.hstack to display as 'animations > v1', etc.
        return rx.hstack(
            rx.el.label(
                chart_name,
                class_name="text-sm font-regular",
                color=rx.color("slate", 11),
            ),
            rx.el.label(
                "›", class_name="text-sm font-medium", color=rx.color("slate", 11)
            ),
            rx.el.label(
                f"v{version}",
                class_name="text-sm font-medium",
                color=rx.color("slate", 12),
            ),
            spacing="1",
        )
    raise ValueError(
        f"Error: Path '{path}' is invalid or not in the expected format (charts/pantry/...). Please check your input."
    )


def tab_selector(tabs=["Preview", "Code"], component_id=None, source_code=""):
    # Create a unique ID if none provided
    if not component_id:
        component_id = "".join(
            random.choices(string.ascii_letters + string.digits, k=10)
        )

    # Create a unique active tab state variable for this specific tab selector
    active_tab = ClientStateVar.create(f"active_tab_{component_id}", 0)

    return rx.box(
        rx.hstack(
            rx.button(
                rx.text("Copy", color=rx.color("slate", 9)),
                on_click=[
                    rx.set_clipboard(source_code),
                    rx.toast.info("Component copied!"),
                ],
                aria_disabled="false",
                background="transparent",
                style={
                    "display": "inline-flex",
                    "align_items": "center",
                    "justify_content": "center",
                    "white_space": "nowrap",
                    "padding_top": "0.5rem",
                    "padding_bottom": "0.5rem",
                    "vertical_align": "middle",
                    "font_weight": "600",
                    "min_width": "32px",
                    "gap": "0.375rem",
                    "font_size": "0.75rem",
                    "height": "1.5rem",
                    "padding_left": "0.75rem",
                    "padding_right": "0.75rem",
                    "cursor": "pointer",
                    "border_radius": "0.5rem",
                },
            ),
            rx.foreach(
                tabs,
                lambda tab, i: rx.button(
                    rx.text(
                        tab,
                        color=rx.cond(
                            active_tab.value == i,
                            rx.color("slate", 12),
                            rx.color("slate", 10),
                        ),
                    ),
                    on_click=[
                        rx.call_function(active_tab.set_value(i)),
                    ],
                    aria_disabled="false",
                    background=rx.cond(
                        active_tab.value == i,
                        rx.color("gray", 3),
                        "transparent",
                    ),
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "justify_content": "center",
                        "white_space": "nowrap",
                        "padding_top": "0.5rem",
                        "padding_bottom": "0.5rem",
                        "vertical_align": "middle",
                        "font_weight": "600",
                        "min_width": "32px",
                        "gap": "0.375rem",
                        "font_size": "0.75rem",
                        "height": "1.5rem",
                        "padding_left": "0.75rem",
                        "padding_right": "0.75rem",
                        "cursor": "pointer",
                        "border_radius": rx.cond(
                            active_tab.value == i, "0.375rem", "0.5rem"
                        ),
                        "box_shadow": rx.cond(
                            active_tab.value == i,
                            "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                            "none",
                        ),
                    },
                ),
            ),
            style={
                "display": "inline-flex",
                "height": "2.125rem",
                "align_items": "baseline",
                "justify_content": "flex-start",
                "border_radius": "0.5rem",
                "padding": "0.25rem",
                "border": f"1.25px dashed {rx.color('gray', 4)}",
            },
        )
    )


def component_wrapper(path: str):
    # Generate a single random ID for this component
    component_id = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    # Create a unique client state variable for this component's preview/code toggle
    active_tab = ClientStateVar.create(f"active_tab_{component_id}", 0)

    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, component_code, flexgen_path = func()

            return rx.box(
                rx.box(
                    rx.el.label(extract_chart_info(path), class_name="text-sm"),
                    rx.box(
                        # Use the tab_selector with our component_id
                        tab_selector(["Preview", "Code"], component_id, component_code),
                        class_name="flex align-center gap-2",
                    ),
                    class_name="h-14 px-4 py-4 w-full flex align-center justify-between items-center bg-background rounded-xl "
                    + rx.cond(active_tab.value == 1, "sticky top-0", "").to(str),
                ),
                rx.box(
                    rx.cond(
                        active_tab.value == 0,  # 0 = Preview, 1 = Code
                        component,
                        rx.code_block(
                            component_code,
                            language="python",
                            theme=rx.color_mode_cond(Theme.light, Theme.darcula),
                            **{
                                "width": "100%",
                                "font_size": "12px",
                                "scrollbar_width": "none",
                                "code_tag_props": {"pre": "transparent"},
                                "custom_style": {
                                    "background": "transparent !important",
                                    "pre": {"background": "transparent !important"},
                                    "code": {"background": "transparent !important"},
                                },
                                "border_radius": "10px",
                            },
                        ),
                    ),
                    class_name="rounded-xl h-full w-full flex align-center justify-center items-center py-6 "
                    + rx.cond(active_tab.value == 0, "px-4", "").to(str),
                ),
                border=f"1px dashed {rx.color('gray', 5)}",
                class_name="rounded-xl shadow-sm size-full flex flex-col p-1",
            )

        return wrapper

    return decorator
