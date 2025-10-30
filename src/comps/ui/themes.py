import reflex as rx
from src.docs.library.base_ui.components.base.button import button
import src.hooks as hooks

THEME_OPTIONS = [
    ("Hematite", "فيْروز", "gray"),
    ("Feyrouz", "فيْروز", "blue"),
    ("Yaqout", "يَاقوت", "red"),
    ("Zumurrud", "زُمُرُّد", "green"),
    ("Kahraman", "كَهْرَمان", "amber"),
    ("Amethyst", "أَمِيثِسْت", "purple"),
]


def theme_buttons():
    return rx.el.div(
        rx.el.div(
            *[
                rx.el.div(
                    button(
                        rx.el.div(
                            rx.el.div(
                                class_name=f"w-3 h-3 rounded-sm bg-{theme_class}-500"
                            ),
                            rx.el.p(name, class_name="text-sm"),
                            class_name="flex flex-row items-center gap-x-2",
                        ),
                        variant="ghost",
                        size="sm",
                        on_click=hooks.current_theme.set_value(theme_class),
                    ),
                    class_name="rounded-lg "
                    + rx.cond(
                        hooks.current_theme.value == theme_class,
                        "border border-primary",
                        "",
                    ).to(str),
                )
                for name, __, theme_class in THEME_OPTIONS
            ],
            class_name=(
                "w-full flex flex-row flex-wrap gap-4 items-center "
                "justify-center md:justify-start px-8 pt-10 "
                + rx.color_mode_cond(
                    f"theme-{hooks.current_theme.value}",
                    f"theme-{hooks.current_theme.value}-dark",
                ).to(str)
            ),
        )
    )
