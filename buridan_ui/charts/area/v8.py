import reflex as rx
from buridan_ui.charts.style import get_tooltip, get_cartesian_grid


def areachart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    def create_gradient(color_key):
        return rx.el.svg.defs(
            rx.el.svg.linear_gradient(
                rx.el.svg.stop(
                    stop_color=rx.color(color_key, 7), offset="0%", stop_opacity=0.3
                ),
                rx.el.svg.stop(
                    stop_color=rx.color(color_key, 7), offset="75%", stop_opacity=0
                ),
                x1=0,
                x2=0,
                y1=0,
                y2=1,
                id=color_key,
            ),
        )

    return rx.box(
        rx.hstack(
            rx.foreach(
                [["Desktop", "red"], ["Mobile", "blue"]],
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
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.area_chart(
            create_gradient("red"),
            create_gradient("blue"),
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="url(#red)",
                stroke=rx.color("red", 8),
                stack_id="1",
            ),
            rx.recharts.area(
                data_key="mobile",
                fill="url(#blue)",
                stroke=rx.color("blue", 8),
                stack_id="1",
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
