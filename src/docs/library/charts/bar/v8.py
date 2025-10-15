import reflex as rx
from src.docs.library.charts.util import (
    get_tooltip,
    get_cartesian_grid,
)


def barchart_v8():
    categories = ["Successful", "Refunded"]
    EUROPE = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [12, 24, 48, 24, 34, 26, 12, 38, 23, 20, 24, 21],
            [0, 1, 4, 2, 0, 0, 0, 2, 1, 0, 0, 8],
        )
    ]

    ASIA = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [31, 32, 44, 23, 35, 48, 33, 38, 41, 39, 32, 19],
            [1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 5],
        )
    ]

    def create_chart(data: list[dict[str, str | int]]):
        return rx.recharts.bar_chart(
            get_cartesian_grid(),
            rx.foreach(
                categories,
                lambda key, index: rx.recharts.bar(
                    data_key=key,
                    fill=f"var(--chart-{index + 1})",
                    stack_id="_",
                ),
            ),
            rx.recharts.x_axis(
                interval=10,
                data_key="date",
                tick_size=10,
                class_name="text-xs font-semibold",
                axis_line=False,
                tick_line=False,
            ),
            get_tooltip(),
            data=data,
            width="100%",
            height=250,
            bar_size=25,
        )

    return rx.box(
        rx.text("Online Transactions", class_name="text-md font-semibold pb-3"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Europe", class_name="text-sm font-semibold"),
                    flex="1",
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Asia", class_name="text-sm font-semibold"),
                    flex="1",
                    value="2",
                ),
            ),
            rx.tabs.content(create_chart(EUROPE), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(ASIA), value="2", margin_top="-5px"),
            default_value="1",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
