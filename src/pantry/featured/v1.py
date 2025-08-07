import reflex as rx

data = [
    {
        "image": "auditors",
        "title": "Pharmacists",
        "description": "Azurill can be seen bouncing and playing on its big, rubbery tail",
    },
    {
        "image": "lawyers",
        "title": "Lawyers",
        "description": "Fans obsess over the particular length and angle of its arms",
    },
    {
        "image": "accountants",
        "title": "Bank owners",
        "description": "They divvy up their prey evenly among the members of their pack",
    },
    {
        "image": "others",
        "title": "Others",
        "description": "Phanpy uses its long nose to shower itself",
    },
]


def create_featured(title: str, description: str):
    return rx.hstack(
        rx.box(
            width="42px",
            height="42px",
            bg=rx.color("gray", 4),
            border_radius="10px",
        ),
        rx.vstack(
            rx.text(title, size="2", weight="bold"),
            rx.text(description, size="1", weight="medium", color_scheme="gray"),
            spacing="1",
            width=["90%" if i <= 1 else "60%" for i in range(6)],
        ),
        width="100%",
        padding="12px 0px",
    )


def featured_v1():
    return rx.vstack(
        rx.heading(
            "PharmLand is not just for Doctors",
            size="4",
            color=rx.color("slate", 12),
        ),
        rx.text(
            "Its lungs contain an organ that creates electricity. The crackling sound of electricity can be heard when it exhales. Azurill’s tail is large and bouncy. It is packed full of the nutrients this Pokémon needs to grow.",
            color=rx.color("slate", 11),
        ),
        rx.hstack(
            *[create_featured(item["title"], item["description"]) for item in data],
            width="100%",
            display="grid",
            grid_template_columns=[
                "repeat(1, 1fr)" if i <= 1 else "repeat(2, 1fr)" for i in range(6)
            ],
            justify_content="start",
            align_items="start",
            padding="24px 0px",
            spacing="0",
            wrap="wrap",
        ),
        width="100%",
        max_width="35em",
        display="flex",
        justify="center",
        align="start",
    )
