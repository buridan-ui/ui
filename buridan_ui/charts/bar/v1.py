import reflex as rx
from buridan_ui.charts.style import info
from buridan_ui.charts.bar.api import BarChart


def barchart_v1():
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
            "Bar Chart - Multiple",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        BarChart(data)
        .x("month")
        .series("desktop", fill="chart-1", radius=6, bar_size=25)
        .series("mobile", fill="chart-2", radius=6, bar_size=25)
        .tooltip(True)
        .grid(True)
        .size("100%", 250)
        .config(bar_category_gap="30%")(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
