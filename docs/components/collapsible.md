---
title: "Collapsible"
description: "Custom collapsible component."
order: 6
---

# Collapsible

Custom collapsible component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Collapsible", "buridan add component collapsible"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.collapsible import collapsible
```

# Examples

Below are examples demonstrating how the component can be used.

## High Level Demo

Uses the simplified collapsible() API with trigger and content props for quick implementation.

--DEMO_AND_SINGLE_FUNCTION(collapsible_example)--

## Low Level Demo

Uses the low-level collapsible.root(), collapsible.panel(), and ClientStateVar for full control over state and structure.

--DEMO_AND_SINGLE_FUNCTION(collapsible_demo)--
