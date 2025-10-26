

# Area Chart

Area Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Usage
Copy the following helper functions into your Reflex application.


```python
import reflex as rx

tooltip = {
    "is_animation_active": False,
    "separator": "",
    "cursor": False,
    "item_style": {
        "color": "currentColor",
        "display": "flex",
        "paddingBottom": "0px",
        "justifyContent": "space-between",
        "textTransform": "capitalize",
    },
    "label_style": {
        "color": rx.color("slate", 10),
        "fontWeight": "500",
    },
    "content_style": {
        "background": rx.color_mode_cond("oklch(0.97 0.00 0)", "oklch(0.14 0.00 286)"),
        "borderColor": rx.color("slate", 5),
        "borderRadius": "5px",
        "fontFamily": "IBM Plex Mono,ui-monospace,monospace",
        "fontSize": "0.875rem",
        "lineHeight": "1.25rem",
        "fontWeight": "500",
        "letterSpacing": "-0.01rem",
        "minWidth": "8rem",
        "width": "175px",
        "padding": "0.375rem 0.625rem ",
        "position": "relative",
    },
}


def info(title: str, size: str, subtitle: str, align: str):
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )


def get_tooltip():
    """Standard tooltip for all charts."""
    return rx.recharts.graphing_tooltip(**tooltip)


def get_cartesian_grid():
    """Standard cartesian grid for charts."""
    return rx.recharts.cartesian_grid(
        horizontal=True, vertical=False, class_name="opacity-25"
    )


def get_x_axis(data_key: str):
    """Standard X axis configuration."""
    return rx.recharts.x_axis(
        data_key=data_key,
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
        interval="preserveStartEnd",
    )
```


# Examples
Below are examples demonstrating how these components and charts can be used.

## Basic
A minimal example showing a single series with a smooth gradient fill.

```python
def areachart_v1():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Area Chart",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stroke_width=2,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "January - June 2024",
            "start",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Linear
Displays data using straight line segments between points.

```python
def areachart_v2():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Area Chart - Linear",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="linear",
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "January - June 2024",
            "start",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Step
Renders the chart with stepped transitions, ideal for discrete intervals.

```python
def areachart_v3():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Area Chart - Step",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="step",
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Stacked
Visualizes multiple data series stacked on top of each other for cumulative comparison.

```python
def areachart_v4():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return rx.box(
        info(
            "Area Chart - Stacked",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stroke_width=2,
                stack_id="a",
            ),
            rx.recharts.area(
                data_key="mobile",
                fill="var(--chart-2)",
                stroke="var(--chart-2)",
                stroke_width=2,
                stack_id="a",
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Dynamic
Demonstrates how data or series can update interactively in real-time.

```python
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
```


## Legend
Adds a built-in legend for easy series identification.

```python
def areachart_v6():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return rx.box(
        info(
            "Area Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="mobile",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stack_id="a",
            ),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-2)",
                stroke="var(--chart-2)",
                stack_id="a",
            ),
            get_x_axis("month"),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Axes
Shows full control over axis configuration, labels, and styling.

```python
def areachart_v7():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return rx.box(
        info(
            "Area Chart - Axes",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="mobile",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stack_id="a",
            ),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-2)",
                stroke="var(--chart-2)",
                stack_id="a",
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            rx.recharts.y_axis(
                width=30,
                axis_line=False,
                min_tick_gap=50,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Custom Legends
Implements a user-defined legend layout for better presentation control.

```python
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
```


## Step with Gradient
Combines stepped transitions with a smooth color gradient for visual emphasis.

```python
def areachart_v9():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

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

    return rx.box(
        info(
            "Area Chart - Step with Gradient",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            rx.el.svg.defs(
                gradient("desktop", "chart-1"),
            ),
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="desktop",
                fill="url(#desktop)",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="step",
                is_animation_active=False,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "January - June 2024",
            "start",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Custom Legend and Axes
A complete example with custom legends, axes, and advanced styling combined.

```python
def areachart_v10():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]
    series = [("mobile", "Mobile", "--chart-1"), ("desktop", "Desktop", "--chart-2")]

    return rx.box(
        info(
            "Area Chart - Stacked with Legend and Custom Axes",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.area_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.area(
                data_key="mobile",
                fill="var(--chart-1)",
                stroke="var(--chart-1)",
                stack_id="a",
            ),
            rx.recharts.area(
                data_key="desktop",
                fill="var(--chart-2)",
                stroke="var(--chart-2)",
                stack_id="a",
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            rx.recharts.y_axis(
                width=30,
                axis_line=False,
                min_tick_gap=50,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            width="100%",
            height=250,
        ),
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
            class_name="py-2 px-4 flex w-full justify-center gap-8",
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```

