import reflex as rx


def inputs_v4():
    return rx.box(
        rx.text(
            "Website URL",
            class_name=(
                # Layout & Spacing
                ""
                # Typography
                + "text-xs font-semibold"
                # Border & Shape
                + ""
                # Effects
                + ""
                # Interactions
                + ""
                # Transitions
                + ""
            ),
        ),
        rx.box(
            rx.text(
                "https://",
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 text-sm",
                # + rx.color_mode_cond(
                #     "!text-gray-400",
                #     "!text-gray-600",
                # ),
            ),
            rx.el.input(
                placeholder="buridan-ui.reflex.run",
                # outline="none",
                class_name=(
                    # Layout & Spacing
                    "pl-20 py-2 w-full "
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
            class_name="relative focus:outline-none",
        ),
        class_name=(
            # Layout & Spacing
            "w-full max-w-[20em] flex flex-col gap-y-2"
            # Typography
            + ""
            # Border & Shape
            + ""
            # Effects
            + ""
            # Interactions
            + ""
            # Transitions
            + ""
        ),
    )
