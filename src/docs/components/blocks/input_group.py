import reflex as rx
from typing import Optional
from reflex.experimental import ClientStateVar

border = ClientStateVar.create("border_stuff", "theme-retro")


def input_with_addons(
    placeholder: str = "",
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    input_type: str = "text",
    class_name: str = "",
    **props,
):
    """
    Simple input with optional prefix and suffix text.
    All styles are hardcoded in Tailwind classes.

    Args:
        placeholder: Input placeholder text
        prefix: Text to show before the input (e.g., "$", "https://")
        suffix: Text to show after the input (e.g., "USD", ".com")
        input_type: HTML input type (default: "text")
        class_name: Additional classes for the container
        **props: Additional props for the input element
    """
    children = []

    # Add prefix if provided
    if prefix:
        children.append(
            rx.text(
                prefix,
                class_name="text-gray-500 text-sm font-medium pl-3 select-none pointer-events-none",
            )
        )

    # Add the input
    children.append(
        rx.el.input(
            type=input_type,
            placeholder=placeholder,
            class_name=(
                "flex-1 bg-transparent border-0 outline-none "
                "text-foreground placeholder:text-gray-500 "
                "px-3 py-2 text-sm "
                + ("pl-2 " if prefix else "")
                + ("pr-2 " if suffix else "")
            ),
            **props,
        )
    )

    # Add suffix if provided
    if suffix:
        children.append(
            rx.text(
                suffix,
                class_name="text-gray-500 text-sm font-medium pr-3 select-none pointer-events-none",
            )
        )

    # Return the container with all elements
    return rx.box(
        *children,
        class_name=(
            "flex items-center w-full h-9 "
            "bg-transparent border-[0.9px] border-gray-500/40 rounded-[var(--border-radius)] "
            "focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20 "
            "transition-all duration-200 " + class_name
        ),
    )


def textarea_with_footer(
    placeholder: str = "",
    footer_text: Optional[str] = None,
    class_name: str = "",
    **props,
):
    """
    Textarea with optional footer text (like character counter).
    All styles are hardcoded in Tailwind classes.

    Args:
        placeholder: Textarea placeholder text
        footer_text: Text to show at the bottom (e.g., "120 characters left")
        class_name: Additional classes for the container
        **props: Additional props for the textarea element
    """
    children = [
        rx.el.textarea(
            placeholder=placeholder,
            class_name=(
                "flex-1 bg-transparent border-0 outline-none resize-none "
                "text-foreground placeholder:text-gray-500 "
                "px-3 py-3 text-sm " + ("pb-2 " if footer_text else "")
            ),
            **props,
        )
    ]

    # Add footer if provided
    if footer_text:
        children.append(
            rx.text(
                footer_text,
                class_name="text-gray-500 text-xs px-3 pb-3 pt-0 select-none pointer-events-none",
            )
        )

    # Return the container
    return rx.box(
        *children,
        class_name=(
            "flex flex-col w-full "
            "bg-transparent border border-gray-500/40 rounded-md "
            "focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20 "
            "transition-all duration-200 " + class_name
        ),
    )


# Example usagag
def input_group():
    """Examples showing all the different input styles"""
    return rx.box(
        rx.button("Retro", on_click=border.set_value("theme-retro")),
        rx.button("Normal", on_click=border.set_value("theme-normal")),
        # Price input with prefix and suffix
        input_with_addons(
            placeholder="0.00",
            prefix="$",
            suffix="USD",
        ),
        # URL input
        input_with_addons(
            placeholder="example.com",
            prefix="https://",
            suffix=".com",
        ),
        # Email input with suffix only
        input_with_addons(
            placeholder="Enter your username",
            suffix="@company.com",
        ),
        # Textarea with character counter
        textarea_with_footer(
            placeholder="Enter your message",
            footer_text="120 characters left",
        ),
        class_name="grid w-full max-w-sm gap-6 " + border.value.to(str),
    )
