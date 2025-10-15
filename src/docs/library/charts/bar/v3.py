import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
)


def barchart_v3():
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
            "Bar Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_cartesian_grid(),
            get_tooltip(),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                stack_id="a",
                radius=[0, 0, 6, 6],
            ),
            rx.recharts.bar(
                data_key="mobile",
                fill="var(--chart-2)",
                stack_id="a",
                radius=[6, 6, 0, 0],
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            rx.recharts.x_axis(
                data_key="month",
                type_="category",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=250,
            bar_gap=2,
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
