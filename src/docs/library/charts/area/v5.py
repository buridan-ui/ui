import reflex as rx

from src.docs.library.charts.util import (
    info,
    get_tooltip,
    get_cartesian_grid,
)


def areachart_v5():
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

    SelectedRange = ClientStateVar.create("area_selected", data)

    def gradient(id_: str, color: str):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.8),
            rx.el.svg.stop(
                stop_color=f"var(--{color})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=id_,
        )

    def area(data_key: str, color: str):
        return rx.recharts.area(
            data_key=data_key,
            fill=f"url(#{data_key})",
            stack_id="a",
            stroke=f"var(--{color})",
            animation_easing="linear",
        )

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
        rx.recharts.area_chart(
            rx.el.svg.defs(
                gradient("desktop", "chart-1"),
                gradient("mobile", "chart-2"),
            ),
            get_tooltip(),
            get_cartesian_grid(),
            area("mobile", "chart-2"),
            area("desktop", "chart-1"),
            rx.recharts.x_axis(
                data_key="date",
                axis_line=False,
                min_tick_gap=32,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            data=SelectedRange.value,
            width="100%",
            height=280,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
