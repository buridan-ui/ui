import reflex as rx
from ...base_ui.components.base.avatar import avatar


def avatar_example():
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/84860195?v=4",
            alt="@LineIndent",
            fallback="CN",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/198465274?s=200&v=4",
            alt="@buridan-ui",
            fallback="BUI",
            class_name="rounded-lg",
        ),
        rx.box(
            avatar(
                src="",
                alt="@buridan-ui",
                fallback="BU",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@buridan-ui",
                fallback="BUI",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                alt="@reflex",
                fallback="RE",
            ),
            class_name=(
                "flex -space-x-2 "
                "*:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:ring-[var(--background)] "
                "*:data-[slot=avatar]:grayscale"
            ),
        ),
        class_name="flex flex-row flex-wrap items-center gap-12 p-8",
    )


def avatar_sizes():
    """Example showing different avatar sizes"""
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-6",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-8",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-10",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-12",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-16",
        ),
        class_name="flex items-center gap-4 p-8",
    )


def avatar_with_badge():
    """Example showing avatar with status badge"""
    return rx.box(
        rx.box(
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@LineIndent",
                fallback="CN",
                class_name="size-12",
            ),
            rx.box(
                class_name=(
                    "absolute bottom-0 right-0 size-3 rounded-full "
                    "bg-green-500 border-2 border-[var(--background)]"
                ),
            ),
            class_name="relative inline-block",
        ),
        class_name="p-8",
    )
