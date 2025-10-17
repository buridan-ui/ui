import reflex as rx


def site_title():
    return rx.el.div(
        rx.el.p(
            "buridan",
            font_weight="700",
            font_size="1.25rem",
            letter_spacing="-0.04em",
        ),
        rx.el.p(
            ".UI",
            font_size="0.6rem",
            position="relative",
            font_weight="600",
        ),
        class_name="flex flex-row items-baseline gap-x-[1px] cursor-pointer",
    )
