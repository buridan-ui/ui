import reflex as rx
from src.docs.library.charts.util import (
    get_tooltip,
    get_x_axis,
)


def barchart_v9():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
    ]

    return rx.box(
        rx.hstack(
            rx.foreach(
                [
                    ["Desktop", "var(--chart-1)"],
                    ["Mobile", "var(--chart-2)"],
                    ["Tablet", "var(--chart-3)"],
                ],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=key[1]),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            rx.recharts.bar(data_key="desktop", fill="var(--chart-1)", radius=4),
            rx.recharts.bar(data_key="mobile", fill="var(--chart-2)", radius=4),
            rx.recharts.bar(data_key="tablet", fill="var(--chart-3)", radius=4),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
