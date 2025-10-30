

# Text Area

Displays a form textarea or a component that looks like a textarea.

# Installation

Copy the following code into your app directory.


```python
"""Custom Textarea component."""

from reflex.components.component import Component
from reflex.components.el import Textarea as TextareaComponent

from ..component import CoreComponent


class ClassNames:
    """Class names for textarea components."""

    ROOT = "focus:shadow-[0px_0px_0px_2px_var(--primary-4)] focus:border-primary-7 focus:hover:border-primary-7 bg-secondary-1 border border-secondary-a4 hover:border-secondary-a6 transition-[color,box-shadow] disabled:border-secondary-4 disabled:bg-secondary-3 disabled:text-secondary-8 disabled:cursor-not-allowed cursor-text min-h-24 rounded-ui-md text-secondary-12 placeholder:text-secondary-9 text-sm disabled:placeholder:text-secondary-8 w-full outline-none max-h-[15rem] resize-none overflow-y-auto px-3 py-2.5 font-medium"


class Textarea(TextareaComponent, CoreComponent):
    """Root component for Textarea."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the textarea component."""
        props.setdefault(
            "custom_attrs",
            {
                "autoComplete": "off",
                "autoCapitalize": "none",
                "autoCorrect": "off",
                "spellCheck": "false",
            },
        )
        props["data-slot"] = "textarea"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


textarea = Textarea.create
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

