import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
)


def areachart_v7():
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
            "Area Chart - Axes",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="mobile",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stack_id="a",
            ),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-2)",
                stroke="var(--chart-2)",
                stack_id="a",
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            rx.recharts.y_axis(
                width=30,
                axis_line=False,
                min_tick_gap=50,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
