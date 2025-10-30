"""
Script to sync components from reflex-ui repo to local UI library.

This script:
1. Clones/updates the reflex-ui repo in a cache directory
2. Copies necessary files (utils, base components, and all component files)
3. Rewrites imports to use relative imports
"""

import re
import subprocess
from pathlib import Path
from typing import List

# Configuration
REPO_URL = "https://github.com/reflex-dev/reflex-ui"
CACHE_DIR = Path(".reflex_ui_cache")
LOCAL_UI_PATH = Path("src/docs/library/base_ui")

# Source paths in the reflex-ui repo
SOURCE_UTILS = "reflex_ui/utils/twmerge.py"
SOURCE_COMPONENTS_DIR = "reflex_ui/components"
SOURCE_BASE_FILES = ["base_ui.py", "component.py"]
SOURCE_BASE_COMPONENTS = "reflex_ui/components/base"


def run_command(cmd: List[str], cwd: Path = None) -> bool:
    """Run a shell command and return success status."""
    try:
        # result = subprocess.run(
        #     cmd, cwd=cwd, capture_output=True, text=True, check=True
        # )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}")
        print(f"Error: {e.stderr}")
        return False


def clone_or_update_repo() -> bool:
    """Clone the repo if it doesn't exist, or pull latest changes if it does."""
    if CACHE_DIR.exists():
        print(f"Cache directory exists at {CACHE_DIR}")
        print("Checking for updates...")

        # Check if there are any remote changes
        if not run_command(["git", "fetch"], cwd=CACHE_DIR):
            return False

        # Check if local is behind remote
        result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD..origin/main"],
            cwd=CACHE_DIR,
            capture_output=True,
            text=True,
        )

        commits_behind = result.stdout.strip()
        if commits_behind and commits_behind != "0":
            print(f"Repository is {commits_behind} commits behind. Pulling updates...")
            if not run_command(["git", "pull"], cwd=CACHE_DIR):
                return False
            print("Repository updated successfully!")
        else:
            print("Repository is up to date. Skipping clone/pull.")
    else:
        print(f"Cloning repository to {CACHE_DIR}...")
        if not run_command(["git", "clone", REPO_URL, str(CACHE_DIR)]):
            return False
        print("Repository cloned successfully!")

    return True


def convert_imports(content: str) -> str:
    """Convert absolute imports to relative imports."""
    # Pattern to match reflex_ui imports
    patterns = [
        #
        (
            r"from reflex_ui\.components\.icons\.others import",
            "from ...icons.others import",
        ),
        # from reflex_ui.components.icons.hugeicon
        (
            r"from reflex_ui\.components\.icons\.hugeicon import",
            "from ...icons.hugeicon import",
        ),
        # from from reflex_ui.components.component ...
        # (r'from reflex_ui\.components\.component import', 'from .component import'),
        # from reflex_ui.components.base_ui import ...
        (r"from reflex_ui\.components\.base_ui import", "from ..base_ui import"),
        # from reflex_ui.components.component import ...
        (r"from reflex_ui\.components\.component import", "from ..component import"),
        # from reflex_ui.utils.twmerge import ...
        (r"from reflex_ui\.utils\.twmerge import", "from ...utils.twmerge import"),
        # Any other reflex_ui.components imports (catch-all)
        (r"from reflex_ui\.components\.([a-zA-Z_]+) import", r"from .\1 import"),
    ]

    modified_content = content
    for pattern, replacement in patterns:
        modified_content = re.sub(pattern, replacement, modified_content)

    return modified_content


def copy_file(source: Path, dest: Path, convert_imports_flag: bool = True) -> None:
    """Copy a file and optionally convert its imports."""
    # Read source file
    with open(source, "r", encoding="utf-8") as f:
        content = f.read()

    # Convert imports if requested
    if convert_imports_flag:
        content = convert_imports(content)

    # Ensure destination directory exists
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Write to destination
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✓ Copied: {source.name}")


def should_skip_file(filename: str) -> bool:
    """Check if a file should be skipped."""
    skip_patterns = ["__init__.py", "__pycache__", ".pyc", ".pyo"]
    return any(pattern in filename for pattern in skip_patterns)


def sync_components() -> None:
    """Main function to sync components from reflex-ui to local library."""
    print("=" * 60)
    print("Reflex UI Component Sync")
    print("=" * 60)

    # Step 1: Clone or update the repository
    if not clone_or_update_repo():
        print("Failed to clone/update repository. Exiting.")
        return

    print("\n" + "=" * 60)
    print("Copying files...")
    print("=" * 60)

    # Step 2: Create directory structure
    components_dest = LOCAL_UI_PATH / "components"
    utils_dest = LOCAL_UI_PATH / "utils"
    base_dest = LOCAL_UI_PATH / "components" / "base"

    # Step 3: Copy utils/twmerge.py
    print("\n[1/3] Copying utils...")
    source_twmerge = CACHE_DIR / SOURCE_UTILS
    dest_twmerge = utils_dest / "twmerge.py"
    if source_twmerge.exists():
        copy_file(source_twmerge, dest_twmerge)
    else:
        print(f"  ⚠ Warning: {SOURCE_UTILS} not found")

    # Step 4: Copy base component files
    print("\n[2/3] Copying base component files...")
    source_components = CACHE_DIR / SOURCE_COMPONENTS_DIR
    for base_file in SOURCE_BASE_FILES:
        source_file = source_components / base_file
        dest_file = components_dest / base_file
        if source_file.exists():
            copy_file(source_file, dest_file)
        else:
            print(f"  ⚠ Warning: {base_file} not found")

    # Step 5: Copy all component files from base/
    print("\n[3/3] Copying component files from base/...")
    source_base = CACHE_DIR / SOURCE_BASE_COMPONENTS

    if source_base.exists() and source_base.is_dir():
        component_files = [
            f
            for f in source_base.iterdir()
            if f.is_file() and f.suffix == ".py" and not should_skip_file(f.name)
        ]

        for component_file in component_files:
            dest_file = base_dest / component_file.name
            copy_file(component_file, dest_file)

        print(f"\nTotal components copied: {len(component_files)}")
    else:
        print(f"  ⚠ Warning: {SOURCE_BASE_COMPONENTS} directory not found")

    # Step 6: Create __init__.py files if they don't exist
    print("\n" + "=" * 60)
    print("Creating __init__.py files...")
    print("=" * 60)

    init_dirs = [LOCAL_UI_PATH, utils_dest, components_dest, base_dest]
    for dir_path in init_dirs:
        init_file = dir_path / "__init__.py"
        if not init_file.exists():
            init_file.parent.mkdir(parents=True, exist_ok=True)
            init_file.touch()
            print(f"  ✓ Created: {init_file.relative_to(LOCAL_UI_PATH.parent)}")

    print("\n" + "=" * 60)
    print("✨ Sync completed successfully!")
    print("=" * 60)
    print(f"\nComponents synced to: {LOCAL_UI_PATH}")


if __name__ == "__main__":
    sync_components()
