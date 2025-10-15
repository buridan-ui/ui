import reflex as rx
from ..button.button import button
from .menu import (
    dropdown_menu_root,
    dropdown_menu_trigger,
    dropdown_menu_content,
    dropdown_menu_label,
    dropdown_menu_item,
    dropdown_menu_shortcut,
    dropdown_menu_sub_trigger,
    dropdown_menu_separator,
    dropdown_menu_sub_content,
)


def dropdown_menu_demo():
    return rx.el.div(
        dropdown_menu_root(
            dropdown_menu_trigger(
                button("Click Me!", variant="outline"),
            ),
            dropdown_menu_content(
                dropdown_menu_label("My Account"),
                dropdown_menu_item(
                    "Profile",
                    dropdown_menu_shortcut("⇧⌘P"),
                ),
                dropdown_menu_item(
                    "Billing",
                    dropdown_menu_shortcut("⌘B"),
                ),
                dropdown_menu_item(
                    "Settings",
                    dropdown_menu_shortcut("⌘S"),
                ),
                dropdown_menu_item(
                    "Keyboard shortcuts",
                    dropdown_menu_shortcut("⌘K"),
                ),
                dropdown_menu_separator(),
                dropdown_menu_item("Team"),
                rx.menu.sub(
                    dropdown_menu_sub_trigger("Invite users"),
                    dropdown_menu_sub_content(
                        dropdown_menu_item("Email"),
                        dropdown_menu_item("Message"),
                        dropdown_menu_separator(),
                        dropdown_menu_item("More..."),
                    ),
                ),
                dropdown_menu_item(
                    "New Team",
                    dropdown_menu_shortcut("⌘+T"),
                ),
                dropdown_menu_separator(),
                dropdown_menu_item("GitHub"),
                dropdown_menu_item("Support"),
                dropdown_menu_item("API", disabled=True),
                dropdown_menu_separator(),
                dropdown_menu_item(
                    "Log out",
                    dropdown_menu_shortcut("⇧⌘Q"),
                ),
                class_name="w-56",
                size="1",
            ),
        ),
        class_name="p-8",
    )
