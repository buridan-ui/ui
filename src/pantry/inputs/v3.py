import reflex as rx


def input_v3():
    return rx.box(
        rx.text("Email", class_name="text-xs font-semibold"),
        rx.box(
            rx.icon(
                tag="mail",
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 size-5 "
                + rx.color_mode_cond(
                    "!text-gray-400",
                    "!text-gray-600",
                ).to(str),
            ),
            rx.el.input(
                placeholder="something@email.com",
                class_name=(
                    "pl-9 py-2 w-full "
                    + "text-sm "
                    + "rounded-md bg-transparent border border-gray-500/40 "
                    + "focus:outline-none focus:border-blue-500"
                ),
            ),
            class_name="relative focus:outline-none",
        ),
        class_name="w-full max-w-[20em] flex flex-col gap-y-2",
    )
