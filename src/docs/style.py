import random
import string
import reflex as rx

from reflex.experimental import ClientStateVar

# --- Markdown Styles ---
PARAGRAPH_CLASS = "text-sm leading-6 pb-4"
HEADING_1_CLASS = "text-2xl py-1"
HEADING_2_CLASS = "text-xl py-1"
LIST_ITEM_CLASS = "text-sm text-slate-11"
LINK_CLASS = "text-accent-8"
CODE_BLOCK_CLASS = "!rounded-xl !bg-transparent"


# --- Helper functions to generate ClientStateVar names ---
def generate_component_id():
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


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


def render_codeblock(
    content: str,
    lang: str = "python",
    copy_button: bool = False,
    line_num: bool = False,
    **props,
) -> rx.Component:
    # Use the following to make line numbers sticky when horizontally scrolling...
    # style={
    #     ".linenumber.react-syntax-highlighter-line-number": {
    #         "position": "sticky",
    #         "left": "0",
    #         "background-color": "var(--input)",
    #         "zIndex": 1,
    #         "textAlign": "right",
    #         "paddingRight": "8px",
    #         "color": "#999",
    #         "userSelect": "none",
    #     }
    # },

    if copy_button:
        _id = generate_component_id()
        is_copied = ClientStateVar.create(var_name=f"is_copied_{_id}", default=False)

    return rx.el.div(
        rx.code_block(
            content,
            font_size="13px",
            language=lang,
            show_line_numbers=line_num,
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
        ),
        (
            rx.el.button(
                rx.cond(
                    is_copied.value,
                    rx.icon("check", size=14),
                    rx.icon("clipboard", size=14),
                ),
                class_name="cursor-pointer flex items-center justify-center absolute top-[15px] right-[15px]",
                on_click=[
                    rx.call_function(is_copied.set_value(True)),
                    rx.set_clipboard(content),
                ],
                on_mouse_down=rx.call_function(is_copied.set_value(False)).debounce(
                    1500
                ),
            )
            if copy_button
            else rx.el.div(class_name="hidden")
        ),
        class_name="w-full rounded-[0.625rem] relative bg-input/18 outline outline-input mb-4",
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
