import random
import string
import reflex as rx

from reflex.experimental import ClientStateVar
from src.docs.style import render_codeblock


def generate_component_id():
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


def render_wrapper_code_block(
    source: str,
    lang: str = "python",
    copy_button: bool = False,
    show_line_num: bool = False,
) -> rx.Component:
    wrapper_id = generate_component_id()

    is_copied = ClientStateVar.create(var_name=f"is_copied_{wrapper_id}", default=False)

    # cleaned_source = "\n".join(source.strip().splitlines())

    return rx.el.div(
        render_codeblock(
            source,
        ),
        # rx.code_block(
        #     cleaned_source,
        #     width="100%",
        #     font_size="13px",
        #     language=lang,
        #     wrap_long_lines=False,
        #     scrollbar_width="none",
        #     show_line_numbers=show_line_num,
        #     code_tag_props={
        #         "pre": "transparent",
        #         "background": "transparent",
        #     },
        #     custom_attrs={
        #         "background": "transparent !important",
        #         "pre": {"background": "transparent !important"},
        #         "code": {"background": "transparent !important"},
        #     },
        #     background="transparent !important",
        # ),
        (
            rx.el.button(
                rx.cond(
                    is_copied.value,
                    rx.icon("check", size=14),
                    rx.icon("clipboard", size=14),
                ),
                class_name="cursor-pointer py-1 px-2 flex items-center justify-center absolute top-[15px] right-[15px]",
                on_click=[
                    rx.call_function(is_copied.set_value(True)),
                    rx.set_clipboard(source),
                ],
                on_mouse_down=rx.call_function(is_copied.set_value(False)).debounce(
                    1500
                ),
            )
            if copy_button
            else rx.fragment()
        ),
        class_name="relative w-full gap-0 py-0",
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
    )


def toggle_button(label: str, is_active: bool, on_click):
    return rx.el.button(
        label,
        background=rx.cond(is_active, rx.color("gray", 4), ""),
        class_name=(
            "text-sm py-1 px-2 rounded-lg cursor-pointer "
            + rx.cond(
                is_active, "font-semibold opacity-[1]", "font-normal opacity-[0.8]"
            ).to(str)
        ),
        on_click=on_click,
    )


def demo_and_code_single_file_wrapper(
    component: rx.Component, source: str
) -> rx.Component:
    wrapper_id = generate_component_id()

    is_preview = ClientStateVar.create(
        var_name=f"active_tab_{wrapper_id}", default=True
    )
    is_copied = ClientStateVar.create(var_name=f"is_copied_{wrapper_id}", default=False)

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                toggle_button("Preview", is_preview.value, is_preview.set_value(True)),
                toggle_button("Code", ~is_preview.value, is_preview.set_value(False)),
                rx.el.button(
                    rx.cond(
                        is_copied.value,
                        rx.icon("check", size=12),
                        rx.icon("copy", size=12),
                    ),
                    class_name="opacity-[0.8] cursor-pointer py-1 px-2 flex items-center justify-center",
                    on_click=[
                        rx.call_function(is_copied.set_value(True)),
                        rx.set_clipboard(source),
                    ],
                    on_mouse_down=rx.call_function(is_copied.set_value(False)).debounce(
                        1500
                    ),
                ),
                class_name="flex flex-row items-center justify-end gap-x-4",
            ),
            rx.el.div(
                rx.cond(
                    is_preview.value,
                    component,
                    render_wrapper_code_block(source),
                ),
                class_name="w-full h-full flex items-center justify-center",
            ),
            class_name="w-full flex flex-col gap-y-0 overflow-hidden border border-dashed border-[var(--input)] px-2 py-4 rounded-xl",
        ),
        class_name="w-full flex py-4 px-4 min-h-[450px]",
    )


def styled_tab_trigger(label: str, value: str) -> rx.Component:
    base_tab_style = {
        "border": "none",
        "background": "transparent",
        "&[data-state=active]": {
            "border": "none",
            "borderBottom": rx.color_mode_cond(
                "1.25px solid black", "1.25px solid white"
            ),
            "background": "transparent",
        },
        "&[data-state=inactive]": {
            "border": "none",
            "background": "transparent",
        },
        "&::before": {
            "display": "none",
        },
    }

    return rx.tabs.trigger(rx.el.p(label), value=value, style=base_tab_style)


def cli_and_manual_installation_wrapper(component_name: str, source: str):
    tab_list_style = {
        "border": "none",
        "boxShadow": "none",
        "background": "transparent",
    }

    tab_content_style = (
        "bg-input/18 w-full flex flex-col gap-y-0 overflow-hidden rounded-xl"
    )

    return rx.tabs.root(
        rx.tabs.list(
            styled_tab_trigger("CLI", "cli"),
            styled_tab_trigger("Manual", "manual"),
            style=tab_list_style,
        ),
        rx.tabs.content(
            rx.el.div(
                render_wrapper_code_block(
                    source=f"buridan add component {component_name}",
                    lang="bash",
                    copy_button=True,
                ),
                class_name=tab_content_style,
            ),
            value="cli",
            class_name="mt-6",
        ),
        rx.tabs.content(
            rx.el.div(
                render_wrapper_code_block(source=source, copy_button=True),
                class_name=tab_content_style,
            ),
            value="manual",
            class_name="mt-6",
        ),
        default_value="cli",
        class_name="px-2",
    )


def _cli_and_manual_installation_wrapper(component_name: str, source: str):
    wrapper_id = generate_component_id()

    is_preview = ClientStateVar.create(
        var_name=f"active_tab_{wrapper_id}", default=True
    )
    is_copied = ClientStateVar.create(var_name=f"is_copied_{wrapper_id}", default=False)

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                toggle_button("CLI", is_preview.value, is_preview.set_value(True)),
                toggle_button("Manual", ~is_preview.value, is_preview.set_value(False)),
                class_name="flex flex-row gap-x-2 items-center",
            ),
            rx.el.button(
                rx.cond(
                    is_copied.value,
                    rx.icon("check", size=12),
                    rx.icon("copy", size=12),
                ),
                class_name="opacity-[0.8] cursor-pointer py-1 px-2 flex items-center justify-center",
                on_click=[
                    rx.call_function(is_copied.set_value(True)),
                    rx.set_clipboard(
                        rx.cond(
                            is_preview.value,
                            f"buridan add component {component_name}",
                            source,
                        )
                    ),
                ],
                on_mouse_down=rx.call_function(is_copied.set_value(False)).debounce(
                    1500
                ),
            ),
            class_name="flex flex-row items-center justify-between gap-x-4 pr-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.cond(
                    is_preview.value,  # True = CLI, False = Manual
                    render_wrapper_code_block(
                        f"buridan add component {component_name}", "bash"
                    ),
                    render_wrapper_code_block(source),
                ),
                class_name="w-full h-full flex items-center justify-center",
            ),
            class_name="bg-input/10 w-full flex flex-col gap-y-0 overflow-hidden rounded-xl",
        ),
        class_name="w-full flex flex-col gap-y-2 p-4",
    )
