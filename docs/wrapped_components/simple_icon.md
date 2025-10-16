---
title: "React Simple Icon"
description: "A lightweight wrapper for popular React icons, allowing easy use of vector icons directly in Reflex components."
order: 0
---

# Simple Icon

A lightweight Reflex wrapper for icons from the [`@icons-pack/react-simple-icons`](https://www.npmjs.com/package/@icons-pack/react-simple-icons) React package, perfect for easily rendering brand icons with custom colors and sizes.

# Installation

Add the following wrapped react code in Reflex inside your app.

```python
"""Simple Icon component wrapper for @icons-pack/react-simple-icons."""

import reflex as rx
from reflex.utils.imports import ImportVar


class SimpleIcon(rx.Component):
    """Simple Icon component wrapper for @icons-pack/react-simple-icons."""

    library = "@icons-pack/react-simple-icons"

    tag = "SiReact"

    color: rx.Var[str]

    size: rx.Var[int | str]

    @classmethod
    def create(cls, icon_name: str, **props):
        """Create a SimpleIcon component.

        Args:
            icon_name: The icon component name (e.g., "SiReact", "SiGithub", "SiPython")
            **props: Additional props like size, color

        Returns:
            The component instance.
        """
        instance = super().create(**props)
        instance.tag = icon_name
        return instance

    def add_imports(self) -> rx.ImportDict:
        """Add the specific icon import."""
        if self.library is None:
            exception = "Library must be set to use SimpleIcon"
            raise ValueError(exception)
        return {
            self.library: ImportVar(
                tag=self.tag,
                is_default=False,
            )
        }


def simple_icon(icon_name: str, **props) -> rx.Component:
    """Create a simple icon component.

    Args:
        icon_name: The Simple Icons component name (e.g., "SiGithub")
        **props: Additional props like size, color

    Returns:
        The SimpleIcon component.
    """
    return SimpleIcon.create(icon_name, **props)
```

# Usage

Make sure you use the correct imports inside your application.

```python
import reflex as rx
from components.simple_icon import simple_icon
```

# Example

## Simple Icon Example

Basic usage of the simple icon component

--DEMO_AND_SINGLE_FUNCTION(simple_icon_v1)--

## Simple Icon Colors

Customize icon colors by passing a color prop

--DEMO_AND_SINGLE_FUNCTION(simple_icon_v2)--

## Simple Icon Sizes

Control icon sizes using the size prop

--DEMO_AND_SINGLE_FUNCTION(simple_icon_v3)--
