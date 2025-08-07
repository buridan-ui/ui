import reflex as rx


def input_v2():
    return rx.box(
        rx.box(
            rx.text(
                "Email",
                class_name="text-xs font-semibold",
            ),
            rx.text("optional", class_name="text-xs font-light text-gray-400"),
            class_name="w-full flex flex-row justify-between items-center",
        ),
        rx.el.input(
            placeholder="something@email.com",
            class_name=(
                "p-2 w-full "
                + "text-sm "
                + "rounded-md bg-transparent border border-gray-500/40 "
                + "focus:outline-none focus:border-blue-500"
            ),
        ),
        class_name="w-full max-w-[20em] flex flex-col gap-y-2",
    )
