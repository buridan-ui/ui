import typer
import pathlib
import shutil
import ast
import subprocess

app = typer.Typer()
add_app = typer.Typer()
app.add_typer(add_app, name="add")

# --- Constants ---
REPO_URL = "https://github.com/buridan-ui/ui.git"
CACHE_DIR = pathlib.Path.home() / ".buridan" / "repo"

# Correctly define source directories based on the CACHE_DIR
COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "components"
WRAPPED_COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "wrapped_components"
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
        if isinstance(node, ast.Call):
            # Check if it's a call to rx.Config
            if isinstance(node.func, ast.Attribute) and node.func.attr == "Config":
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "rx":
                    # Find the app_name keyword argument
                    for keyword in node.keywords:
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
def list_components():
    """
    List available components in the Buridan UI library.
    """
    _update_repo()
    typer.echo("Listing available components from repository...")
    components = [p.name for p in COMPONENTS_DIR.iterdir() if p.is_dir()]
    wrapped_components = [
        p.name for p in WRAPPED_COMPONENTS_DIR.iterdir() if p.is_dir()
    ]
    typer.echo("\n--- Standard Components ---")
    for component in sorted(components):
        typer.echo(f"- {component}")
    typer.echo("\n--- Wrapped React Components ---")
    for component in sorted(wrapped_components):
        typer.echo(f"- {component}")


if __name__ == "__main__":
    app()
