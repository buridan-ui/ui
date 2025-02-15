""" Entry to App """

import reflex as rx

from .blueprints.exports import blueprint_export_config
from .charts.exports import charts_exports_config
from .pages.charts_landing.main import charts_landing_page
from .pages.landing.hero import landing_page
from .pages.started_items.exports import getting_started_config
from .pantry.exports import pantry_exports_config
from .analytics.exports import analytics_config_file
from .analytics.landing import analytics_landing_page


from .routes.routes import Routes
from .wrappers.base.main import base

AppFontURL: str = (
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap"
)

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[AppFontURL],
    style={
        "background": "transparent",
        rx.heading: {"font_family": "inter"},
        rx.text: {"font_family": "inter"},
    },
)


def get_exports(directory: str, config_file: dict[str, list[callable]]):
    return [export() for export in config_file[directory]]


def add_routes(
    routes: list[dict[str, str]],
    export_config: dict[str, list[callable]],
) -> None:
    for route in routes:

        @base(route["path"], route["name"])
        def export_page() -> callable:
            if route["name"] == "Standard Tables":
                return get_exports(route["dir"], export_config)[1:]
            if route["name"] == "Table Pagination":
                return get_exports(route["dir"], export_config)[:1]
            return get_exports(route["dir"], export_config)

        app.add_page(
            export_page(),
            route=route["path"],
            title=f"{route['name']} - Buridan UI",
        )


# ... set the DEV var to True for faster hot reload
# ... ... change the ENV to match the page in progress
DEV: bool = False

if DEV:
    # ... ex: working with X item Y -> set the ENV data as such:
    ENV = {
        "path": "/charts/area-charts",
        "name": "DEV MODE",
        "dir": "area",
        "config": charts_exports_config,
    }

    @base(ENV["path"], ENV["name"])
    def __() -> callable:
        return [export() for export in ENV["config"][ENV["dir"]]]

    app.add_page(__(), "/")
    # app.add_page(landing_page(), route="/", title="Buridan UI")

else:
    app.add_page(landing_page(), route="/", title="Buridan UI")
    app.add_page(charts_landing_page(), route="/charts/ui", title="Charts UI")
    app.add_page(analytics_landing_page(), route="/analytics/ui", title="Analytics UI")
    add_routes(Routes.blueprints, blueprint_export_config)
    add_routes(Routes.pantries, pantry_exports_config)
    add_routes(Routes.charts, charts_exports_config)
    add_routes(Routes.started, getting_started_config)
    add_routes(Routes.analytics, analytics_config_file)
