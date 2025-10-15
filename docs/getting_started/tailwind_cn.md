---
title: "Tailwind Class Merge Utility"
description: "Utility function for merging Tailwind CSS classes in Reflex"
order: 7
---

# Tailwind Class Merge Utility

A utility function for merging and deduplicating Tailwind CSS classes in Reflex components. Essential for combining conditional classes and allowing components to accept additional styling.

# Purpose

The `cn()` utility handles:
- Merging multiple class strings into one
- Deduplicating identical classes
- Resolving conflicts between Tailwind classes
- Processing Reflex `Var` types, strings, lists, and tuples
- Filtering out `None` values for conditional logic

# Installation
Copy the following code into your app directory.

```python
from reflex.utils.imports import ImportVar
from reflex.vars import FunctionVar, Var
from reflex.vars.base import VarData


def cn(
    *classes: Var | str | tuple | list | None,
) -> Var:
    """Merge Tailwind CSS classes. Accepts strings, Vars, lists, or tuples.

    Args:
        *classes: Any number of class strings, Vars, tuples, or lists.

    Returns:
        Var: A Var representing the merged classes string.

    """
    return (
        Var(
            "cn",
            _var_data=VarData(imports={"clsx-for-tailwind": ImportVar(tag="cn")}),
        )
        .to(FunctionVar)
        .call(*classes)
        .to(str)
    )
```
