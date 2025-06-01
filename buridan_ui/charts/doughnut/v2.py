import reflex as rx


def doughnutchart_v2():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    total_visitors = sum(item["visitors"] for item in data)

    return rx.el.div(
        rx.el.div(
            rx.el.label(total_visitors, class_name="text-4xl font-bold"),
            rx.el.label("Total Visitors", class_name="text-sm font-regular"),
            class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col justify-center align-center items-center",
        ),
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
                class_name="recharts-sector darK:hover:brightness-125 transition duration-200 ease",
            ),
            width="100%",
            height=350,
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        class_name="flex flex-col size-full relative",
    )
