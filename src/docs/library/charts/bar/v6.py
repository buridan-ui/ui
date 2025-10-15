import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def barchart_v6():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237, "active": True},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    modified_data = [
        {
            **item,
            "stroke": ("var(--chart-3)" if item.get("active", False) else "none"),
        }
        for item in data
    ]

    return rx.box(
        info(
            "Bar Chart - Active",
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
                radius=6,
                stroke="stroke",
                stroke_width=3,
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            get_x_axis("month"),
            data=modified_data,
            width="100%",
            height=250,
            margin={"top": 25},
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
