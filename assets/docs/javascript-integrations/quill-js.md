

# Quill Integration with Reflex

Use [Quill](https://quilljs.com/) to add a rich text editor to your Reflex web apps. Quill provides a powerful, extensible API for creating and formatting text content directly in the browser. This guide shows how to integrate Quill using a CDN and custom scripts.


# Overview

This guide demonstrates integrating Quill JS rich text editor into a Reflex application.

<div id="quill-editor"
    style="width: 100%; height: 20vh; margin-bottom: 1rem;">
</div>


# Setup

To integrate Quill, you need to add its stylesheet, JavaScript library, and an initialization script to your app.

# Loading External Resources

Define functions that return the necessary stylesheet and library script tags.

```python
import reflex as rx

def quill_stylesheet():
    return rx.el.link(
        href="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css",
        rel="stylesheet",
    )

def quill_custom_font():
    return rx.el.link(
        href="https://fonts.googleapis.com/css?family=Aref+Ruqaa|Mirza|Roboto",
        rel="stylesheet",
    )

def quill_lib():
    return rx.script(src="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.js")
```

# Initialization Script

This script finds the editor `div` and initializes Quill on it.

```python
def quill_init():
    return rx.script(
        """
        setTimeout(function() {
            const quill = new Quill('#quill-editor', {
                theme: 'snow',
                placeholder: 'When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton.',
            });
        }, 500);
    """
    )
```

# Editor Component

This component creates the `div` that Quill will attach to.

```python
def quill_editor():
    return rx.html(
        '''<div id="quill-editor" style="height: 100%;"></div>'''
    )
```

# Application Setup

Add the resources to your app's `head_components` to ensure they are loaded on the page.

```python
app = rx.App(
    head_components=[
        quill_stylesheet(),
        quill_custom_font(),
        quill_lib(),
        quill_init(),
    ],
)
```
