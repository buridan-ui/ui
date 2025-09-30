import reflex as rx

from reflex.experimental import ClientStateVar
from src.static.routes import GettingStartedRoutes, ChartRoutes, PantryRoutes

COMPONENTS_DATA = GettingStartedRoutes + ChartRoutes + PantryRoutes

SearchInput = ClientStateVar.create("search_input", "")

GettingStartedData = ClientStateVar.create("getting_started_data", GettingStartedRoutes)
ChartData = ClientStateVar.create("chart_data", ChartRoutes)
PantryData = ClientStateVar.create("pantry_data", PantryRoutes)
SearchData = ClientStateVar.create("search_data", COMPONENTS_DATA)


def keyboard_shortcut_script():
    """Add keyboard shortcut support with MutationObserver for better page navigation handling."""
    return rx.call_script("""
        // Global flag to prevent multiple initializations
        if (!window.cmdKShortcutInitialized) {
            window.cmdKShortcutInitialized = true;

            function handleCmdKShortcut(e) {
                if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                    e.preventDefault();
                    e.stopPropagation();

                    const trigger = document.getElementById('search-trigger');
                    if (trigger) {
                        // Force a real click event
                        const event = new MouseEvent('click', {
                            view: window,
                            bubbles: true,
                            cancelable: true
                        });
                        trigger.dispatchEvent(event);
                    }
                }
            }

            // Set up global event listener
            document.addEventListener('keydown', handleCmdKShortcut);

            // Watch for DOM changes (page navigation)
            const observer = new MutationObserver(() => {
                // Ensure the event listener is still active after DOM changes
                document.removeEventListener('keydown', handleCmdKShortcut);
                document.addEventListener('keydown', handleCmdKShortcut);
            });

            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    """)


def search_trigger():
    return rx.box(
        rx.box(
            rx.box(
                rx.el.label(
                    "⌘",
                    class_name="w-5 text-center rounded-md",
                    style={
                        "border": f"1.25px dashed {rx.color('gray', 5)}",
                    },
                ),
                rx.el.label(
                    "k",
                    class_name="w-5 text-center rounded-md",
                    style={
                        "border": f"1.25px dashed {rx.color('gray', 5)}",
                    },
                ),
                class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-xs font-bold flex gap-x-1",
            ),
            rx.el.input(
                placeholder="Search documentation",
                read_only=True,
                class_name="p-2 w-full placeholder:text-sm "
                + "text-sm "
                + "rounded-md bg-transparent "
                + "focus:outline-none focus:border-none cursor-pointer",
            ),
            _hover={"color": rx.color("slate", 12), "background": rx.color("gray", 3)},
            border=f"1px solid {rx.color('gray', 5)}",
            class_name=(
                "relative focus:outline-none inline-flex items-center justify-center gap-x-2 rounded-lg text-sm font-semibold "
                "cursor-pointer h-[1.925rem] w-full cursor-pointer"
            ),
        ),
    )


def search_breadcrumb(items):
    """Create a breadcrumb navigation component."""
    breadcrumb_items = []
    for i, item in enumerate(items):
        if i > 0:
            breadcrumb_items.append(
                rx.el.label(
                    "›", class_name="text-sm font-medium", color=rx.color("slate", 11)
                )
            )

        color = rx.color("slate", 12) if i == len(items) - 1 else rx.color("slate", 11)
        weight = "font-medium" if i == len(items) - 1 else "font-regular"

        breadcrumb_items.append(
            rx.el.label(
                item,
                class_name=f"text-sm {weight}",
                color=color,
            )
        )

    return rx.hstack(*breadcrumb_items, spacing="1", cursor="pointer")


def search_result(tags: list, value: dict):
    return rx.link(
        rx.box(
            rx.text(value["name"], class_name="text-sm font-bold"),
            rx.text(
                value["description"], class_name="text-sm font-regular opacity-[0.81]"
            ),
            search_breadcrumb(tags),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=value["path"],
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md",
        _hover={"bg": rx.color("gray", 2)},
    )


def search_result_start(value: dict):
    return rx.link(
        rx.box(
            rx.text(value["name"], class_name="text-sm font-bold"),
            rx.text(
                value["description"], class_name="text-sm font-regular opacity-[0.81]"
            ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=value["path"],
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md",
        _hover={"bg": rx.color("gray", 2)},
    )


def search_input():
    return rx.box(
        rx.box(
            rx.icon(
                tag="search",
                size=14,
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 !text-gray-500/40",
            ),
            rx.el.input(
                on_change=lambda value: SearchInput.set_value(value),
                placeholder="Search documentation ...",
                class_name="py-2 px-7 w-full placeholder:text-sm "
                + "text-sm "
                + "rounded-md bg-transparent border-dashed border-[0.5px] border-gray-500/40 "
                + "focus:outline-none focus:border-gray-500/40",
            ),
            class_name="w-full relative focus:outline-none",
        ),
        class_name="w-full absolute top-0 left-0 p-3 bg-background z-[999]",
    )


def search_content():
    return rx.scroll_area(
        rx.cond(
            SearchInput.value.length() > 0,
            rx.box(
                rx.box(
                    rx.foreach(
                        GettingStartedData.value,
                        lambda value: rx.cond(
                            value["name"].lower().contains(SearchInput.value.lower()),
                            search_result(
                                ["ui", "getting started", value["dir"]], value
                            ),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                rx.box(
                    rx.foreach(
                        ChartData.value,
                        lambda value: rx.cond(
                            value["name"].lower().contains(SearchInput.value.lower()),
                            search_result(["ui", "charts", value["dir"]], value),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                rx.box(
                    rx.foreach(
                        PantryData.value,
                        lambda value: rx.cond(
                            value["name"].lower().contains(SearchInput.value.lower()),
                            search_result(["ui", "pantry", value["dir"]], value),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                rx.foreach(SearchData.value, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


def search() -> rx.Component:
    """Buridan UI search feature"""
    return rx.dialog.root(
        rx.dialog.trigger(
            search_trigger(), id="search-trigger", class_name="hidden md:flex"
        ),
        rx.dialog.content(
            search_input(),
            search_content(),
            on_interact_outside=SearchInput.set_value(""),
            on_escape_key_down=SearchInput.set_value(""),
            class_name="focus:outline-none bg-background h-[60vh] p-3 border-none",
        ),
        on_mount=[keyboard_shortcut_script()],
    )
