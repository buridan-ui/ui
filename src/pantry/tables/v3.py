import reflex as rx


class Table(rx.State):
    data: list[dict[str, str]] = [
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
            "name": "Robert Wolfkisser",
            "job": "Engineer",
            "email": "rob_wolf@gmail.com",
            "rate": "22",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-5.png",
            "name": "Jill Jailbreaker",
            "job": "Engineer",
            "email": "jj@breaker.com",
            "rate": "45",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
            "name": "Henry Silkeater",
            "job": "Designer",
            "email": "henry@silkeater.io",
            "rate": "76",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
            "name": "Bill Horsefighter",
            "job": "Designer",
            "email": "bhorsefighter@gmail.com",
            "rate": "15",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
            "name": "Jeremy Footviewer",
            "job": "Manager",
            "email": "jeremy@foot.dev",
            "rate": "98",
        },
    ]


def create_sidebar_menu_item(name: str, tag: str, color: str):
    return rx.hstack(
        rx.icon(tag=tag, size=14),
        rx.text(name, font_size="11px", color_scheme="gray"),
        color=color,
        width="100%",
        justify="start",
        align="center",
    )


def sidebar_item_option_menu():
    return rx.menu.root(
        rx.menu.trigger(
            rx.icon(tag="ellipsis", size=14, cursor="pointer"),
        ),
        rx.menu.content(
            rx.menu.item(
                create_sidebar_menu_item(
                    "Send message",
                    "mails",
                    "inherit",
                ),
            ),
            rx.menu.item(
                create_sidebar_menu_item(
                    "Add note",
                    "notepad-text",
                    "inherit",
                ),
            ),
            rx.menu.item(
                create_sidebar_menu_item(
                    "Terminate Contract",
                    "trash-2",
                    "red",
                ),
            ),
            size="1",
        ),
    )


def create_data_row(data: dict[str, str]):
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.avatar(src=data["avatar"], size="2", radius="full"),
                rx.vstack(
                    rx.text(
                        data["name"],
                        font_size="12px",
                        weight="medium",
                    ),
                    rx.text(
                        data["job"],
                        color_scheme="gray",
                        font_size="10px",
                        weight="medium",
                    ),
                    spacing="0",
                ),
                align="center",
            ),
        ),
        rx.table.cell(
            rx.vstack(
                rx.text(data["email"], font_size="12px"),
                rx.text("Email", color_scheme="gray", font_size="10px"),
                spacing="0",
            ),
        ),
        rx.table.cell(
            rx.vstack(
                rx.text(f"${data['rate']}.0/h", font_size="12px"),
                rx.text("Rate", font_size="10px", color_scheme="gray"),
                spacing="0",
            ),
        ),
        rx.table.cell(
            rx.hstack(
                rx.button(
                    rx.icon(tag="pencil", size=13, color="gray"),
                    variant="ghost",
                    cursor="pointer",
                ),
                sidebar_item_option_menu(),
            ),
        ),
        width="100%",
        align="center",
        white_space="nowrap",
    )


def tables_v3():
    return rx.table.root(
        rx.table.body(
            rx.foreach(Table.data, create_data_row),
        ),
        width="100%",
        variant="surface",
        max_width="800px",
        size="2",
    )
