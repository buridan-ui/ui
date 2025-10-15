import reflex as rx
from typing import Literal
from reflex.vars import Var
from src.utils.twmerge import cn


def badge(
    *children,
    variant: Literal["default", "secondary", "destructive", "outline"] = "default",
    class_name: str | Var = "",
    **props,
):
    base_classes = (
        "inline-flex items-center justify-center rounded-md border px-2 py-0.5 text-xs font-medium "
        "w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none "
        "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
        "aria-invalid:border-[var(--destructive)] transition-[color,box-shadow] overflow-hidden"
    )

    variant_classes = {
        "default": (
            "border-transparent bg-[var(--primary)] text-[var(--primary-foreground)] "
            "[a&]:hover:bg-[var(--primary)]/90"
        ),
        "secondary": (
            "border-transparent bg-[var(--secondary)] text-[var(--secondary-foreground)] "
            "[a&]:hover:bg-[var(--secondary)]/90"
        ),
        "destructive": (
            "border-transparent bg-[var(--destructive)] text-white "
            "[a&]:hover:bg-[var(--destructive)]/90 "
            "focus-visible:ring-[var(--destructive)]/20 dark:focus-visible:ring-[var(--destructive)]/40 "
            "dark:bg-[var(--destructive)]/60"
        ),
        "outline": (
            "text-[var(--foreground)] border-[var(--input)] "
            "[a&]:hover:bg-[var(--accent)] [a&]:hover:text-[var(--accent-foreground)]"
        ),
    }

    combined_classes = cn(base_classes, variant_classes[variant], class_name)

    return rx.el.span(
        *children,
        data_slot="badge",
        class_name=combined_classes,
        **props,
    )
