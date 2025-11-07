import typer
import pathlib

from cli.interactive import interactive_cli
from cli.utils import (
    _update_repo,
    _get_app_name,
    _check_reflex_project,
    _add_base_ui_component,
    _add_wrapped_react,
    _extract_theme_css,
    BASE_UI_BASE_COMPONENTS_DIR,
    WRAPPED_COMPONENTS_DIR,
    THEMES_CSS_FILE,
)

app = typer.Typer()
add_app = typer.Typer()
app.add_typer(add_app, name="add")


@add_app.command("component")
def add_component(component: str):
    """
    Add a component and its dependencies to your Reflex project.
    """
    _check_reflex_project()
    app_name = _get_app_name()
    app_root_dir = pathlib.Path.cwd() / app_name

    _update_repo()
    typer.secho(f"Adding component: '{component}'...", fg=typer.colors.GREEN)
    added_items = set()
    _add_base_ui_component(component, added_items, app_root_dir)
    typer.secho("Done.", fg=typer.colors.GREEN)


@add_app.command("wrapped-react")
def add_wrapped_react_command(
    component: str,
):  # Renamed to avoid conflict with imported function
    """
    Add a wrapped React component and its dependencies to your Reflex project.
    """
    _check_reflex_project()
    app_name = _get_app_name()
    app_root_dir = pathlib.Path.cwd() / app_name

    _update_repo()
    typer.secho(
        f"Adding wrapped React component: '{component}'...", fg=typer.colors.GREEN
    )
    added_items = set()
    _add_wrapped_react(component, added_items, app_root_dir)
    typer.secho("Done.", fg=typer.colors.GREEN)


@add_app.command("theme")
def add_theme_command(
    theme_name: str,
):  # Renamed to avoid conflict with imported function
    """
    Add a theme (light and dark variants) to your Reflex project.
    """
    _check_reflex_project()
    project_root_dir = pathlib.Path.cwd()

    _update_repo()
    typer.secho(f"Adding theme: '{theme_name}'...", fg=typer.colors.GREEN)

    theme_css_content = _extract_theme_css(theme_name)

    dest_css_dir = project_root_dir / "assets" / "css"
    dest_css_dir.mkdir(parents=True, exist_ok=True)

    dest_file = dest_css_dir / f"{theme_name}.css"
    dest_file.write_text(theme_css_content)
    typer.secho(
        f"  - Added theme '{theme_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )
    typer.secho("Done.", fg=typer.colors.GREEN)


@app.command("list")
def list_all():
    """
    List all available items (components, wrapped React components, themes) in the Buridan UI library.
    """
    _update_repo()
    typer.echo("Listing available items from repository...")

    # List Standard Components from base_ui
    if BASE_UI_BASE_COMPONENTS_DIR.exists():
        components = [
            p.stem
            for p in BASE_UI_BASE_COMPONENTS_DIR.iterdir()
            if p.suffix == ".py" and not p.name.startswith("__")
        ]
        typer.echo("\n--- Base UI Components ---")
        for component in sorted(components):
            typer.echo(f"- {component}")

    # List Wrapped React Components
    if WRAPPED_COMPONENTS_DIR.exists():
        wrapped_components = []
        for p in WRAPPED_COMPONENTS_DIR.iterdir():
            if p.name.startswith("__"):
                continue
            if p.is_dir():
                # It's a directory, so it's a component
                wrapped_components.append(p.name)
            elif p.suffix == ".py":
                # It's a file, so it's a component
                wrapped_components.append(p.stem)

        typer.echo("\n--- Wrapped React Components ---")
        for component in sorted(list(set(wrapped_components))):
            typer.echo(f"- {component}")

    # List Themes
    themes = set()
    if THEMES_CSS_FILE.exists():
        # Need to re-read content here as THEMES_CSS_FILE is a Path object
        import re

        content = THEMES_CSS_FILE.read_text()
        theme_pattern = re.compile(r"\.theme-([a-zA-Z0-9-]+)(?:-dark)?\s*{{")
        for match in theme_pattern.finditer(content):
            themes.add(match.group(1))
    typer.echo("\n--- Themes ---")
    for theme in sorted(list(themes)):
        typer.echo(f"- {theme}")


@app.command("interactive")
def interactive():
    """
    Launch the interactive CLI for Buridan UI.
    """
    interactive_cli()


if __name__ == "__main__":
    app()
