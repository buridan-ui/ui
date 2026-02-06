import reflex as rx

from src.create.ui.menu.fonts import font_menu
from src.create.ui.menu.library import component_library_menu
from src.create.ui.menu.theme import theme_menu

SidebarStyle = "max-w-[12rem] w-full sticky top-18 max-h-[100vh] z-[10]"
ContentStyle = "flex flex-col items-center gap-y-4 [&_.rt-ScrollAreaScrollbar]:mt-[2rem] [&_.rt-ScrollAreaScrollbar]:mb-[2rem]"


def component_sidebar():
    content = rx.el.div(
        component_library_menu(),
        class_name="flex flex-col max-w-[18rem] w-full h-full",
    )

    return rx.el.div(
        rx.scroll_area(
            content,
            class_name=ContentStyle,
        ),
        class_name=SidebarStyle,
    )


def menu_option_sidebar():
    content = rx.el.div(
        component_library_menu(),
        theme_menu(),
        font_menu(),
        class_name="flex flex-col max-w-[18rem] w-full h-full",
    )

    return rx.el.div(
        rx.scroll_area(
            content,
            class_name=ContentStyle,
        ),
        class_name=SidebarStyle,
    )
