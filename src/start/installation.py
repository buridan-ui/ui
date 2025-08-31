import reflex as rx
from src.wrappers.base.main import base
from src.start.style import markdown_component_map

md_content = """
### Step 1: Check your Python version

To use Reflex you need to have Python version 3.9 or above installed on your system.

```bash
python3 --version
```

### Step 2: PIP install the Reflex framework

Use the following command to install Reflex:

```bash
pip3 install reflex
```

Make sure the latest version of Reflex is installed:

```bash
reflex --version
```

### Step 3: Create a new Reflex Web Application

Inside your root directory, run the following command to create a new app:

```bash
reflex init
```

### Step 4: Copy & paste a pantry item directly into your app

You can now easily integrate pantry components within your app and personalize them.
"""


@base(url="/getting-started/installation", page_name="Installation")
def installation():
    return [
        rx.box(
            rx.markdown(md_content, component_map=markdown_component_map),
            class_name="p-4",
        )
    ]
