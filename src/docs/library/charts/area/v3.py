import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def areachart_v3():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Area Chart - Step",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="step",
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
