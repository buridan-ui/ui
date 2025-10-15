import reflex as rx

# --- Markdown Styles ---
PARAGRAPH_CLASS = "text-sm leading-6 pb-4"
HEADING_1_CLASS = "text-2xl py-1"
HEADING_2_CLASS = "text-xl py-1"
LIST_ITEM_CLASS = "text-sm text-slate-11"
LINK_CLASS = "text-accent-8"
CODE_BLOCK_CLASS = "!rounded-xl !bg-transparent"
CODE_BLOCK_BORDER = f"1px dashed {rx.color('gray', 5)}"


# --- Helper error functions during parsing ---
def render_parse_error(msg: str):
    return rx.el.p(msg, class_name="text-sm text-red-500")


# --- Helper functions ---
def render_heading(level: int, text: str) -> rx.Component:
    return rx.heading(
        text, class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS, id=text
    )


def render_paragraph(text: str) -> rx.Component:
    return rx.text(text, class_name=PARAGRAPH_CLASS)


def render_list_item(text: str) -> rx.Component:
    return rx.list_item(rx.text(text, class_name=LIST_ITEM_CLASS))


def render_link(text: str, **props) -> rx.Component:
    return rx.link(text, class_name=LINK_CLASS, **props)


def render_codeblock(content: str, **props) -> rx.Component:
    return rx.el.div(
        rx.code_block(
            content,
            decorations=[{"always_wrap": True}],
            theme=rx.color_mode_cond(
                rx.code_block.themes.one_light, rx.code_block.themes.vs_dark
            ),
            font_size="13px",
            language="python",
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
            class_name=CODE_BLOCK_CLASS,
            border=CODE_BLOCK_BORDER,
        ),
        rx.el.button(
            rx.icon(tag="copy", size=13),
            cursor="pointer",
            position="absolute",
            right="15px",
            top="20px",
            on_click=[
                rx.toast("Command copied"),
                rx.set_clipboard(content),
            ],
        ),
        class_name="w-full rounded-[0.625rem] relative",
    )


# --- Final Component Map ---
markdown_component_map = {
    "h1": lambda text: render_heading(1, text),
    "h2": lambda text: render_heading(2, text),
    "p": render_paragraph,
    "li": render_list_item,
    "codeblock": render_codeblock,
    "a": render_link,
}
