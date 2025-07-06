import reflex as rx

from typing import List, Dict, Union
from buridan_ui.charts.bar.api import BarChart


def barchart_v8():
    categories = ["Successful", "Refunded"]
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    EUROPE = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            months,
            [12, 24, 48, 24, 34, 26, 12, 38, 23, 20, 24, 21],
            [0, 1, 4, 2, 0, 0, 0, 2, 1, 0, 0, 8],
        )
    ]

    ASIA = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            months,
            [31, 32, 44, 23, 35, 48, 33, 38, 41, 39, 32, 19],
            [1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 5],
        )
    ]

    def create_chart(data: List[Dict[str, Union[str, int]]]):
        chart = (
            BarChart(data)
            .x("date")
            .size("100%", 250)
            .config(bar_size=25)
            .x_axis(
                interval=10,
                tick_size=10,
                class_name="text-xs font-semibold",
                axis_line=False,
                tick_line=False,
            )
            .tooltip(True)
            .grid(True)
            .y_axis(hide=True)
        )
        # Add stacked bars dynamically for categories
        for i, key in enumerate(categories):
            chart.series(
                key=key,
                fill=f"chart-{i + 1}",
                stack_id="_",
            )
        return chart()

    return rx.box(
        rx.text("Online Transactions", class_name="text-md font-semibold pb-3"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Europe", class_name="text-sm font-semibold"),
                    flex="1",
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Asia", class_name="text-sm font-semibold"),
                    flex="1",
                    value="2",
                ),
            ),
            rx.tabs.content(create_chart(EUROPE), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(ASIA), value="2", margin_top="-5px"),
            default_value="1",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
