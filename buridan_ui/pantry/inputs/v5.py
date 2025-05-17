import reflex as rx


def input_v5():
    return rx.box(
        rx.text("Price", class_name="text-xs font-semibold"),
        rx.box(
            rx.text(
                "$",
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 text-md",
            ),
            rx.text(
                "USD",
                class_name="absolute right-2 top-1/2 transform -translate-y-1/2 text-sm",
            ),
            rx.el.input(
                placeholder="0.00",
                class_name="pl-6 py-2 w-full "
                + "text-sm "
                + "rounded-md bg-transparent border border-gray-500/40 "
                + "focus:outline-none focus:border-blue-500",
            ),
            class_name="relative focus:outline-none",
        ),
        class_name="w-full max-w-[20em] flex flex-col gap-y-2",
    )
