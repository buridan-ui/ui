import reflex as rx


def prompt_v1():
    return rx.center(
        rx.hstack(
            rx.input(
                placeholder="Say something here...",
                height="40px",
                width="100%",
                padding_left="10px",
                radius="none",
                variant="soft",
                outline="none",
                bg=rx.color("gray", 3),
            ),
            rx.button(
                "Enter",
                height="40px",
                radius="none",
                max_width="8em",
                width="100%",
                cursor="pointer",
            ),
            width="100%",
            max_width="25em",
            height="40px",
            border_radius="8px",
            overflow="hidden",
            spacing="0",
        ),
        width="100%",
        height="25vh",
    )
