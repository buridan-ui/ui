

# Doughnut Chart

Doughnut Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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

## Doughnut Chart
A customizable doughnut chart with flexible styling and data visualization options.

```python
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
```


## Doughnut Chart with Label
Displays a doughnut chart with centered label text for enhanced data presentation.

```python
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
```

