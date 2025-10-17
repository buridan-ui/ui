import typer
import pathlib
import shutil
import ast
import subprocess

app = typer.Typer()

# --- Constants ---
REPO_URL = "https://github.com/buridan-ui/ui.git"
CACHE_DIR = pathlib.Path.home() / ".buridan" / "repo"
DEST_DIR = pathlib.Path.cwd() / "components" / "ui"

# Correctly define source directories based on the CACHE_DIR
COMPONENTS_DIR = CACHE_DIR / "src" / "docs" / "library" / "components"
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


def _find_internal_imports(file_path: pathlib.Path) -> list[str]:
    """Parses a Python file and returns a list of internal imports (from src)."""
    # ... (implementation remains the same)
    if not file_path.exists():
        return []
    content = file_path.read_text()
    tree = ast.parse(content)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and node.module.startswith("src."):
                imports.append(node.module)
    return imports


def _pull_component(component_name: str, pulled_items: set):
    """Pulls a single component and its dependencies from the cache."""
    # ... (implementation remains the same, but sources from CACHE_DIR)
    if component_name in pulled_items:
        return
    pulled_items.add(component_name)

    source_file = COMPONENTS_DIR / component_name / f"{component_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Component '{component_name}' not found in repository.",
            fg=typer.colors.RED,
        )
        return

    dest_file = DEST_DIR / f"{component_name}.py"
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Pulled component '{component_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.CYAN,
    )

    dependencies = _find_internal_imports(dest_file)
    for dep in dependencies:
        parts = dep.split(".")
        if len(parts) > 2 and parts[1] == "utils":
            util_name = parts[2]
            _pull_utility(util_name, pulled_items)


def _pull_utility(util_name: str, pulled_items: set):
    """Pulls a single utility file from the cache."""
    # ... (implementation remains the same, but sources from CACHE_DIR)
    if util_name in pulled_items:
        return
    pulled_items.add(util_name)

    source_file = UTILS_DIR / f"{util_name}.py"
    if not source_file.exists():
        typer.secho(
            f"Utility '{util_name}' not found in repository.", fg=typer.colors.YELLOW
        )
        return

    dest_util_dir = DEST_DIR / "utils"
    dest_util_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_util_dir / f"{util_name}.py"

    init_file = dest_util_dir / "__init__.py"
    if not init_file.exists():
        init_file.touch()

    shutil.copy(source_file, dest_file)
    typer.secho(
        f"  - Pulled dependency '{util_name}' to {dest_file.relative_to(pathlib.Path.cwd())}",
        fg=typer.colors.BLUE,
    )


@app.command("pull")
def pull(component: str):
    """
    Pull a component and its dependencies from the Buridan UI GitHub repository.
    """
    _update_repo()
    typer.secho(f"Starting pull for component: '{component}'...", fg=typer.colors.GREEN)
    pulled_items = set()
    _pull_component(component, pulled_items)
    typer.secho("Done.", fg=typer.colors.GREEN)


@app.command("list")
def list_components():
    """
    List available components in the Buridan UI library.
    """
    _update_repo()
    typer.echo("Listing available components from repository...")
    components = [p.name for p in COMPONENTS_DIR.iterdir() if p.is_dir()]
    for component in sorted(components):
        typer.echo(f"- {component}")


if __name__ == "__main__":
    app()
