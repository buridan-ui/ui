import reflex as rx

from typing import Literal
from reflex.vars import Var
from src.utils.twmerge import cn
from dataclasses import dataclass


@dataclass
class ButtonStyles:
    BASE = (
        "inline-flex items-center justify-center gap-2 whitespace-nowrap "
        "rounded-md text-sm font-medium transition-all "
        "disabled:pointer-events-none disabled:opacity-50 outline-none "
        "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 "
        "[&_svg]:shrink-0 shrink-0"
    )

    FOCUS = (
        "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 "
        "focus-visible:ring-[3px]"
    )

    INVALID = (
        "aria-invalid:ring-[var(--destructive)]/20 "
        "dark:aria-invalid:ring-[var(--destructive)]/40 "
        "aria-invalid:border-[var(--destructive)]"
    )

    VARIANTS = {
        "default": ("bg-primary text-primary-foreground hover:bg-primary/90"),
        "destructive": (
            "bg-[var(--destructive)] text-white hover:bg-[var(--destructive)]/90 "
            "focus-visible:ring-[var(--destructive)]/20 "
            "dark:focus-visible:ring-[var(--destructive)]/40 "
            "dark:bg-[var(--destructive)]/60"
        ),
        "outline": (
            "border border-input bg-background shadow-xs "
            "hover:bg-[var(--accent)] hover:text-[var(--accent-foreground)] "
            "dark:bg-[var(--input)]/30 dark:border-input "
            "dark:hover:bg-[var(--input)]/50"
        ),
        "secondary": ("bg-secondary text-secondary-foreground hover:bg-secondary/80"),
        "ghost": (
            "hover:bg-[var(--accent)] hover:text-[var(--accent-foreground)] "
            "dark:hover:bg-[var(--accent)]/50"
        ),
        "link": "text-[var(--primary)] underline-offset-4 hover:underline",
    }

    SIZES = {
        "default": "h-9 px-4 py-2 has-[>svg]:px-3",
        "sm": "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        "lg": "h-10 rounded-md px-6 has-[>svg]:px-4",
        "icon": "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
    }

    @classmethod
    def compose(cls, variant: str, size: str, custom: str = "") -> Var:
        parts = [
            cls.BASE,
            cls.FOCUS,
            cls.INVALID,
            cls.VARIANTS[variant],
            cls.SIZES[size],
            custom,
        ]

        return cn(*parts)


def button(
    *children,
    variant: Literal[
        "default", "destructive", "outline", "secondary", "ghost", "link"
    ] = "default",
    size: Literal["default", "sm", "lg", "icon", "icon-sm", "icon-lg"] = "default",
    type: str = "button",
    class_name: str = "",
    **props,
):
    """
    Reflex button component with customizable variants and sizes

    Args:
        variant: Button visual style
        size: Button size preset
        type: HTML button type attribute
        class_name: Additional CSS classes
    """
    classes = ButtonStyles.compose(variant, size, class_name)

    return rx.el.button(
        *children, type=type, data_slot="button", class_name=classes, **props
    )
