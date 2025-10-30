---
title: "Button"
description: "A custom button component."
order: 3
---

# Button

A custom button component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Button", "buridan add component button"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.button import button
```

# Examples

Below are examples demonstrating how the component can be used.

## Sizes

Showcases buttons in different predefined sizes (default, small, large, icon, etc).

--DEMO_AND_SINGLE_FUNCTION(button_size_examples)--

## Default

The default visual style for buttons with standard background and hover effects.

--DEMO_AND_SINGLE_FUNCTION(button_default_example)--

## Secondary

A more muted alternative to the default button, useful for less prominent actions.

--DEMO_AND_SINGLE_FUNCTION(button_secondary_example)--

## Outline

Buttons with a bordered outline, blending well with minimal UIs or light themes.

--DEMO_AND_SINGLE_FUNCTION(button_outline_example)--

## Ghost

A button style with no background or border, ideal for subtle UI actions.

--DEMO_AND_SINGLE_FUNCTION(button_ghost_example)--

## Link

A button styled to look like a hyperlink — useful for inline actions or navigation.

--DEMO_AND_SINGLE_FUNCTION(button_link_example)--

## Destructive

A bold style used for destructive or dangerous actions like “Delete”.

--DEMO_AND_SINGLE_FUNCTION(button_destructive_example)--

## Icon

Examples showing icon-only buttons with varying sizes for compact UI elements.

--DEMO_AND_SINGLE_FUNCTION(button_icon_examples)--
