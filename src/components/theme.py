import reflex as rx


def theme_button():
    return rx.el.button(
        rx.color_mode.icon(
            light_component=rx.el.div(
                rx.icon("moon", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
            dark_component=rx.el.div(
                rx.icon("sun", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
        ),
        class_name="rounded-md flex items-center gap-x-2 text-sm font-semibold cursor-pointer",
        border=f"1px solid {rx.color('gray', 3)}",
        _hover={"background": rx.color("gray", 3)},
        style={
            "display": "inline-flex",
            "height": "1.925rem",
            "padding": "0.25rem 0.50rem",
        },
        on_click=rx.toggle_color_mode,
    )
