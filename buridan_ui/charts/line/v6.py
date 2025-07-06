import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.line.api import LineChart


def linechart_v6():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info(
            "Line Chart - Minimal",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        LineChart(data)
        .x("visitors")
        .series(
            "visitors", stroke="chart-1", stroke_width=2, type_="natural", dot=False
        )
        .x_axis(hide=True)(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
