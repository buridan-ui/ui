import reflex as rx
from buridan_ui.charts.style import info
from buridan_ui.charts.area.api import AreaChart


def areachart_v5():
    # Data generation
    import datetime
    import random
    from reflex.experimental import ClientStateVar

    start_date = datetime.date(2024, 4, 1)
    data = [
        {
            "date": (start_date + datetime.timedelta(days=i)).strftime("%b %d"),
            "desktop": random.randint(80, 500),
            "mobile": random.randint(100, 550),
        }
        for i in range(91)
    ]

    # Client-side state for filtering
    SelectedRange = ClientStateVar.create("selected", data)

    select_options = [
        ("Last 3 Months", data),
        ("Last 30 Days", data[-30:]),
        ("Last 7 Days", data[-7:]),
    ]

    return rx.box(
        rx.hstack(
            info(
                "Area Chart - Dynamic",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.el.select(
                *[
                    rx.el.option(label, on_click=SelectedRange.set_value(value))
                    for label, value in select_options
                ],
                default_value="Last 3 Months",
                bg=rx.color("gray", 2),
                border=f"1px solid {rx.color('gray', 4)}",
                class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3",
            ),
            align="center",
            justify="between",
            width="100%",
            wrap="wrap",
        ),
        (
            AreaChart(SelectedRange.value)
            .x("date")
            .series(
                "mobile", color="chart-2", gradient=True, stroke="chart-2", stack_id="a"
            )
            .series(
                "desktop",
                color="chart-1",
                gradient=True,
                stroke="chart-1",
                stack_id="a",
            )
            .tooltip(True)
            .grid(True)
            .size("100%", 280)
        )(),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
