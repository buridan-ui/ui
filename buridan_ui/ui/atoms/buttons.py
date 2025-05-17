import reflex as rx


def button_with_icon(icon: str, **kwargs):
    return rx.box(
        rx.icon(
            tag=icon,
            size=13,
            color=rx.color("slate", 11),
            _hover={"color": rx.color("slate", 12)},
        ),
        _hover={"background": rx.color("gray", 3)},
        border=f"1px solid {rx.color('gray', 5)}",
        class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
        **kwargs,
    )


def button_with_link(icon: str, url: str):
    return rx.box(
        rx.link(
            rx.icon(
                tag=icon,
                size=13,
            ),
            href=url,
            is_external=True,
            text_cdecoration="none",
            color=rx.color("slate", 11),
            _hover={"color": rx.color("slate", 12)},
        ),
        _hover={"background": rx.color("gray", 3)},
        border=f"1px solid {rx.color('gray', 5)}",
        class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
    )


def theme_button():
    return rx.el.button(
        rx.color_mode.icon(
            light_component=rx.el.div(
                rx.icon(
                    "moon",
                    size=13,
                    color=rx.color("slate", 11),
                ),
                rx.el.p("Light", class_name="text-sm"),
                class_name="flex flex-row items-center gap-x-2",
            ),
            dark_component=rx.icon(
                "sun",
                size=14,
                color=rx.color("slate", 11),
            ),
        ),
        on_click=rx.toggle_color_mode,
        _hover={"background": rx.color("gray", 3)},
        border=f"1px solid {rx.color('gray', 5)}",
        class_name="cursor-pointer rounded-lg py-1 px-2 flex items-center justify-center",
    )
