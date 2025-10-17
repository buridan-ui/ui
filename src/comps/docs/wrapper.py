import random
import string
import reflex as rx

from reflex.experimental import ClientStateVar


def generate_component_id():
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


def render_wrapper_code_block(source: str) -> rx.Component:
    return rx.el.div(
        rx.code_block(
            source,
            width="100%",
            font_size="12px",
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
        ),
        class_name="w-full",
    )


def preview_toggle_button(label: str, is_active: bool, on_click):
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
                preview_toggle_button(
                    "Preview", is_preview.value, is_preview.set_value(True)
                ),
                preview_toggle_button(
                    "Code", ~is_preview.value, is_preview.set_value(False)
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
