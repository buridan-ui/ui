import reflex as rx
from ...base_ui.components.base.typography import (
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
        typography_h1("The Legend of Sherwood Forest"),
        class_name="text-center",
    )


def typography_h2_example():
    """H2 example"""
    return typography_h2("The Outlaw and His Merry Men")


def typography_h3_example():
    """H3 example"""
    return typography_h3("A Robin Hood Tale")


def typography_h4_example():
    """H4 example"""
    return typography_h4("The people rallied to his cause")


def typography_p_example():
    """Paragraph example"""
    return typography_p(
        "Robin Hood, seeing the suffering of the common folk, vowed to take from the rich and give to the poor until justice was restored."
    )


def typography_blockquote_example():
    """Blockquote example"""
    return typography_blockquote(
        '"We steal from the rich and give to the needy," he declared, "for no law is just when it starves the innocent."'
    )


def typography_list_example():
    """List example"""
    return typography_list(
        rx.el.li("Little John: The mighty quarterstaff warrior"),
        rx.el.li("Friar Tuck: The jovial man of God"),
        rx.el.li("Maid Marian: The fearless noblewoman"),
    )


def typography_inline_code_example():
    """Inline code example"""
    return typography_inline_code("@buridan-ui/ui")


def typography_lead_example():
    """Lead paragraph example"""
    return typography_lead(
        "A legendary tale of heroism and justice, where one man stood against tyranny to defend the oppressed."
    )


def typography_large_example():
    """Large text example"""
    return typography_large("Will you join our band?")


def typography_small_example():
    """Small text example"""
    return typography_small("Sherwood Forest, England")


def typography_muted_example():
    """Muted text example"""
    return typography_muted("In the reign of King Richard.")


def typography_table_example():
    """Table example"""
    return typography_table(
        rx.el.thead(
            typography_table_header(
                typography_table_head("Sheriff's Treasury"),
                typography_table_head("Common Folk's Wellbeing"),
            ),
        ),
        rx.el.tbody(
            typography_table_row(
                typography_table_cell("Overflowing"),
                typography_table_cell("Starving"),
            ),
            typography_table_row(
                typography_table_cell("Modest"),
                typography_table_cell("Surviving"),
            ),
            typography_table_row(
                typography_table_cell("Empty"),
                typography_table_cell("Thriving"),
            ),
        ),
    )


# Complete demo example


def typography_demo():
    """Complete typography demo with Robin Hood theme"""
    return rx.box(
        typography_h1("The Legend of Sherwood Forest"),
        typography_p(
            "In the days of old England, when King Richard was away at the Crusades, a corrupt Sheriff ruled Nottingham with an iron fist. The poor were taxed beyond measure, while nobles lived in luxury.",
            class_name="text-[var(--muted-foreground)] text-xl leading-7",
        ),
        typography_h2("The Outlaw Emerges", class_name="mt-10"),
        typography_p(
            "One man refused to bow to tyranny. Robin of Locksley, stripped of his lands and title, fled to ",
            rx.link(
                "Sherwood Forest",
                href="#",
                class_name="text-[var(--primary)] font-medium underline underline-offset-4",
            ),
            " where he gathered a band of outlaws dedicated to justice.",
        ),
        typography_blockquote(
            '"We steal from the rich and give to the needy," he declared, "for no law is just when it starves the innocent."'
        ),
        typography_h3("The Merry Men", class_name="mt-8"),
        typography_p(
            "Robin's band grew, attracting the bravest and most skilled fighters in the realm:"
        ),
        typography_list(
            rx.el.li("Little John: The mighty quarterstaff warrior"),
            rx.el.li("Friar Tuck: The jovial man of God"),
            rx.el.li("Maid Marian: The fearless noblewoman"),
        ),
        typography_p(
            "Together, they became legends, robbing tax collectors and corrupt nobles, always staying one step ahead of the Sheriff's men."
        ),
        typography_h3("The Sheriff's Fury", class_name="mt-8"),
        typography_p(
            "The Sheriff of Nottingham grew desperate. Every convoy he sent through Sherwood was ambushed, every cruel tax returned to the poor. His reputation crumbled while Robin's legend grew."
        ),
        typography_h3("The Great Archery Contest", class_name="mt-8"),
        typography_p(
            "In a cunning trap, the Sheriff announced an archery contest with a golden arrow as prize. Robin couldn't resist the challenge."
        ),
        typography_table(
            rx.el.thead(
                typography_table_header(
                    typography_table_head("Sheriff's Treasury"),
                    typography_table_head("Common Folk's Wellbeing"),
                ),
            ),
            rx.el.tbody(
                typography_table_row(
                    typography_table_cell("Overflowing"),
                    typography_table_cell("Starving"),
                ),
                typography_table_row(
                    typography_table_cell("Modest"),
                    typography_table_cell("Surviving"),
                ),
                typography_table_row(
                    typography_table_cell("Empty"),
                    typography_table_cell("Thriving"),
                ),
            ),
        ),
        typography_p(
            "Though disguised, Robin's skill gave him away. But with the help of his Merry Men and the cheering crowd, he escaped. When King Richard returned, he pardoned Robin and restored his lands."
        ),
        typography_p(
            "The legend reminds us: when laws serve only the powerful, it falls to the brave to stand for what is right."
        ),
        class_name="p-8 max-w-3xl",
    )
