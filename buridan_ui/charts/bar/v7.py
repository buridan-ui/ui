import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.bar.api import BarChart


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
        BarChart(data)
        .x("browser")
        .series("visitors", fill="fill", radius=6)
        .grid(False)
        .tooltip(True)
        .x_axis(data_key="visitors", type_="number", hide=True, tick_size=0)
        .y_axis(data_key="browser", type_="category")
        .layout("vertical")
        .size("100%", 250)(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
