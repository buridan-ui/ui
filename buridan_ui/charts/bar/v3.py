import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.bar.api import BarChart


def barchart_v3():
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
            "Bar Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        BarChart(data)
        .x("month")
        .series("desktop", fill="chart-1", stack_id="a", radius=[0, 0, 6, 6])
        .series("mobile", fill="chart-2", stack_id="a", radius=[6, 6, 0, 0])
        .tooltip(True)
        .grid(True)
        .size("100%", 250)
        .x_axis(type_="category", data_key="month")
        .config(bar_gap=2, bar_size=25)
        .legend({"desktop": "Desktop", "mobile": "Mobile"})(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
