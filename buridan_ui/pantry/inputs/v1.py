import reflex as rx


def inputs_v1():
    return rx.box(
        rx.text(
            "Email",
            class_name=(
                # Typography
                "text-xs font-semibold"
            ),
        ),
        rx.el.input(
            placeholder="something@email.com",
            # outline="none",
            class_name=(
                # Layout & Spacing
                "p-2 w-full "
                # Typography
                + "text-sm "
                # Border & Shape
                + "rounded-md bg-transparent border "
                + rx.color_mode_cond(
                    "border-gray-200 ",
                    "border-gray-800 ",
                )
                # Effects
                + ""
                # Interactions
                + "focus:outline-none focus:border-blue-500"
                # Transitions
                + ""
            ),
        ),
        class_name=(
            # Layout & Spacing
            "w-full max-w-[20em] flex flex-col gap-y-2"
        ),
    )
