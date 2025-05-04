import os
import inspect
import importlib
import reflex as rx
from typing import Callable, Dict, List, Any

from buridan_ui.config import BASE_PANTRY_PATH, BASE_CHART_PATH
from buridan_ui.ui.organisms.grid import responsive_grid
from buridan_ui.wrappers.component.wrapper import component_wrapper


# Define a unified configuration system
class ExportConfig:
    def __init__(self):
        # Component configurations
        self.COMPONENTS = {
            "tabs": {"versions": range(1, 4), "func_prefix": "tab"},
            "sidebars": {"versions": range(1, 2), "func_prefix": "sidebar"},
            "accordions": {"versions": range(1, 2), "func_prefix": "accordion"},
            "animations": {"versions": range(1, 4), "func_prefix": "animation"},
            "backgrounds": {"versions": range(1, 5), "func_prefix": "background"},
            "cards": {"versions": range(1, 5), "func_prefix": "card"},
            "faq": {"versions": [1], "func_prefix": "faq"},
            "featured": {"versions": range(1, 3), "func_prefix": "featured"},
            "footers": {"versions": range(1, 3), "func_prefix": "footer"},
            "forms": {"versions": range(1, 4), "func_prefix": "forms"},
            "inputs": {"versions": range(1, 6), "func_prefix": "input"},
            "lists": {"versions": [1], "func_prefix": "lists"},
            "logins": {"versions": range(1, 3), "func_prefix": "logins"},
            "menus": {"versions": [1], "func_prefix": "menus"},
            "onboardings": {"versions": [1], "func_prefix": "onboardings"},
            "payments": {"versions": [1], "func_prefix": "payments"},
            "popups": {"versions": range(1, 3), "func_prefix": "popups"},
            "pricing": {"versions": range(1, 3), "func_prefix": "pricing"},
            "prompts": {"versions": range(1, 3), "func_prefix": "prompt"},
            "subscribe": {"versions": range(1, 4), "func_prefix": "subscribe"},
            "tables": {"versions": range(1, 5), "func_prefix": "tables"},
            "timeline": {"versions": [1], "func_prefix": "timeline"},
        }

        # Chart configurations
        self.CHARTS = {
            "area": {
                "versions": range(1, 9),
                "func_prefix": "areachart",
                "flexgen": "https://reflex.build/gen/85caad0f-95d1-4180-b4eb-fc72edafdc9a/",
            },
            "bar": {"versions": range(1, 11), "func_prefix": "barchart"},
            "line": {"versions": range(1, 9), "func_prefix": "linechart"},
            "pie": {"versions": range(1, 7), "func_prefix": "piechart"},
            "radar": {"versions": range(1, 7), "func_prefix": "radar"},
            "scatter": {"versions": [1], "func_prefix": "scatterchart"},
            "doughnut": {"versions": range(1, 3), "func_prefix": "doughnutchart"},
            "sunburst": {"versions": [1], "func_prefix": "sunburst"},
            "bump": {"versions": [1], "func_prefix": "bump"},
            "chord": {"versions": [1], "func_prefix": "chord"},
        }

        # Pro configurations
        self.PRO = {
            "table": {"versions": range(1, 2), "func_prefix": "integrated_table"},
        }

        # Grid configurations
        self.GRID_CONFIGS = {}

        # Development mode settings
        self.development_mode = False
        self.selected_components = set()
        self.selected_charts = set()
        self.selected_pro = set()

        # Keep a complete list of all component and chart names
        self.all_component_names = set(self.COMPONENTS.keys())
        self.all_chart_names = set(self.CHARTS.keys())
        self.all_pro_names = set(self.PRO.keys())

        # Initialize development environment from environment variables
        self._init_from_env()

    def _init_from_env(self):
        """Initialize development settings from environment variables."""
        self.development_mode = os.environ.get("BURIDAN_DEV_MODE", "").lower() in (
            "true",
            "1",
            "yes",
        )

        if self.development_mode:
            components = os.environ.get("BURIDAN_COMPONENTS", "")
            if components:
                self.selected_components = {
                    c.strip() for c in components.split(",") if c.strip()
                }

            charts = os.environ.get("BURIDAN_CHARTS", "")
            if charts:
                self.selected_charts = {
                    c.strip() for c in charts.split(",") if c.strip()
                }

            pro = os.environ.get("BURIDAN_PRO", "")
            if pro:
                self.selected_pro = {c.strip() for c in pro.split(",") if c.strip()}

            # Print development settings
            print("Development mode: Enabled")
            if self.selected_components:
                print(f"Selected components: {', '.join(self.selected_components)}")
            if self.selected_charts:
                print(f"Selected charts: {', '.join(self.selected_charts)}")
            if self.selected_pro:
                print(f"Selected pro components: {', '.join(self.selected_pro)}")

    def should_include_component(self, component_name: str) -> bool:
        """Check if a component should be included based on development settings."""
        if not self.development_mode:
            return True

        # If charts or pro are specifically selected and components aren't, exclude all components
        if (self.selected_charts and not self.selected_components) or (
            self.selected_pro and not self.selected_components
        ):
            return False

        if not self.selected_components:
            return True

        return component_name in self.selected_components

    def should_include_chart(self, chart_name: str) -> bool:
        """Check if a chart should be included based on development settings."""
        if not self.development_mode:
            return True

        # If components or pro are specifically selected and charts aren't, exclude all charts
        if (self.selected_components and not self.selected_charts) or (
            self.selected_pro and not self.selected_charts
        ):
            return False

        if not self.selected_charts:
            return True

        return chart_name in self.selected_charts

    def should_include_pro(self, pro_name: str) -> bool:
        """Check if a pro component should be included based on development settings."""
        if not self.development_mode:
            return True

        # If components or charts are specifically selected and pro aren't, exclude all pro components
        if (self.selected_components and not self.selected_pro) or (
            self.selected_charts and not self.selected_pro
        ):
            return False

        if not self.selected_pro:
            return True

        return pro_name in self.selected_pro


# Create a singleton config instance
config = ExportConfig()


class SourceRetriever:
    """Class to handle different source code retrieval strategies"""

    @staticmethod
    def pro_source(directory: str, filename: str) -> str:
        """Get source for pantry components."""
        with open(os.path.join("buridan_ui", "pro", directory, filename)) as file:
            return file.read()

    @staticmethod
    def pantry_source(directory: str, filename: str) -> str:
        """Get source for pantry components."""
        with open(os.path.join("buridan_ui", "pantry", directory, filename)) as file:
            return file.read()

    @staticmethod
    def chart_source(func: Callable) -> str:
        """Get source for chart components including style.py."""
        source: str = ""

        # Check if the function name starts with 'sunburst' or 'bump'
        if not (
            func.__name__.startswith("sunburst") or func.__name__.startswith("bump")
        ):
            # Only read the file if the name doesn't start with 'sunburst' or 'bump'
            with open("buridan_ui/charts/style.py") as file:
                source += file.read()
                source += "\n"

        source += inspect.getsource(func)
        return source


class ExportFactory:
    """Factory class for creating exports"""

    @staticmethod
    def create_pro_export(
        directory: str,
        version: int,
        func_prefix: str,
        flexgen_url: str = "",
    ) -> Callable:
        """Create an export function for a pro component."""
        # Import the component dynamically
        component_func = ExportFactory._import_component(
            base_module="buridan_ui.pro",
            directory=directory,
            version=version,
            func_prefix=func_prefix,
        )

        @component_wrapper(f"{BASE_PANTRY_PATH}{directory}/v{version}.py")
        def export():
            return [
                component_func(),
                SourceRetriever.pro_source(directory, f"v{version}.py"),
                flexgen_url,
            ]

        return export

    @staticmethod
    def create_pantry_export(
        directory: str,
        version: int,
        func_prefix: str,
        flexgen_url: str = "https://reflex.build/gen/85caad0f-95d1-4180-b4eb-fc72edafdc9a/",
    ) -> Callable:
        """Create an export function for a pantry component."""
        # Import the component dynamically
        component_func = ExportFactory._import_component(
            base_module="buridan_ui.pantry",
            directory=directory,
            version=version,
            func_prefix=func_prefix,
        )

        @component_wrapper(f"{BASE_PANTRY_PATH}{directory}/v{version}.py")
        def export():
            return [
                component_func(),
                SourceRetriever.pantry_source(directory, f"v{version}.py"),
                flexgen_url,
            ]

        return export

    @staticmethod
    def create_chart_export(
        directory: str,
        version: int,
        func_prefix: str,
        flexgen_url: str = "",
    ) -> Callable:
        """Create an export function for a chart component."""
        # Import the chart component dynamically
        chart_func = ExportFactory._import_component(
            base_module="buridan_ui.charts",
            directory=directory,
            version=version,
            func_prefix=func_prefix,
        )

        @component_wrapper(f"{BASE_CHART_PATH}{directory}/v{version}.py")
        def export():
            return [chart_func(), SourceRetriever.chart_source(chart_func), flexgen_url]

        return export

    @staticmethod
    def _import_component(
        base_module: str, directory: str, version: int, func_prefix: str
    ) -> Callable:
        """Dynamically import a component function."""
        module_path = f"{base_module}.{directory}.v{version}"
        function_name = f"{func_prefix}_v{version}"

        try:
            module = importlib.import_module(module_path)
            return getattr(module, function_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(
                f"Failed to import {function_name} from {module_path}: {e}"
            )

    @staticmethod
    def import_page(module_path: str, func_name: str) -> Callable:
        """Import a page function directly."""
        try:
            module = importlib.import_module(module_path)
            return getattr(module, func_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Failed to import {func_name} from {module_path}: {e}")


def generate_pro_exports() -> Dict[str, List]:
    """Generate all pro component exports dynamically."""
    exports = {}

    # Filter components if in development mode
    component_configs = {}
    for name, details in config.PRO.items():
        if config.should_include_pro(name):
            component_configs[name] = details

    for directory, details in component_configs.items():
        versions = details["versions"]
        func_prefix = details["func_prefix"]
        component_exports = []
        export_items = []

        for version in versions:
            export_func = ExportFactory.create_pro_export(
                directory, version, func_prefix
            )
            export_items.append(export_func())

        # Get any custom grid config for this component type
        grid_config = config.GRID_CONFIGS.get(directory, {})

        # Use responsive_grid to organize the exports
        component_exports.append(responsive_grid(*export_items, **grid_config))
        exports[directory] = component_exports

    return exports


def generate_pantry_exports() -> Dict[str, List]:
    """Generate all pantry component exports dynamically."""
    exports = {}

    # Filter components if in development mode
    component_configs = {}
    for name, details in config.COMPONENTS.items():
        if config.should_include_component(name):
            component_configs[name] = details

    for directory, details in component_configs.items():
        versions = details["versions"]
        func_prefix = details["func_prefix"]
        component_exports = []
        export_items = []

        for version in versions:
            export_func = ExportFactory.create_pantry_export(
                directory, version, func_prefix
            )
            export_items.append(export_func())

        # Get any custom grid config for this component type
        grid_config = config.GRID_CONFIGS.get(directory, {})

        # Use responsive_grid to organize the exports
        component_exports.append(responsive_grid(*export_items, **grid_config))
        exports[directory] = component_exports

    return exports


def generate_chart_exports() -> Dict[str, List]:
    """Generate all chart exports dynamically."""
    exports = {}

    # Filter charts if in development mode
    chart_configs = {}
    for name, details in config.CHARTS.items():
        if config.should_include_chart(name):
            chart_configs[name] = details

    for chart_type, details in chart_configs.items():
        versions = details["versions"]
        func_prefix = details["func_prefix"]
        chart_exports = []
        export_items = []

        for version in versions:
            export_func = ExportFactory.create_chart_export(
                chart_type, version, func_prefix
            )
            export_items.append(export_func())

        # Get any custom grid config for this chart type
        grid_config = config.GRID_CONFIGS.get(chart_type, {})

        # Use responsive_grid to organize the exports
        chart_exports.append(responsive_grid(*export_items, **grid_config))
        exports[chart_type] = chart_exports

    return exports


def filter_routes(routes_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter routes based on development settings.

    This function should be used to filter PantryRoutes and ChartRoutes before adding them.

    Args:
        routes_list: The original list of route dictionaries

    Returns:
        A filtered list of routes based on development settings
    """
    if not config.development_mode:
        return routes_list

    filtered_routes = []

    for route in routes_list:
        directory = route.get("dir")
        if directory:
            # Check if this is a component or chart route
            if directory in config.all_component_names:
                if config.should_include_component(directory):
                    filtered_routes.append(route)
            elif directory in config.all_chart_names:
                if config.should_include_chart(directory):
                    filtered_routes.append(route)
            elif directory in config.all_pro_names:
                if config.should_include_pro(directory):
                    filtered_routes.append(route)
            else:
                # If it's neither, include it by default
                filtered_routes.append(route)
        else:
            # Include routes without a directory by default
            filtered_routes.append(route)

    return filtered_routes


def export_app(app: rx.App):
    from buridan_ui.landing.hero import hero
    from buridan_ui.static.routes import ChartRoutes, PantryRoutes, BuridanProRoutes
    from buridan_ui.static.meta import ChartMetaData, PantryMetaData, ProMetaData
    from buridan_ui.start.buridan import buridan
    from buridan_ui.start.charting import charting
    from buridan_ui.start.installation import installation
    from buridan_ui.start.introduction import introduction
    from buridan_ui.start.changelog.changelog import changelog
    from buridan_ui.wrappers.base.main import base
    from buridan_ui.config import SITE_LOGO_URL, SITE_META_TAGS

    pro_exports_config = generate_pro_exports()
    pantry_exports_config = generate_pantry_exports()
    charts_exports_config = generate_chart_exports()

    def get_exports(directory: str, config_file: dict[str, list[callable]]):
        return [export for export in config_file[directory]]

    def add_routes(
        routes: list[dict[str, str]],
        export_config: dict[str, list[callable]],
        parent_dir: str,
    ) -> None:
        if parent_dir == "charts":
            metadata_source = ChartMetaData

        if parent_dir == "pantry":
            metadata_source = PantryMetaData

        if parent_dir == "pro":
            metadata_source = ProMetaData

        # Filter the routes based on development settings
        filtered_routes = filter_routes(routes)

        for _route in filtered_routes:
            dir_meta = metadata_source[_route["dir"]]

            @base(_route["path"], _route["name"], dir_meta)
            def export_page() -> callable:
                return get_exports(_route["dir"], export_config)

            add_page(export_page(), _route["path"], f"{_route['name']} - Buridan UI")

    def add_page(page_component, route_path, title):
        """Helper function to add pages with consistent metadata"""
        app.add_page(
            page_component,
            route=route_path,
            title=title,
            image=SITE_LOGO_URL,
            meta=SITE_META_TAGS,
        )

    # Add dynamic routes from configurations
    add_routes(ChartRoutes, charts_exports_config, "charts")
    add_routes(PantryRoutes, pantry_exports_config, "pantry")
    add_routes(BuridanProRoutes, pro_exports_config, "pro")

    # Define static routes with consistent structure
    STATIC_ROUTES = [
        {
            "path": "/",
            "component": hero,
            "title": "Buridan Stack",
        },
        {
            "path": "/getting-started/who-is-buridan",
            "component": buridan,
            "title": "Who Is Buridan - Buridan UI",
        },
        {
            "path": "/getting-started/changelog",
            "component": changelog,
            "title": "Changelog - Buridan UI",
        },
        {
            "path": "/getting-started/introduction",
            "component": introduction,
            "title": "Introduction - Buridan UI",
        },
        {
            "path": "/getting-started/installation",
            "component": installation,
            "title": "Installation - Buridan UI",
        },
        {
            "path": "/getting-started/charting",
            "component": charting,
            "title": "Charting - Buridan UI",
        },
    ]

    # Add static routes
    for route in STATIC_ROUTES:
        add_page(route["component"](), route["path"], route["title"])
