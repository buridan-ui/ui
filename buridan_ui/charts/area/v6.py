import reflex as rx

from buridan_ui.charts.style import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def areachart_v6():
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
            "Area Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            *[
                rx.recharts.area(
                    data_key=name,
                    fill=rx.color("accent", 7 + index),
                    stroke="none",
                )
                for index, name in enumerate(["desktop", "mobile"])
            ],
            get_x_axis("month"),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
