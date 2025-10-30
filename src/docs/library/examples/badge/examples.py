import reflex as rx

from ...base_ui.components.base.badge import badge


def badge_demo():
    return rx.box(
        rx.box(
            badge("Badge"),
            badge("Secondary", variant="secondary"),
            badge("Destructive", variant="destructive"),
            badge("Outline", variant="outline"),
            class_name="flex w-full flex-wrap gap-2",
        ),
        rx.box(
            badge(
                rx.icon(tag="badge-check"),
                "Verified",
                variant="secondary",
                class_name="bg-blue-500 text-white dark:bg-blue-600",
            ),
            badge(
                "8",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "99",
                variant="destructive",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "20+",
                variant="outline",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            class_name="flex w-full flex-wrap gap-2",
        ),
        class_name="flex flex-col items-center gap-2 p-8",
    )


def badge_with_icons():
    return rx.box(
        badge(
            rx.icon(tag="check"),
            "Success",
            variant="secondary",
            class_name="bg-green-500 text-white dark:bg-green-600",
        ),
        badge(
            rx.icon(tag="x"),
            "Error",
            variant="destructive",
        ),
        badge(
            rx.icon(tag="triangle-alert"),
            "Warning",
            variant="secondary",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        badge(
            rx.icon(tag="info"),
            "Info",
            variant="secondary",
            class_name="bg-blue-500 text-white dark:bg-blue-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )


def badge_status_examples():
    return rx.box(
        badge("New", variant="default"),
        badge("Popular", variant="secondary"),
        badge("Sale", variant="destructive"),
        badge("Draft", variant="outline"),
        badge(
            rx.icon(tag="star"),
            "Featured",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )


def badge_notification_count():
    return rx.box(
        badge(
            "1",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "5",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "10",
            variant="secondary",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "99+",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        class_name="flex items-center gap-2 p-8",
    )
