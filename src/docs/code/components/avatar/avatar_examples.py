import reflex as rx
from .avatar_installation import avatar


def avatar_example():
    return rx.box(
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
        ),
        avatar(
            src="https://github.com/evilrabbit.png",
            alt="@evilrabbit",
            fallback="ER",
            class_name="rounded-lg",
        ),
        rx.box(
            avatar(
                src="https://github.com/shadcn.png",
                alt="@shadcn",
                fallback="CN",
            ),
            avatar(
                src="https://github.com/maxleiter.png",
                alt="@maxleiter",
                fallback="LR",
            ),
            avatar(
                src="https://github.com/evilrabbit.png",
                alt="@evilrabbit",
                fallback="ER",
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
        # Extra small
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
            class_name="size-6",
        ),
        # Small
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
            class_name="size-8",
        ),
        # Medium
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
            class_name="size-10",
        ),
        # Large
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
            class_name="size-12",
        ),
        # Extra large
        avatar(
            src="https://github.com/shadcn.png",
            alt="@shadcn",
            fallback="CN",
            class_name="size-16",
        ),
        class_name="flex items-center gap-4 p-8",
    )


def avatar_with_badge():
    """Example showing avatar with status badge"""
    return rx.box(
        rx.box(
            avatar(
                src="https://github.com/shadcn.png",
                alt="@shadcn",
                fallback="CN",
                class_name="size-12",
            ),
            # Online indicator
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
