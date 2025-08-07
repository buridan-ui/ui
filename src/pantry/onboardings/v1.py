from __future__ import annotations

import reflex as rx

steps = [
    {
        "id": 1,
        "type": "done",
        "title": "Sign in with your account",
        "description": "To get started, log in with your organization account from your company.",
        "href": "#",
    },
    {
        "id": 2,
        "type": "in progress",
        "title": "Import data",
        "description": "Connect your database to the new workspace by using one of 20+ database connectors.",
        "href": "#",
    },
    {
        "id": 3,
        "type": "open",
        "title": "Create your first report",
        "description": "Generate your first report by using our pre-built templates or easy-to-use report builder.",
        "href": "#",
    },
]


def create_progress_item(data: dict[str, int | str]):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.checkbox(
                        default_checked=data["type"] == "done",
                        disabled=data["type"] != "done",
                    ),
                    rx.text(
                        data["title"],
                        size="3",
                        weight="bold",
                        color=rx.color("slate", 12),
                    ),
                    align="center",
                ),
                rx.hstack(
                    rx.text(data["description"], size="1", color=rx.color("slate", 11)),
                ),
                spacing="2",
            ),
            spacing="5",
        ),
        width="100%",
        align="start",
        justify="start",
        border_radius="8px",
        padding="12px",
        bg=rx.color("gray", 4) if data["type"] == "in progress" else "none",
    )


def onboardings_v1():
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "Hello, Danny",
                size="5",
                weight="bold",
                color=rx.color("slate", 12),
            ),
            rx.text(
                "Let's set up your first data workspace",
                color=rx.color("slate", 11),
                weight="medium",
                size="1",
            ),
            spacing="1",
            align="start",
            justify="start",
            width="100%",
        ),
        *[create_progress_item(data) for data in steps],
        width="100%",
        align="center",
        justify="center",
        max_width="25em",
        padding="12px",
    )
