import calendar
from datetime import datetime

import reflex as rx

current_year = datetime.now().year


def create_menu(default: str, items: list[str]):
    return rx.box(rx.select(items, placeholder=default, width="100%"), flex_grow="1")


def payments_v1():
    return rx.vstack(
        rx.vstack(
            rx.heading("Payment Method", size="5", weight="bold"),
            rx.text(
                "Add a new payment method to your account.",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
            ),
            width="100%",
            spacing="1",
            align="center",
            padding="12px 0px",
        ),
        rx.hstack(
            *[
                rx.button(
                    rx.text(name, font_size="11px", weight="medium"),
                    height="68px",
                    flex="1",
                    variant="surface",
                    cursor="pointer",
                    color_scheme="gray",
                )
                for name in ["Card", "Paypal", "Apple"]
            ],
            width="100%",
            justify="between",
        ),
        rx.vstack(
            rx.input(width="100%", placeholder="Your name..."),
            rx.input(width="100%", placeholder="Card number..."),
            rx.input(placeholder="CVV", width="100%"),
            rx.hstack(
                *[
                    create_menu(name, items)
                    for name, items in [
                        ["Month", list(calendar.month_name)[1:]],
                        [
                            "Year",
                            [
                                str(year)
                                for year in range(current_year, current_year + 10)
                            ],
                        ],
                    ]
                ],
                width="100%",
                display="flex",
            ),
            spacing="4",
            padding="12px 0px",
            width="100%",
        ),
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
        padding="24px 0px",
    )
