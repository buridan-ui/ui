import reflex as rx

from buridan_ui.charts.style import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def areachart_v1():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        rx.vstack(
            info(
                "Area Chart",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.area_chart(
                get_tooltip(),
                get_cartesian_grid(),
                rx.recharts.area(
                    data_key="desktop",
                    fill=rx.color("accent"),
                    stroke=rx.color("accent", 8),
                ),
                get_x_axis("month"),
                data=data,
                width="100%",
                height=250,
            ),
            info(
                "Trending up by 5.2% this month",
                "2",
                "January - June 2024",
                "start",
            ),
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        class_name="w-[100%] p-1",
    )
