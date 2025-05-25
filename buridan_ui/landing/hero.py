import reflex as rx

from buridan_ui.config import VERSION


def button_with_link(icon: str, url: str):
    return rx.box(
        rx.link(
            rx.icon(
                tag=icon,
                size=13,
            ),
            href=url,
            is_external=True,
            text_cdecoration="none",
            color=rx.color("slate", 11),
            _hover={"color": rx.color("slate", 12)},
        ),
        _hover={"background": rx.color("gray", 3)},
        border=f"1px solid {rx.color('gray', 5)}",
        class_name="cursor-pointer rounded-lg py-1 px-1 flex items-center justify-center",
    )


def create_block_design(color: str):
    return rx.box(
        # border_left=f"1.25px dashed {rx.color(color, 5)}",
        # border_right=f"1.25px dashed {rx.color(color, 5)}",
        # color=rx.color(color, 8),
        class_name=f"h-full p-4 col-start-2 row-span-full row-start-1 max-sm:hidden bg-[size:10px_10px] bg-fixed bg-[image:repeating-linear-gradient(315deg,currentColor_0,currentColor_1px,_transparent_0,_transparent_50%)] border-x-[1.25px] border-dashed text-{color} border-{color}",
    )


def create_block_link(name: str, description: str, url: str):
    return rx.el.div(
        rx.el.div(
            rx.el.label(name, class_name="text-lg font-medium"),
            rx.el.label(
                description,
                color=rx.color("slate", 11),
                class_name="text-sm font-medium",
            ),
            class_name="flex flex-col gap-y-1 max-w-sm",
        ),
        button_with_link("chevron-right", url),
        class_name="flex flex-row justify-between align-center items-center w-full",
        **{
            "position": "relative",
            "animation": "rightSlide 0.6s",
            "@keyframes rightSlide": {
                "from": {"bottom": "-25px", "opacity": "0"},
                "to": {"bottom": "0px", "opacity": "1"},
            },
        },
    )


def welcome_msessage():
    return rx.el.div(
        rx.el.div(
            rx.link(
                rx.el.label(
                    "ui",
                    class_name="text-sm underline hover:cursor-pointer",
                ),
                href="https://github.com/buridan-ui",
                is_external=True,
            ),
            "⋅",
            rx.link(
                rx.el.label(
                    "github",
                    class_name="text-sm underline hover:cursor-pointer",
                ),
                href="https://github.com/LineIndent",
                is_external=True,
            ),
            class_name="flex flex-row gap-x-1 align-center items-center justify-end w-full",
        ),
        rx.el.label("The Buridan Stack", class_name="text-lg font-bold"),
        rx.el.label(
            "Build, customize, and deploy data-driven applications effortlessly with Buridan's UI components and dashboard builder, built specifically for the Reflex framework.",
            color=rx.color("slate", 11),
            class_name="text-sm font-medium",
        ),
        class_name="flex flex-col w-full max-w-xl gap-y-2",
    )


def hero():
    return rx.el.div(
        # rx.color_mode.button(),
        rx.el.div(
            rx.el.div(welcome_msessage(), class_name="p-4"),
            rx.divider(
                border_bottom=f"1.25px dashed {rx.color('gray', 5)}", bg="transparent"
            ),
            rx.el.div(
                create_block_design("pattern-ui"),
                create_block_link(
                    f"Buridan UI ({VERSION})",
                    " Beautifully designed Reflex components to build your web apps faster. Open source. ",
                    "/getting-started/introduction/",
                ),
                class_name="flex flex-row justify-start gap-x-4 p-4 w-full align-center items-center overflow-hidden",
            ),
            rx.divider(
                border_bottom=f"1.25px dashed {rx.color('gray', 5)}", bg="transparent"
            ),
            rx.el.div(
                create_block_design("pattern-lab"),
                create_block_link(
                    "Buridan Lab (beta)",
                    "Create custom dashboards with flexible layouts and spans, and visualize data through beautiful, interactive charts.",
                    "https://buridan-lab.reflex.run/",
                ),
                class_name="flex flex-row justify-start gap-x-4 p-4 w-full align-center items-center",
            ),
            class_name="flex flex-col w-full max-w-xl justify-start align-center items-center",
        ),
        class_name="w-full h-[100vh] flex flex-col justify-center align-center items-center bg-background",
    )
