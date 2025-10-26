

# Radar Chart

Radar Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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
A minimal example showing multivariate data in a radial layout with filled areas.

```python
def radar_v1():
    stats = [
        {"category": "Farming", "score": 8},
        {"category": "Fighting", "score": 7},
        {"category": "Aggressiveness", "score": 6},
        {"category": "Map Awareness", "score": 5},
        {"category": "Objective Control", "score": 9},
        {"category": "Positioning", "score": 7},
    ]

    return rx.box(
        info(
            "Radar Chart",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.radar(
                data_key="score",
                stroke="none",
                fill="var(--chart-1)",
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center",
    )
```


## Stroke with Dots
Displays data points with visible markers along the radar lines for clarity.

```python
def radar_v2():
    stats = [
        {"category": "Farming", "score": 8},
        {"category": "Fighting", "score": 7},
        {"category": "Aggressiveness", "score": 6},
        {"category": "Map Awareness", "score": 5},
        {"category": "Objective Control", "score": 9},
        {"category": "Positioning", "score": 7},
    ]

    return rx.box(
        info(
            "Radar Chart - Dots",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.radar(
                data_key="score",
                dot=True,
                stroke="var(--chart-2)",
                fill="var(--chart-1)",
                custom_attrs={"strokeWidth": 2},
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center",
    )
```


## Stacked
Visualizes multiple data series layered on top of each other for comparison.

```python
def radar_v3():
    stats = [
        {"category": "Farming", "score": 6, "average": 8},
        {"category": "Fighting", "score": 8, "average": 9},
        {"category": "Aggressiveness", "score": 5, "average": 8},
        {"category": "Map Awareness", "score": 9, "average": 9},
        {"category": "Objective Control", "score": 7, "average": 8},
        {"category": "Positioning", "score": 6, "average": 9},
    ]

    return rx.vstack(
        info(
            "Radar Chart - Stacked",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            get_tooltip(),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.radar(
                data_key="average", fill_opacity=0.5, stroke="none", fill="teal"
            ),
            rx.recharts.radar(
                data_key="score",
                fill_opacity=1.0,
                stroke="none",
                fill="var(--chart-1)",
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Lines Only
Shows only the outline strokes without filled areas for a cleaner look.

```python
def radar_v4():
    stats = [
        {"category": "Farming", "score": 8, "average": 8},
        {"category": "Fighting", "score": 7, "average": 9},
        {"category": "Aggressiveness", "score": 6, "average": 8},
        {"category": "Map Awareness", "score": 5, "average": 9},
        {"category": "Objective Control", "score": 9, "average": 8},
        {"category": "Positioning", "score": 7, "average": 9},
    ]

    return rx.vstack(
        info(
            "Radar Chart - Lines Only",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            get_tooltip(),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
            ),
            rx.recharts.radar(
                data_key="average",
                stroke="teal",
                fill="none",
                custom_attrs={"strokeWidth": 2},
            ),
            rx.recharts.radar(
                data_key="score",
                fill="none",
                stroke="var(--chart-1)",
                custom_attrs={"strokeWidth": 2},
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Circle Grid
Uses circular grid lines instead of polygon shapes for the background.

```python
def radar_v5():
    stats = [
        {"category": "Farming", "score": 8},
        {"category": "Fighting", "score": 7},
        {"category": "Aggressiveness", "score": 6},
        {"category": "Map Awareness", "score": 5},
        {"category": "Objective Control", "score": 9},
        {"category": "Positioning", "score": 7},
    ]

    return rx.box(
        info(
            "Radar Chart - Circle Grid",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            get_tooltip(),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
                grid_type="circle",
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
                axis_line_type="circle",
            ),
            rx.recharts.radar(
                data_key="score",
                dot=True,
                stroke="var(--chart-2)",
                fill="var(--chart-1)",
                custom_attrs={"strokeWidth": 2},
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Filled Grid
Renders the grid with filled background sections for enhanced visual contrast.

```python
def radar_v6():
    stats = [
        {"category": "Farming", "score": 7},
        {"category": "Fighting", "score": 6},
        {"category": "Aggressiveness", "score": 7},
        {"category": "Map Awareness", "score": 6},
        {"category": "Objective Control", "score": 6},
        {"category": "Positioning", "score": 7},
    ]

    return rx.box(
        info(
            "Radar Chart - Filled Grid",
            "3",
            "Player performance across key gameplay categories",
            "center",
        ),
        rx.recharts.radar_chart(
            get_tooltip(),
            rx.recharts.polar_grid(
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300 fill-[gray] opacity-20",
                    "text-sm stroke-gray-700 fill-[gray] opacity-20",
                ),
                grid_type="circle",
            ),
            rx.recharts.polar_angle_axis(
                data_key="category",
                class_name=rx.color_mode_cond(
                    "text-sm stroke-gray-300",
                    "text-sm stroke-gray-700",
                ),
                axis_line_type="circle",
            ),
            rx.recharts.radar(
                data_key="score",
                dot=False,
                fill="var(--chart-1)",
                stroke="none",
            ),
            data=stats,
            width="100%",
            height=250,
            margin={"left": 20, "right": 20},
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Performance trends in key gameplay categories",
            "center",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 items-center [&_.recharts-tooltip-item-separator]:w-full",
    )
```

