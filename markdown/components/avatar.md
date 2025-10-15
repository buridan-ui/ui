

# Avatar

An image element with a fallback for representing the user.

# Installation

Copy the following code into your app directory.


```python
import reflex as rx
from typing import Optional
from reflex.vars import Var
from src.utils.twmerge import cn


def avatar(
    src: Optional[str] = None,
    alt: str = "",
    fallback: Optional[str] = None,
    class_name: str | Var = "",
    **props,
):
    base_avatar = "relative flex size-8 shrink-0 overflow-hidden rounded-full"
    image_styles = "aspect-square size-full object-cover"
    fallback_styles = (
        "bg-[var(--muted)] flex size-full items-center justify-center "
        "rounded-full text-sm font-medium"
    )

    if src:
        content = rx.image(
            src=src,
            alt=alt,
            data_slot="avatar-image",
            class_name=image_styles,
        )
    elif fallback:
        content = rx.el.div(
            fallback,
            data_slot="avatar-fallback",
            class_name=fallback_styles,
        )
    else:
        content = rx.el.div()

    return rx.el.div(
        content,
        data_slot="avatar",
        class_name=cn(base_avatar, class_name),
        **props,
    )
```


# Examples

## General

Displays a basic avatar with either a user image or a fallback placeholder.


```python
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
```


## Sizes

Demonstrates how to scale the avatar component using Tailwind utility classes.


```python
def avatar_sizes():
    """Example showing different avatar sizes"""
    return rx.box(
        # Extra small
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-6",
        ),
        # Small
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-8",
        ),
        # Medium
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-10",
        ),
        # Large
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-12",
        ),
        # Extra large
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-16",
        ),
        class_name="flex items-center gap-4 p-8",
    )
```


## With Badge

Shows how to combine an avatar with status or notification badges for added context.


```python
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
```

