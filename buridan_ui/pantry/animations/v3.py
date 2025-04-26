import reflex as rx


def animation_v3() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "buridan/ui",
            size="5",
            font_weight="900",
            style={
                "position": "relative",
                "animation": "shakeEffect 0.5s ease-in-out infinite",
                "@keyframes shakeEffect": {
                    "0%": {"transform": "translateX(0)"},
                    "25%": {"transform": "translateX(-10px)"},
                    "50%": {"transform": "translateX(10px)"},
                    "75%": {"transform": "translateX(-10px)"},
                    "100%": {"transform": "translateX(0)"},
                },
            },
        ),
        width="100%",
        height="20em",
        align="center",
        justify="center",
    )
