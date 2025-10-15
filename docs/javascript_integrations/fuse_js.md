---
title: "Fuse JS"
description: "Client-side fuzzy search with Fuse.js in Reflex"
order: 0
---

# Fuse Integration with Reflex

Use [Fuse.js](https://fusejs.io) for lightweight, client-side fuzzy search inside your Reflex web apps. This guide shows how to integrate it using CDN, connect it to Reflex state, and build a responsive search UI with results.


--DEMO_AND_SINGLE_FUNCTION(center_fuse_front_end_search)--


# Overview

This guide demonstrates integrating Fuse.js fuzzy search into a Reflex application using client-side state management and custom JavaScript.

# Project Structure

You need three files:
- `app.py` - Main Reflex application
- `assets/list.json` - Search data
- `assets/fuse.js` - Search logic

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

The `fuse.js` file initializes Fuse.js and exposes search functions globally:

```javascript
// Fuse.js configuration (note: no require() since we load via CDN)
const fuseOptions = {
  keys: ["title", "author.firstName", "author.lastName"], // Added lastName
  includeScore: true,
  threshold: 0.3, // Adjust for search sensitivity
};

let fuse; // This will store the Fuse instance

// Initialize Fuse.js with data
function initializeFuse(list) {
  try {
    fuse = new Fuse(list, fuseOptions);
    console.log("Fuse.js initialized successfully with", list.length, "items");
  } catch (error) {
    console.error("Error initializing Fuse.js:", error);
  }
}

// Perform a search
function searchFuse(query) {
  console.log("searchFuse called with query:", query);
  if (!fuse) {
    console.warn("Fuse.js not initialized yet");
    return [];
  }

  if (!query || query.trim() === "") {
    return [];
  }

  try {
    const results = fuse.search(query);
    console.log('Search results for "' + query + '":', results);
    return results;
  } catch (error) {
    console.error("Error during search:", error);
    return [];
  }
}

window.initializeFuse = initializeFuse;
window.searchFuse = searchFuse;

console.log("Search functions defined and attached to window");
```

# Client State Management

Define client-side state variables for reactive updates:

```python
from reflex.experimental import ClientStateVar

docs = ClientStateVar.create("docs", default=[], global_ref=True)
query = ClientStateVar.create("query", default="", global_ref=True)
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

Inject Fuse.js CDN and custom scripts into the document head:

```python
def fuse_cdn_script():
    return rx.script(src="https://cdn.jsdelivr.net/npm/fuse.js@7.1.0")

def custom_search_script():
    return rx.script(src="/fuse/fuse.js")

def load_json_file_and_initialize():
    return rx.script('''
        fetch('/fuse/list.json')
            .then(response => response.json())
            .then(data => {
                setTimeout(() => {
                    window.initializeFuse(data);
                    window.fuseInitialized = true;
                }, 2000);
            });
    ''')
```

# Search Input Component

Create a debounced search input that updates client state:

```python
def search_input():
    return rx.box(
        rx.icon(tag="search", size=14),
        rx.el.input(
            id="search_input",
            on_change=rx.call_script('''
                (() => {
                    if (!window._debouncedSearch) {
                        let timeout;
                        window._debouncedSearch = function () {
                            clearTimeout(timeout);
                            timeout = setTimeout(() => {
                                const inputValue = document.getElementById("search_input").value;
                                const results = window.searchFuse(inputValue);
                                refs._client_state_setDocs(results);
                                refs._client_state_setQuery(inputValue);
                            }, 300);
                        };
                    }
                    window._debouncedSearch();
                })();
            '''),
            auto_focus=True,
            placeholder="Search documentation ...",
        ),
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
                            rx.el.p(rx.el.strong("Title: "), doc["item"]["title"]),
                            rx.el.p(rx.el.strong("Author: "),
                                doc["item"]["author"]["firstName"] + " " +
                                doc["item"]["author"]["lastName"]),
                            rx.el.p(rx.el.strong("Score: "), f"{doc['score']:.6f}"),
                        ),
                    ),
                    no_results_found(),
                ),
            ),
        ),
    )
```

# Dialog Integration

Wrap the search in a dialog with keyboard shortcut trigger:

```python
def fuse_search_front_end_only():
    return rx.dialog.root(
        rx.dialog.trigger(search_trigger()),
        rx.dialog.content(
            search_input(),
            search_content(),
        ),
    )
```

# Application Setup

Register scripts in the app initialization:

```python
app = rx.App(
    head_components=[
        fuse_cdn_script(),
        custom_search_script(),
        load_json_file_and_initialize(),
    ],
)
```

# Key Concepts

Client state variables enable reactive updates without server round-trips. The debounce pattern prevents excessive search calls during typing. Fuse.js handles fuzzy matching with configurable sensitivity via the threshold option. Results include match scores for relevance ranking.

# Customization

Adjust `threshold` in fuseOptions (0.0 = exact match, 1.0 = match anything). Modify `keys` array to search different fields. Change debounce timeout (300ms default) for responsiveness vs performance tradeoffs.
