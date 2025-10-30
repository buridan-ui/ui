import reflex as rx
from ...base_ui.components.base.button import button
from ...base_ui.components.base.menu import menu


def dropdown_menu_demo():
    return rx.el.div(
        menu.root(
            menu.trigger(
                button("Click Me!", variant="outline"),
            ),
            menu.portal(
                menu.positioner(
                    menu.popup(
                        menu.group(
                            menu.group_label("My Account"),
                            menu.item(
                                "Profile",
                                rx.text(
                                    "⇧⌘P",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                            ),
                            menu.item(
                                "Billing",
                                rx.text(
                                    "⌘B",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                            ),
                            menu.item(
                                "Settings",
                                rx.text(
                                    "⌘S",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                            ),
                            menu.item(
                                "Keyboard shortcuts",
                                rx.text(
                                    "⌘K",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                            ),
                        ),
                        menu.separator(),
                        menu.item("Team"),
                        menu.submenu_root(
                            menu.submenu_trigger(
                                "Invite users",
                                rx.icon("chevron-right", class_name="ml-auto size-4"),
                            ),
                            menu.portal(
                                menu.positioner(
                                    menu.popup(
                                        menu.item("Email"),
                                        menu.item("Message"),
                                        menu.separator(),
                                        menu.item("More..."),
                                        class_name="w-44",
                                    ),
                                ),
                            ),
                        ),
                        menu.item(
                            "New Team",
                            rx.text(
                                "⌘+T",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                        ),
                        menu.separator(),
                        menu.item("GitHub"),
                        menu.item("Support"),
                        menu.item("API", disabled=True),
                        menu.separator(),
                        menu.item(
                            "Log out",
                            rx.text(
                                "⇧⌘Q",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                        ),
                        class_name="w-56",
                    ),
                ),
            ),
        ),
        class_name="p-8",
    )
