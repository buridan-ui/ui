

# MiniSearch Integration with Reflex

Use [MiniSearch](https://lucaong.github.io/minisearch/) for lightweight, client-side fuzzy search inside your Reflex web apps. This guide shows how to integrate it using CDN, connect it to Reflex state, and build a responsive search UI with results.



```python
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
```



# Overview

This guide demonstrates integrating MiniSearch fuzzy search into a Reflex application using client-side state management and custom JavaScript.

# Project Structure

You need three files:
- `app.py` - Main Reflex application
- `assets/list.json` - Search data
- `assets/minisearch.js` - Search logic

# Data Format

Your `list.json` should contain an array of searchable objects:
```json
[
  {
    "title": "Battle for Natural",
    "author": {
      "firstName": "Emily",
      "lastName": "Cain"
    }
  }
]
```

# Search Script Setup

The `minisearch.js` file initializes MiniSearch and exposes search functions globally:
```javascript
let miniSearch;

// Initialize Minisearch with the loaded data
window.initializeMinisearch = function (data) {
  console.log("Initializing Minisearch with data:", data);

  // Create a new MiniSearch instance
  miniSearch = new MiniSearch({
    fields: ["title", "author.firstName", "author.lastName"], // fields to index for full-text search
    storeFields: ["title", "author"], // fields to return with search results
    searchOptions: {
      boost: { title: 2 }, // boost title matches
      fuzzy: 0.2, // enable fuzzy matching
      prefix: true, // enable prefix matching
      combineWith: "AND", // combine search terms with AND
    },
  });

  // Add IDs to documents if they don't have them
  const dataWithIds = data.map((item, index) => ({
    id: item.id || index, // Use existing ID or assign index as ID
    ...item,
  }));

  // Add all documents to the index
  miniSearch.addAll(dataWithIds);

  console.log("Minisearch initialized successfully");
};

// Search function that returns results in the same format as Fuse.js
window.searchMinisearch = function (searchQuery) {
  if (!miniSearch) {
    console.warn("Minisearch not initialized yet");
    return [];
  }

  if (!searchQuery || searchQuery.trim() === "") {
    return [];
  }

  console.log("Searching for:", searchQuery);

  try {
    // Perform the search
    const results = miniSearch.search(searchQuery, {
      fuzzy: 0.2,
      prefix: true,
      boost: { title: 2 },
    });

    console.log("Raw Minisearch results:", results);

    // Transform results to match Fuse.js format
    const transformedResults = results.map((result, index) => ({
      item: {
        title: result.title,
        author: result.author,
      },
      refIndex: result.id || index,
      score: 1 - result.score, // Invert score to match Fuse.js format (lower is better in Fuse)
    }));

    console.log("Transformed results:", transformedResults);
    return transformedResults;
  } catch (error) {
    console.error("Search error:", error);
    return [];
  }
};
```

# Client State Management

Define client-side state variables for reactive updates:
```python
from reflex.experimental import ClientStateVar

docs = ClientStateVar.create("docs_minisearch", default=[], global_ref=True)
query = ClientStateVar.create("query_minisearch", default="", global_ref=True)
```

# Type Definitions

Structure your data types for type safety:
```python
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
```

# Loading External Resources

Inject MiniSearch CDN and custom scripts into the document head:
```python
def minisearch_cdn_script():
    return rx.script(src="https://cdn.jsdelivr.net/npm/minisearch@7.1.0/dist/umd/index.min.js")

def custom_minisearch_search_script():
    return rx.script(src="/js_integration/search/minisearch.js")

def load_json_file_and_initialize_minisearch():
    return rx.script('''
        console.log("Fetching list.json...");
        fetch('/js_integration/search/list.json')
            .then(response => response.json())
            .then(data => {
                console.log("Loaded list.json:", data);
                window.initializeMinisearch(data);
                window.minisearchInitialized = true;
            })
            .catch(error => console.error('Error loading JSON:', error));
    ''')
```

# Search Input Component

Create a debounced search input that updates client state:
```python
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
                on_change=rx.call_script('''
                    (() => {
                        if (!window._debouncedSearch) {
                            let timeout;
                            window._debouncedSearch = function () {
                                clearTimeout(timeout);
                                timeout = setTimeout(() => {
                                    const inputValue = document.getElementById("search_input_minisearch").value;
                                    const results = window.searchMinisearch(inputValue);
                                    refs._client_state_setDocs_minisearch(results);
                                    refs._client_state_setQuery_minisearch(inputValue);
                                }, 300);
                            };
                        }
                        window._debouncedSearch();
                    })();
                '''),
                auto_focus=True,
                placeholder="Search documentation ...",
                class_name="py-2 pl-7 w-full placeholder:text-sm text-sm rounded-lg outline-none focus:outline-none"
            ),
            class_name="w-full relative focus:outline-none",
        ),
        class_name="w-full flex flex-col absolute top-0 left-0 p-3 z-[999]",
    )
```

# Rendering Results

Display search results with conditional rendering:
```python
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
                            rx.el.p(
                                rx.fragment(
                                    rx.el.strong("Title: "),
                                    doc["item"]["title"],
                                ),
                            ),
                            rx.el.p(
                                rx.fragment(
                                    rx.el.strong("Author: "),
                                    doc["item"]["author"]["firstName"] + " " +
                                    doc["item"]["author"]["lastName"],
                                ),
                            ),
                            rx.el.p(
                                rx.fragment(
                                    rx.el.strong("Score: "),
                                    f"{doc['score']:.6f}",
                                ),
                            ),
                            font_size="14px",
                        ),
                    ),
                    no_results_found(),
                ),
            ),
            class_name="flex flex-col gap-y-2 px-2"
        ),
        class_name="w-full h-full pt-11",
    )
```

# Dialog Integration

Wrap the search in a dialog with keyboard shortcut trigger:
```python
def minisearch_search_front_end_only():
    return rx.dialog.root(
        rx.dialog.trigger(search_trigger(), id="search-trigger"),
        rx.dialog.content(
            search_input(),
            search_content(),
            class_name="w-full max-w-[650px] mx-auto outline-none p-3 h-[57vh]"
        ),
    )
```

# Application Setup

Register scripts in the app initialization:
```python
app = rx.App(
    head_components=[
        minisearch_cdn_script(),
        custom_minisearch_search_script(),
        load_json_file_and_initialize_minisearch(),
    ],
)
```

# Key Concepts

Client state variables enable reactive updates without server round-trips. The debounce pattern prevents excessive search calls during typing. MiniSearch handles fuzzy matching with configurable prefix search and boosting. Results include match scores for relevance ranking.

# Customization

Adjust `fuzzy` in searchOptions (0.0-1.0, where higher values allow more character differences). Modify `fields` array to search different fields. Change `boost` values to prioritize certain fields (e.g., boost title matches over author). Adjust debounce timeout (300ms default) for responsiveness vs performance tradeoffs. Enable/disable `prefix` matching for as-you-type search behavior.
