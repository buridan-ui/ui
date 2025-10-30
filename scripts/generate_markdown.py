import re
import inspect
import pathlib
import importlib
import sys
import ast
import shutil

# Add the project root to the Python path to allow imports from 'src'
ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

# --- PATHS ---
DOCS_SOURCE_DIR = ROOT_DIR / "docs"
MARKDOWN_OUTPUT_DIR = ROOT_DIR / "assets" / "docs"  # Updated output directory
COMPONENTS_LIBRARY_DIR = ROOT_DIR / "src" / "docs" / "library"


def dynamic_load_components(directory: pathlib.Path) -> dict:
    """
    Dynamically loads component functions and classes from a given directory
    and its subdirectories.
    """
    registry = {}
    for py_file in directory.rglob("*.py"):
        if py_file.name.startswith("__"):
            continue

        relative_py_file = py_file.relative_to(ROOT_DIR)
        module_path = ".".join(relative_py_file.with_suffix("").parts)

        try:
            module = importlib.import_module(module_path)
            for name, obj in inspect.getmembers(module):
                if (
                    inspect.isfunction(obj) or inspect.isclass(obj)
                ) and obj.__module__ == module.__name__:
                    registry[name.lower()] = obj
        except Exception as e:
            print(
                f"Warning: Could not import from module {module_path}. Error: {e}",
                file=sys.stderr,
            )
    return registry


def get_source_code(
    command: str, argument: str | None, registry: dict
) -> tuple[str, str] | None:
    """
    Retrieves the source code for a component based on the parsed command and argument.
    Returns a tuple of (code, language) or None if not found.
    """
    command_lower = command.lower()
    arg_lower = argument.lower() if argument else None

    func_name = None
    language = "python"

    if command_lower in [
        "demo_and_single_function",
        "full_source_page_of_component",
    ]:
        func_name = arg_lower
    elif command_lower == "show_code_with_language":
        try:
            args = ast.literal_eval(argument)
            if isinstance(args, list) and len(args) > 0:
                func_name = args[0].lower()
                if len(args) > 1 and args[1]:
                    language = args[1]
        except (ValueError, SyntaxError) as e:
            print(
                f"Warning: Could not parse argument for SHOW_CODE_WITH_LANGUAGE: {argument}. Error: {e}",
                file=sys.stderr,
            )
            return None
    elif arg_lower is None and command_lower in registry:
        func_name = command_lower

    if not func_name or func_name not in registry:
        return None

    func_obj = registry[func_name]

    try:
        if command_lower == "full_source_page_of_component":
            source_file = inspect.getfile(func_obj)
            code = pathlib.Path(source_file).read_text()
        else:
            code = inspect.getsource(func_obj)
        return code, language
    except Exception as e:
        print(
            f"Warning: Could not get source for '{func_name}'. Error: {e}",
            file=sys.stderr,
        )

    return None


def convert_to_pure_markdown(content: str, registry: dict) -> str:
    """
    Replaces custom component delimiters in markdown content with formatted code blocks.
    """
    delimiter_pattern = r"--([\w_]+)(?:\((.*)\))?--"

    def replacer(match):
        command = match.group(1)
        argument = match.group(2)

        if command.lower() == "cli_and_manual_installation":
            if not argument:
                return "Error: Missing argument for CLI_AND_MANUAL_INSTALLATION"

            try:
                args = ast.literal_eval(argument)
                if not isinstance(args, list) or len(args) != 2:
                    return (
                        "Error: Invalid argument format for CLI_AND_MANUAL_INSTALLATION"
                    )

                component_name, cli_command = args
                component_name_lower = component_name.lower()

                if component_name_lower not in registry:
                    return f"Error: Component '{component_name}' not found in registry."

                func = registry[component_name_lower]
                source_file = inspect.getfile(func)
                source_code = pathlib.Path(source_file).read_text()

                cli_section = f"### CLI\n\n```bash\n{cli_command}\n```"
                manual_section = (
                    f"### Manual Installation\n\n```python\n{source_code.strip()}\n```"
                )

                return f"\n{cli_section}\n\n{manual_section}\n"

            except (ValueError, SyntaxError, IndexError) as e:
                return f"Error parsing arguments for CLI_AND_MANUAL_INSTALLATION: {e}"
            except Exception as e:
                return f"Error processing CLI_AND_MANUAL_INSTALLATION: {e}"

        # Fallback to old logic for other commands
        source_info = get_source_code(command, argument, registry)
        if source_info:
            code, language = source_info
            return f"\n```{language}\n{code.strip()}\n```\n"
        return ""

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) > 2:
            content = parts[2]

    return re.sub(delimiter_pattern, replacer, content)


def main():
    """Main function to generate pure markdown files from the docs directory."""
    print("Starting markdown generation process...")

    # Clean up old output directories
    print("Cleaning up old output directories...")
    dirs_to_clean = [
        ROOT_DIR / "markdown",
        ROOT_DIR / "assets" / "markdown",
        MARKDOWN_OUTPUT_DIR,
    ]
    for d in dirs_to_clean:
        if d.exists():
            shutil.rmtree(d)
            print(f"Removed old directory: {d}")

    # Load components
    print(f"Loading components from: {COMPONENTS_LIBRARY_DIR}")
    component_registry = dynamic_load_components(COMPONENTS_LIBRARY_DIR)
    print(f"Successfully loaded {len(component_registry)} components.")

    # Ensure output directory exists
    MARKDOWN_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory set to: {MARKDOWN_OUTPUT_DIR}")

    # Process markdown files
    print(f"Processing markdown files from: {DOCS_SOURCE_DIR}")
    file_count = 0
    for md_file in DOCS_SOURCE_DIR.rglob("*.md"):
        file_count += 1
        original_content = md_file.read_text()
        pure_md_content = convert_to_pure_markdown(original_content, component_registry)

        # Create new path with hyphens
        relative_path = md_file.relative_to(DOCS_SOURCE_DIR)
        hyphenated_parts = [part.replace("_", "-") for part in relative_path.parts]
        hyphenated_relative_path = pathlib.Path(*hyphenated_parts)
        output_path = MARKDOWN_OUTPUT_DIR / hyphenated_relative_path

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(pure_md_content)

        print(f"Processed: {md_file.relative_to(ROOT_DIR)}. Status: OK")

    print(f"\nMarkdown generation complete. Processed {file_count} files.")


if __name__ == "__main__":
    main()
