---
title: "Installation"
description: "Steps to install and start using Buridan in your project."
order: 2
---

# Check your Python version

To use Buridan UI components, you need to have **Python version 3.11 or above** installed on your system.

```bash
python3 --version
```

# Install Reflex (if you haven't already)

Buridan UI components are built with Reflex. If you don't have Reflex installed, use the following command:

```bash
pip install reflex
```

Make sure the latest version of Reflex is installed:

```bash
reflex --version
```

# Install the Buridan UI CLI

The Buridan UI CLI allows you to easily add components to your Reflex project.

```bash
pip install buridan-ui
```

# Create or navigate to your Reflex Web Application

The `buridan` CLI commands must be run from the root directory of your Reflex project (where your `rxconfig.py` file is located).

If you need to create a new Reflex app:

```bash
reflex init my_app_name
cd my_app_name
```

# Add Buridan UI Components

Now you can use the `buridan add` command to add components to your project. The CLI will automatically place the components in the correct location within your app's source directory (e.g., `my_app_name/components/ui/`).

## Add a specific component (e.g., `button`)
  ```bash
  buridan add button
  ```
  This command will:
  *   Ensure your local component library cache is up-to-date.
  *   Validate that you are in a Reflex project.
  *   Add the `button.py` component and its necessary utility dependencies (like `twmerge.py`) to your project.

## **List available components:**
  ```bash
  buridan list
  ```
This command will show you all the components available in the Buridan UI library.

# Use the Components in Your App

Once components are added, you can import and use them in your Reflex application files. For example, if you added the `button` component:

```python
from your_app_name.components.ui.button import button

def index():
    return button("Click Me!")
```
(Note: `your_app_name` would be replaced by the actual `app_name` from your `rxconfig.py`.)
