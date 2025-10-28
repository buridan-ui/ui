---
title: "Dialog"
description: "Custom dialog component."
order: 8
---

# Dialog

Custom dialog component.

# Installation

Copy the following code into your app directory.

--CLI_AND_MANUAL_INSTALLATION(["Dialog", "buridan add component dialog"])--

# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.dialog import dialog
```

# Examples

Below are examples demonstrating how the component can be used.

## High Level

Uses the simplified dialog() API with trigger, title, description, and content props for quick implementation.

--DEMO_AND_SINGLE_FUNCTION(dialog_hh)--

## Low Level

Uses the low-level dialog.root(), dialog.trigger(), dialog.portal() etc. for full control over structure and styling

--DEMO_AND_SINGLE_FUNCTION(dialog_ll)--
