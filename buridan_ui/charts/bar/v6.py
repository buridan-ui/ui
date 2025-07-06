import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.bar.api import BarChart


def barchart_v6():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237, "active": True},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    modified_data = [
        {
            **item,
            "stroke": "var(--chart-3)" if item.get("active", False) else "none",
        }
        for item in data
    ]

    return rx.box(
        info(
            "Bar Chart - Active",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        BarChart(modified_data)
        .x("month")
        .series(
            "desktop",
            fill="chart-1",
            stack_id="a",
            radius=6,
            stroke="stroke",
            stroke_width=3,
        )
        .size("100%", 250)
        .config(margin={"top": 25}, bar_size=25)(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
