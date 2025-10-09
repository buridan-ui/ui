import reflex as rx


def changelog_meta(tag: str, text: str):
    return rx.box(
        (
            rx.icon(tag=tag, size=14, color=rx.color("slate", 11))
            if text
            else rx.box(class_name="hidden")
        ),
        rx.text(text, class_name="text-sm font-semibold"),
        class_name="flex flex-row gap-x-2 items-center",
    )


def changelog_wrapper(title: str, date: str, version: str, log: str):
    return rx.box(
        rx.box(
            rx.box(
                changelog_meta("calendar-range", date),
                changelog_meta("git-compare", version),
                class_name="flex flex-row gap-x-4 items-center",
            ),
            rx.text(title, class_name="text-2xl font-semibold"),
            class_name="flex flex-col gap-y-2",
        ),
        rx.markdown(
            log,
            component_map={
                "ul": lambda *children: rx.list(*children, class_name="py-3"),
                "li": lambda text: rx.list_item(
                    rx.el.span("•", class_name="text-[12px]"),
                    rx.text(f"{text}", class_name="text-[12px]"),
                    class_name="flex flex-row items-center gap-x-4 py-1",
                ),
            },
        ),
        border=f"1px dashed {rx.color('gray', 5)}",
        class_name="rounded-xl p-4",
    )
