import reflex as rx
from src.docs.library.charts.util import (
    get_tooltip,
    get_x_axis,
)


def linechart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]
    return rx.box(
        rx.hstack(
            rx.foreach(
                [["Desktop", "var(--chart-1)"], ["Mobile", "var(--chart-2)"]],
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
        rx.recharts.line_chart(
            get_tooltip(),
            rx.recharts.line(
                data_key="desktop",
                stroke="var(--chart-1)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.line(
                data_key="mobile",
                stroke="var(--chart-2)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
