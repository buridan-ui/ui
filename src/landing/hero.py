import reflex as rx

from ..templates.search.search import search


def doc_icon_svg(fill: str, background: str) -> rx.Component:
    return rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <rect width="16" height="16" rx="2" fill="{background}"/>
            <path d="M10 9V13H12V9H10Z" fill="{fill}"/>
            <path d="M4 3V13H6V9H10V7H6V5H10V7H12V3H4Z" fill="{fill}"/>
        </svg>""",
        class_name="flex justify-center items-center",
    )


def title():
    return rx.box(
        rx.text(
            "buridan",
            font_weight="700",
            font_size="1.25rem",
            letter_spacing="-0.04em",
        ),
        rx.text(
            ".UI",
            font_size="0.6rem",
            position="relative",
            font_weight="600",
        ),
        class_name="flex flex-row items-baseline gap-x-[1px]",
    )


def nav_link(name: str, url: str = "#"):
    return rx.link(
        name,
        href=url,
        text_decoration="none",
        font_weight="400",
        color=rx.color("slate", 11),
        _hover={"color": rx.color("slate", 12)},
    )


def links():
    return rx.box(
        nav_link("Getting Started", "/getting-started/introduction"),
        nav_link("Charts", "/charts/area-charts"),
        nav_link("Pantry", "/pantry/accordions"),
        nav_link("Changelog", "/getting-started/changelog"),
        font_weight="400",
        class_name="hidden md:flex flex-row items-center text-sm no-underline gap-x-4",
    )


def navbar():
    return rx.box(
        rx.box(
            title(),
            links(),
            class_name="flex flex-row items-baseline gap-x-8",
        ),
        rx.box(
            search(),
            rx.link(
                rx.el.button(
                    rx.color_mode_cond(
                        doc_icon_svg(fill="white", background="black"),
                        doc_icon_svg(fill="black", background="white"),
                    ),
                    "Build",
                    class_name="rounded-md flex items-center gap-x-2 text-sm font-semibold",
                    border=f"1px solid {rx.color('gray', 3)}",
                    _hover={"background": rx.color("gray", 3)},
                    style={
                        "display": "inline-flex",
                        "height": "1.925rem",
                        "padding": "0.25rem 0.50rem",
                    },
                ),
                href="https://build.reflex.dev/",
                text_decoration="none",
                color=rx.color("slate", 12),
                _hover={"color": rx.color("slate", 12)},
            ),
            class_name="flex flex-row items-center gap-x-4",
        ),
        class_name="w-full h-10 absolute top-0 left-0 px-4 py-6 items-center justify-between flex flex-row",
    )


def header():
    return rx.text(
        "The Reflex Library for Web Apps",
        font_size="max(48px,min(5vw,76px))",
        font_weight="800",
        letter_spacing="-0.05em",
        line_height="1",
    )


def sub_header():
    return rx.box(
        rx.el.p(
            rx.fragment(
                "The ",
                rx.el.strong(rx.el.u("Buridan Library")),
                " provides Reflex developers ",
                rx.el.strong("modern UI components, smart layouts,"),
                " and ",
                rx.el.strong("clean design for building stunning web apps."),
            ),
            font_size="max(15px,min(2vw,20px))",
            font_weight="400",
            letter_spacing="-0.01em",
            line_height="1.8",
        ),
        class_name="w-full max-w-[750px] flex text-left md:text-center p-[12px] md:p-[40px 32px]",
    )


def product_details(*children, props: str = "") -> rx.Component:
    """Individual product feature card component."""
    return rx.box(
        *children,
        class_name="p-8 h-full flex items-center justify-center" + props,
    )


def products_showcase() -> rx.Component:
    """Main products grid component with dividers."""
    return rx.box(
        product_details(props=" hidden md:flex"),
        product_details(
            rx.box(
                rx.link(
                    rx.el.button(
                        "Get Started",
                        class_name="py-3 px-4 rounded-md w-full",
                        background=rx.color("slate", 12),
                        color=rx.color("slate", 1),
                    ),
                    href="/getting-started/introduction/",
                    text_decoration="none",
                    color=rx.color("slate", 12),
                    _hover={"color": rx.color("slate", 12)},
                    class_name="w-full cursor-pointer",
                ),
                rx.link(
                    rx.el.button(
                        "Learn Reflex",
                        class_name="py-3 px-4 rounded-md w-full",
                        border=f"1px solid {rx.color('gray', 3)}",
                        _hover={"background": rx.color("gray", 3)},
                    ),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    text_decoration="none",
                    color=rx.color("slate", 12),
                    _hover={"color": rx.color("slate", 12)},
                    class_name="w-full cursor-pointer",
                ),
                class_name="flex flex-col w-full sm:flex-row items-center gap-y-3 md:gap-x-3 text-sm font-semibold",
            )
        ),
        product_details(props=" hidden md:flex"),
        class_name="grid grid-cols-1 lg:grid-cols-3 w-full",
    )


def hero():
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
                header(),
                class_name="w-full flex items-center justify-center p-[12px] md:p-[24px]",
            ),
            rx.box(sub_header(), class_name="w-full flex items-center justify-center"),
            products_showcase(),
            class_name="w-full h-screen flex flex-col items-center justify-center divide-dashed divide-neutral-500/50",
            max_width="calc(1234px)",
        ),
        class_name="w-full h-screen flex flex-col items-center justify-center",
    )
