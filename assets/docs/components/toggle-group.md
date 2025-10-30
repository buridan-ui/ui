

# Toggle Group

Custom toggle group component.

# Installation

Copy the following code into your app directory.


### CLI

```bash
buridan add component toggle_group
```

### Manual Installation

```python
"""Custom toggle group component."""

from typing import Literal

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for toggle group components."""

    ROOT = "inline-flex items-center gap-1 p-1 rounded-ui-md bg-secondary-3 data-[orientation=vertical]:flex-col data-[disabled]:opacity-50 data-[disabled]:cursor-not-allowed"


class ToggleGroupBaseComponent(BaseUIComponent):
    """Base component for toggle group components."""

    library = f"{PACKAGE_NAME}/toggle-group"

    @property
    def import_var(self):
        """Return the import variable for the toggle group component."""
        return ImportVar(tag="ToggleGroup", package_path="", install=False)


class ToggleGroupRoot(ToggleGroupBaseComponent):
    """Provides a shared state to a series of toggle buttons."""

    tag = "ToggleGroup"

    # The open state of the toggle group represented by an array of the values of all pressed toggle buttons. This is the uncontrolled counterpart of value.
    default_value: Var[list[str | int]]

    # The open state of the toggle group represented by an array of the values of all pressed toggle buttons. This is the controlled counterpart of default_value.
    value: Var[list[str | int]]

    # Callback fired when the pressed states of the toggle group changes.
    on_value_change: EventHandler[passthrough_event_spec(list[str | int], dict)]

    # When false only one item in the group can be pressed. If any item in the group becomes pressed, the others will become unpressed. When true multiple items can be pressed. Defaults to False.
    toggle_multiple: Var[bool]

    # Whether the toggle group should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    # The component orientation (layout flow direction). Defaults to "horizontal".
    orientation: Var[LiteralOrientation]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the toggle group root component."""
        props["data-slot"] = "toggle-group"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


toggle_group = ToggleGroupRoot.create
```


# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.toggle_group import toggle_group
```

# Examples

Below are examples demonstrating how the component can be used.

## General


```python
def toggle_group_example():
    """A basic toggle group example."""
    return toggle_group(
        toggle(rx.icon("bold"), value="bold"),
        toggle(rx.icon("italic"), value="italic"),
        toggle(rx.icon("underline"), value="underline"),
        default_value=["bold"],
    )
```


## Multiple Selection


```python
def toggle_group_multiple():
    """A toggle group example allowing multiple selections."""
    return toggle_group(
        toggle(rx.icon("align-left"), value="left"),
        toggle(rx.icon("align-center"), value="center"),
        toggle(rx.icon("align-right"), value="right"),
        toggle_multiple=True,
        default_value=["left", "right"],
    )
```


## Disabled


```python
def toggle_group_disabled():
    """A disabled toggle group example."""
    return toggle_group(
        toggle(rx.icon("bold"), value="bold"),
        toggle(rx.icon("italic"), value="italic"),
        toggle(rx.icon("underline"), value="underline"),
        disabled=True,
    )
```

