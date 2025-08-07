import reflex as rx


def popups_v2():
    return rx.center(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "Open Dialog",
                    variant="surface",
                    color_scheme="gray",
                    cursor="pointer",
                ),
            ),
            rx.dialog.content(
                rx.hstack(
                    rx.text(
                        "Need more help?",
                        size="4",
                        weight="bold",
                        color=rx.color("slate", 11),
                    ),
                    justify="center",
                    padding="15px 0px 5px 0px",
                ),
                rx.vstack(
                    rx.vstack(
                        rx.button(
                            "Message Us",
                            radius="full",
                            padding="20px",
                            width="100%",
                            variant="surface",
                            cursor="pointer",
                        ),
                        rx.button(
                            "Live Chat",
                            radius="full",
                            padding="20px",
                            width="100%",
                            variant="surface",
                            color_scheme="gray",
                            cursor="pointer",
                        ),
                        rx.text(
                            "● Chat Online",
                            color_scheme="grass",
                            size="1",
                            weight="medium",
                            align="center",
                        ),
                        width="100%",
                        padding="10px 10px",
                        align="center",
                    ),
                    rx.divider(),
                    rx.hstack(
                        *[
                            rx.center(
                                rx.icon(tag=tag, size=15),
                                width="35px",
                                height="35px",
                                border_radius="35px",
                                border="1px solid gray",
                            )
                            for tag in ["github", "twitter", "facebook"]
                        ],
                        align="center",
                        justify="center",
                        width="100%",
                        spacing="5",
                        padding="10px",
                    ),
                    align="center",
                    padding="5px 0px",
                ),
                width="320px",
                padding="0px",
            ),
        ),
        height="25vh",
    )
