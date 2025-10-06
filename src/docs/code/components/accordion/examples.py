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


def accordion_example():
    trigger_class = "py-2 px-1 hover:bg-transparent"
    trigger_text_class = "text-sm font-medium"
    icon_class = "w-3.5 h-3.5 transition-transform duration-200"
    content_padding_class = "py-0 px-1"
    content_vstack_class = "flex flex-col space-y-2"
    item_border_class = "border-b border-[var(--input)] last:border-b-0"

    return rx.el.div(
        rx.accordion.root(
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.el.p("Models", class_name=trigger_text_class),
                        rx.accordion.icon(class_name=icon_class),
                        class_name=trigger_class,
                    )
                ),
                rx.accordion.content(
                    rx.el.div(
                        rx.foreach(items1, lambda i: rx.el.p(i, class_name="text-sm")),
                        class_name=content_vstack_class,
                    ),
                    class_name=content_padding_class,
                ),
                class_name=item_border_class,
            ),
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.el.p("Spacecraft", class_name=trigger_text_class),
                        rx.accordion.icon(class_name=icon_class),
                        class_name=trigger_class,
                    )
                ),
                rx.accordion.content(
                    rx.el.div(
                        rx.foreach(items2, lambda i: rx.el.p(i, class_name="text-sm")),
                        class_name=content_vstack_class,
                    ),
                    class_name=content_padding_class,
                ),
                class_name=item_border_class,
            ),
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.el.p("Space Discoveries", class_name=trigger_text_class),
                        rx.accordion.icon(class_name=icon_class),
                        class_name=trigger_class,
                    )
                ),
                rx.accordion.content(
                    rx.el.div(
                        rx.foreach(items3, lambda i: rx.el.p(i, class_name="text-sm")),
                        class_name=content_vstack_class,
                    ),
                    class_name=content_padding_class,
                ),
                class_name=item_border_class,
            ),
            collapsible=True,
            class_name="w-full max-w-[28em] rounded-none gap-0 ease-out",
            variant="ghost",
            color_scheme="gray",
        ),
        class_name="w-full h-[40vh] flex justify-center items-center",
    )
