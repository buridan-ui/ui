import reflex as rx
from reflex.experimental import ClientStateVar
from src.config import VERSION
from src.templates.search.search import search
from src.templates.drawer.drawer import drawer

# Chart Theme Components
Chart_Theme = ClientStateVar.create("chart_theme", "")
THEME_OPTIONS = [
    ("Feyrouz", "فيْروز", "theme-blue"),
    ("Yaqout", "يَاقوت", "theme-red"),
    ("Zumurrud", "زُمُرُّد", "theme-green"),
    ("Kahraman", "كَهْرَمان", "theme-amber"),
    ("Amethyst", "أَمِيثِسْت", "theme-purple"),
]


def _create_theme_option(name: str, arabic_name: str, color_class: str):
    """Create a single theme option."""
    return rx.popover.close(
        rx.el.div(
            rx.el.button(
                f"{name} {arabic_name}",
                class_name="w-full text-left",
                type="button",
            ),
            rx.el.div(
                style={"backgroundColor": "var(--chart-2)"},
                class_name=f"h-2 w-2 rounded {color_class}",
            ),
            on_click=[
                rx.call_function(Chart_Theme.set_value(color_class).to(str)),
                rx.call_script(
                    """
                    document.querySelectorAll('.recharts-wrapper').forEach(chart => {
                      chart.style.display = 'none';
                      void chart.offsetHeight;
                      chart.style.display = '';
                    });
                    """
                ),
            ],
            class_name="flex flex-row gap-x-2 items-center px-3 py-2 w-full justify-between hover:px-4 transition-[padding] duration-200 ease-out cursor-pointer",
        ),
        class_name="cursor-pointer",
    )


def _create_theme_content():
    """Create theme selection content."""
    content_items = []
    for i, (name, arabic_name, color_class) in enumerate(THEME_OPTIONS):
        content_items.append(_create_theme_option(name, arabic_name, color_class))

    return rx.box(
        *content_items,
        class_name="bg-background w-[160px] flex flex-col text-sm rounded-md shadow-md",
    )


def theme_select_menu():
    """Create theme selection menu."""
    return rx.box(
        rx.popover.root(
            rx.popover.trigger(
                rx.el.button(
                    "Chart Theme",
                    rx.el.div(
                        style={"backgroundColor": "var(--chart-2)"},
                        class_name=f"h-2 w-2 rounded-full {Chart_Theme.value.to(str)}",
                    ),
                    class_name="text-sm px-2 font-semibold flex flex-row justify-between items-center gap-x-4 rounded-md cursor-pointer",
                    type="button",
                    color=rx.color("slate", 11),
                ),
            ),
            rx.popover.content(
                _create_theme_content(),
                side="bottom",
                side_offset=15,
                class_name="items-center bg-transparent !shadow-none !p-0 border-none w-auto overflow-visible font-sans pointer-events-auto",
            ),
        ),
        style={
            "display": "inline-flex",
            "height": "1.925rem",
            "align_items": "baseline",
            "justify_content": "flex-start",
            "padding": "0.25rem",
        },
        border=f"1px solid {rx.color('gray', 3)}",
        class_name="rounded-md",
        _hover={"color": rx.color("slate", 12), "background": rx.color("gray", 3)},
    )


def buridan_doc_navbar_header():
    return (
        rx.el.div(
            rx.link(
                rx.box(
                    rx.text(
                        "buridan",
                        font_weight="700",
                        font_size="1rem",
                        letter_spacing="-0.04em",
                    ),
                    rx.text(
                        ".UI",
                        font_size="0.6rem",
                        position="relative",
                        font_weight="600",
                    ),
                    color=rx.color("slate", 12),
                    class_name="flex flex-row items-baseline gap-x-[1px]",
                ),
                text_decoration="none",
                href="/",
            ),
            rx.badge(VERSION, color_scheme="gray", size="1", variant="outline"),
            class_name="flex flex-row w-full items-end gap-x-2",
        ),
    )


def site_theme() -> rx.Component:
    return rx.el.button(
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
        border=f"1px solid {rx.color('gray', 5)}",
        on_click=rx.toggle_color_mode,
        _hover={"color": rx.color("slate", 12), "background": rx.color("gray", 3)},
    )


def site_github() -> rx.Component:
    return rx.link(
        rx.el.button(rx.icon("github", size=14), class_name="cursor-pointer"),
        color=f"{rx.color('slate', 12)} !important",
        href="https://github.com/buridan-ui",
        text_decoration="none",
        border=f"1px solid {rx.color('gray', 5)}",
        class_name=(
            "inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
            "cursor-pointer h-[1.925rem] w-[1.925rem] cursor-pointer"
        ),
        _hover={"color": rx.color("slate", 12), "background": rx.color("gray", 3)},
    )


def doc_navbar(url: str):
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.box(drawer(), class_name="flex xl:hidden"),
                buridan_doc_navbar_header(),
                class_name="max-w-[18rem] w-full flex flex-row gap-x-2 xl:gap-x-0 items-center justify-start px-4",
            ),
            rx.el.div(
                rx.box(theme_select_menu(), class_name="hidden md:flex")
                if url.startswith("/charts/")
                else rx.box(class_name="hidden"),
                search(),
                site_github(),
                site_theme(),
                class_name="w-full flex flex-row gap-x-2 items-center justify-end px-4",
            ),
            class_name="xl:max-w-[80rem] 2xl:max-w-[75rem] w-full mx-auto flex flex-row items-center",
        ),
        border_bottom=f"0.90px solid {rx.color('gray', 5)}",
        class_name="w-full h-12 flex items-enter justify-center absolute top-0 z-[99]",
    )
