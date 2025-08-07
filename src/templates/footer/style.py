from dataclasses import dataclass, field


@dataclass
class FooterStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            # "padding": ["12px 0px" if i >= 5 else "12px 0.75em" for i in range(6)],
        },
    )

    footer_item: dict[str, str] = field(
        default_factory=lambda: {
            "display": "grid",
            "grid_template_columns": [
                f"repeat({i}, minmax(0, 1fr))" for i in [2, 2, 4, 4, 5, 5]
            ],
            "justify": "start",
            "gap": "1rem 3rem",
            "width": "100%",
        },
    )


FooterStyle: FooterStyle = FooterStyle()
