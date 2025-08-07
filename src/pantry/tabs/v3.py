import reflex as rx
from reflex.experimental import ClientStateVar

ActiveTab = ClientStateVar.create("tab_v3", 0)
TabList = ["github", "twitter", "youtube"]


def tab_v3():
    return rx.box(
        rx.hstack(
            rx.foreach(
                TabList,
                lambda tab, i: rx.button(
                    rx.icon(
                        tag=tab,
                        width="14px",
                        height="14px",
                        color=rx.cond(
                            ActiveTab.value == i,
                            rx.color("slate", 12),
                            rx.color("slate", 10),
                        ),
                    ),
                    on_click=[
                        rx.call_function(ActiveTab.set_value(i)),
                    ],
                    aria_disabled="false",
                    background=rx.cond(
                        ActiveTab.value == i,
                        rx.color("gray", 3),
                        "transparent",
                    ),
                    style={
                        "display": "flex",
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
                            ActiveTab.value == i, "0.375rem", "0.5rem"
                        ),
                        "box_shadow": rx.cond(
                            ActiveTab.value == i,
                            "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                            "none",
                        ),
                    },
                ),
            ),
            style={
                "display": "inline-flex",
                "min_height": "2.125rem",
                "align_items": "baseline",
                "justify_content": "flex-start",
                "border_radius": "0.5rem",
                "padding": "0.25rem",
                "border": f"1.25px dashed {rx.color('gray', 4)}",
            },
        )
    )
