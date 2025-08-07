import reflex as rx


def subscribe_v2():
    return rx.box(
        rx.box(
            rx.text("Sign up to our newsletter", class_name="text-md"),
            rx.box(
                rx.el.input(
                    placeholder="Enter your email...",
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
                class_name="relative focus:outline-none w-full",
            ),
            rx.button(
                "Subscribe",
                class_name="w-full !text-sm bg-blue-500",
            ),
            class_name="w-full max-w-[20em] h-full flex flex-col gap-y-4 items-center justify-center",
        ),
        class_name="w-full h-[25vh] flex justify-center items-center align-center",
    )
