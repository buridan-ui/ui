import reflex as rx
from typing import Optional


def input_with_addons(
    placeholder: str = "",
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    input_type: str = "text",
    class_name: str = "",
    **props,
):
    children = []

    if prefix:
        children.append(
            rx.text(
                prefix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pl-3 select-none pointer-events-none",
            )
        )

    children.append(
        rx.el.input(
            type=input_type,
            placeholder=placeholder,
            class_name=(
                "flex-1 bg-transparent border-0 outline-none "
                "text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] "
                "px-3 py-2 text-sm "
                + ("pl-2 " if prefix else "")
                + ("pr-2 " if suffix else "")
            ),
            **props,
        )
    )

    if suffix:
        children.append(
            rx.text(
                suffix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pr-3 select-none pointer-events-none",
            )
        )

    return rx.box(
        *children,
        class_name=(
            "flex items-center w-full h-9 "
            "bg-transparent border border-[var(--input)] dark:bg-[var(--input)]/30 rounded-[var(--radius)] shadow-xs "
            "focus-within:border-[var(--ring)] focus-within:ring-[var(--ring)]/50 focus-within:ring-[3px] "
            "transition-[color,box-shadow] " + class_name
        ),
    )


def textarea_with_footer(
    placeholder: str = "",
    footer_text: Optional[str] = None,
    class_name: str = "",
    **props,
):
    children = [
        rx.el.textarea(
            placeholder=placeholder,
            class_name=(
                "flex-1 bg-transparent border-0 outline-none resize-none "
                "text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] placeholder:text-sm "
                "px-3 py-3 text-sm " + ("pb-2 " if footer_text else "")
            ),
            **props,
        )
    ]

    if footer_text:
        children.append(
            rx.text(
                footer_text,
                class_name="text-[var(--muted-foreground)] text-xs px-3 pb-3 pt-0 select-none pointer-events-none",
            )
        )

    return rx.box(
        *children,
        class_name=(
            "flex flex-col w-full "
            "bg-transparent border border-[var(--input)] dark:bg-[var(--input)]/30 rounded-[var(--radius)] shadow-xs "
            "focus-within:border-[var(--ring)] focus-within:ring-[var(--ring)]/50 focus-within:ring-[3px] "
            "transition-[color,box-shadow] " + class_name
        ),
    )
