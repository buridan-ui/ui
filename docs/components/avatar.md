---
title: "Avatar"
description: "Displays a user's profile picture, initials, or fallback icon."
order: 1
---

# Avatar

Displays a user's profile picture, initials, or fallback icon.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Avatar", "buridan add component avatar"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.avatar import avatar
```

# Examples

Below are examples demonstrating how the component can be used.

## General

Displays a basic avatar with either a user image or a fallback placeholder.

--DEMO_AND_SINGLE_FUNCTION(avatar_example)--

## Sizes

Demonstrates how to scale the avatar component using Tailwind utility classes.

--DEMO_AND_SINGLE_FUNCTION(avatar_sizes)--

## With Badge

Shows how to combine an avatar with status or notification badges for added context.

--DEMO_AND_SINGLE_FUNCTION(avatar_with_badge)--
