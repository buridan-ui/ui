from buridan_ui.charts.line.api import LineChart


def linechart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return (
        LineChart(data)
        .x("month")
        .series(
            "desktop",
            stroke="var(--chart-1)",
            type_="linear",
            dot=False,
            stroke_width=2,
        )
        .series(
            "mobile", stroke="var(--chart-2)", type_="linear", dot=False, stroke_width=2
        )
        .legend(labels={"desktop": "Desktop", "mobile": "Mobile"}, position="top")
        .size("100%", 250)
    )()
