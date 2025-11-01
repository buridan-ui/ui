import typer
import pathlib
import shutil
import ast
import subprocess
import re

# --- Constants ---
REPO_URL = "https://github.com/buridan-ui/ui.git"
CACHE_DIR = pathlib.Path.home() / ".buridan" / "repo"

# Source directories from the cloned repo
BASE_UI_DIR = CACHE_DIR / "src" / "docs" / "library" / "base_ui"
BASE_UI_COMPONENTS_DIR = BASE_UI_DIR / "components"
BASE_UI_BASE_COMPONENTS_DIR = BASE_UI_COMPONENTS_DIR / "base"
BASE_UI_ICONS_DIR = BASE_UI_DIR / "icons"
BASE_UI_UTILS_DIR = BASE_UI_DIR / "utils"

WRAPPED_COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "wrapped_components"
THEMES_CSS_FILE = CACHE_DIR / "assets" / "css" / "wrapper.css"


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


def _find_base_ui_component_imports(file_path: pathlib.Path) -> list[str]:
    """Parses a Python file and returns a list of local component dependencies."""
    if not file_path.exists():
        return []
    content = file_path.read_text()
    tree = ast.parse(content)
    dependencies = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.level == 1:
            # Assuming level 1 imports are peer dependencies in the same 'base' directory
            if node.module:
                dependencies.append(node.module)
    return list(set(dependencies))


def _copy_base_ui_scaffolding(app_root_dir: pathlib.Path):
    """Copies the base UI scaffolding (utils, icons, and base component files)."""
    dest_dir = app_root_dir / "components" / "ui"
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir.parent / "__init__.py").touch()
    (dest_dir / "__init__.py").touch()

    # Copy icons and utils directories
    icons_dest = dest_dir / "icons"
    if not icons_dest.exists():
        shutil.copytree(BASE_UI_ICONS_DIR, icons_dest)
        typer.secho(
            f"  - Added icons to {icons_dest.relative_to(pathlib.Path.cwd())}",
            fg=typer.colors.BLUE,
        )

    utils_dest = dest_dir / "utils"
    if not utils_dest.exists():
        shutil.copytree(BASE_UI_UTILS_DIR, utils_dest)
        typer.secho(
            f"  - Added utils to {utils_dest.relative_to(pathlib.Path.cwd())}",
            fg=typer.colors.BLUE,
        )

    # Copy base_ui.py and component.py
    for base_file in ["base_ui.py", "component.py"]:
        source = BASE_UI_COMPONENTS_DIR / base_file
        dest = dest_dir / base_file
        if not dest.exists():
            shutil.copy(source, dest)
            typer.secho(
                f"  - Added base file '{base_file}' to {dest.relative_to(pathlib.Path.cwd())}",
                fg=typer.colors.BLUE,
            )

    # Ensure base component directory exists
    (dest_dir / "base").mkdir(exist_ok=True)
    (dest_dir / "base" / "__init__.py").touch()


def _add_base_ui_component(
    component_name: str, added_items: set, app_root_dir: pathlib.Path
):
    """Adds a single base_ui component and its dependencies."""
    if component_name in added_items:
        return

    source_file = BASE_UI_BASE_COMPONENTS_DIR / f"{component_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Component '{component_name}' not found in base_ui components.",
            fg=typer.colors.RED,
        )
        # Check for older components for backward compatibility
        old_source_file = (
            CACHE_DIR
            / "src"
            / "docs"
            / "library"
            / "components"
            / component_name
            / f"{component_name}.py"
        )
        if old_source_file.exists():
            typer.secho(
                f"Note: '{component_name}' seems to be an older component. Please check its dependencies manually.",
                fg=typer.colors.YELLOW,
            )
            # Fallback to old logic if needed, or just inform user. For now, just informing.
        return

    added_items.add(component_name)

    # Copy scaffolding first
    if "base_ui_scaffold" not in added_items:
        _copy_base_ui_scaffolding(app_root_dir)
        added_items.add("base_ui_scaffold")

    dest_file = app_root_dir / "components" / "ui" / "base" / f"{component_name}.py"
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Added component '{component_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )

    dependencies = _find_base_ui_component_imports(source_file)
    for dep_name in dependencies:
        _add_base_ui_component(dep_name, added_items, app_root_dir)


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


def _add_wrapped_react(
    component_name: str, added_items: set, app_root_dir: pathlib.Path
):
    """Adds a single wrapped react component and its utility dependencies."""
    if component_name in added_items:
        return
    added_items.add(component_name)

    source_file = WRAPPED_COMPONENTS_DIR / f"{component_name}.py"
    if not source_file.is_file():
        source_file = WRAPPED_COMPONENTS_DIR / component_name / f"{component_name}.py"

    if not source_file.exists():
        typer.secho(
            f"Wrapped React component '{component_name}' not found in repository.",
            fg=typer.colors.RED,
        )
        return

    dest_dir = app_root_dir / "components" / "wrapped_react"
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "__init__.py").touch()
    (dest_dir.parent / "__init__.py").touch()

    dest_file = dest_dir / f"{component_name}.py"
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Added wrapped react component '{component_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )

    # Wrapped components might have util dependencies from the old structure
    dependencies = _find_util_imports(dest_file)
    if dependencies:
        # This part needs to be thought out. For now, let's assume wrapped components are self-contained
        # or their utils are handled differently. The user request is about base_ui components.
        typer.secho(
            f"  - Note: Wrapped component might have legacy util dependencies: {dependencies}. Please verify.",
            fg=typer.colors.YELLOW,
        )


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
        rf"(\.(?:theme-{re.escape(theme_name)}))\s*{{([^}}]*)}}", re.DOTALL
    )
    # Regex to find the dark theme block
    dark_theme_pattern = re.compile(
        rf"(\.(?:theme-{re.escape(theme_name)}-dark))\s*{{([^}}]*)}}", re.DOTALL
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

    return "\n\n".join(extracted_css)


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
