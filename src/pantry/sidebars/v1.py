import reflex as rx
from reflex import Color
from reflex.experimental import ClientStateVar

ACTIVE_ITEM = ClientStateVar.create("active_item", "")

SIDEBAR_CONTENT_ONE = [
    {"name": "Authentication"},
    {"name": "SMS Template"},
    {"name": "Email Templates"},
]

SIDEBAR_CONTENT_TWO = [
    {"name": "Sessions"},
    {"name": "JWT templates"},
    {"name": "Webhooks"},
    {"name": "Domains"},
    {"name": "Integrations"},
    {"name": "API Keys"},
]

SIDEBAR_CONTENT_THREE = [
    {"name": "Dashboard"},
    {"name": "Analytics"},
    {"name": "Users"},
    {"name": "Settings"},
    {"name": "Notifications"},
    {"name": "Logs"},
    {"name": "Roles & Permissions"},
    {"name": "Data Export"},
    {"name": "Security"},
    {"name": "Billing"},
    {"name": "Activity Feed"},
]


def create_divider():
    """Create a consistent divider."""
    return rx.divider(
        border_bottom=f"0.81px solid {rx.color('gray', 4)}", bg="transparent"
    )


def create_sidebar_menu_items(routes: list[dict[str, str | Color]]):
    """Create menu items from routes."""

    def item(data):
        item_name = data["name"]
        return rx.hstack(
            rx.link(
                rx.text(
                    item_name,
                    _hover={"color": rx.color("slate", 12)},
                    color=rx.cond(
                        ACTIVE_ITEM.value == item_name,
                        rx.color("slate", 12),
                        rx.color("slate", 11),
                    ),
                    size="2",
                    font_weight=rx.cond(
                        ACTIVE_ITEM.value == item_name, "semibold", "normal"
                    ),
                ),
                href=f"#{item_name}",
                text_decoration="none",
                on_click=ACTIVE_ITEM.set_value(item_name),
                width="100%",
                padding_left="10px",
            ),
            spacing="0",
            align_items="center",
            width="100%",
            border_left=rx.cond(
                ACTIVE_ITEM.value == item_name,
                f"1px solid {rx.color('blue', 10)}",
                f"0.81px solid {rx.color('gray', 4)}",
            ),
            height="25px",
        )

    return rx.vstack(rx.foreach(routes, item), spacing="0", width="100%")


def side_bar_wrapper(title: str, component: rx.Component):
    """Create a sidebar section."""

    return rx.vstack(
        rx.text(title, size="1", color=rx.color("slate", 12), weight="bold"),
        component,
        padding="1em",
    )


def sidebar_v1():
    content = rx.box(
        ACTIVE_ITEM,
        side_bar_wrapper("General", create_sidebar_menu_items(SIDEBAR_CONTENT_ONE)),
        create_divider(),
        side_bar_wrapper("Developers", create_sidebar_menu_items(SIDEBAR_CONTENT_TWO)),
        create_divider(),
        side_bar_wrapper("Personal", create_sidebar_menu_items(SIDEBAR_CONTENT_THREE)),
    )

    return rx.scroll_area(
        content,
        height="100vh",
        width="100%",
        max_width="240px",
    )
