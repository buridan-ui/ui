---
title: "Tooltip"
description: "Tooltip component from base-ui components."
order: 27
---

# Tooltip

Tooltip component from base-ui components.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Tooltip", "buridan add component tooltip"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.tooltip import tooltip
```

# Examples

Below are examples demonstrating how the component can be used.

## General

Basic example of a tooltip using the high-level API.

--DEMO_AND_SINGLE_FUNCTION(tooltip_example)--

## With Long Content

Demonstrates a tooltip with multi-line or long content.

--DEMO_AND_SINGLE_FUNCTION(tooltip_with_long_content)--

## Custom Placement

Shows tooltips positioned in non-default locations using side and align settings.

--DEMO_AND_SINGLE_FUNCTION(tooltip_with_custom_placement)--

## Low Level Tooltip

Shows how to build a group of icon tooltips using the low-level API.

--DEMO_AND_SINGLE_FUNCTION(tooltip_group_example)--
