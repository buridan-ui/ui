

# Bar Chart

Bar charts are ideal for visualizing categorical data and comparing multiple series side by side.
They can be stacked, oriented horizontally, or customized with legends and axes.

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

## Multiple Series
A simple vertical bar chart comparing data categories.

```python
def barchart_v1():
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
            "Bar Chart - Multiple",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.foreach(
                ["desktop", "mobile"],
                lambda name, index: rx.recharts.bar(
                    data_key=name,
                    fill=f"var(--chart-{index + 1})",
                    radius=6,
                ),
            ),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
            bar_size=25,
            bar_category_gap="30%",
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Horizontal
Display multiple datasets within the same chart for comparison.

```python
def barchart_v2():
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
            "Bar Chart - Horizontal",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                radius=6,
            ),
            rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
            rx.recharts.y_axis(
                data_key="month",
                type_="category",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            layout="vertical",
            width="100%",
            height=250,
            bar_gap=2,
            margin={"left": -20},
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Stacked with Legends
Combine related values by stacking bars for cumulative insights.

```python
def barchart_v3():
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
            "Bar Chart - Legend",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_cartesian_grid(),
            get_tooltip(),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                stack_id="a",
                radius=[0, 0, 6, 6],
            ),
            rx.recharts.bar(
                data_key="mobile",
                fill="var(--chart-2)",
                stack_id="a",
                radius=[6, 6, 0, 0],
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            rx.recharts.x_axis(
                data_key="month",
                type_="category",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            rx.recharts.legend(),
            data=data,
            width="100%",
            height=250,
            bar_gap=2,
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Labeled
Flip the orientation to show bars horizontally for improved readability.

```python
def barchart_v4():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        info(
            "Bar Chart - Labeled",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_cartesian_grid(),
            get_tooltip(),
            rx.recharts.bar(
                rx.recharts.label_list(
                    data_key="desktop",
                    position="top",
                    stroke="10",
                    offset=10,
                ),
                data_key="desktop",
                fill="var(--chart-1)",
                stack_id="a",
                radius=6,
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
            margin={"top": 25},
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Dynamic
Demonstrate dynamic updates or data-driven interactivity in your bar chart.

```python
def barchart_v5():
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
    ]

    formatted_data = [
        {
            "date": datetime.strptime(item["date"], "%Y-%m-%d").strftime("%b %d"),
            "desktop": item["desktop"],
            "mobile": item["mobile"],
        }
        for item in data
    ]

    SelectedType = ClientStateVar.create("bar_selected", "mobile")

    return rx.box(
        rx.hstack(
            info(
                "Bar Chart - Dynamic",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
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
            justify="between",
            width="100%",
            wrap="wrap",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            get_cartesian_grid(),
            rx.recharts.bar(
                data_key=SelectedType.value,
                fill="var(--chart-1)",
                radius=[2, 2, 0, 0],
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


## Active
Add a built-in legend for clarity when displaying multiple series.

```python
def barchart_v6():
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237, "active": True},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    modified_data = [
        {
            **item,
            "stroke": ("var(--chart-3)" if item.get("active", False) else "none"),
        }
        for item in data
    ]

    return rx.box(
        info(
            "Bar Chart - Active",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_cartesian_grid(),
            get_tooltip(),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                stack_id="a",
                radius=6,
                stroke="stroke",
                stroke_width=3,
            ),
            rx.recharts.y_axis(type_="number", hide=True),
            get_x_axis("month"),
            data=modified_data,
            width="100%",
            height=250,
            margin={"top": 25},
            bar_size=25,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Mixed Horizontal
Create a fully custom legend layout using Reflex components.

```python
def barchart_v7():
    data = [
        {"browser": "Chrome", "visitors": 275, "fill": "var(--chart-1)"},
        {"browser": "Safari", "visitors": 200, "fill": "var(--chart-2)"},
        {"browser": "Firefox", "visitors": 187, "fill": "var(--chart-3)"},
        {"browser": "Edge", "visitors": 173, "fill": "var(--chart-4)"},
        {"browser": "Other", "visitors": 90, "fill": "var(--chart-5)"},
    ]

    return rx.box(
        info(
            "Bar Chart - Mixed",
            "3",
            "Showing total visitors for the last 6 months",
            "start",
        ),
        rx.recharts.bar_chart(
            get_tooltip(),
            rx.recharts.bar(
                data_key="visitors",
                fill="fill",
                radius=6,
            ),
            rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
            rx.recharts.y_axis(
                data_key="browser",
                type_="category",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=data,
            layout="vertical",
            width="100%",
            height=250,
        ),
        info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
        margin_right="20px",
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Custom Tabs
Customize and format your x and y axes for improved presentation.

```python
def barchart_v8():
    categories = ["Successful", "Refunded"]
    EUROPE = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [12, 24, 48, 24, 34, 26, 12, 38, 23, 20, 24, 21],
            [0, 1, 4, 2, 0, 0, 0, 2, 1, 0, 0, 8],
        )
    ]

    ASIA = [
        {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
        for month, successful, refunded in zip(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            [31, 32, 44, 23, 35, 48, 33, 38, 41, 39, 32, 19],
            [1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 5],
        )
    ]

    def create_chart(data: list[dict[str, str | int]]):
        return rx.recharts.bar_chart(
            get_cartesian_grid(),
            rx.foreach(
                categories,
                lambda key, index: rx.recharts.bar(
                    data_key=key,
                    fill=f"var(--chart-{index + 1})",
                    stack_id="_",
                ),
            ),
            rx.recharts.x_axis(
                interval=10,
                data_key="date",
                tick_size=10,
                class_name="text-xs font-semibold",
                axis_line=False,
                tick_line=False,
            ),
            get_tooltip(),
            data=data,
            width="100%",
            height=250,
            bar_size=25,
        )

    return rx.box(
        rx.text("Online Transactions", class_name="text-md font-semibold pb-3"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.text("Europe", class_name="text-sm font-semibold"),
                    flex="1",
                    value="1",
                ),
                rx.tabs.trigger(
                    rx.text("Asia", class_name="text-sm font-semibold"),
                    flex="1",
                    value="2",
                ),
            ),
            rx.tabs.content(create_chart(EUROPE), value="1", margin_top="-5px"),
            rx.tabs.content(create_chart(ASIA), value="2", margin_top="-5px"),
            default_value="1",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Custom Legends
Show how the chart adapts across different screen sizes and layouts.

```python
def barchart_v9():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
    ]

    return rx.box(
        rx.hstack(
            rx.foreach(
                [
                    ["Desktop", "var(--chart-1)"],
                    ["Mobile", "var(--chart-2)"],
                    ["Tablet", "var(--chart-3)"],
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
        rx.recharts.bar_chart(
            get_tooltip(),
            rx.recharts.bar(data_key="desktop", fill="var(--chart-1)", radius=4),
            rx.recharts.bar(data_key="mobile", fill="var(--chart-2)", radius=4),
            rx.recharts.bar(data_key="tablet", fill="var(--chart-3)", radius=4),
            get_x_axis("month"),
            data=data,
            width="100%",
            height=250,
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```


## Alternating Colors
Apply gradient fills to your bars for a modern, polished look.

```python
def barchart_v10():
    sport = [
        {"date": "Jan 23", "Running": 167, "Cycling": 145},
        {"date": "Feb 23", "Running": 125, "Cycling": 110},
        {"date": "Mar 23", "Running": 156, "Cycling": 149},
        {"date": "Apr 23", "Running": 165, "Cycling": 112},
        {"date": "May 23", "Running": 153, "Cycling": 138},
        {"date": "Jun 23", "Running": 124, "Cycling": 145},
        {"date": "Jul 23", "Running": 164, "Cycling": 134},
    ]

    activities = ["Running", "Cycling"]
    chart_colors = ["var(--chart-1)", "var(--chart-2)"]

    def create_alternating_chart(active_key: str):
        return rx.recharts.bar_chart(
            get_tooltip(),
            *[
                rx.recharts.bar(
                    is_animation_active=False,
                    radius=4,
                    data_key=key,
                    fill=color,
                    custom_attrs={
                        "opacity": rx.cond(
                            key == active_key,
                            "0.25",
                            "1",
                        )
                    },
                )
                for key, color in zip(activities, chart_colors)
            ],
            get_x_axis("date"),
            data=sport,
            width="100%",
            height=250,
            bar_category_gap="20%",
        )

    return rx.box(
        rx.tabs.root(
            rx.tabs.list(
                *[
                    rx.tabs.trigger(
                        rx.text(activity, class_name="text-sm font-semibold"),
                        value=str(i + 1),
                    )
                    for i, activity in enumerate(activities)
                ]
            ),
            *[
                rx.tabs.content(
                    create_alternating_chart(active),
                    value=str(i + 1),
                    margin_top="-5px",
                )
                for i, active in enumerate(activities)
            ],
            default_value="1",
            width="100%",
        ),
        class_name="w-full flex flex-col gap-y-4 p-1 [&_.recharts-tooltip-item-separator]:w-full",
    )
```

