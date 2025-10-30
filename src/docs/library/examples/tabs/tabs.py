import reflex as rx
from ...base_ui.components.base.tabs import tabs


def tabs_example():
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab(
                "Overview",
                value="overview",
            ),
            tabs.tab(
                "Projects",
                value="projects",
            ),
            tabs.tab(
                "Account",
                value="account",
            ),
            class_name="relative z-0 flex gap-1 px-1 rounded-none border-b border-input",
        ),
        tabs.panel(
            rx.el.div(
                rx.el.p("Overview Content"),
                class_name="relative flex h-32 items-center justify-center",
            ),
            value="overview",
            class_name="relative flex h-32 items-center justify-center -outline-offset-1 outline-blue-800 focus-visible:rounded-md focus-visible:outline focus-visible:outline-2",
        ),
        tabs.panel(
            rx.el.div(
                rx.el.p("Projects Content"),
                class_name="relative flex h-32 items-center justify-center",
            ),
            value="projects",
            class_name="relative flex h-32 items-center justify-center -outline-offset-1 outline-blue-800 focus-visible:rounded-md focus-visible:outline focus-visible:outline-2",
        ),
        tabs.panel(
            rx.el.div(
                rx.el.p("Account Content"),
                class_name="relative flex h-32 items-center justify-center",
            ),
            value="account",
            class_name="relative flex h-32 items-center justify-center -outline-offset-1 outline-blue-800 focus-visible:rounded-md focus-visible:outline focus-visible:outline-2",
        ),
        default_value="overview",
        class_name="rounded-md border border-input",
    )
