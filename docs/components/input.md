---
title: "Input"
description: "Custom input component."
order: 11
---

# Input

Custom input component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Input", "buridan add component input"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.input import input
```

# Examples
Below are examples demonstrating how the component can be used.

## Basic Demo
A simple text input demonstrating the default appearance and behavior.

--DEMO_AND_SINGLE_FUNCTION(input_demo)--

## Email
An input field optimized for email address entry.

--DEMO_AND_SINGLE_FUNCTION(input_email)--

## Password
An input field that hides characters for secure password entry.

--DEMO_AND_SINGLE_FUNCTION(input_password)--

## Disabled
An example of an input field in a disabled state.

--DEMO_AND_SINGLE_FUNCTION(input_disabled)--

## File Input
An input field for selecting and uploading files.

--DEMO_AND_SINGLE_FUNCTION(input_file)--

## Custom Input
An input field with a custom width and styling.

--DEMO_AND_SINGLE_FUNCTION(input_custom_width)--
