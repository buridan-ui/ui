

# Card

A card component that displays content in a card format.

# Installation

Copy the following code into your app directory.


### CLI

```bash
buridan add component card
```

### Manual Installation

```python
"""Custom card component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.components.el import Div
from reflex.vars.base import Var

from ..component import CoreComponent


class ClassNames:
    """Class names for the card component."""

    ROOT = "rounded-default border border-input bg-secondary"
    HEADER = "flex flex-col gap-2 p-4"
    TITLE = "text-2xl font-semibold text-secondary-foreground"
    DESCRIPTION = "text-sm text-secondary-foreground/80 font-[450]"
    CONTENT = "flex flex-col gap-4 px-4 pb-4"
    FOOTER = "flex flex-row justify-between items-center px-4 pb-4"


class CardComponent(Div, CoreComponent):
    """Base component for the card component."""


class CardRoot(CardComponent):
    """A card component that displays content in a card format."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card component."""
        props["data-slot"] = "card"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CardHeader(CardComponent):
    """A header component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card header component."""
        props["data-slot"] = "card-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class CardTitle(CardComponent):
    """A title component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card title component."""
        props["data-slot"] = "card-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class CardDescription(CardComponent):
    """A description component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card description component."""
        props["data-slot"] = "card-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class CardContent(CardComponent):
    """A content component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card content component."""
        props["data-slot"] = "card-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class CardFooter(CardComponent):
    """A footer component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card footer component."""
        props["data-slot"] = "card-footer"
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class HighLevelCard(CardComponent):
    """A high level card component that displays content in a card format."""

    # Card props
    title: Var[str | Component | None]
    description: Var[str | Component | None]
    content: Var[str | Component | None]
    footer: Var[str | Component | None]

    @classmethod
    def create(cls, *children, **props):
        """Create the card component."""
        title = props.pop("title", "")
        description = props.pop("description", "")
        content = props.pop("content", "")
        footer = props.pop("footer", "")

        return CardRoot.create(
            (
                CardHeader.create(
                    CardTitle.create(title) if title is not None else None,
                    (
                        CardDescription.create(description)
                        if description is not None
                        else None
                    ),
                )
                if title or description
                else None
            ),
            CardContent.create(content) if content is not None else None,
            CardFooter.create(footer) if footer is not None else None,
            *children,
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "title",
            "description",
            "content",
            "footer",
        ]


class Card(ComponentNamespace):
    """A card component that displays content in a card format."""

    root = staticmethod(CardRoot.create)
    header = staticmethod(CardHeader.create)
    title = staticmethod(CardTitle.create)
    description = staticmethod(CardDescription.create)
    content = staticmethod(CardContent.create)
    footer = staticmethod(CardFooter.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelCard.create)


card = Card()
```


# Usage

Make sure to correctly set your imports relative to the component.

```python
from components.base_ui.card import card
```


# Examples

Below are examples demonstrating how the component can be used.

## String

Displays a basic avatar with either a user image or a fallback placeholder.


```python
def card_low_level():
    return rx.el.div(
        card.root(
            card.header(
                rx.el.div(
                    rx.el.p("Card Title", class_name="text-md"), class_name="w-full p-4"
                ),
            ),
            card.content(
                rx.el.div(
                    rx.el.p("Card Content", class_name="text-md"),
                    class_name="w-full p-4",
                ),
            ),
            card.footer(
                rx.el.div(
                    rx.el.p("Card Footer", class_name="text-md"),
                    class_name="w-full p-4",
                ),
            ),
            class_name="w-full max-w-[35em]",
        ),
        class_name="py-8 w-full max-w-[35em]",
    )
```

