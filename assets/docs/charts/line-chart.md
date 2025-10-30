

# Line Chart

Line Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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
A minimal example showing a single series with a smooth line connection.

```python
def linechart_v1():
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
            "Line Chart",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="desktop",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="natural",
                dot=False,
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


## Linear
Displays data using straight line segments between points.

```python
def linechart_v2():
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
            "Line Chart - Linear",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="desktop",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="linear",
                dot=False,
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


## Label
Shows data points with labels for clear value identification.

```python
def linechart_v3():
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
            "Line Chart - Label",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                rx.recharts.label_list(
                    position="top",
                    offset=20,
                    custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                ),
                data_key="desktop",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="linear",
                dot=True,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20, "top": 25},
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Multiple
Visualizes multiple data series on the same chart for comparison.

```python
def linechart_v4():
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
            "Line Chart - Multiple",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.foreach(
                ["desktop", "mobile"],
                lambda name, index: rx.recharts.line(
                    data_key=name,
                    stroke=f"var(--chart-{index + 1})",
                    stroke_width=2,
                    type_="natural",
                    dot=False,
                    stack_id="a",
                ),
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


## Title Label
Includes a title and labels for comprehensive chart context.

```python
def linechart_v5():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info(
            "Line Chart - Title Label",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                rx.recharts.label_list(
                    position="top",
                    offset=20,
                    custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                    data_key="browser",
                ),
                data_key="visitors",
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="natural",
                dot=True,
            ),
            data=data,
            width="100%",
            height=250,
            margin={"left": 25, "right": 20, "top": 25},
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Minimal
A clean, stripped-down version focusing on essential data visualization.

```python
def linechart_v6():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info(
            "Line Chart - Minimal",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key="visitors",
                type_="natural",
                dot=False,
                stroke="var(--chart-1)",
                stroke_width=2,
            ),
            data=data,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20, "top": 25},
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Dynamic
Demonstrates how data or series can update interactively in real-time.

```python
def linechart_v7():
    from reflex.experimental import ClientStateVar

    data = [
        {"date": "2024-04-01", "desktop": 222, "mobile": 150},
        {"date": "2024-04-02", "desktop": 97, "mobile": 180},
        {"date": "2024-04-03", "desktop": 167, "mobile": 120},
        {"date": "2024-04-04", "desktop": 242, "mobile": 260},
        {"date": "2024-04-05", "desktop": 373, "mobile": 290},
        {"date": "2024-04-06", "desktop": 301, "mobile": 340},
        {"date": "2024-04-07", "desktop": 245, "mobile": 180},
        {"date": "2024-04-08", "desktop": 409, "mobile": 320},
        {"date": "2024-04-09", "desktop": 59, "mobile": 110},
        {"date": "2024-04-10", "desktop": 261, "mobile": 190},
        {"date": "2024-04-11", "desktop": 327, "mobile": 350},
        {"date": "2024-04-12", "desktop": 292, "mobile": 210},
        {"date": "2024-04-13", "desktop": 342, "mobile": 380},
        {"date": "2024-04-14", "desktop": 137, "mobile": 220},
        {"date": "2024-04-15", "desktop": 120, "mobile": 170},
        {"date": "2024-04-16", "desktop": 138, "mobile": 190},
        {"date": "2024-04-17", "desktop": 446, "mobile": 360},
        {"date": "2024-04-18", "desktop": 364, "mobile": 410},
        {"date": "2024-04-19", "desktop": 243, "mobile": 180},
        {"date": "2024-04-20", "desktop": 89, "mobile": 150},
        {"date": "2024-04-21", "desktop": 137, "mobile": 200},
        {"date": "2024-04-22", "desktop": 224, "mobile": 170},
        {"date": "2024-04-23", "desktop": 138, "mobile": 230},
        {"date": "2024-04-24", "desktop": 387, "mobile": 290},
        {"date": "2024-04-25", "desktop": 215, "mobile": 250},
        {"date": "2024-04-26", "desktop": 75, "mobile": 130},
        {"date": "2024-04-27", "desktop": 383, "mobile": 420},
        {"date": "2024-04-28", "desktop": 122, "mobile": 180},
        {"date": "2024-04-29", "desktop": 315, "mobile": 240},
        {"date": "2024-04-30", "desktop": 454, "mobile": 380},
        {"date": "2024-05-01", "desktop": 165, "mobile": 220},
        {"date": "2024-05-02", "desktop": 293, "mobile": 310},
        {"date": "2024-05-03", "desktop": 247, "mobile": 190},
        {"date": "2024-05-04", "desktop": 385, "mobile": 420},
        {"date": "2024-05-05", "desktop": 481, "mobile": 390},
        {"date": "2024-05-06", "desktop": 498, "mobile": 520},
        {"date": "2024-05-07", "desktop": 388, "mobile": 300},
        {"date": "2024-05-08", "desktop": 149, "mobile": 210},
        {"date": "2024-05-09", "desktop": 227, "mobile": 180},
        {"date": "2024-05-10", "desktop": 293, "mobile": 330},
        {"date": "2024-05-11", "desktop": 335, "mobile": 270},
        {"date": "2024-05-12", "desktop": 197, "mobile": 240},
        {"date": "2024-05-13", "desktop": 197, "mobile": 160},
        {"date": "2024-05-14", "desktop": 448, "mobile": 490},
        {"date": "2024-05-15", "desktop": 473, "mobile": 380},
        {"date": "2024-05-16", "desktop": 338, "mobile": 400},
        {"date": "2024-05-17", "desktop": 499, "mobile": 420},
        {"date": "2024-05-18", "desktop": 315, "mobile": 350},
        {"date": "2024-05-19", "desktop": 235, "mobile": 180},
        {"date": "2024-05-20", "desktop": 177, "mobile": 230},
        {"date": "2024-05-21", "desktop": 82, "mobile": 140},
        {"date": "2024-05-22", "desktop": 81, "mobile": 120},
        {"date": "2024-05-23", "desktop": 252, "mobile": 290},
        {"date": "2024-05-24", "desktop": 294, "mobile": 220},
        {"date": "2024-05-25", "desktop": 201, "mobile": 250},
        {"date": "2024-05-26", "desktop": 213, "mobile": 170},
        {"date": "2024-05-27", "desktop": 420, "mobile": 460},
        {"date": "2024-05-28", "desktop": 233, "mobile": 190},
        {"date": "2024-05-29", "desktop": 78, "mobile": 130},
        {"date": "2024-05-30", "desktop": 340, "mobile": 280},
        {"date": "2024-05-31", "desktop": 178, "mobile": 230},
        {"date": "2024-06-01", "desktop": 178, "mobile": 200},
        {"date": "2024-06-02", "desktop": 470, "mobile": 410},
        {"date": "2024-06-03", "desktop": 103, "mobile": 160},
        {"date": "2024-06-04", "desktop": 439, "mobile": 380},
        {"date": "2024-06-05", "desktop": 88, "mobile": 140},
        {"date": "2024-06-06", "desktop": 294, "mobile": 250},
        {"date": "2024-06-07", "desktop": 323, "mobile": 370},
        {"date": "2024-06-08", "desktop": 385, "mobile": 320},
        {"date": "2024-06-09", "desktop": 438, "mobile": 480},
        {"date": "2024-06-10", "desktop": 155, "mobile": 200},
        {"date": "2024-06-11", "desktop": 92, "mobile": 150},
        {"date": "2024-06-12", "desktop": 492, "mobile": 420},
        {"date": "2024-06-13", "desktop": 81, "mobile": 130},
        {"date": "2024-06-14", "desktop": 426, "mobile": 380},
        {"date": "2024-06-15", "desktop": 307, "mobile": 350},
        {"date": "2024-06-16", "desktop": 371, "mobile": 310},
    ]

    formatted_data = [
        {
            "date": datetime.strptime(item["date"], "%Y-%m-%d").strftime("%b %d"),
            "desktop": item["desktop"],
            "mobile": item["mobile"],
        }
        for item in data
    ]

    SelectedType = ClientStateVar.create("selected_line", "mobile")
    DotTrigger = ClientStateVar.create("dot_trigger", False)

    return rx.box(
        rx.hstack(
            info(
                "Line Chart - Dynamic",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.hstack(
                rx.checkbox(
                    "Show Dots", on_change=DotTrigger.set_value(~DotTrigger.value)
                ),
                rx.el.select(
                    rx.el.option("Mobile", on_click=SelectedType.set_value("mobile")),
                    rx.el.option("Desktop", on_click=SelectedType.set_value("desktop")),
                    default_value="Mobile",
                    bg=rx.color("gray", 2),
                    border=f"1px solid {rx.color('gray', 4)}",
                    class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3",
                ),
                align="center",
            ),
            align="center",
            justify="between",
            width="100%",
            wrap="wrap",
        ),
        rx.recharts.line_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.line(
                data_key=SelectedType.value,
                stroke="var(--chart-1)",
                stroke_width=2,
                type_="natural",
                dot=DotTrigger.value,
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            get_x_axis("date"),
            data=formatted_data,
            width="100%",
            height=280,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Custom Legends
Implements a user-defined legend layout for better presentation control.

```python
def linechart_v8():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]
    return rx.box(
        rx.hstack(
            rx.foreach(
                [["Desktop", "var(--chart-1)"], ["Mobile", "var(--chart-2)"]],
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
        rx.recharts.line_chart(
            get_tooltip(),
            rx.recharts.line(
                data_key="desktop",
                stroke="var(--chart-1)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.line(
                data_key="mobile",
                stroke="var(--chart-2)",
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```

