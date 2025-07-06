import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.line.api import LineChart


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
            "Line Chart", "3", "Showing total visitors for the last 6 months", "start"
        ),
        LineChart(data)
        .x("month")
        .series(
            "desktop", stroke="chart-1", stroke_width=2, type_="natural", dot=False
        )(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
