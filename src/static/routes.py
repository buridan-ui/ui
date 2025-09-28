from src.config_generator import get_component_config

_GS_Base = "/getting-started/"
_Pro = "/pro/"

BuridanProRoutes = [
    {
        "name": "Integrated Tables",
        "path": f"{_Pro}integrated-tables",
        "dir": "table",
        "description": "Advanced table layout with dynamic data integration.",
    },
]

GettingStartedRoutes = [
    {
        "name": "Introduction",
        "path": f"{_GS_Base}introduction",
        "dir": "introduction",
        "description": "Overview of what Buridan UI is and how it works.",
    },
    {
        "name": "Who is Buridan?",
        "path": f"{_GS_Base}who-is-buridan",
        "dir": "buridan",
        "description": "A brief backstory on Buridan and the philosophy behind the framework.",
    },
    {
        "name": "Installation",
        "path": f"{_GS_Base}installation",
        "dir": "installation",
        "description": "Steps to install and start using Buridan in your project.",
    },
    {
        "name": "Theming",
        "path": f"{_GS_Base}theming",
        "dir": "theming",
        "description": "Customize your app’s appearance using themes and tokens.",
    },
    {
        "name": "Charting Walkthrough",
        "path": f"{_GS_Base}charting",
        "dir": "charting",
        "description": "Step-by-step guide to building charts using Buridan.",
    },
    {
        "name": "Dashboard Walkthrough",
        "path": f"{_GS_Base}dashboard",
        "dir": "dashboard",
        "description": "Build a full dashboard UI using Buridan components.",
    },
    {
        "name": "ClientStateVar",
        "path": f"{_GS_Base}client-state-var",
        "dir": "clientstate",
        "description": "Use client-side state variables to manage local interactivity.",
    },
    {
        "name": "Changelog",
        "path": f"{_GS_Base}changelog",
        "dir": "changelog",
        "description": "Track feature additions, improvements, and bug fixes.",
    },
]

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
