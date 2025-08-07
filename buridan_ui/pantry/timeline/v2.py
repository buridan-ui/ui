import reflex as rx


def timeline_v2():
    return rx.ordered_list(
        rx.text(
            rx.box(
                rx.box(bg=rx.color("blue"), class_name="size-3 shrink-0 rounded-full"),
                rx.box(
                    rx.el.time(
                        rx.text("12/02/2025"),
                        class_name="text-xs/none font-medium text-slate-11",
                    ),
                    rx.text("Kickoff", class_name="text-lg font-bold text-slate-12"),
                    rx.text(
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga officiis tempora ipsumadipisci tenetur sunt quae exercitationem sed pariatur porro!",
                        class_name="mt-0.5 text-sm text-slate-10",
                    ),
                    class_name="-mt-2",
                ),
                class_name="relative flex items-start gap-4 group-odd:flex-row-reverse group-odd:text-right group-even:order-last",
            ),
            rx.box(aria_hidden=True),
            class_name="group relative grid grid-cols-2 odd:-me-3 even:-ms-3",
        ),
        rx.text(
            rx.box(
                rx.box(bg=rx.color("blue"), class_name="size-3 shrink-0 rounded-full"),
                rx.box(
                    rx.el.time(
                        rx.text("5/03/2025"),
                        class_name="text-xs/none font-medium text-slate-11",
                    ),
                    rx.text(
                        "First Milestone", class_name="text-lg font-bold text-slate-12"
                    ),
                    rx.text(
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga officiis tempora ipsum adipisci tenetur sunt quae exercitationem sed pariatur porro!",
                        class_name="mt-0.5 text-sm text-slate-10",
                    ),
                    class_name="-mt-2",
                ),
                class_name="relative flex items-start gap-4 group-odd:flex-row-reverse group-odd:text-right group-even:order-last",
            ),
            rx.box(aria_hidden=True),
            class_name="group relative grid grid-cols-2 odd:-me-3 even:-ms-3",
        ),
        rx.text(
            rx.box(
                rx.box(bg=rx.color("blue"), class_name="size-3 shrink-0 rounded-full"),
                rx.box(
                    rx.el.time(
                        rx.text("24/04/2025"),
                        class_name="text-xs/none font-medium text-slate-11",
                    ),
                    rx.text("Launch", class_name="text-lg font-bold text-slate-12"),
                    rx.text(
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga officiis tempora ipsum adipisci tenetur sunt quae exercitationem sed pariatur porro!",
                        class_name="mt-0.5 text-sm text-slate-10",
                    ),
                    class_name="-mt-2",
                ),
                class_name="relative flex items-start gap-4 group-odd:flex-row-reverse group-odd:text-right group-even:order-last",
            ),
            rx.box(aria_hidden=True),
            class_name="group relative grid grid-cols-2 odd:-me-3 even:-ms-3",
        ),
        class_name="relative space-y-8 before:absolute before:top-0 before:left-1/2 before:h-full before:w-[1px] before:-translate-x-1/2 before:rounded-full before:bg-neutral-500/40",
    )
