import reflex as rx
from src.docs.library.components.button.button import button


def site_theme() -> rx.Component:
    return button(
        rx.color_mode.icon(
            light_component=rx.el.div(
                rx.icon("moon", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
            dark_component=rx.el.div(
                rx.icon("sun", size=14, color=rx.color("slate", 12)),
                class_name="flex flex-row items-center gap-x-2",
            ),
        ),
        class_name=(
            "inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
            "cursor-pointer h-[1.925rem] w-[1.925rem]"
        ),
        on_click=rx.toggle_color_mode,
        variant="ghost",
        size="sm",
    )


def site_github() -> rx.Component:
    return rx.link(
        button(
            rx.icon("github", size=14),
            class_name="cursor-pointer",
            variant="ghost",
            size="sm",
        ),
        color=f"{rx.color('slate', 12)} !important",
        href="https://github.com/buridan-ui",
        text_decoration="none",
        class_name=(
            "inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
            "cursor-pointer h-[1.925rem] w-[1.925rem] cursor-pointer"
        ),
    )


def site_reflex_build():
    return rx.el.a(
        button(
            rx.el.image(
                rx.color_mode_cond(
                    "/svg/reflex/reflex_light.svg",
                    "/svg/reflex/reflex_dark.svg",
                ),
            ),
            "Build",
            variant="ghost",
        ),
        href="https://build.reflex.dev/",
    )
