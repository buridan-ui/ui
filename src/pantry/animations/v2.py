import reflex as rx


def animation_v2() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "buridan/ui",
            size="5",
            font_weight="900",
            style={
                "position": "relative",
                "animation": "rightSlide 2s infinite",
                "@keyframes rightSlide": {
                    "from": {"right": "-30px", "opacity": "0"},
                    "to": {"right": "0px", "opacity": "1"},
                },
            },
        ),
        width="100%",
        height="20em",
        align="center",
        justify="center",
    )
