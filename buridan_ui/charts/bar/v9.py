import reflex as rx
from buridan_ui.charts.bar.api import BarChart


def barchart_v9():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
    ]

    legend_labels = {
        "desktop": "Desktop",
        "mobile": "Mobile",
        "tablet": "Tablet",
    }

    colors = {
        "desktop": "chart-1",
        "mobile": "chart-2",
        "tablet": "chart-3",
    }

    return rx.box(
        BarChart(data)
        .x("month")
        .series("desktop", fill=colors["desktop"], radius=4)
        .series("mobile", fill=colors["mobile"], radius=4)
        .series("tablet", fill=colors["tablet"], radius=4)
        .tooltip(True)
        .legend(legend_labels, position="top")
        .size("100%", 250)(),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
