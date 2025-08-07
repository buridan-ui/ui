import reflex as rx

__prompts__ = [
    [
        "Vivamus suscipit tortor eget",
        "Phasellus volutpat metus ac urna egestas, sed consequat quam lacinia.",
    ],
    [
        "Integer malesuada nunc vel",
        "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.",
    ],
    [
        "Nullam quis risus eget urna",
        "Donec ullamcorper nulla non metus auctor fringilla. Vestibulum dapibus nunc ac augue.",
    ],
    [
        "Etiam sit amet orci eget",
        "Cras ultricies ligula sed magna dictum porta. Integer tincidunt nulla in velit.",
    ],
    [
        "Curabitur non nulla sit amet",
        "Quisque velit nisi, pretium ut lacinia in, elementum id enim. Proin eget tortor risus.",
    ],
    [
        "Sed porttitor lectus nibh",
        "Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Curabitur arcu erat, accumsan id imperdiet et.",
    ],
    [
        "Aliquam erat volutpat",
        "Cras ultricies ligula sed magna dictum porta. Nulla quis lorem ut libero malesuada feugiat.",
    ],
    [
        "Quisque velit nisi",
        "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui.",
    ],
    [
        "Mauris blandit aliquet",
        "Nulla porttitor accumsan tincidunt. Nulla quis lorem ut libero malesuada feugiat.",
    ],
    [
        "Pellentesque in ipsum",
        "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.",
    ],
]

border = rx.color_mode_cond(
    f"1px solid {rx.color('indigo', 3)}",
    f"1px solid {rx.color('slate', 7, True)}",
)
background = rx.color_mode_cond(
    rx.color("indigo", 1),
    rx.color("indigo", 3),
)

box_shadow = rx.color_mode_cond("0px 1px 3px rgba(25, 33, 61, 0.1)", "none")


title = rx.hstack(
    rx.text("Prompt Library", size="6", weight="bold"),
    rx.dialog.close(rx.icon(tag="x", size=20, cursor="pointer")),
    width="100%",
    align="center",
    justify="between",
)


def popups_v1():
    return rx.center(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    "Open Dialog",
                    variant="surface",
                    color_scheme="gray",
                    cursor="pointer",
                ),
            ),
            rx.dialog.content(
                title,
                rx.vstack(
                    *[
                        rx.vstack(
                            rx.text(name, color=rx.color("slate", 11)),
                            rx.text(subtitle, color=rx.color("slate", 12)),
                            spacing="1",
                        )
                        for name, subtitle in __prompts__
                    ],
                    height="45vh",
                    overflow="scroll",
                    mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 90%, hsl(0, 0%, 0%, 0) 100%)",
                    padding="12px 0px",
                ),
            ),
        ),
        height="25vh",
    )
