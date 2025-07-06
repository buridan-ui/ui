import reflex as rx
from buridan_ui.charts.bar.api import BarChart


def barchart_v10():
    sport = [
        {"date": "Jan 23", "Running": 167, "Cycling": 145},
        {"date": "Feb 23", "Running": 125, "Cycling": 110},
        {"date": "Mar 23", "Running": 156, "Cycling": 149},
        {"date": "Apr 23", "Running": 165, "Cycling": 112},
        {"date": "May 23", "Running": 153, "Cycling": 138},
        {"date": "Jun 23", "Running": 124, "Cycling": 145},
        {"date": "Jul 23", "Running": 164, "Cycling": 134},
    ]

    activities = ["Running", "Cycling"]
    chart_colors = ["var(--chart-1)", "var(--chart-2)"]

    def create_chart(active_key: str):
        chart = (
            BarChart(sport)
            .x("date")
            .size("100%", 250)
            .config(bar_category_gap="20%")
            .tooltip(True)
        )

        for key, color in zip(activities, chart_colors):
            opacity = rx.cond(key == active_key, "0.25", "1")
            chart.series(
                key=key,
                fill=color,
                radius=4,
                is_animation_active=False,
                custom_attrs={"opacity": opacity},
            )

        return chart()

    return rx.box(
        rx.tabs.root(
            rx.tabs.list(
                *[
                    rx.tabs.trigger(
                        rx.text(activity, class_name="text-sm font-semibold"),
                        value=str(i + 1),
                    )
                    for i, activity in enumerate(activities)
                ]
            ),
            *[
                rx.tabs.content(
                    create_chart(active),
                    value=str(i + 1),
                    margin_top="-5px",
                )
                for i, active in enumerate(activities)
            ],
            default_value="1",
            width="100%",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
