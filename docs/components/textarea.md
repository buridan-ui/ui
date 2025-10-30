---
title: "Textarea"
description: "Custom Textarea component."
order: 23
---

# Textarea

Custom Textarea component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Textarea", "buridan add component textarea"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.textarea import textarea
```

# Examples
Below are examples demonstrating how the component can be used.

## Basic Demo
A standard multiline text area for general text input.

--DEMO_AND_SINGLE_FUNCTION(textarea_demo)--

## Disabled
A text area shown in a disabled, non-editable state.

--DEMO_AND_SINGLE_FUNCTION(textarea_disabled)--

## Custom Text Area
A text area with custom styling or dimensions.

--DEMO_AND_SINGLE_FUNCTION(textarea_custom)--
