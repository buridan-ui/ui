

# React Spinner

A lightweight Reflex wrapper for spinners from the [`react-spinners`](https://www.npmjs.com/package/react-spinners) React package, perfect for easily rendering loading animations with custom colors and sizes.

# Installation

Add the following wrapped react code in Reflex inside your app.


### CLI

```bash
buridan add wrapped-react react_spinner
```

### Manual Installation

```python
"""Spinner component wrapper for react-spinners."""

import reflex as rx
from reflex.utils.imports import ImportVar


class Spinner(rx.Component):
    """React Spinner component."""

    library = "react-spinners"

    tag = "ClipLoader"

    color: rx.Var[str] | str = "var(--chart-1)"

    size: rx.Var[int]

    loading: rx.Var[bool]

    @classmethod
    def create(cls, spinner_type: str = "ClipLoader", **props):
        instance = super().create(**props)
        instance.tag = spinner_type
        return instance

    def add_imports(self):
        return {self.library: ImportVar(tag=self.tag, is_default=False)}


def spinner(spinner_type: str = "ClipLoader", **props):
    """Create a spinner. Types: ClipLoader, BeatLoader, CircleLoader, etc."""
    return Spinner.create(spinner_type, **props)
```


# Usage

Make sure you use the correct imports inside your application.

```python
import reflex as rx
from components.react_spinner import spinner
```
