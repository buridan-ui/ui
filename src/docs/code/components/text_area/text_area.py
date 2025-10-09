import reflex as rx
from typing import Optional


def textarea(placeholder: Optional[str] = None, class_name: str = "", **props):
    base_classes = (
        "placeholder:text-[var(--muted-foreground)] "
        "selection:bg-[var(--primary)] selection:text-[var(--primary-foreground)] "
        "dark:bg-[var(--input)]/30 border-[var(--input)] "
        "min-h-20 w-full rounded-md border bg-transparent px-3 py-2 text-base shadow-xs "
        "transition-[color,box-shadow] outline-none resize-none "
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
        "md:text-sm "
        "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
        "aria-invalid:border-[var(--destructive)]"
    )

    return rx.el.textarea(
        placeholder=placeholder,
        data_slot="textarea",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
