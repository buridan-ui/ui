import reflex as rx
from reflex.experimental import ClientStateVar

from typing import TypedDict, List

docs = ClientStateVar.create("docs_minisearch", default=[], global_ref=True)
query = ClientStateVar.create("query_minisearch", default="", global_ref=True)


class AuthorDict(TypedDict):
    firstName: str
    lastName: str


class ItemDict(TypedDict):
    title: str
    author: AuthorDict


class DocDict(TypedDict):
    item: ItemDict
    refIndex: int
    score: float


def minisearch_cdn_script():
    return rx.script(
        src="https://cdn.jsdelivr.net/npm/minisearch@7.1.0/dist/umd/index.min.js"
    )


def custom_minisearch_search_script():
    return rx.script(src="/js_integration/search/minisearch.js")


def load_json_file_and_initialize_minisearch():
    return rx.script(
        """
        console.log("Fetching list.json...");
        fetch('/js_integration/search/list.json')
            .then(response => response.json())
            .then(data => {
                console.log("Loaded list.json:", data);
                window.initializeMinisearch(data);
                window.minisearchInitialized = true;
            })
            .catch(error => console.error('Error loading JSON:', error));
        """
    )


def search_trigger() -> rx.Component:
    """Render the search trigger button."""
    return rx.box(
        rx.icon(
            "search",
            class_name="absolute left-2 top-1/2 transform -translate-y-1/2 text-md w-4 h-4 flex-shrink-0 !text-slate-9",
        ),
        rx.text(
            "⌘K",
            class_name="absolute right-2 top-1/2 transform -translate-y-1/2 text-sm bg-slate-3 rounded-md text-sm !text-slate-9 px-[5px] py-[2px] hidden md:inline",
        ),
        rx.el.input(
            placeholder="Search",
            read_only=True,
            class_name="bg-transparent border-none outline-none focus:outline-none pl-4 cursor-pointer hidden md:block",
        ),
        border="0.81px solid gray",
        class_name="py-[6px] px-[12px] w-full cursor-pointer flex max-h-[32px] min-h-[32px] rounded-[10px] relative",
    )


def no_results_found():
    return rx.box(
        rx.el.p(
            rx.fragment(
                "No results found for ",
                rx.el.strong(f"'{query.value}'"),
            ),
        ),
        class_name="w-full flex items-center justify-center text-sm py-4",
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
                id="search_input_minisearch",
                on_change=rx.call_script(
                    """
                    (() => {
                        if (!window._debouncedSearch) {
                            let timeout;
                            window._debouncedSearch = function () {
                                clearTimeout(timeout);
                                timeout = setTimeout(() => {
                                    const inputValue = document.getElementById("search_input_minisearch").value;
                                    const results = window.searchMinisearch(inputValue);
                                    console.log("searchMinisearch called with query:", inputValue, results);
                                    refs._client_state_setDocs_minisearch(results);
                                    refs._client_state_setQuery_minisearch(inputValue);
                                }, 300);
                            };
                        }
                        window._debouncedSearch();
                    })();
                    """
                ),
                auto_focus=True,
                placeholder="Search documentation ...",
                class_name="py-2 pl-7 md:pr-[310px] w-full placeholder:text-sm text-sm rounded-lg outline-none focus:outline-none",
            ),
            class_name="w-full relative focus:outline-none",
        ),
        class_name="w-full flex flex-col absolute top-0 left-0 p-3 z-[999]",
    )


def search_content():
    return rx.scroll_area(
        rx.box(
            rx.cond(
                query.value.to(str).strip() != "",
                rx.cond(
                    docs.value.to(List[DocDict]).length() > 0,
                    rx.foreach(
                        docs.value.to(List[DocDict]),
                        lambda doc: rx.box(
                            *[
                                rx.el.p(
                                    rx.fragment(
                                        rx.el.strong("Title: "),
                                        doc["item"]["title"],
                                    ),
                                ),
                                rx.el.p(
                                    rx.fragment(
                                        rx.el.strong("Author: "),
                                        doc["item"]["author"]["firstName"]
                                        + " "
                                        + doc["item"]["author"]["lastName"],
                                    ),
                                ),
                                rx.el.p(
                                    rx.fragment(
                                        rx.el.strong("Score: "),
                                        f"{doc['score']:.6f}",
                                    ),
                                ),
                            ],
                            font_size="14px",
                        ),
                    ),
                    no_results_found(),
                ),
            ),
            class_name="flex flex-col gap-y-2 px-2",
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


def minisearch_search_front_end_only() -> rx.Component:
    """Create the main search component for Reflex Web"""
    return rx.dialog.root(
        rx.dialog.trigger(search_trigger(), id="search-trigger"),
        rx.dialog.content(
            search_input(),
            search_content(),
            class_name="w-full max-w-[650px] mx-auto outline-none p-3 h-[57vh]",
        ),
    )


def center_minisearch_front_end_search():
    return rx.box(
        docs,
        query,
        rx.box(
            minisearch_search_front_end_only(),
            class_name="flex w-full items-center justify-center max-w-72",
        ),
        class_name="flex w-full items-center justify-center",
    )
