import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.bar.api import BarChart


def barchart_v2():
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
            "Bar Chart - Horizontal",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        BarChart(data)
        .x("month")
        .series("desktop", fill="chart-1", radius=6)
        .tooltip(True)
        .grid(False)
        .size("100%", 250)
        .layout("vertical")
        .x_axis(show=True, data_key="desktop", type_="number", hide=True, tick_size=0)
        .y_axis(show=True, data_key="month", type_="category", hide=False)
        .config(bar_gap=2, margin={"left": -20})(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
