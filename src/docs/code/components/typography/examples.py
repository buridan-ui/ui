import reflex as rx
from .typography import (
    typography_h1,
    typography_h2,
    typography_h3,
    typography_h4,
    typography_p,
    typography_blockquote,
    typography_list,
    typography_inline_code,
    typography_lead,
    typography_large,
    typography_small,
    typography_muted,
    typography_table,
    typography_table_header,
    typography_table_head,
    typography_table_row,
    typography_table_cell,
)


def typography_h1_example():
    """H1 example"""
    return rx.el.div(
        typography_h1("Taxing Laughter: The Joke Tax Chronicles"),
        class_name="text-center",
    )


def typography_h2_example():
    """H2 example"""
    return typography_h2("The People of the Kingdom")


def typography_h3_example():
    """H3 example"""
    return typography_h3("The Joke Tax")


def typography_h4_example():
    """H4 example"""
    return typography_h4("People stopped telling jokes")


def typography_p_example():
    """Paragraph example"""
    return typography_p(
        "The king, seeing how much happier his subjects were, realized the error of his ways and repealed the joke tax."
    )


def typography_blockquote_example():
    """Blockquote example"""
    return typography_blockquote(
        '"After all," he said, "everyone enjoys a good joke, so it\'s only fair that they should pay for the privilege."'
    )


def typography_list_example():
    """List example"""
    return typography_list(
        rx.el.li("1st level of puns: 5 gold coins"),
        rx.el.li("2nd level of jokes: 10 gold coins"),
        rx.el.li("3rd level of one-liners: 20 gold coins"),
    )


def typography_inline_code_example():
    """Inline code example"""
    return typography_inline_code("@radix-ui/react-alert-dialog")


def typography_lead_example():
    """Lead paragraph example"""
    return typography_lead(
        "A modal dialog that interrupts the user with important content and expects a response."
    )


def typography_large_example():
    """Large text example"""
    return typography_large("Are you absolutely sure?")


def typography_small_example():
    """Small text example"""
    return typography_small("Email address")


def typography_muted_example():
    """Muted text example"""
    return typography_muted("Enter your email address.")


def typography_table_example():
    """Table example"""
    return typography_table(
        rx.el.thead(
            typography_table_header(
                typography_table_head("King's Treasury"),
                typography_table_head("People's happiness"),
            ),
        ),
        rx.el.tbody(
            typography_table_row(
                typography_table_cell("Empty"),
                typography_table_cell("Overflowing"),
            ),
            typography_table_row(
                typography_table_cell("Modest"),
                typography_table_cell("Satisfied"),
            ),
            typography_table_row(
                typography_table_cell("Full"),
                typography_table_cell("Ecstatic"),
            ),
        ),
    )


# Complete demo example


def typography_demo():
    """Complete typography demo matching shadcn example"""
    return rx.box(
        typography_h1("Taxing Laughter: The Joke Tax Chronicles"),
        typography_p(
            "Once upon a time, in a far-off land, there was a very lazy king who spent all day lounging on his throne. One day, his advisors came to him with a problem: the kingdom was running out of money.",
            class_name="text-[var(--muted-foreground)] text-xl leading-7",
        ),
        typography_h2("The King's Plan", class_name="mt-10"),
        typography_p(
            "The king thought long and hard, and finally came up with ",
            rx.link(
                "a brilliant plan",
                href="#",
                class_name="text-[var(--primary)] font-medium underline underline-offset-4",
            ),
            ": he would tax the jokes in the kingdom.",
        ),
        typography_blockquote(
            '"After all," he said, "everyone enjoys a good joke, so it\'s only fair that they should pay for the privilege."'
        ),
        typography_h3("The Joke Tax", class_name="mt-8"),
        typography_p(
            "The king's subjects were not amused. They grumbled and complained, but the king was firm:"
        ),
        typography_list(
            rx.el.li("1st level of puns: 5 gold coins"),
            rx.el.li("2nd level of jokes: 10 gold coins"),
            rx.el.li("3rd level of one-liners: 20 gold coins"),
        ),
        typography_p(
            "As a result, people stopped telling jokes, and the kingdom fell into a gloom. But there was one person who refused to let the king's foolishness get him down: a court jester named Jokester."
        ),
        typography_h3("Jokester's Revolt", class_name="mt-8"),
        typography_p(
            "Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even in the royal toilet. The king was furious, but he couldn't seem to stop Jokester."
        ),
        typography_h3("The People's Rebellion", class_name="mt-8"),
        typography_p(
            "The people of the kingdom, feeling uplifted by the laughter, started to tell jokes and puns again, and soon the entire kingdom was in on the joke."
        ),
        typography_table(
            rx.el.thead(
                typography_table_header(
                    typography_table_head("King's Treasury"),
                    typography_table_head("People's happiness"),
                ),
            ),
            rx.el.tbody(
                typography_table_row(
                    typography_table_cell("Empty"),
                    typography_table_cell("Overflowing"),
                ),
                typography_table_row(
                    typography_table_cell("Modest"),
                    typography_table_cell("Satisfied"),
                ),
                typography_table_row(
                    typography_table_cell("Full"),
                    typography_table_cell("Ecstatic"),
                ),
            ),
        ),
        typography_p(
            "The king, seeing how much happier his subjects were, realized the error of his ways and repealed the joke tax. Jokester was declared a hero, and the kingdom lived happily ever after."
        ),
        typography_p(
            "The moral of the story is: never underestimate the power of a good laugh and always be careful of bad ideas."
        ),
        class_name="p-8 max-w-3xl",
    )
