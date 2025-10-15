import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
)


def linechart_v6():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info(
            "Line Chart - Minimal",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="visitors",
                type_="natural",
                dot=False,
                stroke="var(--chart-1)",
                stroke_width=2,
            ),
            data=data,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20, "top": 25},
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
