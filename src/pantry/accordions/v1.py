import reflex as rx

items1 = [
    "01. Genesis launched a new era of exploration.",
    "02. Explorer uncovered new planets beyond our reach.",
    "03. Voyager 1 ventured into interstellar space.",
    "04. Apollo landed humans on the Moon.",
]

items2 = [
    "05. Curiosity sent back valuable data from Mars.",
    "06. The Hubble Telescope captured distant galaxies.",
    "07. James Webb will explore the universe's origins.",
    "08. The ISS orbits Earth, conducting critical experiments.",
]

items3 = [
    "09. Saturn's rings have fascinated scientists for years.",
    "10. The Mars Rover is studying the planet's surface.",
    "11. NASA's Artemis program aims to return humans to the Moon.",
    "12. Solar missions help us understand space weather.",
]


def create_accordion_item(title, items):
    return rx.accordion.item(
        rx.accordion.header(
            rx.accordion.trigger(
                rx.text(title, size="1", weight="medium"),
                rx.accordion.icon(size=14),
                padding="0.5em 0.1em",
                color=rx.color("slate", 12),
                _hover={"bg": "none"},
            ),
        ),
        rx.accordion.content(
            rx.vstack(
                rx.foreach(
                    items,
                    lambda item: rx.text(item, size="1", color=rx.color("slate", 11)),
                ),
                spacing="2",
                color=rx.color("slate", 12),
            ),
            padding="0em 0.1em",
        ),
        border_bottom=f"0.81px solid {rx.color('gray', 5)}",
    )


def accordion_v1():
    return rx.box(
        rx.accordion.root(
            create_accordion_item("Models", items1),
            create_accordion_item("Spacecraft", items2),
            create_accordion_item("Space Discoveries", items3),
            border_bottom=f"0.81px solid {rx.color('gray', 5)}",
            collapsible=True,
            width="100%",
            max_width="28em",
            variant="ghost",
            color_scheme="gray",
            border_radius="0",
            gap="0",
            easing="ease-out",
        ),
        width="100%",
        height="40vh",
        display="flex",
        justify_content="center",
        align_items="center",
    )
