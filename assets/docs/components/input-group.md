

# Input Group

Combines inputs with prefixes, suffixes, or footers for structured data entry.

# Installation

Copy the following code into your app directory.


```python
import reflex as rx
from typing import Optional, Union


def input_with_addons(
    *children,
    placeholder: str = "",
    prefix: Optional[Union[str, "rx.Component"]] = None,
    suffix: Optional[Union[str, "rx.Component"]] = None,
    input_type: str = "text",
    class_name: str = "",
    **props,
):
    children = list(children)

    if prefix:
        if isinstance(prefix, str):
            prefix = rx.text(
                prefix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pl-2 select-none pointer-events-none",
            )
        children.insert(0, prefix)

    children.append(
        rx.el.input(
            type=input_type,
            placeholder=placeholder,
            class_name=(
                "flex-1 bg-transparent border-0 outline-none "
                "text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] "
                "px-2 py-2 text-sm "
                + ("pl-2 " if prefix else "")
                + ("pr-2 " if suffix else "")
            ),
            **props,
        )
    )

    if suffix:
        if isinstance(suffix, str):
            suffix = rx.text(
                suffix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pr-2 select-none pointer-events-none",
            )
        children.append(suffix)

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
```


# Examples

## Price Input
An input field with a currency prefix for entering prices.


```python
def input_price():
    return rx.el.div(
        input_with_addons(
            placeholder="0.00",
            prefix="$",
            suffix="USD",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
```


## URL Input
An input field with a prefixed URL scheme for web addresses.


```python
def input_url():
    return rx.el.div(
        input_with_addons(
            placeholder="example.com",
            prefix="https://",
            suffix=".com",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
```


## Email Input
An input field that appends a fixed domain for email entry.


```python
def input_email():
    return rx.el.div(
        input_with_addons(
            placeholder="Enter your username",
            suffix="@company.com",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
```


## Textarea with Footer
A multiline input with a footer displaying additional information or controls.


```python
def input_textarea():
    return rx.el.div(
        textarea_with_footer(
            placeholder="Enter your message",
            footer_text="120 characters left",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
```

