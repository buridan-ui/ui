import os
from src.config_generator import get_component_config


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """A simple frontmatter parser."""
    metadata = {}
    if not content.startswith("---"):
        return metadata, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return metadata, content

    frontmatter = parts[1]
    rest_of_content = parts[2]

    for line in frontmatter.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]

            if key == "order" and value.isdigit():
                value = int(value)

            metadata[key] = value

    return metadata, rest_of_content.lstrip()


def _generate_doc_routes(section_folder, base_path):
    """
    Generates routes for a documentation section by reading frontmatter from markdown files.

    Args:
        section_folder: The folder name inside 'docs/' (e.g., 'getting_started').
        base_path: The base URL path for the routes (e.g., '/getting-started/').

    Returns:
        A list of route dictionaries, sorted by the 'order' in metadata.
    """
    routes = []
    docs_path = f"docs/{section_folder}"

    try:
        filenames = [f for f in os.listdir(docs_path) if f.endswith(".md")]
    except FileNotFoundError:
        print(f"Warning: Documentation directory not found at '{docs_path}'")
        return []

    for filename in filenames:
        file_path = os.path.join(docs_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue

        metadata, _ = _parse_frontmatter(content)

        if not metadata or "name" not in metadata:
            continue

        path_slug = filename.replace(".md", "").replace("_", "-")
        route_info = {
            "name": metadata["name"],
            "path": f"{base_path}{path_slug}",
            "dir": metadata.get("dir", path_slug),
            "description": metadata.get("description", ""),
            "order": metadata.get("order", 99),
        }
        routes.append(route_info)

    routes.sort(key=lambda x: x["order"])

    for route in routes:
        del route["order"]

    return routes


# --- Getting Started Section ---

GettingStartedRoutes = _generate_doc_routes(
    section_folder="getting_started",
    base_path="/getting-started/",
)

# --- Component Routes (Pantry & Charts) ---

# Dynamically generate routes from the config
all_components = get_component_config()

PantryRoutes = []
ChartRoutes = []

for name, details in all_components.items():
    route_info = {
        "name": name,
        "path": details["url"],
        "dir": details["dir"],
        "description": f"Explore {name} components.",  # Generic description
    }
    if details["group"] == "Pantry":
        PantryRoutes.append(route_info)
    elif details["group"] == "Charts":
        ChartRoutes.append(route_info)

# Sort them alphabetically by name
PantryRoutes = sorted(PantryRoutes, key=lambda x: x["name"])
ChartRoutes = sorted(ChartRoutes, key=lambda x: x["name"])
