import reflex as rx


def github_link():
    return rx.link(
        rx.el.button(
            rx.icon("github", size=14),
            class_name="rounded-md flex items-center gap-x-2 text-sm font-semibold cursor-pointer",
            border=f"1px solid {rx.color('gray', 3)}",
            _hover={"background": rx.color("gray", 3)},
            style={
                "display": "inline-flex",
                "height": "1.925rem",
                "padding": "0.25rem 0.50rem",
            },
        ),
        href="https://github.com/buridan-ui/ui",
        text_decoration="none",
        color=rx.color("slate", 12),
        _hover={"color": rx.color("slate", 12)},
    )
