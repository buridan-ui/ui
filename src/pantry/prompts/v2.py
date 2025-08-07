import reflex as rx


def prompt_v2():
    return rx.center(
        rx.vstack(
            rx.text_area(
                placeholder="Ask me anything...",
                width="100%",
                height="100%",
                rows="4",
                padding_bottom="35px",
            ),
            rx.hstack(
                rx.button(
                    "Send",
                    height="20px",
                    padding="5px",
                    variant="surface",
                ),
                width="100%",
                align="center",
                justify="end",
                position="absolute",
                bottom="0",
                left="0",
                padding="10px 12px",
            ),
            position="relative",
            width="100%",
            max_width="40em",
            border=f"1px solid {rx.color('gray', 6)}",
            border_radius="8px",
        ),
        width="100%",
        height="25vh",
    )
