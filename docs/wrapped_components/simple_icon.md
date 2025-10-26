---
title: "React Simple Icon"
description: "A lightweight wrapper for popular React icons, allowing easy use of vector icons directly in Reflex components."
order: 0
---

# Simple Icon

A lightweight Reflex wrapper for icons from the [`@icons-pack/react-simple-icons`](https://www.npmjs.com/package/@icons-pack/react-simple-icons) React package, perfect for easily rendering brand icons with custom colors and sizes.

# Installation

Add the following wrapped react code in Reflex inside your app.

--CLI_AND_MANUAL_INSTALLATION(["SimpleIcon", "buridan add wrapped-react simple_icon"])--

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
