import reflex as rx
from .simple_icon import simple_icon


def simple_icon_v1() -> rx.Component:
    return rx.el.div(
        simple_icon("SiGithub"),
        class_name="w-full h-full p-8 flex items-center justify-center",
    )


def simple_icon_v2() -> rx.Component:
    return rx.el.div(
        simple_icon("SiReact", color="#61DAFB"),
        simple_icon("SiPython", color="#3776AB"),
        simple_icon("SiJavascript", color="#F7DF1E"),
        class_name="w-full h-full p-8 flex flex-row items-center justify-center gap-x-4",
    )


def simple_icon_v3() -> rx.Component:
    return rx.el.div(
        simple_icon("SiGithub", size="1em"),
        simple_icon("SiGithub", size="2em"),
        simple_icon("SiGithub", size="3em"),
        class_name="w-full h-full p-8 flex flex-row items-center justify-center gap-x-4",
    )
