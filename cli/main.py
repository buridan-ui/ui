import typer
import pathlib
import shutil
import ast
import subprocess
import re

app = typer.Typer()
add_app = typer.Typer()
app.add_typer(add_app, name="add")

# --- Constants ---
REPO_URL = "https://github.com/buridan-ui/ui.git"
CACHE_DIR = pathlib.Path.home() / ".buridan" / "repo"

# Correctly define source directories based on the CACHE_DIR
COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "components"
WRAPPED_COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "wrapped_components"
THEMES_CSS_FILE = CACHE_DIR / "assets" / "css" / "wrapper.css"
UTILS_DIR = CACHE_DIR / "src" / "utils"


def _run_git_command(command: list[str], cwd: pathlib.Path | None = None):
    """Runs a git command and handles errors."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        typer.secho(
            "Error: git is not installed. Please install git to use this feature.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    except subprocess.CalledProcessError as e:
        typer.secho(f"Git command failed: {e.stderr}", fg=typer.colors.RED)
        raise typer.Exit(1)


def _update_repo():
    """Clones or pulls the Buridan UI repository."""
    typer.secho("Updating component library...", fg=typer.colors.YELLOW)
    if not CACHE_DIR.exists():
        typer.echo(f"Cloning repository into {CACHE_DIR}...")
        CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)
        _run_git_command(["git", "clone", REPO_URL, str(CACHE_DIR)])
    else:
        typer.echo(f"Pulling latest changes in {CACHE_DIR}...")
        _run_git_command(["git", "-C", str(CACHE_DIR), "pull"])
    typer.secho("Component library is up to date.", fg=typer.colors.GREEN)


def _find_util_imports(file_path: pathlib.Path) -> list[str]:
    """Parses a Python file and returns a list of util dependencies."""
    if not file_path.exists():
        return []
    content = file_path.read_text()
    tree = ast.parse(content)
    dependencies = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and node.module.startswith("src.utils"):
                util_name = node.module.split(".")[2]
                dependencies.append(util_name)
    return list(set(dependencies))


def _extract_theme_css(theme_name: str) -> str:
    """Extracts the CSS for a given theme and its dark variant from wrapper.css."""
    if not THEMES_CSS_FILE.exists():
        typer.secho(
            f"Error: Theme CSS file not found at {THEMES_CSS_FILE}.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    content = THEMES_CSS_FILE.read_text()
    extracted_css = []

    # Regex to find the light theme block
    light_theme_pattern = re.compile(
        rf"(\.theme-{re.escape(theme_name)})\s*{{([^}}]+)}}", re.DOTALL
    )
    # Regex to find the dark theme block
    dark_theme_pattern = re.compile(
        rf"(\.theme-{re.escape(theme_name)}-dark)\s*{{([^}}]+)}}", re.DOTALL
    )

    light_match = light_theme_pattern.search(content)
    if light_match:
        extracted_css.append(f"{light_match.group(1)} {{{light_match.group(2)}}}")
    else:
        typer.secho(
            f"Warning: Light theme '.theme-{theme_name}' not found in wrapper.css.",
            fg=typer.colors.YELLOW,
        )

    dark_match = dark_theme_pattern.search(content)
    if dark_match:
        extracted_css.append(f"{dark_match.group(1)} {{{dark_match.group(2)}}}")
    else:
        typer.secho(
            f"Warning: Dark theme '.theme-{theme_name}-dark' not found in wrapper.css.",
            fg=typer.colors.YELLOW,
        )

    if not extracted_css:
        typer.secho(
            f"Error: No CSS found for theme '{theme_name}' or its dark variant.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    return "\\n\\n".join(extracted_css)


def _add_component(component_name: str, added_items: set, app_root_dir: pathlib.Path):
    """Adds a single component and its utility dependencies."""
    if component_name in added_items:
        return
    added_items.add(component_name)

    source_file = COMPONENTS_DIR / component_name / f"{component_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Component '{component_name}' not found in repository.",
            fg=typer.colors.RED,
        )
        return

    dest_file = app_root_dir / "components" / "ui" / f"{component_name}.py"
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Added component '{component_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )

    dependencies = _find_util_imports(dest_file)
    for util_name in set(dependencies):
        _add_utility(util_name, added_items, app_root_dir)


def _add_wrapped_react(
    component_name: str, added_items: set, app_root_dir: pathlib.Path
):
    """Adds a single wrapped react component and its utility dependencies."""
    if component_name in added_items:
        return
    added_items.add(component_name)

    source_file = WRAPPED_COMPONENTS_DIR / component_name / f"{component_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Wrapped React component '{component_name}' not found in repository.",
            fg=typer.colors.RED,
        )
        return

    dest_file = app_root_dir / "components" / "ui" / f"{component_name}.py"
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Added wrapped react component '{component_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )

    dependencies = _find_util_imports(dest_file)
    for util_name in set(dependencies):
        _add_utility(util_name, added_items, app_root_dir)


@add_app.command("wrapped-react")
def add_wrapped_react(component: str):
    """
    Add a wrapped React component and its dependencies to your Reflex project.
    """
    _check_reflex_project()
    app_name = _get_app_name()
    app_root_dir = pathlib.Path.cwd() / app_name

    _update_repo()
    _ensure_package_structure(app_root_dir)
    typer.secho(
        f"Adding wrapped React component: '{component}'...", fg=typer.colors.GREEN
    )
    added_items = set()
    _add_wrapped_react(component, added_items, app_root_dir)
    typer.secho("Done.", fg=typer.colors.GREEN)


@add_app.command("theme")
def add_theme(theme_name: str):
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


def _add_utility(util_name: str, added_items: set, app_root_dir: pathlib.Path):
    """Adds a single utility file from the cache."""
    if util_name in added_items:
        return
    added_items.add(util_name)

    source_file = UTILS_DIR / f"{util_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Utility '{util_name}' not found in repository.", fg=typer.colors.YELLOW
        )
        return

    dest_util_dir = app_root_dir / "components" / "ui" / "utils"
    dest_util_dir.mkdir(parents=True, exist_ok=True)
    (dest_util_dir / "__init__.py").touch()

    dest_file = dest_util_dir / f"{util_name}.py"
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Added dependency '{util_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.BLUE,
    )


def _ensure_package_structure(app_root_dir: pathlib.Path):
    """Ensures the destination directories are valid Python packages."""
    (app_root_dir / "components").mkdir(parents=True, exist_ok=True)
    (app_root_dir / "components" / "__init__.py").touch()

    (app_root_dir / "components" / "ui").mkdir(exist_ok=True)
    (app_root_dir / "components" / "ui" / "__init__.py").touch()


def _get_app_name() -> str:
    """Parses rxconfig.py to find the app_name."""
    rxconfig_path = pathlib.Path.cwd() / "rxconfig.py"
    content = rxconfig_path.read_text()
    tree = ast.parse(content)

    app_name = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.targets[0], ast.Name) and node.targets[0].id == "config":
                if isinstance(node.value, ast.Call):
                    # Check if it's a call to a Config class (e.g., BuridanuiConfig or rx.Config)
                    if isinstance(node.value.func, (ast.Name, ast.Attribute)):
                        for keyword in node.value.keywords:
                            if keyword.arg == "app_name":
                                if isinstance(keyword.value, ast.Constant):
                                    app_name = keyword.value.value
                                    break
            if app_name:
                break

    if not app_name:
        typer.secho(
            "Error: Could not find 'app_name' in rxconfig.py.", fg=typer.colors.RED
        )
        raise typer.Exit(1)
    return app_name


def _check_reflex_project():
    """Check if the command is run from the root of a Reflex project."""
    if not (pathlib.Path.cwd() / "rxconfig.py").exists():
        typer.secho(
            "Error: This command must be run from the root of a Reflex project.",
            fg=typer.colors.RED,
        )
        typer.secho("('rxconfig.py' not found)", fg=typer.colors.RED)
        raise typer.Exit(1)


@add_app.command("component")
def add_component(component: str):
    """
    Add a component and its dependencies to your Reflex project.
    """
    _check_reflex_project()
    app_name = _get_app_name()
    app_root_dir = pathlib.Path.cwd() / app_name

    _update_repo()
    _ensure_package_structure(app_root_dir)
    typer.secho(f"Adding component: '{component}'...", fg=typer.colors.GREEN)
    added_items = set()
    _add_component(component, added_items, app_root_dir)
    typer.secho("Done.", fg=typer.colors.GREEN)


@app.command("list")
def list_all():
    """
    List all available items (components, wrapped React components, themes) in the Buridan UI library.
    """
    _update_repo()
    typer.echo("Listing available items from repository...")

    # List Standard Components
    components = [p.name for p in COMPONENTS_DIR.iterdir() if p.is_dir()]
    typer.echo("\n--- Standard Components ---")
    for component in sorted(components):
        typer.echo(f"- {component}")

    # List Wrapped React Components
    wrapped_components = [
        p.name for p in WRAPPED_COMPONENTS_DIR.iterdir() if p.is_dir()
    ]
    typer.echo("\n--- Wrapped React Components ---")
    for component in sorted(wrapped_components):
        typer.echo(f"- {component}")

    # List Themes
    themes = set()
    if THEMES_CSS_FILE.exists():
        content = THEMES_CSS_FILE.read_text()
        # Regex to find base theme names (e.g., .theme-blue, ignoring -dark suffix)
        theme_pattern = re.compile(r"\.theme-([a-zA-Z0-9-]+?)(?:-dark)?\s*{")
        for match in theme_pattern.finditer(content):
            themes.add(match.group(1))
    typer.echo("\n--- Themes ---")
    for theme in sorted(list(themes)):
        typer.echo(f"- {theme}")


if __name__ == "__main__":
    app()
