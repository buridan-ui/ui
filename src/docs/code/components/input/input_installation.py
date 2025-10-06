import reflex as rx
from typing import Optional


def input(
    type: str = "text", placeholder: Optional[str] = None, class_name: str = "", **props
):
    base_classes = (
        "file:text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] "
        "selection:bg-[var(--primary)] selection:text-[var(--primary-foreground)] "
        "dark:bg-[var(--input)]/30 border-[var(--input)] "
        "h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs "
        "transition-[color,box-shadow] outline-none "
        "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium "
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
        "md:text-sm "
        "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
        "aria-invalid:border-[var(--destructive)]"
    )

    return rx.el.input(
        type=type,
        placeholder=placeholder,
        data_slot="input",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
