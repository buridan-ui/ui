import reflex as rx

from ..style import info, tooltip


def barchart_v7():
    data = [
        {"browser": "Chrome", "visitors": 275, "fill": rx.color("accent", 7)},
        {"browser": "Safari", "visitors": 200, "fill": rx.color("accent", 8)},
        {"browser": "Firefox", "visitors": 187, "fill": rx.color("accent", 9)},
        {"browser": "Edge", "visitors": 173, "fill": rx.color("accent", 10)},
        {"browser": "Other", "visitors": 90, "fill": rx.color("accent", 11)},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Bar Chart - Mixed",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.bar_chart(
                rx.recharts.graphing_tooltip(**tooltip),
                rx.recharts.bar(
                    data_key="visitors",
                    fill="fill",
                    radius=6,
                ),
                rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
                rx.recharts.y_axis(
                    data_key="browser",
                    type_="category",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                layout="vertical",
                width="100%",
                height=250,
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            margin_right="20px",
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        width="100%",
        padding="0.5em",
    )
