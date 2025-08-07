import reflex as rx


stats = [
    {"id": 1, "name": "Transactions every 24 hours", "value": "44 million"},
    {"id": 2, "name": "Assets under holding", "value": "$119 trillion"},
    {"id": 3, "name": "New users annually", "value": "46,000"},
]


def stat_v1():
    return rx.box(
        rx.box(
            rx.foreach(
                stats,
                lambda stat: rx.box(
                    rx.text(stat["name"], class_name="text-gray-500 font-light"),
                    rx.text(
                        stat["value"],
                        class_name="order-first text-2xl font-semibold tracking-tight sm:text-3xl",
                    ),
                    class_name="mx-auto flex max-w-xs flex-col gap-y-4",
                ),
            ),
            class_name="grid grid-cols-1 gap-x-8 gap-y-16 text-center lg:grid-cols-3",
        ),
        class_name="mx-auto max-w-7xl px-6 lg:px-8",
    )
