import reflex as rx


def doughnutchart_v1():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.el.div(
        rx.recharts.pie_chart(
            rx.recharts.pie(
                rx.foreach(
                    ["red", "blue", "green", "amber", "purple"],
                    lambda color, index: rx.recharts.cell(
                        fill="var(--chart-2)", class_name=f"theme-{color}"
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                inner_radius=90,
                custom_attrs={"paddingAngle": 3, "cornerRadius": 5},
            ),
            width="100%",
            height=350,
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        rx.hstack(
            rx.foreach(
                [
                    ["Chrome", "red"],
                    ["Safari", "blue"],
                    ["Firefox", "green"],
                    ["Edge", "amber"],
                    ["Other", "purple"],
                ],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=rx.color(key[1])),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full justify-center flex-wrap",
        ),
        class_name="flex flex-col size-full relative",
    )
