import os
import json

# Base route prefixes
getting_started = "/getting-started/"
pantry = "/pantry/"
charts = "/charts/"

# Hardcoded Getting Started section
GETTING_STARTED = [
    {
        "name": "Introduction",
        "path": f"{getting_started}introduction",
        "dir": "introduction",
        "description": "Overview of what Buridan UI is and how it works.",
    },
    {
        "name": "Who is Buridan?",
        "path": f"{getting_started}who-is-buridan",
        "dir": "buridan",
        "description": "A brief backstory on Buridan and the philosophy behind the framework.",
    },
    {
        "name": "Installation",
        "path": f"{getting_started}installation",
        "dir": "installation",
        "description": "Steps to install and start using Buridan in your project.",
    },
    {
        "name": "Theming",
        "path": f"{getting_started}theming",
        "dir": "theming",
        "description": "Customize your app’s appearance using themes and tokens.",
    },
    {
        "name": "Charting Walkthrough",
        "path": f"{getting_started}charting",
        "dir": "charting",
        "description": "Step-by-step guide to building charts using Buridan.",
    },
    {
        "name": "Dashboard Walkthrough",
        "path": f"{getting_started}dashboard",
        "dir": "dashboard",
        "description": "Build a full dashboard UI using Buridan components.",
    },
    {
        "name": "ClientStateVar",
        "path": f"{getting_started}client-state-var",
        "dir": "clientstate",
        "description": "Use client-side state variables to manage local interactivity.",
    },
    {
        "name": "Changelog",
        "path": f"{getting_started}changelog",
        "dir": "changelog",
        "description": "Track feature additions, improvements, and bug fixes.",
    },
]


def title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def build_routes(
    folder: str, base: str, description_overrides: dict[str, str], suffix: str = ""
) -> list[dict]:
    routes = []
    for entry in sorted(os.listdir(folder)):
        full_path = os.path.join(folder, entry)
        if os.path.isdir(full_path) and not entry.startswith("__"):
            slug = entry.replace("_", "-").lower()
            name = title_from_slug(slug)
            if suffix:
                name = f"{name} {suffix}"

            route = {
                "name": name,
                "path": f"{base}{slug}",
                "dir": entry,
                "description": description_overrides.get(
                    entry, "No description available."
                ),
            }
            routes.append(route)
    return sorted(routes, key=lambda r: r["name"])


# Optional: Add real overrides if needed
chart_description_overrides = {
    "area": "Display continuous data with filled area charts.",
    "bar": "Use vertical or horizontal bars to compare values.",
    "line": "Plot trends over time or ordered categories using lines.",
    "pie": "Display data as slices of a circular pie.",
    "doughnut": "Donut-style charts to show part-to-whole proportions.",
    "radar": "Compare multiple variables across axes in a radar format.",
    "scatter": "Show correlations between two numerical variables.",
}

pantry_description_overrides = {
    "accordions": "Expandable accordion sections for showing and hiding content.",
    "animations": "Prebuilt animation utilities for smooth transitions.",
    "backgrounds": "Flexible background sections for visual structure.",
    "cards": "Modular content containers for displaying grouped information.",
    "descriptive-lists": "Use description lists to pair labels with detailed values.",
    "featured": "Highlight key content with featured callout components.",
    "footers": "Footer layouts with links, branding, and legal content.",
    "frequently-asked-questions": "FAQ layout for answering common user questions.",
    "inputs": "Reusable input components for forms and interactions.",
    "logins": "Authentication page templates for login and signup.",
    "menus": "Dropdown and popover menus for navigation or options.",
    "onboarding-and-progress": "Guided onboarding steps and progress indicators.",
    "payments-and-billing": "Sections for pricing, plans, and payment details.",
    "popups": "Alert boxes and modal popups for messages and actions.",
    "pricing-sections": "Prebuilt pricing tables and plan comparison layouts.",
    "prompt-boxes": "Lightweight prompts for alerts, confirmations, and actions.",
    "sidebars": "Responsive sidebar layouts for navigation or content grouping.",
    "standard-forms": "Ready-to-use forms with fields and validation.",
    "standard-tables": "Clean and sortable tables for structured data.",
    "stats": "Visual stats blocks for metrics and KPIs.",
    "subscribe": "Subscription forms and call-to-action sections.",
    "tabs": "Tab navigation components to switch between views.",
    "timeline": "Timeline layouts for step-based or historical data.",
}

# Folder inputs
CHART_DIR = "buridan_ui/charts"
PANTRY_DIR = "buridan_ui/pantry"

# Write to a file
OUTPUT_FILE = "./buridan_ui/static/generated_routes.py"


if __name__ == "__main__":
    CHARTS = build_routes(CHART_DIR, charts, chart_description_overrides, "Charts")
    PANTRY = build_routes(PANTRY_DIR, pantry, pantry_description_overrides)

    with open(OUTPUT_FILE, "w") as f:
        f.write("# This file was auto-generated. Do not edit manually.\n\n")

        f.write("GETTING_STARTED = ")
        json.dump(GETTING_STARTED, f, indent=4)
        f.write("\n\n")

        f.write("CHARTS = ")
        json.dump(CHARTS, f, indent=4)
        f.write("\n\n")

        f.write("PANTRY = ")
        json.dump(PANTRY, f, indent=4)
        f.write("\n")

    print(
        f"Wrote {len(GETTING_STARTED)} GETTING_STARTED, {len(CHARTS)} CHARTS, {len(PANTRY)} PANTRY routes to {OUTPUT_FILE}"
    )
