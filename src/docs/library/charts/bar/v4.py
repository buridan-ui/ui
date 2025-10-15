import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def barchart_v4():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Bar Chart - Labeled",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_cartesian_grid(),
            get_tooltip(),
            rx.recharts.bar(
                rx.recharts.label_list(
                    data_key="desktop",
                    position="top",
                    stroke="10",
                    offset=10,
                ),
                data_key="desktop",
                fill="var(--chart-1)",
                stack_id="a",
                radius=6,
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
            margin={"top": 25},
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
