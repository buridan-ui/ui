import reflex as rx
from ...base_ui.components.base.kbd import kbd_group, kbd


def kbd_demo():
    """
    Example matching the shadcn KbdDemo component.
    Shows keyboard shortcuts with modifier keys.
    """
    return rx.box(
        # Mac modifier keys
        kbd_group(
            kbd("⌘"),
            kbd("⇧"),
            kbd("⌥"),
            kbd("⌃"),
        ),
        # Keyboard shortcut combination
        kbd_group(
            kbd("Ctrl"),
            rx.el.span("+"),
            kbd("B"),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )


# Additional examples


def kbd_shortcuts():
    """Common keyboard shortcuts"""
    return rx.box(
        rx.box(
            rx.text("Save:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Copy:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("C"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Paste:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("V"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Undo:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Z"),
            ),
            class_name="flex items-center",
        ),
        class_name="flex flex-col gap-3 p-8",
    )


def kbd_special_keys():
    """Special key examples"""
    return rx.box(
        kbd("Enter"),
        kbd("Esc"),
        kbd("Tab"),
        kbd("Space"),
        kbd("←"),
        kbd("→"),
        kbd("↑"),
        kbd("↓"),
        kbd("Delete"),
        kbd("Backspace"),
        class_name="flex flex-wrap gap-2 p-8",
    )


def kbd_complex_shortcuts():
    """Complex multi-key shortcuts"""
    return rx.box(
        # Three modifier keys
        rx.box(
            rx.text("Screenshot:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Shift"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Mac command
        rx.box(
            rx.text("Quit:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("⌘"),
                rx.el.span("+"),
                kbd("Q"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Function key
        rx.box(
            rx.text("Full Screen:", class_name="text-sm font-medium mr-2"),
            kbd("F11"),
            class_name="flex items-center",
        ),
        class_name="p-8",
    )


def kbd_with_icons():
    """Kbd with icons"""
    return rx.box(
        kbd_group(
            kbd(
                rx.icon(tag="command", size=12),
            ),
            rx.el.span("+"),
            kbd("K"),
        ),
        kbd_group(
            kbd(
                rx.icon(tag="arrow-left", size=12),
            ),
            kbd(
                rx.icon(tag="arrow-right", size=12),
            ),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )
