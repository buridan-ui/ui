---
title: "Badge"
description: "A badge component that displays a label."
order: 2
---

# Badge

A badge component that displays a label.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Badge", "buridan add component badge"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.badge import badge
```

# Examples

Below are examples demonstrating how the component can be used.

## Default

Displays a standard badge using the default variant, ideal for basic labeling.

--DEMO_AND_SINGLE_FUNCTION(badge_demo)--

## With Icons

Demonstrates how to include icons inside badges for visual context or emphasis.

--DEMO_AND_SINGLE_FUNCTION(badge_with_icons)--

## Status

Showcases how badges can represent different statuses, like success or error, using color.

--DEMO_AND_SINGLE_FUNCTION(badge_status_examples)--

## Notification Count

Illustrates how to use badges for showing counts, such as unread notifications or messages.

--DEMO_AND_SINGLE_FUNCTION(badge_notification_count)--
