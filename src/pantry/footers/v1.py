from dataclasses import dataclass, field
from typing import Literal, Optional

import reflex as rx

footer_data = {
    "product": [
        {"text": "Pricing", "href": "#"},
        {"text": "Changelog", "href": "#"},
        {"text": "Docs", "href": "#"},
        {"text": "Download", "href": "#"},
    ],
    "company": [
        {"text": "About us", "href": "#"},
        {"text": "Blog", "href": "#"},
        {"text": "Careers", "href": "#", "note": "— We're hiring"},
        {"text": "Customers", "href": "#"},
        {"text": "Newsroom", "href": "#"},
        {"text": "Sitemap", "href": "#"},
    ],
    "resources": [
        {"text": "Community", "href": "#"},
        {"text": "Help & Support", "href": "#"},
        {"text": "eBook", "href": "#"},
        {"text": "What's New", "href": "#"},
        {"text": "Status", "href": "#"},
    ],
    "developers": [
        {"text": "Api", "href": "#"},
        {"text": "Status", "href": "#"},
        {"text": "GitHub", "href": "#", "note": "— New"},
    ],
    "industries": [
        {"text": "Financial Services", "href": "#"},
        {"text": "Education", "href": "#"},
    ],
}

FooterItem = dict[str, str | Optional[str]]


@dataclass
class FooterV1Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "wrap": "wrap",
            "gap": "1em",
            "padding": "1em",
        },
    )

    title: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 12),
            "weight": "bold",
            "size": "2",
        },
    )

    link: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "weight": "medium",
            "size": "2",
        },
    )

    stack: dict[str, str] = field(
        default_factory=lambda: {"min_width": "200px", "padding": "1em 0em"},
    )

    icon: dict[str, str] = field(
        default_factory=lambda: {
            "size": 20,
            "color": rx.color("slate", 10),
            "_hover": {
                "color": rx.color("slate", 12),
                "fill": rx.color("slate", 12),
            },
            "fill": rx.color("slate", 10),
            "cursor": "pointer",
        },
    )


FooterV1Style: FooterV1Style = FooterV1Style()


def styled_text(text_: str, style: dict[str, str]) -> rx.Component:
    return rx.text(text_, **style)


def company(brand: str, copyright_: str) -> rx.Component:
    return rx.vstack(
        styled_text(brand, FooterV1Style.title),
        styled_text(copyright_, FooterV1Style.link),
        **FooterV1Style.stack,
    )


def with_note(link_text: str, note: str) -> rx.Component:
    return rx.hstack(
        link_text,
        rx.text(note, color=rx.color("blue")),
        **FooterV1Style.link,
        width="100%",
    )


def stack(title: str, data: list[FooterItem]) -> rx.Component:
    return rx.vstack(
        rx.text(title, **FooterV1Style.title),
        *[
            (
                with_note(item["text"], item["note"])
                if "note" in item
                else rx.text(item["text"], **FooterV1Style.link)
            )
            for item in data
        ],
        **FooterV1Style.stack,
    )


icons = Literal["github", "twitter", "facebook"]


def icon(name: icons) -> rx.Component:
    return rx.icon(tag=name, **FooterV1Style.icon)


def text(name: str) -> rx.Component:
    return rx.text(name, **FooterV1Style.link)


def footer_v1():
    return rx.hstack(
        company("Brand", "© 2024 Buridan UI."),
        stack("Product", footer_data["product"]),
        stack("Company", footer_data["company"]),
        stack("Resources", footer_data["resources"]),
        stack("Developers", footer_data["developers"]),
        stack("Industries", footer_data["industries"]),
        rx.divider(),
        rx.hstack(
            rx.hstack(text("Terms"), text("Privacy"), text("Status")),
            rx.hstack(icon("github"), icon("twitter"), icon("facebook")),
            width="100%",
            justify="between",
        ),
        **FooterV1Style.base,
    )
