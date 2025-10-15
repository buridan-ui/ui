

# Text Area

Displays a form textarea or a component that looks like a textarea.

# Installation

Copy the following code into your app directory.


```python
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
```


# Examples

## Basic Demo
A standard multiline text area for general text input.


```python
def textarea_demo():
    return rx.el.div(
        rx.el.p("Textarea", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="Enter your message here...",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Disabled
A text area shown in a disabled, non-editable state.


```python
def textarea_disabled():
    return rx.el.div(
        rx.el.p("Disabled Textarea", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="This is disabled",
            disabled=True,
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Custom Text Area
A text area with custom styling or dimensions.


```python
def textarea_custom():
    return rx.el.div(
        rx.el.p("Custom Height", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="Taller textarea",
            class_name="min-h-32",
        ),
        class_name="w-full max-w-md p-8",
    )
```

