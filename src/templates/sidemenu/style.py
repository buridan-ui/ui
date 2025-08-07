from dataclasses import dataclass, field

import reflex as rx


@dataclass
class SideMenuStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "bottom": "0",
            "width": "330px",
            "height": "100vh",
            "overflow": "auto",
            "position": "sticky",
            "padding": "80px 1em 80px 1.5em",
            "scrollbar_width": "none",
            "background": rx.color("gray", 2),
            "display": ["none" if i <= 3 else "flex" for i in range(6)],
            "mask": "linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 92%, hsl(0, 0%, 0%, 0) 100%)",
            "border_right": f"1px solid {rx.color('gray', 4)}",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "position": "relative",
            "spacing": "5",
        },
    )


SideMenuStyle: SideMenuStyle = SideMenuStyle()
