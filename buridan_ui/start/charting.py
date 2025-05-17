import reflex as rx
from buridan_ui.wrappers.base.main import base


def label(text, add_ons: str = ""):
    return rx.el.label(
        text,
        class_name=f"text-[13px] font-regular {add_ons}",
        color=rx.color("slate", 11),
    )


def create_code_line(code_string: str):
    return rx.hstack(
        rx.code_block(
            code_string,
            width="100%",
            font_size="12px",
            language="bash",
            wrap_long_lines=True,
            scrollbar_width="none",
            code_tag_props={"pre": "transparent", "bg": "transparent"},
            custom_attrs={"bg": "transparent"},
            bg="transparent",
            class_name="rounded-md shadow-sm",
            border=f"0.81px solid {rx.color('gray', 4)}",
            show_line_numbers=True,
        ),
        rx.el.button(
            rx.icon(tag="copy", size=13),
            cursor="pointer",
            position="absolute",
            right="15px",
            top="15px",
            on_click=[
                rx.toast("Command copied"),
                rx.set_clipboard(code_string),
            ],
        ),
        width="100%",
        align="center",
        position="relative",
    )


def text_wrapper(title: str, description: str):
    return rx.el.div(
        rx.el.label(title, class_name="text-md font-bold"),
        rx.el.label(
            description,
            class_name="text-[13px] font-regular",
            color=rx.color("slate", 11),
        ),
        class_name="flex flex-col gap-y-2",
    )


def text_wrapper_open(title: str, component):
    return rx.el.div(
        rx.el.label(title, class_name="text-md font-bold"),
        *component,
        class_name="flex flex-col gap-y-2",
    )


@base("/getting-started/charting", "Charting Walkthrough")
def charting():
    return [
        rx.box(
            rx.vstack(
                text_wrapper(
                    "1. Introduction",
                    "Reflex chart components compile to Recharts under the hood, making them highly customizable and easy to integrate with your data. By leveraging Reflex, you can effortlessly create interactive, dynamic charts with minimal configuration. Whether you're building line charts, bar charts, or complex data visualizations, Reflex streamlines the process while offering the flexibility of Recharts' robust features.",
                ),
                text_wrapper_open(
                    "2. Setting Up Your Environment",
                    [
                        rx.el.div(
                            label(
                                "If you haven't done so already, make sure you have the latest version of Reflex installed on your machine. Visit the "
                            ),
                            rx.link("installation", class_name="underline"),
                            label(
                                " guide to walk you through the installation process."
                            ),
                        ),
                    ],
                ),
                text_wrapper_open(
                    "3. Data & State Management",
                    [
                        rx.el.div(
                            label(
                                "Most charts in this guide use static data as an example. This approach helps keep the UI simple, clean, and the site fast. However, real-world applications will likely require the use of Reflex's "
                            ),
                            rx.el.b("state"),
                            label(
                                " to build full-stack data applications, or any application that involves dynamic data handling."
                            ),
                        ),
                        label(
                            "To get started, create a separate file and define your state like this:",
                            "pt-4",
                        ),
                        create_code_line(
                            """import reflex as rx

class State(rx.State):

    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]
                            """
                        ),
                    ],
                ),
                text_wrapper_open(
                    "4. Creating Your Chart",
                    [
                        rx.el.div(
                            label(" "),
                            label("The Buridan UI library includes "),
                            rx.el.b("7"),
                            label(" chart types: "),
                            rx.link(
                                "area",
                                class_name="underline font-bold",
                                href="/charts/area-charts",
                            ),
                            label(", "),
                            rx.link(
                                "bar",
                                class_name="underline font-bold",
                                href="/charts/bar-charts",
                            ),
                            label(", "),
                            rx.link(
                                "line",
                                class_name="underline font-bold",
                                href="/charts/line-charts",
                            ),
                            label(", "),
                            rx.link(
                                "pie",
                                class_name="underline font-bold",
                                href="/charts/pie-charts",
                            ),
                            label(", "),
                            rx.link(
                                "doughnut",
                                class_name="underline font-bold",
                                href="/charts/doughnut-charts",
                            ),
                            label(", "),
                            rx.link(
                                "radar",
                                class_name="underline font-bold",
                                href="/charts/radar-charts",
                            ),
                            label(", and "),
                            rx.link(
                                "scatter",
                                class_name="underline font-bold",
                                href="/charts/scatter-charts",
                            ),
                            label(
                                " charts. For this walkthrough, we’ll focus on area charts."
                            ),
                        ),
                        label(
                            "To set up the area chart, import your state class inside the file that will contain your area chart component, then create the following function:",
                            "pt-4",
                        ),
                        create_code_line(
                            """from .state import State
                            
def area_chart():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="desktop",
            fill=rx.color("accent"),
            stroke=rx.color("accent", 8),
        ),
        data=State.data,
        width="100%",
        height=250,
    )
                            """
                        ),
                        label(
                            "Two main props are necessary to get the chart to show: ",
                        ),
                        label(
                            "1. `data_key`: This defines which data field in your dataset will be used for the chart's Y-axis values. In this example, it's set to `desktop`.",
                        ),
                        label(
                            "2. `data`: This prop links the chart to the state data, allowing the chart to visualize the data array from your state class. Here, `State.data` is used to feed the chart with data.",
                        ),
                    ],
                ),
                text_wrapper_open(
                    "5. Customization: Cartesian Grid",
                    [
                        rx.el.div(
                            label(" "),
                            label(
                                "The Cartesian Grid component in Reflex allows you to customize the grid of your chart. By default, most charts come with a basic grid, but you can easily modify it to suit your design needs."
                            ),
                        ),
                        label(
                            "To add a customized Cartesian grid to your chart, use the following code snippet:",
                            "pt-4",
                        ),
                        create_code_line(
                            """rx.recharts.cartesian_grid(
    horizontal=True, 
    vertical=False, 
    class_name="opacity-25"
)"""
                        ),
                        label(
                            "In this example:",
                        ),
                        label(
                            "1. `horizontal=True`: Enables the horizontal grid lines, making it easier to follow the data along the Y-axis.",
                        ),
                        label(
                            "2. `vertical=False`: Disables the vertical grid lines, keeping the chart cleaner and focusing on the horizontal axis.",
                        ),
                        label(
                            "3. `class_name='opacity-25'`: Applies a low opacity to the grid lines, making them less intrusive and giving the chart a more subtle appearance.",
                        ),
                    ],
                ),
                text_wrapper_open(
                    "6. Customization: XAxis",
                    [
                        rx.el.div(
                            label(" "),
                            label(
                                "The XAxis component in Reflex allows you to customize the appearance and behavior of the horizontal axis in your chart. It controls things like axis labels, tick marks, and line visibility."
                            ),
                            label(
                                "The following also applies to the YAxis, however, in order to keep a consistent UI, the buridan charts typically lack the YAxis."
                            ),
                        ),
                        label(
                            "To customize the X Axis, you can use the following code snippet:",
                            "pt-4",
                        ),
                        create_code_line(
                            """rx.recharts.x_axis(
    data_key="month",
    axis_line=False,
    tick_size=10,
    tick_line=False,
    custom_attrs={"fontSize": "12px"},
    interval="preserveStartEnd",
)"""
                        ),
                        label(
                            "In this example:",
                        ),
                        label(
                            "1. `data_key='month'`: Sets the data field for the X-axis labels (in this case, the 'month' field).",
                        ),
                        label(
                            "2. `axis_line=False`: Hides the axis line, making the X-axis without a visible line.",
                        ),
                        label(
                            "3. `tick_size=10`: Sets the size of the tick marks on the X-axis.",
                        ),
                        label(
                            "4. `tick_line=False`: Disables the tick lines, so they won’t be drawn on the X-axis.",
                        ),
                        label(
                            "5. `custom_attrs={'fontSize': '12px'}`: Customizes the font size of the tick labels.",
                        ),
                        label(
                            "6. `interval='preserveStartEnd'`: Ensures that the first and last ticks are always visible, even if there’s overlap.",
                        ),
                    ],
                ),
                text_wrapper_open(
                    "7. Customization: ToolTip (Advanced)",
                    [
                        rx.el.div(
                            label(" "),
                            label(
                                "The ToolTip component in Reflex is highly customizable and allows you to create rich, interactive tooltips for your charts. It provides a variety of props for controlling animations, styling, and behavior of the tooltip content. Since it has many props, we’ll focus on how you can customize its styles using a dictionary instead of a data class for a more flexible approach."
                            ),
                        ),
                        label(
                            "To customize the tooltip with a dictionary, use the following code snippet:",
                            "pt-4",
                        ),
                        create_code_line(
                            """tooltip_styles = {
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
        "color": rx.color("slate", 9),
        "fontWeight": "500",
    },
    "content_style": {
        "background": rx.color("slate", 1),
        "borderColor": rx.color("slate", 5),
        "borderRadius": "5px",
        "fontFamily": "var(--font-instrument-sans)",
        "fontSize": "0.875rem",
        "lineHeight": "1.25rem",
        "fontWeight": "500",
        "letterSpacing": "-0.01rem",
        "minWidth": "8rem",
        "width": "175px",
        "padding": "0.375rem 0.625rem ",
        "position": "relative",
    },
    "general_style": "[&_.recharts-tooltip-item-separator]:w-full",
}"""
                        ),
                        label(
                            "In this example, we are using a dictionary to define various style properties for the tooltip, such as `item_style`, `label_style`, and `content_style`. These properties control the look and feel of the tooltip, from the color of the text to the layout of the content. The `general_style` prop is used to apply additional custom styles to specific parts of the tooltip.",
                        ),
                    ],
                ),
                text_wrapper_open(
                    "8. Final Thoughts",
                    [
                        label(
                            "In this walkthrough, we covered how to set up and customize your Reflex charts. We explored setting up state, creating a chart, customizing the Cartesian grid, X axis, and advanced tooltip features. With Reflex, you can build highly interactive and customizable charts that are easy to integrate into your applications."
                        ),
                    ],
                ),
                width="100%",
                spacing="6",
            ),
            width="100%",
            display="flex",
            justify_content="start",
            class_name="p-4",
        )
    ]
