import reflex as rx


from .style import FooterStyle
from src.static.routes import GettingStartedRoutes, ChartRoutes, PantryRoutes


def create_footer_item(title: str, routes: list[dict[str, str]]):
    def item(data):
        return rx.el.div(
            rx.link(
                rx.el.label(
                    (
                        data["name"]
                        if data["name"] != "Frequently Asked Questions"
                        else "FAQ"
                    ),
                    _hover={"color": rx.color("slate", 12)},
                    class_name="text-sm font-regular cursor-pointer "
                    + rx.color_mode_cond("text-slate-700", "text-slate-200").to(str),
                ),
                href=data["path"],
                text_decoration="none",
            ),
            class_name="w-full",
        )

    return rx.vstack(
        rx.text(title, weight="bold", size="1", color=rx.color("slate", 12)),
        rx.hstack(*[item(data) for data in routes], **FooterStyle.footer_item),
        width="100%",
        padding="0.5em 0em",
        spacing="2",
    )


def title():
    return rx.box(
        rx.text(
            "buridan",
            font_weight="700",
            font_size="1rem",
            letter_spacing="-0.04em",
        ),
        rx.text(
            ".UI",
            font_size="0.45rem",
            position="relative",
            font_weight="600",
        ),
        class_name="flex flex-row items-baseline gap-x-[1px]",
    )


def footer():
    return rx.el.div(
        rx.el.div(
            create_footer_item("Home", GettingStartedRoutes),
            create_footer_item("Charts UI", ChartRoutes),
            create_footer_item("Pantry UI", PantryRoutes),
            class_name="w-full h-full py-6 flex flex-col",
        ),
        rx.el.div(
            title(),
            rx.el.label(
                "© 2024 - 2025 Ahmad Hakim. All rights reserved.",
                class_name="text-sm font-light",
            ),
            class_name="flex flex-col gap-y-2 py-6",
            border_top=f"0.90px solid {rx.color('gray', 5)}",
        ),
        border_top=f"0.90px solid {rx.color('gray', 5)}",
        class_name="xl:max-w-[80rem] 2xl:max-w-[75rem] w-full mx-auto flex flex-col gap-x-0 px-4",
    )


def desktop_footer():
    return rx.vstack(
        rx.vstack(
            title(),
            rx.el.label(
                "© 2024 - 2025 Ahmad Hakim. All rights reserved.",
                class_name="text-sm font-light",
            ),
            spacing="2",
            width="100%",
        ),
        class_name="py-5",
    )
