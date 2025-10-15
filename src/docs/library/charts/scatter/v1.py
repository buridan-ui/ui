import reflex as rx


def scatterchart_v1():
    scat = [
        {"name": " ", "x": 10, "y": 30},
        {"name": "B", "x": 20, "y": 50},
        {"name": "C", "x": 30, "y": 70},
        {"name": "D", "x": 40, "y": 20},
        {"name": "E", "x": 50, "y": 90},
        {"name": "F", "x": 60, "y": 40},
        {"name": "G", "x": 70, "y": 60},
        {"name": "H", "x": 80, "y": 100},
        {"name": "I", "x": 90, "y": 10},
        {"name": " ", "x": 100, "y": 80},
    ]

    scat_2 = [
        {"name": "K", "x": 5, "y": 15},
        {"name": "L", "x": 15, "y": 40},
        {"name": "M", "x": 25, "y": 60},
        {"name": "N", "x": 35, "y": 10},
        {"name": "O", "x": 45, "y": 80},
        {"name": "P", "x": 55, "y": 30},
        {"name": "Q", "x": 65, "y": 50},
        {"name": "R", "x": 75, "y": 90},
        {"name": "S", "x": 85, "y": 20},
        {"name": "T", "x": 95, "y": 70},
    ]
    return rx.el.div(
        rx.hstack(
            rx.foreach(
                [
                    ["Data 1", "var(--chart-1)"],
                    ["Data 2", "var(--chart-2)"],
                ],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=key[1]),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.scatter_chart(
            rx.recharts.scatter(data=scat, data_key="name", fill="var(--chart-1)"),
            rx.recharts.scatter(data=scat_2, data_key="name", fill="var(--chart-2)"),
            rx.recharts.y_axis(
                data_key="y",
                hide=True,
            ),
            rx.recharts.x_axis(
                data_key="x",
                type_="number",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            width="100%",
            height=350,
            class_name="px-4",
        ),
        class_name="flex flex-col size-full",
    )
