# import reflex as rx
# from typing import Optional


# def input_with_addons(
#     placeholder: str = "",
#     prefix: Optional[str] = None,
#     suffix: Optional[str] = None,
#     input_type: str = "text",
#     class_name: str = "",
#     **props,
# ):
#     children = []

#     if prefix:
#         children.append(
#             rx.text(
#                 prefix,
#                 class_name="text-gray-500 text-sm font-medium pl-3 select-none pointer-events-none",
#             )
#         )

#     children.append(
#         rx.el.input(
#             type=input_type,
#             placeholder=placeholder,
#             class_name=(
#                 "flex-1 bg-transparent border-0 outline-none "
#                 "text-foreground placeholder:text-gray-500 "
#                 "px-3 py-2 text-sm "
#                 + ("pl-2 " if prefix else "")
#                 + ("pr-2 " if suffix else "")
#             ),
#             **props,
#         )
#     )

#     if suffix:
#         children.append(
#             rx.text(
#                 suffix,
#                 class_name="text-gray-500 text-sm font-medium pr-3 select-none pointer-events-none",
#             )
#         )

#     return rx.box(
#         *children,
#         class_name=(
#             "flex items-center w-full h-9 "
#             "bg-transparent border border-neutral-500/30 rounded-[var(--radius)] "
#             "focus-within:border-[var(--focus-border)] focus-within:ring-2 focus-within:ring-[var(--focus-ring)] "
#             "transition-all duration-200 " + class_name
#         ),
#     )


# def textarea_with_footer(
#     placeholder: str = "",
#     footer_text: Optional[str] = None,
#     class_name: str = "",
#     **props,
# ):
#     children = [
#         rx.el.textarea(
#             placeholder=placeholder,
#             class_name=(
#                 "flex-1 bg-transparent border-0 outline-none resize-none "
#                 "text-foreground placeholder:text-gray-500 placeholder:text-sm "
#                 "px-3 py-3 text-sm " + ("pb-2 " if footer_text else "")
#             ),
#             **props,
#         )
#     ]

#     if footer_text:
#         children.append(
#             rx.text(
#                 footer_text,
#                 class_name="text-gray-500 text-xs px-3 pb-3 pt-0 select-none pointer-events-none",
#             )
#         )

#     return rx.box(
#         *children,
#         class_name=(
#             "flex flex-col w-full "
#             "bg-transparent border border-neutral-500/30 rounded-[var(--radius)] "
#             "focus-within:border-[var(--focus-border)] focus-within:ring-2 focus-within:ring-[var(--focus-ring)] "
#             "transition-all duration-200 " + class_name
#         ),
#     )


# # Example usagag
# def input_group():
#     """Examples showing all the different input styles"""
#     return rx.box(
#         # Price input with prefix and suffix
#         input_with_addons(
#             placeholder="0.00",
#             prefix="$",
#             suffix="USD",
#         ),
#         # URL input
#         input_with_addons(
#             placeholder="example.com",
#             prefix="https://",
#             suffix=".com",
#         ),
#         # Email input with suffix only
#         input_with_addons(
#             placeholder="Enter your username",
#             suffix="@company.com",
#         ),
#         # Textarea with character counter
#         textarea_with_footer(
#             placeholder="Enter your message",
#             footer_text="120 characters left",
#         ),
#         class_name="grid w-full max-w-sm gap-6",
#     )

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
    """
    Simple input with optional prefix and suffix text.
    Uses CSS variables from your shadcn theme.
    """
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
    """
    Textarea with optional footer text (like character counter).
    Uses CSS variables from your shadcn theme.
    """
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


# Example usage
def input_group():
    """Examples showing all the different input styles"""
    return rx.box(
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
        class_name="grid w-full max-w-sm gap-6",
    )
