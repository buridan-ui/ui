import reflex as rx
from ...base_ui.components.base.dialog import dialog
from ...base_ui.components.base.button import button
from ...base_ui.components.base.input import input


def dialog_hh():
    return dialog(
        trigger=button("Open Dialog", variant="outline"),
        title="Are you absolutely sure?",
        description="This action cannot be undone. This will permanently delete your account and remove your data from our servers.",
        content=rx.flex(
            button("Cancel", variant="outline", class_name="flex-1"),
            button("Continue", class_name="flex-1"),
            class_name="flex gap-2 w-full",
        ),
    )


def dialog_ll():
    return dialog.root(
        # Trigger button
        dialog.trigger(
            render_=button("Open Dialog"),
        ),
        # Portal with backdrop and popup
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                # Header section
                rx.box(
                    rx.flex(
                        dialog.title("Edit Profile"),
                        dialog.close(
                            render_=button(
                                rx.icon("x", class_name="size-4"),
                                variant="ghost",
                                size="icon-sm",
                                class_name="text-secondary-11",
                            ),
                        ),
                        class_name="flex justify-between items-baseline gap-1",
                    ),
                    dialog.description(
                        "Make changes to your profile here. Click save when you're done."
                    ),
                    class_name="flex flex-col gap-2",
                ),
                # Content section
                rx.box(
                    rx.box(
                        rx.text("Name", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your name"),
                    ),
                    rx.box(
                        rx.text("Email", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your email", type="email"),
                    ),
                    rx.flex(
                        dialog.close(
                            render_=button(
                                "Cancel", variant="outline", class_name="flex-1"
                            ),
                        ),
                        button("Save Changes", class_name="flex-1"),
                        class_name="flex gap-2 w-full",
                    ),
                    class_name="flex flex-col gap-4",
                ),
            ),
        ),
    )
