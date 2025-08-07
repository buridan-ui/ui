from dataclasses import dataclass, field

import reflex as rx
from reflex.constants.colors import Color

from src.pantry.footers.v1 import FooterV1Style

active: Color = rx.color("slate", 12)
passive: Color = rx.color("slate", 10)


@dataclass
class FooterV2Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "20vh",
            "align": "center",
            "justify": "center",
            "padding": "0em 1em",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "35em",
            "justify": "between",
            "align": "center",
            "padding": "1em 0em",
        },
    )

    link: dict[str, str] = field(
        default_factory=lambda: {"color": passive, "size": "2"},
    )

    brand: dict[str, str] = field(
        default_factory=lambda: {"color": active, "size": "2"},
    )


FooterV2Style: FooterV2Style = FooterV2Style()


def media(name: str) -> rx.Component:
    return rx.link(rx.text(name, **FooterV1Style.link), href="#")


def footer_v2() -> rx.vstack:
    return rx.vstack(
        rx.divider(max_width="35em", color=rx.color("slate", 11)),
        rx.hstack(
            rx.text("© 2024 Buridan UI", **FooterV2Style.brand),
            rx.hstack(media("Twitter"), media("Dribble"), media("GitHub")),
            **FooterV2Style.content,
        ),
        **FooterV2Style.base,
    )
