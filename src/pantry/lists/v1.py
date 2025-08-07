import reflex as rx

design = ["Figma", "Sketch"]
development = ["HTML", "CSS", "Tailwind CSS", "React", "Vue"]
collaboration = ["Mailchimp", "Slack", "Notion"]
expertise = [
    "UI/UX Design",
    "Design Systems",
    "Custom Illustrations",
    "Responsive Design",
]
skills = [
    "Strong communication",
    "Problem-solving",
    "Attention to detail",
    "Time management",
]


def create_list_item(title: str, items: list[str]):
    return rx.hstack(
        rx.text(title, weight="medium", color=rx.color("slate", 11), size="1"),
        rx.hstack(
            *[
                rx.text(item, weight="bold", color=rx.color("slate", 12), size="1")
                for item in items
            ],
            justify="start",
            wrap="wrap",
            spacing="2",
            width="100%",
            max_width="20em",
        ),
        justify="between",
        wrap="wrap",
        width="100%",
        max_width="30em",
        spacing="2",
    )


def lists_v1():
    return rx.vstack(
        create_list_item("Design Tools:", design),
        create_list_item("Development:", development),
        create_list_item("Collaboration:", collaboration),
        create_list_item("Design Expertise:", expertise),
        create_list_item("Soft Skills:", skills),
        width="100%",
        align="center",
        justify="center",
    )
