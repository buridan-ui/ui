import reflex as rx


def subscribe_v1():
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(
                    tag="mail",
                    class_name="absolute left-2 top-1/2 transform -translate-y-1/2 size-5 "
                    + rx.color_mode_cond(
                        "!text-gray-400",
                        "!text-gray-600",
                    ),
                ),
                rx.el.input(
                    placeholder="Enter your email...",
                    # outline="none",
                    class_name=(
                        # Layout & Spacing
                        "pl-9 pr-20 py-2 w-full "
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
                rx.button(
                    "Join",
                    class_name="absolute right-2 top-1/2 transform -translate-y-1/2 h-2/3 !text-sm bg-blue-500",
                ),
                class_name="w-full relative focus:outline-none",
            ),
            rx.text("No spam, unsubscribe at any time.", class_name="text-sm"),
            class_name="w-full max-w-[20em] h-full flex flex-col gap-y-2 items-center justify-center align-start",
        ),
        class_name="w-full h-[25vh] flex justify-center items-center align-center",
    )
