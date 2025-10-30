

# Scatter Chart

Scatter Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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
A minimal example showing the relationship between two variables with individual data points.


```python
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
```

