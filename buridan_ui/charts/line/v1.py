import reflex as rx

from buridan_ui.charts.style import (
    info,
    get_tooltip,
    get_cartesian_grid,
    get_x_axis,
)


def linechart_v1():
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
            "Line Chart",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="desktop",
                stroke=rx.color("accent", 8),
                stroke_width=2,
                type_="natural",
                dot=False,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )


def _line_chart():
    data = [
        {"month": " ", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": " ", "desktop": 214, "mobile": 140},
    ]
    return rx.box(
        rx.hstack(
            rx.foreach(
                [["Desktop", "red"], ["Mobile", "blue"]],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=rx.color(key[1])),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="desktop",
                stroke=rx.color("red"),
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.line(
                data_key="mobile",
                stroke=rx.color("blue"),
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=350,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
