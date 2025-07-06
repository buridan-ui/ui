from buridan_ui.charts.area.api import AreaChart


def areachart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return (
        AreaChart(data)
        .x("month")
        .series(
            "desktop", color="chart-1", stroke="chart-1", gradient=True, stack_id="1"
        )
        .series(
            "mobile", color="chart-2", stroke="chart-2", gradient=True, stack_id="1"
        )
        .tooltip(True)
        .grid(True)
        .legend(
            {
                "desktop": "Desktop",
                "mobile": "Mobile",
            },
            position="bottom",
        )
        .size("100%", 250)()
    )
