

# Pie Chart

Pie Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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
A minimal example showing proportional data distribution in a circular format.

```python
def piechart_v1():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Hovering Labels
Displays labels that appear dynamically when hovering over chart segments.

```python
def piechart_v2():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Hovering Labels", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                label=True,
                label_line=False,
                class_name="text-sm font-bold",
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Inner Labels
Shows labels positioned inside each pie segment for compact presentation.

```python
def piechart_v3():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Inner Labels", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.recharts.label_list(
                    fill=rx.color("slate", 12),
                    class_name="text-sm font-bold",
                ),
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Legend
Adds a built-in legend for easy segment identification and reference.

```python
def piechart_v4():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Legend", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                legend_type="square",
            ),
            rx.recharts.legend(class_name="text-sm font-bold"),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Doughnut
Renders the pie chart with a hollow center for a modern doughnut style.

```python
def piechart_v5():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Doughnut", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                inner_radius=60,
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Active
Demonstrates interactive segment highlighting and selection states.

```python
def piechart_v6():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.box(
        info("Pie Chart - Active", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            get_tooltip(),
            rx.recharts.pie(
                rx.foreach(
                    range(6),
                    lambda color, index: rx.recharts.cell(
                        fill=f"var(--chart-{index + 1})",
                    ),
                ),
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                inner_radius=60,
                custom_attrs={
                    "strokeWidth": 5,
                    "activeIndex": 1,
                    "activeShape": {"outerRadius": 120},
                },
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```

