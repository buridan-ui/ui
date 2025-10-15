import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def linechart_v4():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return rx.box(
        info(
            "Line Chart - Multiple",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.foreach(
                ["desktop", "mobile"],
                lambda name, index: rx.recharts.line(
                    data_key=name,
                    stroke=f"var(--chart-{index + 1})",
                    stroke_width=2,
                    type_="natural",
                    dot=False,
                    stack_id="a",
                ),
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
