

# Badge

Displays a badge or a component that looks like a badge.

# Installation

Copy the following code into your app directory.


```python
"""Badge component."""

from typing import Literal

from reflex.components.el import Span
from reflex.vars.base import Var

from ..component import CoreComponent

BaseColorType = Literal[
    "primary",
    "secondary",
    "info",
    "success",
    "warning",
    "destructive",
    "gray",
    "mauve",
    "slate",
    "sage",
    "olive",
    "sand",
    "tomato",
    "red",
    "ruby",
    "crimson",
    "pink",
    "plum",
    "purple",
    "violet",
    "iris",
    "indigo",
    "blue",
    "cyan",
    "teal",
    "jade",
    "green",
    "grass",
    "brown",
    "orange",
    "sky",
    "mint",
    "lime",
    "yellow",
    "amber",
    "gold",
    "bronze",
]
LiteralBadgeVariant = Literal["solid", "soft"]
LiteralBadgeSize = Literal["xs", "sm", "md"]

DEFAULT_BASE_CLASSES = "inline-flex items-center font-medium [&_svg]:pointer-events-none [&_svg]:shrink-0 gap-1.5"

# Light colors that need dark text on solid backgrounds for better contrast
LIGHT_COLORS = {"sky", "mint", "lime", "yellow", "amber", "secondary"}

BADGE_VARIANTS = {
    "size": {
        "xs": "px-1.5 py-0.5 h-4 rounded-ui-xss text-[11px] [&_svg]:size-3",
        "sm": "px-1.5 py-0.5 h-5 rounded-ui-xs text-xs [&_svg]:size-3.5",
        "md": "px-2 py-0.5 h-6 rounded-ui-sm text-sm [&_svg]:size-4",
    }
}


def get_color_classes(color: str, variant: LiteralBadgeVariant) -> str:
    """Get the color-specific classes based on color and variant."""
    if variant == "solid":
        text_color = "text-black/90" if color in LIGHT_COLORS else "text-white"
        return f"border-transparent bg-{color}-9 {text_color}"
    # Soft variant
    return f"border-transparent bg-{color}-3 text-{color}-11"


def get_badge_classes(
    color: str, variant: LiteralBadgeVariant, size: LiteralBadgeSize
) -> str:
    """Get the complete badge class string."""
    color_classes = get_color_classes(color, variant)
    size_classes = BADGE_VARIANTS["size"][size]

    return f"{DEFAULT_BASE_CLASSES} {size_classes} {color_classes}"


class Badge(Span, CoreComponent):
    """A badge component that displays a label."""

    # Badge color
    color: BaseColorType | Var[str]

    # Badge variant
    variant: Var[LiteralBadgeVariant]

    # Badge size
    size: Var[LiteralBadgeSize]

    @classmethod
    def create(cls, *children, **props) -> Span:
        """Create the badge component."""
        variant = props.pop("variant", "solid")
        color = props.pop("color", "primary")
        size = props.pop("size", "sm")

        cls.set_class_name(get_badge_classes(color, variant, size), props)

        return super().create(*children, **props)

    def _exclude_props(self) -> list[str]:
        return [*super()._exclude_props(), "color", "variant", "size"]


badge = Badge.create
```


# Examples

## Default

Displays a standard badge using the default variant, ideal for basic labeling.


```python
def badge_demo():
    return rx.box(
        rx.box(
            badge("Badge"),
            badge("Secondary", variant="secondary"),
            badge("Destructive", variant="destructive"),
            badge("Outline", variant="outline"),
            class_name="flex w-full flex-wrap gap-2",
        ),
        rx.box(
            badge(
                rx.icon(tag="badge-check"),
                "Verified",
                variant="secondary",
                class_name="bg-blue-500 text-white dark:bg-blue-600",
            ),
            badge(
                "8",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "99",
                variant="destructive",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "20+",
                variant="outline",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            class_name="flex w-full flex-wrap gap-2",
        ),
        class_name="flex flex-col items-center gap-2 p-8",
    )
```


## With Icons

Demonstrates how to include icons inside badges for visual context or emphasis.


```python
def badge_with_icons():
    return rx.box(
        badge(
            rx.icon(tag="check"),
            "Success",
            variant="secondary",
            class_name="bg-green-500 text-white dark:bg-green-600",
        ),
        badge(
            rx.icon(tag="x"),
            "Error",
            variant="destructive",
        ),
        badge(
            rx.icon(tag="triangle-alert"),
            "Warning",
            variant="secondary",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        badge(
            rx.icon(tag="info"),
            "Info",
            variant="secondary",
            class_name="bg-blue-500 text-white dark:bg-blue-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )
```


## Status

Showcases how badges can represent different statuses, like success or error, using color.


```python
def badge_status_examples():
    return rx.box(
        badge("New", variant="default"),
        badge("Popular", variant="secondary"),
        badge("Sale", variant="destructive"),
        badge("Draft", variant="outline"),
        badge(
            rx.icon(tag="star"),
            "Featured",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )
```


## Notification Count

Illustrates how to use badges for showing counts, such as unread notifications or messages.


```python
def badge_notification_count():
    return rx.box(
        badge(
            "1",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "5",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "10",
            variant="secondary",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "99+",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        class_name="flex items-center gap-2 p-8",
    )
```

