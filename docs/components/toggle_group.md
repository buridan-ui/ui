---
title: "Toggle Group"
description: "Custom toggle group component."
order: 26
---

# Toggle Group

Custom toggle group component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["ToggleGroupRoot", "buridan add component toggle_group"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.toggle_group import toggle_group
```

# Examples

Below are examples demonstrating how the component can be used.

## General

A basic toggle group with single-selection mode, allowing only one active toggle at a time.

--DEMO_AND_SINGLE_FUNCTION(toggle_group_example)--

## Multiple Selection

Allows selecting multiple toggles simultaneously by enabling the multiple property.

--DEMO_AND_SINGLE_FUNCTION(toggle_group_multiple)--

## Disabled

Demonstrates a toggle group where all items are disabled and non-interactive.

--DEMO_AND_SINGLE_FUNCTION(toggle_group_disabled)--
