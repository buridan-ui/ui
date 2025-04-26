import reflex as rx


def inputs_v2():
    return rx.box(
        rx.box(
            rx.text(
                "Email",
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
            rx.text(
                "optional",
                class_name=(
                    # Layout & Spacing
                    ""
                    # Typography
                    + "text-xs font-light text-gray-400"
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
            class_name=(
                # Layout & Spacing
                "w-full flex flex-row justify-between items-center"
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
