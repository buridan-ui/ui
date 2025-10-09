import os
import inspect
import importlib
import reflex as rx
from typing import Callable, Dict, List, Any

from src.config_generator import get_component_config
from src.config import (
    SITE_LOGO_URL,
    SITE_META_TAGS,
)
from src.components.layout import responsive_grid
from src.wrappers.component.wrapper import (
    component_wrapper,
)
from src.wrappers.base.main import base
from src.docs.docs_generator import generate_docs_routes
from src.types import RouteConfig, ComponentConfig
from src.landing.hero import hero


class ExportConfig:
    """Unified configuration system for all exports."""

    def __init__(self):
        self._init_configurations()
        self._init_development_settings()
        self._init_getting_started_routes()

    def _init_configurations(self):
        """Initialize all component, chart, and pro configurations."""
        all_components_config = get_component_config()

        self.COMPONENTS = {}
        self.CHARTS = {}

        for config in all_components_config.values():
            component_name = config["dir"]
            versions = range(1, config["quantity"] + 1)
            func_prefix = config["func_prefix"]

            config_obj = ComponentConfig(versions=versions, func_prefix=func_prefix)

            if config["group"] == "Pantry":
                self.COMPONENTS[component_name] = config_obj
            elif config["group"] == "Charts":
                self.CHARTS[component_name] = config_obj

        # Grid configurations for custom layouts
        self.GRID_CONFIGS = {}

        # Keep sets of all names for filtering
        self.all_component_names = set(self.COMPONENTS.keys())
        self.all_chart_names = set(self.CHARTS.keys())

    def _init_development_settings(self):
        """Initialize development mode settings from environment variables."""
        self.development_mode = os.environ.get("BURIDAN_DEV_MODE", "").lower() in (
            "true",
            "1",
            "yes",
        )

        self.selected_components = set()
        self.selected_charts = set()
        self.selected_pro = set()

        if self.development_mode:
            self._parse_dev_selections()
            self._print_dev_settings()

    def _init_getting_started_routes(self):
        """Initialize all getting started route configurations."""
        docs_routes = generate_docs_routes()

        # Add the landing page explicitly
        landing_page_route = RouteConfig("/", hero, "Buridan Stack")
        docs_routes.insert(0, landing_page_route)  # Add to the beginning of the list

        self.STATIC_ROUTES = docs_routes

    def _parse_dev_selections(self):
        """Parse development selections from environment variables."""
        components = os.environ.get("BURIDAN_COMPONENTS", "")
        if components:
            self.selected_components = {
                c.strip() for c in components.split(",") if c.strip()
            }

        charts = os.environ.get("BURIDAN_CHARTS", "")
        if charts:
            self.selected_charts = {c.strip() for c in charts.split(",") if c.strip()}

        pro = os.environ.get("BURIDAN_PRO", "")
        if pro:
            self.selected_pro = {c.strip() for c in pro.split(",") if c.strip()}

    def _print_dev_settings(self):
        """Print development settings for debugging."""
        print("Development mode: Enabled")
        if self.selected_components:
            print(f"Selected components: {', '.join(self.selected_components)}")
        if self.selected_charts:
            print(f"Selected charts: {', '.join(self.selected_charts)}")

    def should_include_component(self, component_name: str) -> bool:
        """Check if a component should be included based on development settings."""
        if not self.development_mode:
            return True

        # If other categories are selected but components aren't, exclude all components
        if (self.selected_charts or self.selected_pro) and not self.selected_components:
            return False

        return (
            not self.selected_components or component_name in self.selected_components
        )

    def should_include_chart(self, chart_name: str) -> bool:
        """Check if a chart should be included based on development settings."""
        if not self.development_mode:
            return True

        # If other categories are selected but charts aren't, exclude all charts
        if (self.selected_components or self.selected_pro) and not self.selected_charts:
            return False

        return not self.selected_charts or chart_name in self.selected_charts


# ============================================================================
# SOURCE RETRIEVAL STRATEGIES
# ============================================================================


class SourceRetriever:
    """Handles different source code retrieval strategies."""

    @staticmethod
    def get_pantry_source(directory: str, filename: str) -> str:
        """Get source for pantry components."""
        with open(os.path.join("src", "pantry", directory, filename)) as file:
            return file.read()

    @staticmethod
    def get_chart_source(func: Callable) -> str:
        """Get source for chart components including style.py when needed."""
        source = ""

        with open("src/charts/style.py") as file:
            source += file.read() + "\n"

        source += inspect.getsource(func)

        return source


# ============================================================================
# EXPORT FACTORY
# ============================================================================


class ExportFactory:
    """Factory for creating different types of export functions."""

    @staticmethod
    def create_pantry_export(
        directory: str, config: ComponentConfig, version: int
    ) -> Callable:
        """Create an export function for a pantry component."""
        component_func = ExportFactory._import_component(
            "src.pantry", directory, version, config.func_prefix
        )

        @component_wrapper(f"pantry/{directory}/v{version}.py")
        def export():
            return [
                component_func(),
                SourceRetriever.get_pantry_source(directory, f"v{version}.py"),
            ]

        return export

    @staticmethod
    def create_chart_export(
        directory: str, config: ComponentConfig, version: int
    ) -> Callable:
        """Create an export function for a chart component."""
        chart_func = ExportFactory._import_component(
            "src.charts", directory, version, config.func_prefix
        )

        @component_wrapper(f"charts/{directory}/v{version}.py")
        def chart_export():
            return [
                chart_func(),
                SourceRetriever.get_chart_source(chart_func),
            ]

        return chart_export

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


# ============================================================================
# EXPORT GENERATORS
# ============================================================================


class ExportGenerator:
    """Handles generation of different export types."""

    def __init__(self, config: ExportConfig):
        self.config = config

    def generate_pantry_exports(self) -> Dict[str, List]:
        """Generate all pantry component exports."""
        return self._generate_exports(
            self.config.COMPONENTS,
            self.config.should_include_component,
            ExportFactory.create_pantry_export,
        )

    def generate_chart_exports(self) -> Dict[str, List]:
        """Generate all chart exports."""
        exports = {}

        filtered_configs = {
            name: config
            for name, config in self.config.CHARTS.items()
            if self.config.should_include_chart(name)
        }

        for chart_type, chart_config in filtered_configs.items():
            export_items = []

            # Generate version exports
            for version in chart_config.versions:
                export_func = ExportFactory.create_chart_export(
                    chart_type, chart_config, version
                )
                export_items.append(export_func())

            # Apply grid configuration
            grid_config = self.config.GRID_CONFIGS.get(chart_type, {})
            exports[chart_type] = [responsive_grid(*export_items, **grid_config)]

        return exports

    def _generate_exports(
        self,
        configs: Dict[str, ComponentConfig],
        should_include_func: Callable,
        export_factory_func: Callable,
    ) -> Dict[str, List]:
        """Generic method to generate exports for any component type."""
        exports = {}

        filtered_configs = {
            name: config
            for name, config in configs.items()
            if should_include_func(name)
        }

        for directory, component_config in filtered_configs.items():
            export_items = []

            for version in component_config.versions:
                export_func = export_factory_func(directory, component_config, version)
                export_items.append(export_func())

            # Apply grid configuration
            grid_config = self.config.GRID_CONFIGS.get(directory, {})
            exports[directory] = [responsive_grid(*export_items, **grid_config)]

        return exports


# ============================================================================
# ROUTE MANAGEMENT
# ============================================================================


class RouteManager:
    """Manages route filtering and registration."""

    def __init__(self, config: ExportConfig):
        self.config = config

    def filter_routes(self, routes_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter routes based on development settings."""
        if not self.config.development_mode:
            return routes_list

        filtered_routes = []
        for route in routes_list:
            directory = route.get("dir")
            if not directory or self._should_include_route(directory):
                filtered_routes.append(route)

        return filtered_routes

    def _should_include_route(self, directory: str) -> bool:
        """Check if a route should be included based on its directory."""
        if directory in self.config.all_component_names:
            return self.config.should_include_component(directory)
        elif directory in self.config.all_chart_names:
            return self.config.should_include_chart(directory)
        else:
            return True  # Include unknown routes by default


# ============================================================================
# MAIN APPLICATION EXPORTER
# ============================================================================


class ApplicationExporter:
    """Main class for exporting the complete application."""

    def __init__(self):
        self.config = ExportConfig()
        self.generator = ExportGenerator(self.config)
        self.route_manager = RouteManager(self.config)

    def export_app(self, app: rx.App):
        """Export the complete application with all routes and configurations."""
        # Import required metadata and routes
        from src.static.routes import ChartRoutes, PantryRoutes

        # Generate all exports
        pantry_exports = self.generator.generate_pantry_exports()
        chart_exports = self.generator.generate_chart_exports()

        # Add dynamic routes
        self.add_pages(app, ChartRoutes, chart_exports)
        self.add_pages(app, PantryRoutes, pantry_exports)

        # Add static routes
        self._add_static_routes(app)

    def add_pages(self, app, routes, exports):
        """Helper function to add pages with consistent metadata."""
        from src.config_generator import get_component_config

        all_configs = get_component_config()

        for route in routes:
            if route["dir"] in exports:

                def build_page(current_route, component):
                    @base(
                        url=current_route["path"],
                        page_name=current_route["name"],
                        dir_meta=all_configs.get(current_route["name"], {}).get(
                            "meta", []
                        ),
                    )
                    def page_fn():
                        return component

                    return page_fn

                page_component = exports[route["dir"]]
                page_function = build_page(route, page_component)

                app.add_page(
                    page_function,
                    route=route["path"],
                    title=route["name"],
                    meta=SITE_META_TAGS,
                )

    def _add_static_routes(self, app: rx.App):
        """Add all static routes from configuration."""
        for route_config in self.config.STATIC_ROUTES:
            self._add_page(
                app, route_config.component, route_config.path, route_config.title
            )

    def _add_page(
        self, app: rx.App, page_component: Callable, route_path: str, title: str
    ):
        """Helper function to add pages with consistent metadata."""
        app.add_page(
            page_component,
            route=route_path,
            title=title,
            image=SITE_LOGO_URL,
            meta=SITE_META_TAGS,
        )


# ============================================================================
# SINGLETON INSTANCE & PUBLIC API
# ============================================================================

# Create singleton instances
# _config = ExportConfig()
_exporter = ApplicationExporter()


# Public API functions
def export_app(app: rx.App):
    """Export the complete application - main entry point."""
    _exporter.export_app(app)


def filter_routes(routes_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter routes based on development settings - utility function."""
    return _exporter.route_manager.filter_routes(routes_list)
