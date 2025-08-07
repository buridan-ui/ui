import reflex as rx

services = [
    ["Website Design", "Content Creation"],
    ["UX Design", "Consulting"],
    ["Research", "Other"],
]


def item_and_title(title: str, placeholder: str):
    return rx.vstack(
        rx.text(title, font_size="11px", weight="medium", color_scheme="gray"),
        rx.input(placeholder=placeholder, width="100%"),
        width="100%",
        spacing="2",
    )


def check_box_item(name: str):
    return rx.box(rx.checkbox(name), width="100%")


def forms_v1():
    return rx.vstack(
        rx.vstack(
            rx.heading("Contact our team", size="5", weight="bold"),
            rx.text(
                "Got any questions about the product? We're here to help. Fill out the form below to get started.",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
                text_align="center",
            ),
            width="100%",
            spacing="1",
            align="center",
            padding="12px 0px",
        ),
        rx.hstack(
            item_and_title("First Name", "First name"),
            item_and_title("Last Name", "Last name"),
            width="100%",
            display="flex",
        ),
        item_and_title("Email", "example@someplace.com"),
        rx.vstack(
            rx.text("Message", font_size="11px", color_scheme="gray", weight="medium"),
            rx.text_area(
                width="100%",
                placeholder="Leave us message...",
                rows="5",
            ),
            width="100%",
            spacing="2",
        ),
        rx.vstack(
            rx.text("Services", font_size="11px", color_scheme="gray", weight="medium"),
            *[
                rx.hstack(
                    check_box_item(x),
                    check_box_item(y),
                    width="100%",
                )
                for x, y in services
            ],
            width="100%",
            spacing="2",
        ),
        rx.spacer(),
        rx.button(
            "Continue",
            width="100%",
            cursor="pointer",
            variant="surface",
            color_scheme="gray",
        ),
        width="100%",
        max_width="21em",
        height="100%",
        justify="center",
        align="center",
    )
