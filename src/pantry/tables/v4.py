import reflex as rx
from typing import Dict, List


class Tables(rx.State):
    data: List[Dict[str, str]] = [
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-9.png",
            "name": "Robert Wolfkisser",
            "job": "Engineer",
            "email": "rob_wolf@gmail.com",
            "role": "Collaborator",
            "lastActive": "2 days ago",
            "active": True,
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-6.png",
            "name": "Jill Jailbreaker",
            "job": "Engineer",
            "email": "jj@breaker.com",
            "role": "Collaborator",
            "lastActive": "6 days ago",
            "active": True,
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-10.png",
            "name": "Henry Silkeater",
            "job": "Designer",
            "email": "henry@silkeater.io",
            "role": "Contractor",
            "lastActive": "2 days ago",
            "active": False,
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
            "name": "Bill Horsefighter",
            "job": "Designer",
            "email": "bhorsefighter@gmail.com",
            "role": "Contractor",
            "lastActive": "5 days ago",
            "active": True,
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
            "name": "Jeremy Footviewer",
            "job": "Manager",
            "email": "jeremy@foot.dev",
            "role": "Manager",
            "lastActive": "3 days ago",
            "active": False,
        },
    ]


def tables_v4():
    def render_row(data: dict[str, str]):
        return rx.table.row(
            rx.table.cell(
                rx.hstack(
                    rx.avatar(src=data["avatar"], size="2", radius="full"),
                    rx.vstack(
                        rx.text(
                            data["name"],
                            size="1",
                            color=rx.color("slate", 12),
                            weight="bold",
                        ),
                        rx.text(data["email"], size="1", color=rx.color("slate", 10)),
                        spacing="0",
                    ),
                    align="center",
                )
            ),
            rx.table.cell(
                rx.text(data["role"], size="1", weight="medium"), width="320px"
            ),
            rx.table.cell(rx.text(data["lastActive"], size="1", weight="regular")),
            rx.table.cell(
                rx.badge(
                    rx.cond(data["active"], "ACTIVE", "DISABLED"),
                    color_scheme=rx.cond(data["active"], "blue", "gray"),
                    size="1",
                    width="100%",
                    display="flex",
                    justify_content="center",
                    padding="0.25em 0.15em",
                ),
            ),
            white_space="nowrap",
            align="center",
        )

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    ["Employee", "Role", "Last active", "Status"],
                    lambda title: rx.table.column_header_cell(
                        rx.text(
                            title, size="1", weight="bold", color=rx.color("slate", 11)
                        )
                    ),
                ),
                white_space="nowrap",
            ),
        ),
        rx.table.body(rx.foreach(Tables.data, render_row)),
        width="100%",
        variant="ghost",
        max_width="800px",
        size="2",
    )
