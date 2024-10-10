import asyncio

import reflex as rx
from reflex import color

from .thumbnail_items.exports import export_thumbnail

from ..templates.shared.navbar import right_items, left_items
from ..routes.pantry_routes import PANTRY_ROUTES


def wrapper(title: str, instructions: str, tag: str):

    return rx.hstack(
        rx.vstack(
            rx.text(title, size="2", weight="bold", color=rx.color("slate", 12)),
            rx.text(instructions, size="2", weight="bold", color=rx.color("slate", 11)),
            width="100%",
            spacing="1",
            align="start",
            justify="start",
            text_align="start",
        ),
        rx.box(
            background_size="16px 16px",
            background_image=f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            mask=f"radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="100%",
            position="absolute",
        ),
        rx.icon(
            tag=tag,
            size=26,
            position="absolute",
            bottom="16px",
            right="16px",
        ),
        align="start",
        justify="start",
        position="relative",
        flex="1 1 300px",
        height="220px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 3),
        border_radius="12px",
        padding="16px",
        overflow="hidden",
        z_index="30",
        box_shadow="0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
    )


def create_background():
    return rx.box(
        background_size="90px 90px",
        background_image=(
            "linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)"
        ),
        mask=(
            # "radial-gradient(25% 25% at 75% 75%, hsl(0, 0%, 0%, 0.75), hsl(0, 0%, 0%, 0)), "
            "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
            # "radial-gradient(30% 50% at 50% 50%, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0)), "
            "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
        ),
        width="100%",
        height="100%",
        position="absolute",
        z_index="1",
    )


def create_navigation():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                    width="28px",
                    height="28px",
                    border_radius="49%",
                    object_fit="fit",
                    border=f"1px solid {rx.color('slate', 12)}",
                ),
                left_items(),
                align="center",
                padding="0px 14px",
            ),
            rx.box(
                right_items(),
                padding="0px 14px",
            ),
            align="center",
            justify="between",
            padding="18px 0px",
            backdrop_filter="blur(4px)",
            max_width="75em",
            width="100%",
            position="fixed",
        ),
        width="100%",
        z_index="100",
        max_width="70em",
        position="relative",
        justify_content="center",
        top="0",
    )


ROOT = dict(
    width="100%",
    align="center",
    justify="start",
    overflow="scroll",
    padding="0px 12px",
    min_height="100vh",
    background=rx.color("gray", 3),
)

CONTENT = dict(
    spacing="1",
    z_index="50",
    width="100%",
    padding="12px",
    align="center",
    justify="start",
    max_width="70em",
    text_align="center",
)


def create_section_header(title: str, description: str):
    return rx.vstack(
        rx.heading(
            title,
            weight="bold",
            size="8",
            font_family="var(--chakra-fonts-serif)",
            color=rx.color("slate", 12),
        ),
        rx.text(
            description,
            size="4",
            weight="medium",
            max_width="45em",
            color=rx.color("slate", 11),
        ),
        width="100%",
        text_align="start",
        padding="14px 0px",
    )


def create_footer_item(title: str, item_list: list[dict[str, str]]):
    return rx.vstack(
        rx.text(title, weight="bold", size="2", color=rx.color("slate", 11)),
        rx.hstack(
            *[
                rx.text(
                    item["name"],
                    weight="bold",
                    size="1",
                    text_align="start",
                    color=rx.color("slate", 12),
                )
                for item in item_list
            ],
            display="grid",
            grid_template_columns=[
                f"repeat({i}, minmax(0, 1fr))" for i in [2, 2, 3, 4, 4]
            ],
            justify="start",
            width="100%",
            gap="1rem 3rem",
        ),
        width="100%",
    )


class Index(rx.State):
    default_icon: bool = True

    async def toggle_icon(self):
        self.default_icon = False
        yield
        await asyncio.sleep(1)
        self.default_icon = True


@rx.page("/", "buridan-ui")
def index():
    return rx.vstack(
        create_navigation(),
        rx.vstack(
            rx.divider(height="10em", opacity="0"),
            rx.hstack(
                # rx.heading(
                #     "Buridan UI",
                #     weight="bold",
                #     size="2",
                #     letter_spacing="-1px",
                #     font_family="var(--chakra-fonts-serif)",
                #     color=rx.color("slate", 11),
                # ),
                # rx.separator(orientation="vertical", width="1.25px", height="30px"),
                *[
                    rx.badge(
                        rx.heading(
                            name,
                            size="2",
                            letter_spacing="-1px",
                            font_family="var(--chakra-fonts-serif)",
                            color=rx.color("slate", 11),
                        ),
                        variant="surface",
                        color_scheme="gray",
                    )
                    for name in ["Accessible", "Modern", "Open Source"]
                ],
                align="center",
                backdrop_filter="blur(24px)",
                z_index="20",
            ),
            rx.heading(
                "A Component Library Built With ",
                rx.text.em("Reflex"),
                weight="bold",
                size="9",
                font_family="var(--chakra-fonts-serif)",
                color=rx.color("slate", 12),
            ),
            rx.text(
                "Speed up your development with ready-made components designed for seamless integration. Create stunning applications effortlessly!",
                size="5",
                weight="medium",
                color=rx.color("slate", 11),
                max_width="45em",
                align="center",
            ),
            rx.hstack(
                rx.button(
                    "Getting Started",
                    variant="surface",
                    flex="4",
                    size="3",
                    color_scheme="gray",
                    z_index="20",
                ),
                rx.button(
                    "Pantry",
                    variant="soft",
                    color_scheme="gray",
                    flex="2",
                    size="3",
                    z_index="20",
                ),
                width="100%",
                max_width="20em",
                justify="center",
                padding="24px 0px",
            ),
            rx.divider(height="12em", opacity="0"),
            create_section_header(
                "Components Entirely Built With Reflex",
                "A full-stack framework complete with built-in features, including a comprehensive theming system, ready-to-use UI components, and customizable elements.",
            ),
            rx.hstack(
                wrapper(
                    "Fully Customizable Components",
                    "Easily adjust colors, fonts, and styles to create a unique look that enhances your application's user experience.",
                    "component",
                ),
                wrapper(
                    "Light & Dark Mode",
                    "Component Theming offers ready-to-use light and dark modes, allowing you to switch seamlessly between styles.",
                    "sun-moon",
                ),
                wrapper(
                    "Open Source License",
                    "Our components are available under an open source license, empowering you to use, modify, and share them freely.",
                    "code",
                ),
                gap="2rem",
                width="100%",
                display="grid",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 3, 3]
                ],
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            create_section_header(
                "Reflex Components",
                "Built on the Reflex framework, our components provide a set of prebuilt UI elements that streamline the development of responsive, web-based applications.",
            ),
            rx.hstack(
                *export_thumbnail,
                width="100%",
                display="grid",
                gap="1rem",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 2, 3, 4, 4]
                ],
                min_height="100vh",
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            create_section_header(
                "You're One Step Away From Shipping Your Web Application",
                "Download and install Reflex to start building out your idea, or check our the get started pages for more information.",
            ),
            rx.box(
                rx.hstack(
                    rx.button(
                        "Get Started",
                        variant="surface",
                        color_scheme="gray",
                        flex="2",
                        size="3",
                        z_index="20",
                    ),
                    rx.button(
                        "pip install reflex",
                        rx.cond(
                            Index.default_icon,
                            rx.icon(tag="clipboard-list", size=14),
                            rx.icon(tag="check", size=14, color=rx.color("grass", 12)),
                        ),
                        variant="soft",
                        color_scheme="gray",
                        flex="3",
                        size="3",
                        z_index="20",
                        display="flex",
                        justify_content="space-between",
                        cursor="pointer",
                        on_click=Index.toggle_icon,
                    ),
                    max_width="25em",
                    justify="start",
                    padding="24px 0px",
                ),
                width="100%",
            ),
            rx.divider(height="2.5em", opacity="0"),
            rx.vstack(
                rx.spacer(),
                rx.divider(height="15em", opacity="0"),
                rx.hstack(
                    rx.vstack(
                        left_items(),
                        rx.hstack(
                            rx.link(
                                rx.icon(
                                    tag="github",
                                    size=18,
                                    color=rx.color("slate", 11),
                                ),
                                href="#",
                                color_scheme="gray",
                                bg=rx.color("gray", 4),
                                border_radius="20%",
                                padding="3.5px",
                            ),
                            rx.link(
                                rx.icon(
                                    tag="youtube",
                                    size=18,
                                    color=rx.color("slate", 11),
                                ),
                                href="#",
                                color_scheme="gray",
                                bg=rx.color("gray", 4),
                                border_radius="20%",
                                padding="3.5px",
                            ),
                            align="center",
                        ),
                        justify="center",
                        flex=["100%", "100%", "100%", "20%", "20%"],
                        align="start",
                    ),
                    rx.vstack(
                        create_footer_item(
                            "Home",
                            [
                                {"name": "Installation"},
                                {"name": "Who is Buridan?"},
                                {"name": "Interactive Tables"},
                            ],
                        ),
                        rx.divider(height="1em", opacity="0"),
                        create_footer_item(
                            "Pantry",
                            PANTRY_ROUTES,
                        ),
                        rx.divider(height="1em", opacity="0"),
                        create_footer_item(
                            "Resources",
                            [
                                {"name": "Reflex Framework"},
                                {"name": "Source Code"},
                                {"name": "GitHub"},
                                {"name": "@LineIndent"},
                            ],
                        ),
                        rx.divider(height="1em", opacity="0"),
                        width="100%",
                        flex=["100%", "100%", "100%", "50%", "65%"],
                    ),
                    width="100%",
                    align="start",
                    flex_wrap=[
                        "wrap-reverse",
                        "wrap-reverse",
                        "wrap-reverse",
                        "wrap",
                        "wrap",
                    ],
                ),
                width="100%",
                border_top=f"1px solid {rx.color('gray', 12)}",
                padding="32px 0px",
                bg=rx.color("gray", 3),
                mask="linear-gradient(to top, hsl(0, 0%, 0%, 1) 50%, hsl(0, 0%, 0%, 0))",
                align="end",
                justify="between",
            ),
            **CONTENT,
        ),
        create_background(),
        **ROOT,
    )
