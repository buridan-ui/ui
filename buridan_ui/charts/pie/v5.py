import reflex as rx
from buridan_ui.charts.pie.api import PieChart
from buridan_ui.charts.style import info


def piechart_v5():
    data: list[dict] = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Doughnut", "3", "January - June 2024", "center"),
        PieChart(data)
        .values("visitors", "browser")
        .colors(
            [
                "var(--chart-1)",
                "var(--chart-2)",
                "var(--chart-3)",
                "var(--chart-4)",
                "var(--chart-5)",
            ]
        )
        .radius(inner=60)
        .size("100%", 250)(),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
