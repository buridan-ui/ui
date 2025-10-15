import reflex as rx
from src.docs.library.charts.util import get_tooltip, get_cartesian_grid


def areachart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    series = [("desktop", "Desktop", "--chart-1"), ("mobile", "Mobile", "--chart-2")]

    def create_gradient(var_name):
        return rx.el.svg.defs(
            rx.el.svg.linear_gradient(
                rx.el.svg.stop(
                    stop_color=f"var({var_name})", offset="5%", stop_opacity=0.8
                ),
                rx.el.svg.stop(
                    stop_color=f"var({var_name})", offset="95%", stop_opacity=0.1
                ),
                x1=0,
                x2=0,
                y1=0,
                y2=1,
                id=var_name.strip("-"),
            )
        )

    return rx.box(
        rx.hstack(
            rx.foreach(
                series,
                lambda s: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=f"var({s[2]})"),
                    rx.text(
                        s[1],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full justify-center gap-8",
        ),
        rx.recharts.area_chart(
            *(create_gradient(s[2]) for s in series),
            get_tooltip(),
            get_cartesian_grid(),
            *(
                rx.recharts.area(
                    data_key=s[0],
                    fill=f"url(#{s[2].strip('-')})",
                    stroke=f"var({s[2]})",
                    stack_id="1",
                )
                for s in series
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
