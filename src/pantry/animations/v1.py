import reflex as rx


def animation_v1() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "buridan/ui",
            size="5",
            font_weight="900",
            style={
                "position": "relative",
                "@keyframes opacity": {
                    "0%": {"opacity": "0"},
                    "100%": {"opacity": "1"},
                },
                "animation": "opacity 2s infinite",
            },
        ),
        width="100%",
        height="20em",
        align="center",
        justify="center",
    )
