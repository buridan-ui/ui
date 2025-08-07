import reflex as rx


class Table(rx.State):
    data: list[dict[str, str]] = [
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
            "name": "Robert Wolfkisser",
            "job": "Engineer",
            "email": "rob_wolf@gmail.com",
            "phone": "+44 (452) 886 09 12",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-7.png",
            "name": "Jill Jailbreaker",
            "job": "Engineer",
            "email": "jj@breaker.com",
            "phone": "+44 (934) 777 12 76",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
            "name": "Henry Silkeater",
            "job": "Designer",
            "email": "henry@silkeater.io",
            "phone": "+44 (901) 384 88 34",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
            "name": "Bill Horsefighter",
            "job": "Designer",
            "email": "bhorsefighter@gmail.com",
            "phone": "+44 (667) 341 45 22",
        },
        {
            "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-10.png",
            "name": "Jeremy Footviewer",
            "job": "Manager",
            "email": "jeremy@foot.dev",
            "phone": "+44 (881) 245 65 65",
        },
    ]

    color_map: dict[str, str] = {
        "Engineer": "blue",
        "Manager": "cyan",
        "Designer": "pink",
    }


def create_data_row(data: dict[str, str]):
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.avatar(src=data["avatar"], size="1"),
                rx.text(
                    data["name"],
                    color_scheme="gray",
                    font_size="11px",
                    weight="medium",
                ),
                align="center",
            ),
        ),
        rx.table.cell(
            rx.badge(data["job"], color_scheme=Table.color_map[data["job"]], size="1"),
        ),
        rx.table.cell(
            rx.text(
                data["email"],
                color_scheme="blue",
                font_size="11px",
                _hover={"text_decoration_line": "underline"},
                cursor="pointer",
            ),
        ),
        rx.table.cell(
            rx.text(
                data["phone"],
                color_scheme="gray",
                font_size="11px",
                weight="regular",
            ),
        ),
        rx.table.cell(rx.icon(tag="pencil", size=13, color="gray")),
        rx.table.cell(rx.icon(tag="trash-2", size=13)),
        align="center",
        white_space="nowrap",
    )


def tables_v2():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    ["Employee", "Job Title", "Email", "Phone", "", ""],
                    lambda title: rx.table.column_header_cell(
                        rx.text(title, font_size="12px", weight="bold"),
                    ),
                ),
            ),
        ),
        rx.table.body(
            rx.foreach(Table.data, create_data_row),
        ),
        width="100%",
        variant="surface",
        max_width="800px",
        size="2",
    )


def _tables_v2():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    ["Employee", "Job Title", "Email", "Phone", "", ""],
                    lambda title: rx.table.column_header_cell(
                        rx.text(title, font_size="12px", weight="bold"),
                    ),
                ),
            ),
        ),
        rx.table.body(
            rx.foreach(Table.data, create_data_row),
        ),
        width="100%",
        variant="surface",
        size="2",
    )
