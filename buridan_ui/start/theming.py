import reflex as rx
from buridan_ui.wrappers.base.main import base

md_content = """
# 1. Introduction

Buridan UI includes built-in support for **chart theming** using CSS variables and the `oklch()` color format — giving you full control over chart palettes in both light and dark modes. Themes are defined at the CSS level and can be easily extended or customized.

This guide explains how to:

- Add the theming CSS to your Reflex project
- Switch between color themes
- Access chart colors via CSS variables in your components

Whether you're building dashboards, reports, or data apps — theming helps you keep things consistent and beautiful across the board.

# 2. Adding the Theme CSS File

To use Buridan's chart themes, you need to include the theme CSS in your project. Here's how to do it:

Create a new file in your Reflex app’s `assets/` folder (if it doesn't exist, create it):

```text
assets/
└── theme.css
```

Paste the following content into **theme.css**:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Default theme */
:root {
    --chart-1: oklch(0.81 0.1 252);
    --chart-2: oklch(0.62 0.19 260);
    --chart-3: oklch(0.55 0.22 263);
    --chart-4: oklch(0.49 0.22 264);
    --chart-5: oklch(0.42 0.18 266);
}

/* Dark theme */
.dark { ... }

/* Theme overrides */
.theme-blue { ... }
.theme-red { ... }
.theme-green { ... }
.theme-amber { ... }
.theme-purple { ... }
```

You can copy the full content from the chart theme [source](https://github.com/buridan-ui/ui/blob/main/assets/css/globals.css).

Import this CSS file in your **rx.App** declaration. Once imported, your app will automatically apply the default :root colors for charts:

```python
import reflex as rx

app = rx.App(stylesheets=["/theme.css"])
```

# 3. Usage Example: Using Chart Colors in Components

After importing the theme, any component that supports inline styles or Tailwind class bindings can access the chart colors via:

```css
var(--chart-1)
var(--chart-2)
...

```

For example, in a chart that takes in **fill** prop (such as that in area charts or bar charts):

```python
fill="var(--chart-1)"
```

This will set the fill color to the default value and theme (from inside the **.root**). Buridan ships with multiple pre-defined color themes for charts. To switch themes, apply one of the pre-defined theme system crated inside your **theme.css** file. For example, the following will set the **--chart-1** color to the **red theme** if we apply that theme to an outter component:

```python
rx.box(
    ...
    rx.recharts.area_chart(
        get_tooltip(),
        get_cartesian_grid(),
        rx.recharts.area(
            data_key="desktop",
            fill="var(--chart-1)",
            stroke="var(--chart-1)",
            stroke_width=2,
        ),
        get_x_axis("month"),
        data=data,
        width="100%",
        height=250,
    ),
    ...
    class_name="theme-red"  <- .theme-red from theme.css
)
```
The theme system is fully CSS-based, so switching themes won’t trigger any extra rendering — it’s instant, clean, and declarative.

# 4. Customizing or Extending Themes

Want to create your own chart palette? Just define a new theme block in theme.css:

```css
.theme-coral {
    --chart-1: oklch(0.82 0.18 40);
    --chart-2: oklch(0.7 0.19 38);
    ...
}
```

# 7. Summary

Buridan UI’s theming system gives you centralized control over color palettes, built-in support for light and dark modes, and simple switching between blue, red, green, amber, and purple themes. Designed with CSS-native flexibility, it works seamlessly across components, charts, and any custom UI elements. Add the CSS file once, and your entire app stays visually consistent and easy to style.

Happy theming! 🎨

"""


@base("/getting-started/theming", "Theming")
def theming():
    return [
        rx.box(
            rx.markdown(
                md_content,
                component_map={
                    "h1": lambda t: rx.heading(t, class_name="text-xl py-3"),
                    "p": lambda t: rx.text(
                        t,
                        class_name="text-sm leading-6 pb-4",
                    ),
                    "li": lambda t: rx.list_item(
                        rx.text(t, color=rx.color("slate", 11), class_name="text-sm"),
                    ),
                    "codeblock": lambda c, **p: rx.hstack(
                        rx.code_block(
                            c,
                            width="100%",
                            font_size="12px",
                            # language="bash",
                            wrap_long_lines=True,
                            scrollbar_width="none",
                            code_tag_props={"pre": "transparent", "bg": "transparent"},
                            custom_attrs={"bg": "transparent"},
                            bg="transparent",
                            class_name="rounded-md shadow-sm",
                            border=f"1px dashed {rx.color('gray', 5)}",
                        ),
                        rx.el.button(
                            rx.icon(tag="copy", size=13),
                            cursor="pointer",
                            position="absolute",
                            right="15px",
                            top="20px",
                            on_click=[
                                rx.toast("Command copied"),
                                rx.set_clipboard(c),
                            ],
                        ),
                        width="100%",
                        align="center",
                        position="relative",
                    ),
                    "a": lambda t, **p: rx.link(t, color=rx.color("accent", 8), **p),
                },
            ),
            class_name="p-4",
        )
    ]
