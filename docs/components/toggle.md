---
title: "Toggle"
description: "Custom toggle component."
order: 25
---

# Toggle

Custom toggle component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Toggle", "buridan add component toggle"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.toggle import toggle
```

# Examples

Below are examples demonstrating how the component can be used.

## General
A simple toggle component that can be pressed to switch between active and inactive states.

--DEMO_AND_SINGLE_FUNCTION(toggle_example)--

## Pressed State
Demonstrates a toggle that starts in the pressed state by default.

--DEMO_AND_SINGLE_FUNCTION(toggle_pressed)--

## Disabled
Shows a toggle that is disabled and cannot be interacted with.

--DEMO_AND_SINGLE_FUNCTION(toggle_disabled)--
