

# Button

Displays a button or a component that looks like a button.

# Installation

Copy the following code into your app directory.


```python
"""Custom button component."""

from typing import Literal

from reflex.components.core.cond import cond
from reflex.components.el import Button as BaseButton
from reflex.vars.base import Var

from ..component import CoreComponent
from ...icons.others import spinner

LiteralButtonVariant = Literal[
    "primary", "destructive", "outline", "secondary", "ghost", "link", "dark"
]
LiteralButtonSize = Literal[
    "xs", "sm", "md", "lg", "xl", "icon-xs", "icon-sm", "icon-md", "icon-lg", "icon-xl"
]

DEFAULT_CLASS_NAME = "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-colors disabled:cursor-not-allowed disabled:border disabled:border-secondary-4/80 disabled:bg-secondary-3 disabled:text-secondary-8 shrink-0 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 text-medium cursor-pointer box-border"

BUTTON_VARIANTS = {
    "variant": {
        "primary": "bg-primary-9 text-white hover:bg-primary-10",
        "destructive": "bg-destructive-9 hover:bg-destructive-10 text-white",
        "outline": "border border-secondary-a4 bg-secondary-1 hover:bg-secondary-3 text-secondary-12",
        "secondary": "bg-secondary-4 text-secondary-12 hover:bg-secondary-5",
        "ghost": "hover:bg-secondary-3 text-secondary-11",
        "link": "text-secondary-12 underline-offset-4 hover:underline",
        "dark": "bg-secondary-12 text-secondary-1 hover:bg-secondary-12/80",
    },
    "size": {
        "xs": "px-1.5 h-7 rounded-ui-xs gap-1.5",
        "sm": "px-2 h-8 rounded-ui-sm gap-2",
        "md": "px-2.5 h-9 rounded-ui-md gap-2",
        "lg": "px-3 h-10 rounded-ui-lg gap-2.5",
        "xl": "px-3.5 h-12 rounded-ui-xl gap-3",
        "icon-xs": "size-7 rounded-ui-xs",
        "icon-sm": "size-8 rounded-ui-sm",
        "icon-md": "size-9 rounded-ui-md",
        "icon-lg": "size-10 rounded-ui-lg",
        "icon-xl": "size-12 rounded-ui-xl",
    },
}


class Button(BaseButton, CoreComponent):
    """A custom button component."""

    # Button variant. Defaults to "primary".
    variant: Var[LiteralButtonVariant]

    # Button size. Defaults to "md".
    size: Var[LiteralButtonSize]

    # The loading state of the button
    loading: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseButton:
        """Create the button component."""
        variant = props.pop("variant", "primary")
        cls.validate_variant(variant)

        size = props.pop("size", "md")
        cls.validate_size(size)

        loading = props.pop("loading", False)
        disabled = props.pop("disabled", False)

        button_classes = f"{DEFAULT_CLASS_NAME} {BUTTON_VARIANTS['variant'][variant]} {BUTTON_VARIANTS['size'][size]}"

        cls.set_class_name(button_classes, props)

        children_list = list(children)

        if isinstance(loading, Var):
            props["disabled"] = cond(loading, True, disabled)
            children_list.insert(0, cond(loading, spinner()))
        else:
            props["disabled"] = True if loading else disabled
            children_list.insert(0, spinner()) if loading else None

        return super().create(*children_list, **props)

    @staticmethod
    def validate_variant(variant: LiteralButtonVariant):
        """Validate the button variant."""
        if variant not in BUTTON_VARIANTS["variant"]:
            available_variants = ", ".join(BUTTON_VARIANTS["variant"].keys())
            message = (
                f"Invalid variant: {variant}. Available variants: {available_variants}"
            )
            raise ValueError(message)

    @staticmethod
    def validate_size(size: LiteralButtonSize):
        """Validate the button size."""
        if size not in BUTTON_VARIANTS["size"]:
            available_sizes = ", ".join(BUTTON_VARIANTS["size"].keys())
            message = f"Invalid size: {size}. Available sizes: {available_sizes}"
            raise ValueError(message)

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "size",
            "variant",
            "loading",
        ]


button = Button.create
```


# Examples

## Sizes

Showcases buttons in different predefined sizes (default, small, large, icon, etc).


```python
def button_size_examples():
    return rx.el.div(
        button("Small", size="sm"),
        button("Default", size="default"),
        button("Large", size="lg"),
        class_name="flex items-center gap-3",
    )
```


## Default

The default visual style for buttons with standard background and hover effects.


```python
def button_default_example():
    return rx.el.div(button("Default", variant="default"))
```


## Secondary

A more muted alternative to the default button, useful for less prominent actions.


```python
def button_secondary_example():
    return rx.el.div(button("Secondary", variant="secondary"))
```


## Outline

Buttons with a bordered outline, blending well with minimal UIs or light themes.


```python
def button_outline_example():
    return rx.el.div(button("Outline", variant="outline"))
```


## Ghost

A button style with no background or border, ideal for subtle UI actions.


```python
def button_ghost_example():
    return rx.el.div(button("Ghost", variant="ghost"))
```


## Link

A button styled to look like a hyperlink — useful for inline actions or navigation.


```python
def button_link_example():
    return rx.el.div(button("Link", variant="link"))
```


## Destructive

A bold style used for destructive or dangerous actions like “Delete”.


```python
def button_destructive_example():
    return rx.el.div(button("Destructive", variant="destructive"))
```


## Icon

Examples showing icon-only buttons with varying sizes for compact UI elements.


```python
def button_icon_examples():
    return rx.el.div(
        button(rx.icon("mail", class_name="size-4"), variant="outline", size="icon-sm"),
        class_name="flex items-center gap-3",
    )
```

