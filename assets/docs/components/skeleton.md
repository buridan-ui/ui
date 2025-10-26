

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
