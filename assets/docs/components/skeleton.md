

# Skeleton

Custom skeleton component.

# Installation

Copy the following code into your app directory.


### CLI

```bash
buridan add component skeleton
```

### Manual Installation

```python
"""Custom skeleton component."""

from reflex.components.component import Component
from reflex.components.el import Div
from reflex.vars.base import Var

from ...utils.twmerge import cn


class ClassNames:
    """Class names for skeleton component."""

    ROOT = "animate-pulse bg-secondary-6"


def skeleton_component(
    class_name: str | Var[str] = "",
) -> Component:
    """Skeleton component."""
    return Div.create(class_name=cn(ClassNames.ROOT, class_name))


skeleton = skeleton_component
```


# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.skeleton import skeleton_component
```

# Examples

Below are examples demonstrating how the component can be used.

## General


```python
def skeleton_example():
    """A basic skeleton example."""
    return skeleton_component(class_name="h-8 w-32 rounded-md")
```


## Card Loading State


```python
def skeleton_card_example():
    """A skeleton example simulating a loading card."""
    return rx.box(
        rx.flex(
            skeleton_component(class_name="h-12 w-12 rounded-full"),
            rx.flex(
                skeleton_component(class_name="h-4 w-[250px] rounded-md"),
                skeleton_component(class_name="h-4 w-[200px] rounded-md"),
                direction="column",
                spacing="2",
            ),
            spacing="4",
        ),
        class_name="flex items-center space-x-4 rounded-md border p-4 w-96",
    )
```

