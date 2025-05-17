import reflex as rx


def input_v4():
    return rx.box(
        rx.text("Website URL", class_name="text-xs font-semibold"),
        rx.box(
            rx.text(
                "https://",
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 text-sm",
            ),
            rx.el.input(
                placeholder="buridan-ui.reflex.run",
                class_name=(
                    "pl-[4em] py-2 w-full "
                    + "text-sm "
                    + "rounded-md bg-transparent border border-gray-500/40 "
                    + "focus:outline-none focus:border-blue-500"
                ),
            ),
            class_name="relative focus:outline-none",
        ),
        class_name="w-full max-w-[20em] flex flex-col gap-y-2",
    )
