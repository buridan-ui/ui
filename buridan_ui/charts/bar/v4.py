import reflex as rx

from ..style import info, tooltip


def barchart_v4():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Bar Chart - Labeled",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                ),
                rx.recharts.graphing_tooltip(**tooltip),
                rx.recharts.bar(
                    rx.recharts.label_list(
                        data_key="desktop",
                        position="top",
                        stroke="10",
                        offset=10,
                    ),
                    data_key="desktop",
                    fill=rx.color("accent"),
                    stack_id="a",
                    radius=6,
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
                data=data,
                width="100%",
                height=250,
                margin={"top": 25},
                bar_size=25,
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        width="100%",
        padding="0.5em",
    )
