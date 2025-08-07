import reflex as rx

department = ["Team", "Billing", "Deployment", "Account", "Support"]
priority = ["1 - highest", "2", "3", "4 - lowest"]


def create_menu(default: str, items: list[str]):
    return rx.select(items, placeholder=default, width="48%")


def create_button(name: str, flex_width: str):
    return rx.button(
        name,
        variant="soft",
        flex=flex_width,
        cursor="pointer",
        color_scheme="gray",
    )


def forms_v2():
    return rx.vstack(
        rx.vstack(
            rx.heading("Report an issue", size="5", weight="bold"),
            rx.text(
                "What area are you having problems with?",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
            ),
            width="100%",
            spacing="1",
            align="center",
            padding="6px 0px",
        ),
        rx.vstack(
            rx.text("Tags", font_size="11px", color_scheme="gray", weight="bold"),
            rx.hstack(
                *[
                    create_menu(name, items)
                    for name, items in [
                        ["Department", department],
                        ["Priority", priority],
                    ]
                ],
                width="100%",
            ),
            width="100%",
            spacing="2",
        ),
        rx.vstack(
            rx.text("Subject", font_size="11px", color_scheme="gray", weight="bold"),
            rx.input(width="100%", placeholder="I need help with..."),
            width="100%",
            spacing="2",
        ),
        rx.vstack(
            rx.text(
                "Description",
                font_size="11px",
                color_scheme="gray",
                weight="bold",
            ),
            rx.text_area(
                width="100%",
                placeholder="Please include all information relevant to your issue.",
                rows="5",
            ),
            width="100%",
            spacing="2",
        ),
        rx.hstack(
            create_button("Cancel", "1"),
            create_button("Submit", "3"),
            width="100%",
            display="flex,",
            padding="12px 0px",
        ),
        width="100%",
        max_width="21em",
        height="100%",
        justify="center",
        align="center",
        padding="2.5em 0em",
    )
