import reflex as rx


def capitalize_words(segment: str) -> str:
    return " ".join(word.lower() for word in segment.replace("-", " ").split())


def base_content_path_ui(route: str) -> rx.hstack:
    segments = route.strip("/").split("/")
    path_names = [
        item for segment in segments[:-1] for item in [capitalize_words(segment), "›"]
    ] + [capitalize_words(segments[-1])]

    return rx.hstack(
        rx.el.label(
            "ui", class_name="text-sm font-medium", color=rx.color("slate", 11)
        ),
        rx.el.label("›", class_name="text-sm font-medium", color=rx.color("slate", 11)),
        *[
            (
                rx.el.label(
                    name, class_name="text-sm font-medium", color=rx.color("slate", 11)
                )
                if index != len(path_names) - 1
                else rx.el.label(
                    name,
                    class_name="text-sm font-medium",
                )
            )
            for index, name in enumerate(path_names)
        ],
        spacing="1",
    )
