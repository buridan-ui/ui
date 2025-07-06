import reflex as rx

from buridan_ui.charts.style import info
from buridan_ui.charts.area.api import AreaChart


def areachart_v6():
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
            "Area Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        (
            AreaChart(data)
            .x("month")
            .series("mobile", color="chart-1", stroke="chart-1", stack_id="a")
            .series("desktop", color="chart-2", stroke="chart-2", stack_id="a")
            .tooltip(True)
            .grid(True)
            .legend(
                labels={"mobile": "Mobile", "desktop": "Desktop"},
                position="top",
            )
            .size("100%", 250)
        )(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
