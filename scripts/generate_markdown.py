import re
import inspect
import pathlib
import importlib
import sys
import ast

# Add the project root to the Python path to allow imports from 'src'
ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

# --- PATHS ---
DOCS_SOURCE_DIR = ROOT_DIR / "docs"
MARKDOWN_OUTPUT_DIR = ROOT_DIR / "markdown"
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

        # Construct the module path from the file path
        # e.g., /path/to/project/src/docs/library/button.py -> src.docs.library.button
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

    # Determine the function name from the command/argument
    if command_lower in ["demo_and_single_function", "full_source_page_of_component"]:
        func_name = arg_lower
    elif command_lower == "show_code_with_language":
        try:
            # Safely evaluate something like "['my_func', 'python']"
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

    if not func_name:
        return None

    if func_name not in registry:
        print(
            f"Warning: Component '{func_name}' not found in registry.", file=sys.stderr
        )
        return None

    func_obj = registry[func_name]

    try:
        if command_lower == "full_source_page_of_component":
            source_file = inspect.getfile(func_obj)
            code = pathlib.Path(source_file).read_text()
        else:
            code = inspect.getsource(func_obj)
        return code, language
    except TypeError:
        # This can happen if the object is a class defined in another function, etc.
        # We try to get the module source as a fallback.
        try:
            source_file = inspect.getfile(func_obj)
            code = pathlib.Path(source_file).read_text()
            return code, "python"
        except Exception as e:
            print(
                f"Warning: Could not get source for '{func_name}'. Error: {e}",
                file=sys.stderr,
            )
    except Exception as e:
        print(
            f"Warning: Could not get source for '{func_name}'. Error: {e}",
            file=sys.stderr,
        )

    return None


def convert_to_pure_markdown(content: str, registry: dict) -> str:
    """
    Replaces custom component delimiters in markdown content with
    formatted code blocks.
    """
    delimiter_pattern = r"--([\w_]+)(?:\(([^)]+)\))?--"

    def replacer(match):
        command = match.group(1)
        argument = match.group(2)

        source_info = get_source_code(command, argument, registry)

        if source_info:
            code, language = source_info
            return f"\n```{language}\n{code.strip()}\n```\n"

        # If the delimiter cannot be resolved, remove it from the final output.
        return ""

    # First, remove frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) > 2:
            content = parts[2]

    return re.sub(delimiter_pattern, replacer, content)


def main():
    """
    Main function to generate pure markdown files from the docs directory.
    """
    print("Starting markdown generation process...")

    # 1. Load all available components from the library
    print(f"Loading components from: {COMPONENTS_LIBRARY_DIR}")
    component_registry = dynamic_load_components(COMPONENTS_LIBRARY_DIR)
    print(f"Successfully loaded {len(component_registry)} components.")

    # 2. Ensure the main output directory exists
    MARKDOWN_OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"Output directory set to: {MARKDOWN_OUTPUT_DIR}")

    # 3. Process each markdown file found in the source directory
    print(f"Processing markdown files from: {DOCS_SOURCE_DIR}")
    file_count = 0
    for md_file in DOCS_SOURCE_DIR.rglob("*.md"):
        file_count += 1
        print(f"  -> Processing: {md_file.relative_to(ROOT_DIR)}")

        # Read original content
        original_content = md_file.read_text()

        # Convert to pure markdown
        pure_md_content = convert_to_pure_markdown(original_content, component_registry)

        # Determine the correct output path, preserving directory structure
        relative_path = md_file.relative_to(DOCS_SOURCE_DIR)
        output_path = MARKDOWN_OUTPUT_DIR / relative_path

        # Create subdirectories in the output folder if they don't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the transformed content to the new file
        output_path.write_text(pure_md_content)
        print(f"     \- Saved to: {output_path.relative_to(ROOT_DIR)}")

    print(f"\nMarkdown generation complete. Processed {file_count} files.")


if __name__ == "__main__":
    main()
