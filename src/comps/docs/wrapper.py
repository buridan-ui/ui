import reflex as rx
from src.docs.style import render_codeblock


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


def demo_and_code_single_file_wrapper(
    component: rx.Component, source: str
) -> rx.Component:
    tab_list_style = {
        "border": "none",
        "boxShadow": "none",
        "background": "transparent",
    }

    return rx.tabs.root(
        rx.tabs.list(
            styled_tab_trigger("Preview", "preview"),
            styled_tab_trigger("Source Code", "source-code"),
            style=tab_list_style,
        ),
        rx.tabs.content(
            component,
            value="preview",
            class_name="mt-6 min-h-[250px] flex items-center justify-center outline outline-input rounded-default",
        ),
        rx.tabs.content(
            render_codeblock(content=source, copy_button=True, line_num=True),
            value="source-code",
            class_name="mt-6",
        ),
        default_value="preview",
        class_name="px-4",
    )


def cli_and_manual_installation_wrapper(cli_command: str, source: str) -> rx.Component:
    tab_list_style = {
        "border": "none",
        "boxShadow": "none",
        "background": "transparent",
    }

    return rx.tabs.root(
        rx.tabs.list(
            styled_tab_trigger("CLI", "cli"),
            styled_tab_trigger("Manual", "manual"),
            style=tab_list_style,
        ),
        rx.tabs.content(
            render_codeblock(
                content=cli_command,
                lang="bash",
                copy_button=True,
                line_num=False,
            ),
            value="cli",
            class_name="mt-6",
        ),
        rx.tabs.content(
            render_codeblock(content=source, copy_button=True, line_num=True),
            value="manual",
            class_name="mt-6",
        ),
        default_value="cli",
        class_name="px-4",
    )
