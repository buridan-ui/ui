import typer
import pathlib
import sys

# Add the parent directory to the sys.path to allow importing from utils.py
sys.path.append(str(pathlib.Path(__file__).parent))

from utils import (
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

try:
    import inquirer
except ImportError:
    typer.secho(
        "Error: 'inquirer' is not installed. Please install it using 'pip install inquirer'.",
        fg=typer.colors.RED,
    )
    raise typer.Exit(1)


def _get_available_base_ui_components():
    if not BASE_UI_BASE_COMPONENTS_DIR.exists():
        return []
    return sorted(
        [
            p.stem
            for p in BASE_UI_BASE_COMPONENTS_DIR.iterdir()
            if p.suffix == ".py" and not p.name.startswith("__")
        ]
    )


def _get_available_wrapped_react_components():
    if not WRAPPED_COMPONENTS_DIR.exists():
        return []
    wrapped_components = []
    for p in WRAPPED_COMPONENTS_DIR.iterdir():
        if p.name.startswith("__"):
            continue
        if p.is_dir():
            wrapped_components.append(p.name)
        elif p.suffix == ".py":
            wrapped_components.append(p.stem)
    return sorted(list(set(wrapped_components)))


def _get_available_themes():
    themes = set()
    if THEMES_CSS_FILE.exists():
        content = THEMES_CSS_FILE.read_text()
        import re

        theme_pattern = re.compile(r"\.theme-([a-zA-Z0-9-]+)(?:-dark)?\s*\{")
        for match in theme_pattern.finditer(content):
            themes.add(match.group(1))
    return sorted(list(themes))


def interactive_cli():
    _update_repo()  # Ensure local repo is up to date

    while True:
        questions = [
            inquirer.List(
                "main_choice",
                message="What do you want to do?",
                choices=[
                    "List Base UI Components",
                    "List Wrapped React Components",
                    "List Themes",
                    "Add Base UI Component",
                    "Add Wrapped React Component",
                    "Add Theme",
                    "Exit",
                ],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers is None or answers["main_choice"] == "Exit":
            typer.secho("Exiting interactive CLI. Goodbye!", fg=typer.colors.GREEN)
            break

        choice = answers["main_choice"]

        if choice == "List Base UI Components":
            components = _get_available_base_ui_components()
            if components:
                typer.secho(
                    "\n--- Available Base UI Components ---", fg=typer.colors.YELLOW
                )
                for comp in components:
                    typer.echo(f"- {comp}")
            else:
                typer.secho("No Base UI components found.", fg=typer.colors.YELLOW)
            input("\nPress Enter to continue...")

        elif choice == "List Wrapped React Components":
            wrapped_components = _get_available_wrapped_react_components()
            if wrapped_components:
                typer.secho(
                    "\n--- Available Wrapped React Components ---",
                    fg=typer.colors.YELLOW,
                )
                for comp in wrapped_components:
                    typer.echo(f"- {comp}")
            else:
                typer.secho(
                    "No Wrapped React components found.", fg=typer.colors.YELLOW
                )
            input("\nPress Enter to continue...")

        elif choice == "List Themes":
            themes = _get_available_themes()
            if themes:
                typer.secho("\n--- Available Themes ---", fg=typer.colors.YELLOW)
                for theme in themes:
                    typer.echo(f"- {theme}")
            else:
                typer.secho("No themes found.", fg=typer.colors.YELLOW)
            input("\nPress Enter to continue...")

        elif choice == "Add Base UI Component":
            _check_reflex_project()
            app_name = _get_app_name()
            app_root_dir = pathlib.Path.cwd() / app_name
            components = _get_available_base_ui_components()
            if not components:
                typer.secho(
                    "No Base UI components available to add.", fg=typer.colors.RED
                )
                input("\nPress Enter to continue...")
                continue

            comp_questions = [
                inquirer.List(
                    "component_to_add",
                    message="Select Base UI Component to Add",
                    choices=components,
                ),
            ]
            comp_answers = inquirer.prompt(comp_questions)
            if comp_answers and comp_answers["component_to_add"]:
                component_to_add = comp_answers["component_to_add"]
                typer.secho(
                    f"Adding Base UI component: '{component_to_add}'...",
                    fg=typer.colors.GREEN,
                )
                added_items = set()
                _add_base_ui_component(component_to_add, added_items, app_root_dir)
                typer.secho("Done.", fg=typer.colors.GREEN)
            input("\nPress Enter to continue...")

        elif choice == "Add Wrapped React Component":
            _check_reflex_project()
            app_name = _get_app_name()
            app_root_dir = pathlib.Path.cwd() / app_name
            wrapped_components = _get_available_wrapped_react_components()
            if not wrapped_components:
                typer.secho(
                    "No Wrapped React components available to add.", fg=typer.colors.RED
                )
                input("\nPress Enter to continue...")
                continue

            comp_questions = [
                inquirer.List(
                    "component_to_add",
                    message="Select Wrapped React Component to Add",
                    choices=wrapped_components,
                ),
            ]
            comp_answers = inquirer.prompt(comp_questions)
            if comp_answers and comp_answers["component_to_add"]:
                component_to_add = comp_answers["component_to_add"]
                typer.secho(
                    f"Adding Wrapped React component: '{component_to_add}'...",
                    fg=typer.colors.GREEN,
                )
                added_items = set()
                _add_wrapped_react(component_to_add, added_items, app_root_dir)
                typer.secho("Done.", fg=typer.colors.GREEN)
            input("\nPress Enter to continue...")

        elif choice == "Add Theme":
            _check_reflex_project()
            project_root_dir = pathlib.Path.cwd()
            themes = _get_available_themes()
            if not themes:
                typer.secho("No themes available to add.", fg=typer.colors.RED)
                input("\nPress Enter to continue...")
                continue

            theme_questions = [
                inquirer.List(
                    "theme_to_add",
                    message="Select Theme to Add",
                    choices=themes,
                ),
            ]
            theme_answers = inquirer.prompt(theme_questions)
            if theme_answers and theme_answers["theme_to_add"]:
                theme_to_add = theme_answers["theme_to_add"]
                typer.secho(f"Adding theme: '{theme_to_add}'...", fg=typer.colors.GREEN)
                try:
                    theme_css_content = _extract_theme_css(theme_to_add)
                    dest_css_dir = project_root_dir / "assets" / "css"
                    dest_css_dir.mkdir(parents=True, exist_ok=True)
                    dest_file = dest_css_dir / f"{theme_to_add}.css"
                    dest_file.write_text(theme_css_content)
                    typer.secho(
                        f"  - Added theme '{theme_to_add}' to {dest_file.relative_to(pathlib.Path.cwd())}",
                        fg=typer.colors.CYAN,
                    )
                    typer.secho("Done.", fg=typer.colors.GREEN)
                except typer.Exit:  # Catch Exit from _extract_theme_css
                    pass
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    interactive_cli()
