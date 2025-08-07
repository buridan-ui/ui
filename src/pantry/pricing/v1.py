import reflex as rx

title = rx.heading("Freelancer", size="4")
subtitle = rx.text(
    "Perfect for independent designers for prototyping and demonstrations",
    font_size="14px",
    weight="medium",
    color=rx.color("slate", 11),
)

price = rx.heading("14", size="9", weight="medium", margin="0")
tag = rx.text("$", font_size="24px")
statement = rx.text(
    "Per month billed annually or $14 month to month",
    font_size="14px",
    weight="medium",
    color=rx.color("slate", 11),
)


def create_card_specs(description: str):
    return rx.hstack(
        rx.icon(tag="check", size=14),
        rx.text(
            description,
            font_size="14px",
            weight="medium",
            color=rx.color("slate", 12),
        ),
        spacing="3",
        align_items="center",
    )


def pricing_v1():
    return rx.vstack(
        rx.vstack(
            rx.vstack(title, subtitle, width="320px", height="125px", padding="30px"),
            rx.hstack(
                rx.hstack(
                    tag,
                    price,
                    justify_content="start",
                    align_items="start",
                    spacing="1",
                ),
                statement,
                width="320px",
                height="125px",
                background=rx.color("gray", 4),
                justify_content="space-between",
                align_items="center",
                padding="30px",
                spacing="8",
            ),
        ),
        rx.vstack(
            rx.vstack(
                create_card_specs("1 User"),
                create_card_specs("5 Projects"),
                create_card_specs("Download images and prototypes"),
                create_card_specs("Enhanced security and password protection"),
            ),
            rx.spacer(),
            rx.button(
                "GET STARTED",
                width="100%",
                height="55px",
                color_scheme="gray",
                variant="outline",
                cursor="pointer",
            ),
            height="250px",
            width="320px",
            padding="10px 30px 30px 30px",
        ),
        width="320px",
        background=rx.color("gray", 3),
        box_shadow="0px 6px 8px 0px hsla(0, 0%, 0%, 0.25)",
        border_top="10px solid hsla(200, 60%, 40%, 1)",
        font_family="Futura",
    )
