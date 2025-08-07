import reflex as rx


def pricing_v2():
    return rx.box(
        # Heading
        rx.box(
            rx.text(
                "Pricing",
                class_name="text-base/7 font-semibold",
                color=rx.color("slate", 12),
            ),
            rx.text(
                "Choose the right plan for you",
                class_name="mt-2 text-5xl font-semibold tracking-tight text-balance sm:text-6xl",
                color=rx.color("slate", 12),
            ),
            class_name="mx-auto max-w-4xl text-center",
        ),
        rx.text(
            "Choose an affordable plan that’s packed with the best features for engaging your audience, creating customer loyalty, and driving sales.",
            class_name="mx-auto mt-6 max-w-2xl text-center text-lg font-medium text-pretty sm:text-xl/8",
            color=rx.color("slate", 11),
        ),
        # Pricing Cards
        rx.box(
            # Hobby Tier
            rx.box(
                rx.text(
                    "Hobby",
                    id_="tier-hobby",
                    class_name="text-base/7 font-semibold",
                    color=rx.color("slate", 12),
                ),
                rx.box(
                    rx.text(
                        "$29",
                        class_name="text-5xl font-semibold tracking-tight",
                        color=rx.color("slate", 12),
                    ),
                    rx.text(
                        "/month",
                        class_name="text-base",
                        color=rx.color("slate", 10),
                    ),
                    class_name="mt-4 flex items-baseline gap-x-2",
                ),
                rx.text(
                    "The perfect plan if you're just getting started with our product.",
                    class_name="mt-6 text-base/7",
                    color=rx.color("slate", 11),
                ),
                rx.unordered_list(
                    *[
                        rx.text(
                            rx.el.svg(
                                rx.el.path(
                                    d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z",
                                    clip_rule="evenodd",
                                    fill_rule="evenodd",
                                ),
                                viewbox="0 0 20 20",
                                fill="currentColor",
                                class_name="h-6 w-5 flex-none",
                                color=rx.color("slate", 12),
                            ),
                            text,
                            class_name="flex gap-x-3",
                            color=rx.color("slate", 11),
                        )
                        for text in [
                            "25 products",
                            "Up to 10,000 subscribers",
                            "Advanced analytics",
                            "24-hour support response time",
                        ]
                    ],
                    role="list",
                    class_name="mt-8 space-y-3 text-sm/6 sm:mt-10",
                ),
                rx.el.button(
                    "Get started today",
                    class_name="mt-8 w-full rounded-md border py-3 px-4 sm:mt-10",
                    border_color=rx.color("slate", 6),
                    color=rx.color("slate", 12),
                    background="transparent",
                ),
                class_name="rounded-3xl p-8 ring-1 sm:mx-8 sm:p-10 lg:mx-0",
                border=f"1px solid {rx.color('slate', 6)}",
                background="transparent",
            ),
            # Enterprise Tier
            rx.box(
                rx.text(
                    "Enterprise",
                    id_="tier-enterprise",
                    class_name="text-base/7 font-semibold",
                    color=rx.color("slate", 12),
                ),
                rx.box(
                    rx.text(
                        "$99",
                        class_name="text-5xl font-semibold tracking-tight",
                        color=rx.color("slate", 12),
                    ),
                    rx.text(
                        "/month",
                        class_name="text-base",
                        color=rx.color("slate", 10),
                    ),
                    class_name="mt-4 flex items-baseline gap-x-2",
                ),
                rx.text(
                    "Dedicated support and infrastructure for your company.",
                    class_name="mt-6 text-base/7",
                    color=rx.color("slate", 11),
                ),
                rx.unordered_list(
                    *[
                        rx.text(
                            rx.el.svg(
                                rx.el.path(
                                    d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z",
                                    clip_rule="evenodd",
                                    fill_rule="evenodd",
                                ),
                                viewbox="0 0 20 20",
                                fill="currentColor",
                                class_name="h-6 w-5 flex-none",
                                color=rx.color("slate", 12),
                            ),
                            text,
                            class_name="flex gap-x-3",
                            color=rx.color("slate", 11),
                        )
                        for text in [
                            "Unlimited products",
                            "Unlimited subscribers",
                            "Advanced analytics",
                            "Dedicated support representative",
                            "Marketing automations",
                            "Custom integrations",
                        ]
                    ],
                    role="list",
                    class_name="mt-8 space-y-3 text-sm/6 sm:mt-10",
                ),
                rx.el.button(
                    "Get started today",
                    class_name="mt-8 w-full rounded-md border py-3 px-4 sm:mt-10",
                    border_color=rx.color("slate", 6),
                    color=rx.color("slate", 12),
                    background="transparent",
                ),
                class_name="rounded-3xl p-8 shadow-2xl ring-1 sm:p-10",
                border=f"1px solid {rx.color('slate', 6)}",
                background="transparent",
            ),
            class_name="mx-auto mt-16 grid max-w-lg grid-cols-1 items-center gap-y-6 sm:mt-20 lg:max-w-4xl lg:grid-cols-2",
        ),
        class_name="relative isolate px-6 py-24 sm:py-32 lg:px-8",
    )
