import reflex as rx

stats = [
    {"id": 1, "name": "Creators on the platform", "value": "8,000+"},
    {"id": 2, "name": "Flat platform fee", "value": "3%"},
    {"id": 3, "name": "Uptime guarantee", "value": "99.9%"},
    {"id": 4, "name": "Paid out to creators", "value": "$70M"},
]


border_classes = rx.Var.create(
    [
        (
            "rounded-t-lg "
            "md:rounded-tl-lg md:rounded-tr-none md:rounded-bl-none md:rounded-br-none "
        ),
        (
            "rounded-none "
            "md:rounded-tr-lg md:rounded-tl-none md:rounded-bl-none md:rounded-br-none "
        ),
        (
            "rounded-none "
            "md:rounded-bl-lg md:rounded-tl-none md:rounded-tr-none md:rounded-br-none "
        ),
        (
            "rounded-b-lg "
            "md:rounded-br-lg md:rounded-tl-none md:rounded-tr-none md:rounded-bl-none "
        ),
    ]
)


def stat_v2():
    return rx.box(
        rx.box(
            rx.foreach(
                stats,
                lambda stat, idx: rx.box(
                    rx.text(stat["name"], class_name="text-gray-500 font-light"),
                    rx.text(
                        stat["value"],
                        class_name="order-first text-2xl font-semibold tracking-tight sm:text-3xl",
                    ),
                    class_name=(
                        "flex flex-col justify-between h-full w-full p-6 border border-dashed border-slate-500/60 overflow-hidden "
                        f"{border_classes[idx]}"
                    ),
                ),
            ),
            class_name=(
                "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 "
                "auto-rows-fr gap-2 text-center"
            ),
        ),
        class_name="mx-auto max-w-7xl px-6 lg:px-8",
    )
