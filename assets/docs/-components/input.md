

# Input

Displays a form input field or a component that looks like an input field.

# Installation

Copy the following code into your app directory.


```python
from reflex.components.el import Input
from reflex.components.component import ComponentNamespace

INPUT = (
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


class InputComponent(Input):
    """Styled input component that extends rx.el.input."""

    @classmethod
    def create(cls, *children, **props):
        """Create the input component with default styling."""
        # Get existing class_name or empty string
        existing_class = props.get("class_name", "")

        # Merge base classes with any custom classes
        props["class_name"] = f"{INPUT} {existing_class}".strip()

        # Set data slot
        props["data_slot"] = "input"

        # Set default type if not provided
        if "type" not in props:
            props["type"] = "text"

        return super().create(*children, **props)


class Input(ComponentNamespace):
    """Namespace for Input component."""

    __call__ = staticmethod(InputComponent.create)


input = Input()
```


# Examples

## Basic Demo
A simple text input demonstrating the default appearance and behavior.


```python
def input_demo():
    return rx.el.div(
        rx.text("Text Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Enter your name",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Email
An input field optimized for email address entry.


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


## Password
An input field that hides characters for secure password entry.


```python
def input_password():
    return rx.el.div(
        rx.el.p("Password Input", class_name="text-sm font-medium mb-2"),
        input(
            type="password",
            placeholder="Enter your password",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Disabled
An example of an input field in a disabled state.


```python
def input_disabled():
    return rx.el.div(
        rx.el.p("Disabled Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Disabled input",
            disabled=True,
        ),
        class_name="w-full max-w-md p-8",
    )
```


## File Input
An input field for selecting and uploading files.


```python
def input_file():
    return rx.el.div(
        rx.el.p("File Input", class_name="text-sm font-medium mb-2"),
        input(
            type="file",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Custom Input
An input field with a custom width and styling.


```python
def input_custom_width():
    return rx.el.div(
        rx.el.p("Custom Width", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Max width 300px",
            class_name="max-w-[300px]",
        ),
        class_name="w-full max-w-md p-8",
    )
```

