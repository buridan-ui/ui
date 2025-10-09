import reflex as rx


# Used in --show_code(theme_css_example)--
def theme_css_example():
    return rx.markdown("""```css
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
```""")


# Used in --show_code(app_stylesheets_example)--
def app_stylesheets_example():
    return rx.markdown("""```python
import reflex as rx

app = rx.App(stylesheets=["/theme.css"])
```""")


# Used in --show_code(fill_prop_example)--
def fill_prop_example():
    return rx.markdown("""```python
fill="var(--chart-1)"
```""")


# Used in --show_code(theme_red_example)--
def theme_red_example():
    # Placeholders for demonstration
    def get_tooltip():
        return rx.box("Tooltip")

    def get_cartesian_grid():
        return rx.box("Cartesian Grid")

    def get_x_axis(label):
        return rx.box(f"X-Axis: {label}")

    data = []

    return rx.box(
        # ...
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
        # ...
        class_name="theme-red",  # <- .theme-red from theme.css
    )


# Used in --show_code(custom_theme_css_example)--
def custom_theme_css_example():
    return rx.markdown("""```css
.theme-coral {
    --chart-1: oklch(0.82 0.18 40);
    --chart-2: oklch(0.7 0.19 38);
    ...
}
```""")
