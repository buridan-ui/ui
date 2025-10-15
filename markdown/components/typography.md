

# Typography

Styles for headings, paragraphs, lists, and other text elements using Tailwind utility classes.

# Installation

Copy the following code into your app directory.


```python
import reflex as rx


def typography_h1(*children, class_name: str = "", **props):
    """Large heading - h1"""
    base_classes = "scroll-m-20 text-4xl font-extrabold tracking-tight text-balance"
    return rx.el.h1(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h2(*children, class_name: str = "", **props):
    """Section heading - h2"""
    base_classes = "scroll-m-20 border-b border-input pb-2 text-3xl font-semibold tracking-tight first:mt-0"
    return rx.el.h2(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h3(*children, class_name: str = "", **props):
    """Subsection heading - h3"""
    base_classes = "scroll-m-20 text-2xl font-semibold tracking-tight"
    return rx.el.h3(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h4(*children, class_name: str = "", **props):
    """Small heading - h4"""
    base_classes = "scroll-m-20 text-xl font-semibold tracking-tight"
    return rx.el.h4(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_p(*children, class_name: str = "", **props):
    """Paragraph text"""
    base_classes = "leading-7 [&:not(:first-child)]:mt-6"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_blockquote(*children, class_name: str = "", **props):
    """Blockquote for quotes"""
    base_classes = "mt-6 border-l-2 pl-6 italic"
    return rx.el.blockquote(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_list(*children, class_name: str = "", **props):
    """Unordered list"""
    base_classes = "my-6 ml-6 list-disc [&>li]:mt-2"
    return rx.el.ul(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_inline_code(*children, class_name: str = "", **props):
    """Inline code"""
    base_classes = "bg-[var(--muted)] relative rounded px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold"
    return rx.el.code(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_lead(*children, class_name: str = "", **props):
    """Lead paragraph (larger intro text)"""
    base_classes = "text-[var(--muted-foreground)] text-xl"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_large(*children, class_name: str = "", **props):
    """Large text"""
    base_classes = "text-lg font-semibold"
    return rx.el.div(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_small(*children, class_name: str = "", **props):
    """Small text"""
    base_classes = "text-sm leading-none font-medium"
    return rx.el.small(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_muted(*children, class_name: str = "", **props):
    """Muted text"""
    base_classes = "text-[var(--muted-foreground)] text-sm"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_table(*children, class_name: str = "", **props):
    """Table wrapper with styling"""
    base_classes = "my-6 w-full overflow-y-auto"
    return rx.el.div(
        rx.el.table(
            *children,
            class_name="w-full",
        ),
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def typography_table_header(*children, **props):
    """Table header row"""
    return rx.el.tr(
        *children,
        class_name="even:bg-[var(--muted)] m-0 border-t border-input p-0",
        **props,
    )


def typography_table_head(*children, **props):
    """Table header cell"""
    return rx.el.th(
        *children,
        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
        **props,
    )


def typography_table_row(*children, **props):
    """Table body row"""
    return rx.el.tr(
        *children,
        class_name="even:bg-[var(--muted)] m-0 border-t border-input p-0",
        **props,
    )


def typography_table_cell(*children, **props):
    """Table body cell"""
    return rx.el.td(
        *children,
        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
        **props,
    )
```


# Examples

## All Styles
A showcase of all typography styles in one example.


```python
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
```


## H1
An example of a large primary heading style.


```python
def typography_h1_example():
    """H1 example"""
    return rx.el.div(
        typography_h1("The Legend of Sherwood Forest"),
        class_name="text-center",
    )
```


## H2
A secondary heading with slightly smaller text.


```python
def typography_h2_example():
    """H2 example"""
    return typography_h2("The Outlaw and His Merry Men")
```


## H3
A tertiary heading for subsection titles.


```python
def typography_h3_example():
    """H3 example"""
    return typography_h3("A Robin Hood Tale")
```


## H4
A small heading used for minor sections or labels.


```python
def typography_h4_example():
    """H4 example"""
    return typography_h4("The people rallied to his cause")
```


## Paragraph
A standard paragraph text style for body content.


```python
def typography_p_example():
    """Paragraph example"""
    return typography_p(
        "Robin Hood, seeing the suffering of the common folk, vowed to take from the rich and give to the poor until justice was restored."
    )
```


## Blockquote
A styled blockquote element for quoted text.


```python
def typography_blockquote_example():
    """Blockquote example"""
    return typography_blockquote(
        '"We steal from the rich and give to the needy," he declared, "for no law is just when it starves the innocent."'
    )
```


## List
A demonstration of styled ordered and unordered lists.


```python
def typography_list_example():
    """List example"""
    return typography_list(
        rx.el.li("Little John: The mighty quarterstaff warrior"),
        rx.el.li("Friar Tuck: The jovial man of God"),
        rx.el.li("Maid Marian: The fearless noblewoman"),
    )
```


## Inline Code
Inline code styling for short snippets within text.


```python
def typography_inline_code_example():
    """Inline code example"""
    return typography_inline_code("@buridan-ui/ui")
```


## Lead
A larger, attention-grabbing paragraph for introductions.


```python
def typography_lead_example():
    """Lead paragraph example"""
    return typography_lead(
        "A legendary tale of heroism and justice, where one man stood against tyranny to defend the oppressed."
    )
```


## Large
An example of text with a slightly larger font size.


```python
def typography_large_example():
    """Large text example"""
    return typography_large("Will you join our band?")
```


## Small
A smaller, subdued text style for fine print or notes.


```python
def typography_small_example():
    """Small text example"""
    return typography_small("Sherwood Forest, England")
```


## Muted
A muted text style with reduced contrast for secondary information.


```python
def typography_muted_example():
    """Muted text example"""
    return typography_muted("In the reign of King Richard.")
```

