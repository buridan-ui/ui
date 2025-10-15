import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
)


def piechart_v3():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Inner Labels", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.recharts.label_list(
                    fill=rx.color("slate", 12),
                    class_name="text-sm font-bold",
                ),
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
