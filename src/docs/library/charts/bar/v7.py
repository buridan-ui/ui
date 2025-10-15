import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
)


def barchart_v7():
    data = [
        {"browser": "Chrome", "visitors": 275, "fill": "var(--chart-1)"},
        {"browser": "Safari", "visitors": 200, "fill": "var(--chart-2)"},
        {"browser": "Firefox", "visitors": 187, "fill": "var(--chart-3)"},
        {"browser": "Edge", "visitors": 173, "fill": "var(--chart-4)"},
        {"browser": "Other", "visitors": 90, "fill": "var(--chart-5)"},
    ]

    return rx.box(
        info(
            "Bar Chart - Mixed",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
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
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
