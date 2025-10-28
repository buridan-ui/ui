import reflex as rx
from ...base_ui.components.base.accordion import accordion


def accordion_example():
    """Accordion with space exploration data - only one section open at a time."""

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

    return accordion.root(
        accordion.item(
            accordion.header(
                accordion.trigger(
                    "Models",
                    # icon("PlusSignIcon", class_name="size-4 shrink-0 transition-all ease-out group-data-[panel-open]:scale-110 group-data-[panel-open]:rotate-45"),
                ),
            ),
            accordion.panel(
                rx.box(
                    *[rx.text(item, class_name="mb-2") for item in items1],
                    class_name="py-2 px-4",
                ),
            ),
            value="section-1",
        ),
        accordion.item(
            accordion.header(
                accordion.trigger(
                    "Spacecraft",
                    # icon("PlusSignIcon", class_name="size-4 shrink-0 transition-all ease-out group-data-[panel-open]:scale-110 group-data-[panel-open]:rotate-45"),
                ),
            ),
            accordion.panel(
                rx.box(
                    *[rx.text(item, class_name="mb-2") for item in items2],
                    class_name="py-2 px-4",
                ),
            ),
            value="section-2",
        ),
        accordion.item(
            accordion.header(
                accordion.trigger(
                    "Space Discoveries",
                    # icon("PlusSignIcon", class_name="size-4 shrink-0 transition-all ease-out group-data-[panel-open]:scale-110 group-data-[panel-open]:rotate-45"),
                ),
            ),
            accordion.panel(
                rx.box(
                    *[rx.text(item, class_name="mb-2") for item in items3],
                    class_name="py-2 px-4",
                ),
            ),
            value="section-3",
        ),
        class_name="w-full max-w-md mx-auto",
        open_multiple=False,
        default_value=[],
    )
