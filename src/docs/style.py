import reflex as rx

markdown_component_map = {
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
            language="bash",
            wrap_long_lines=True,
            scrollbar_width="none",
            code_tag_props={
                "pre": "transparent",
                "background": "transparent",
            },
            custom_attrs={
                "background": "transparent !important",
                "pre": {"background": "transparent !important"},
                "code": {"background": "transparent !important"},
            },
            background="transparent !important",
            class_name="rounded-md shadow-sm !bg-transparent",
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
}
