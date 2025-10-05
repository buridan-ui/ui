import reflex as rx
from typing import Optional


def input(
    type: str = "text", placeholder: Optional[str] = None, class_name: str = "", **props
):
    """
    Input component matching shadcn/ui styling.
    Uses CSS variables from your theme for colors.

    Args:
        type: HTML input type
        placeholder: Placeholder text
        class_name: Additional classes
        **props: Additional props for the input element
    """

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


def textarea(placeholder: Optional[str] = None, class_name: str = "", **props):
    """
    Textarea component matching shadcn/ui styling.
    Uses CSS variables from your theme for colors.

    Args:
        placeholder: Placeholder text
        class_name: Additional classes
        **props: Additional props for the textarea element
    """

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


# Example usage


def input_examples():
    """Examples showing different input types and states"""
    return rx.box(
        # Basic inputs
        rx.box(
            rx.text("Text Input", class_name="text-sm font-medium mb-2"),
            input(
                type="text",
                placeholder="Enter your name",
            ),
            class_name="mb-6",
        ),
        # Email input
        rx.box(
            rx.text("Email Input", class_name="text-sm font-medium mb-2"),
            input(
                type="email",
                placeholder="name@example.com",
            ),
            class_name="mb-6",
        ),
        # Password input
        rx.box(
            rx.text("Password Input", class_name="text-sm font-medium mb-2"),
            input(
                type="password",
                placeholder="Enter your password",
            ),
            class_name="mb-6",
        ),
        # Disabled input
        rx.box(
            rx.text("Disabled Input", class_name="text-sm font-medium mb-2"),
            input(
                type="text",
                placeholder="Disabled input",
                disabled=True,
            ),
            class_name="mb-6",
        ),
        # File input
        rx.box(
            rx.text("File Input", class_name="text-sm font-medium mb-2"),
            input(
                type="file",
            ),
            class_name="mb-6",
        ),
        # Textarea
        rx.box(
            rx.text("Textarea", class_name="text-sm font-medium mb-2"),
            textarea(
                placeholder="Enter your message here...",
            ),
            class_name="mb-6",
        ),
        # With custom class
        rx.box(
            rx.text("Custom Width", class_name="text-sm font-medium mb-2"),
            input(
                type="text",
                placeholder="Max width 300px",
                class_name="max-w-[300px]",
            ),
        ),
        class_name="w-full max-w-md p-8",
    )
