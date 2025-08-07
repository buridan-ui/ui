import reflex as rx


def input_v1():
    return rx.box(
        rx.text("Email", class_name="text-xs font-semibold"),
        rx.el.input(
            placeholder="something@email.com",
            class_name=(
                "p-2 w-full "
                + "text-sm "
                + "rounded-md bg-transparent border border-gray-500/40 "
                + "focus:outline-none focus:border-blue-500 shadow-sm"
            ),
        ),
        class_name="w-full max-w-[20em] flex flex-col gap-y-2",
    )
