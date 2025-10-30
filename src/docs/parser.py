import re
import ast
import inspect
import pathlib
import importlib
import reflex as rx

from typing import Dict, Callable, List
from src.docs.constants import DocParserCommands
from src.docs.style import render_parse_error, markdown_component_map
from src.comps.docs.wrapper import (
    demo_and_code_single_file_wrapper,
    cli_and_manual_installation_wrapper,
)


class DocParser:
    def __init__(
        self,
        components_registry: Dict[str, Callable] | None = None,
        dynamic_load_dirs: List[str] | None = None,
    ):
        self.components_registry = components_registry or {}
        if dynamic_load_dirs:
            for directory in dynamic_load_dirs:
                self.components_registry.update(self._dynamic_load(directory))

        self.command_handlers = {
            DocParserCommands.DEMO_AND_CODE_SINGLE_FILE: self._handle_demo_and_code_single_file,
            DocParserCommands.SHOW_CODE_WITH_LANGUAGE: self._handle_show_code_with_language,
            DocParserCommands.DEMO_AND_SINGLE_FUNCTION: self._handle_demo_and_single_function,
            DocParserCommands.FULL_SOURCE_PAGE_OF_COMPONENT: self._handel_full_source_page_of_component,
            DocParserCommands.CLI_AND_MANUAL_INSTALLATION: self._handle_cli_and_manual_installation,
        }

    def parse_and_render(self, content: str) -> List[rx.Component]:
        sections = self._parse_sections(content)
        components = []
        for section in sections:
            if section["type"] == "content":
                components.append(
                    rx.markdown(
                        section["value"],
                        component_map=markdown_component_map,
                        class_name="px-4",
                    )
                )
            elif section["type"] == "command":
                components.append(
                    self._handle_command(section["command"], section["argument"])
                )
        return components

    def _handle_command(self, command: str, argument: str | None) -> rx.Component:
        command_lower = command.lower()
        handler = self.command_handlers.get(command_lower)

        if handler:
            return handler(argument)

        if command_lower in self.components_registry and argument is None:
            component_func = self.components_registry[command_lower]
            return component_func()

        return render_parse_error(msg=f"Unknown component or command: {command}")

    def _dynamic_load(self, directory: str) -> Dict[str, Callable]:
        """Dynamically loads components from a given directory."""
        registry = {}
        root_dir = pathlib.Path(__file__).parent.parent.parent
        search_path = root_dir / directory

        if not search_path.is_dir():
            print(f"Warning: Dynamic load directory not found: {directory}")
            return {}

        for py_file in search_path.rglob("*.py"):
            if py_file.name.startswith("__"):
                continue

            # Create module path for importlib
            relative_py_file = py_file.relative_to(root_dir)
            module_path = ".".join(relative_py_file.with_suffix("").parts)
            try:
                module = importlib.import_module(module_path)
                for name, obj in inspect.getmembers(module):
                    if (
                        inspect.isfunction(obj) or inspect.isclass(obj)
                    ) and obj.__module__ == module.__name__:
                        registry[name.lower()] = obj
            except Exception as e:
                print(f"Error loading components from module {module_path}: {e}")
        return registry

    def _parse_sections(self, content: str) -> List[Dict]:
        delimiter_pattern = r"--([\w_]+)(?:\(([^)]+)\))?--"
        sections = []
        current_pos = 0

        for match in re.finditer(delimiter_pattern, content):
            if match.start() > current_pos:
                text_content = content[current_pos : match.start()].strip()
                if text_content:
                    sections.append({"type": "content", "value": text_content})

            command = match.group(1)
            argument = match.group(2)
            sections.append(
                {"type": "command", "command": command, "argument": argument}
            )
            current_pos = match.end()

        if current_pos < len(content):
            remaining_content = content[current_pos:].strip()
            if remaining_content:
                sections.append({"type": "content", "value": remaining_content})

        return sections

    def _create_code_block_markdown(
        self, code: str, language: str = "python"
    ) -> rx.Component:
        md_code = f"```{language}\n{code}```"

        return rx.markdown(
            md_code,
            component_map=markdown_component_map,
            class_name="px-4",
        )

    def _handle_cli_and_manual_installation(self, argument: str | None):
        if not argument:
            return render_parse_error(
                msg="Missing argument for cli_and_manual_installation"
            )

        try:
            args = ast.literal_eval(argument)
            if not isinstance(args, list) or len(args) != 2:
                return render_parse_error(
                    msg='Invalid argument format for CLI_AND_MANUAL_INSTALLATION. Expected ["ComponentName", "cli command"]'
                )

            component_name, cli_command = args
            component_name_lower = component_name.lower()

            if component_name_lower not in self.components_registry:
                return render_parse_error(msg=f"Component not found: {component_name}")

            func = self.components_registry[component_name_lower]
            file_path = inspect.getfile(func)
            full_source = pathlib.Path(file_path).read_text()

            return cli_and_manual_installation_wrapper(cli_command, full_source)

        except (ValueError, SyntaxError, IndexError) as e:
            return render_parse_error(
                msg=f"Error parsing arguments for CLI_AND_MANUAL_INSTALLATION: {e}"
            )
        except Exception as e:
            return render_parse_error(msg=f"Error loading source: {e}")

    def _handel_full_source_page_of_component(
        self, argument: str | None
    ) -> rx.Component:
        if not argument:
            return render_parse_error(
                msg="Missing argument for full_source_page_of_component"
            )

        arg_lower = argument.lower()
        if arg_lower not in self.components_registry:
            return render_parse_error(msg=f"Component not found: {argument}")

        func = self.components_registry[arg_lower]

        try:
            file_path = inspect.getfile(func)
            full_source = pathlib.Path(file_path).read_text()

            return self._create_code_block_markdown(full_source, "python")

        except Exception as e:
            return render_parse_error(msg=f"Error loading source: {e}")

    def _handle_show_code_with_language(self, argument: str | None) -> rx.Component:
        if not argument:
            return render_parse_error(
                msg="Missing arguments for show_code_with_language"
            )

        try:
            args = ast.literal_eval(argument)

            if not isinstance(args, list) or len(args) == 0:
                return render_parse_error(
                    msg="Invalid argument format. Expected a list. Example: [function_name, code_block_langauge]"
                )

            arg_lower = args[0].lower()
            if arg_lower not in self.components_registry:
                return render_parse_error(
                    msg=f"Missing component for show_code_with_language: {args[0]}"
                )

            return self._create_code_block_markdown(
                inspect.getsource(self.components_registry[arg_lower]), args[1]
            )

        except (ValueError, SyntaxError):
            return render_parse_error(
                msg="Error parsing arguments. Ensure they are in a valid format."
            )

    def _handle_demo_and_code_single_file(self, argument: str | None) -> rx.Component:
        if not argument:
            return render_parse_error(
                msg="Missing arguments for demo_and_code_single_file"
            )

        arg_lower = argument.lower()
        try:
            if not isinstance(arg_lower, str):
                return render_parse_error(
                    msg="Invalid argument format. Expected a string. Example: function_name"
                )

            if arg_lower not in self.components_registry:
                return render_parse_error(
                    msg=f"Missing component for demo_and_code_single_file: {argument}"
                )

            component = self.components_registry[arg_lower]
            module = inspect.getmodule(component)
            source_code = inspect.getsource(module)
            component_file_path = inspect.getfile(component)
            is_chart_demo = "/src/docs/library/charts/" in component_file_path

            return demo_and_code_single_file_wrapper(
                component(), source_code, is_chart_demo
            )

        except (ValueError, SyntaxError):
            return render_parse_error(
                msg="Error parsing arguments. Ensure they are in a valid format."
            )

    def _handle_demo_and_single_function(self, argument: str | None) -> rx.Component:
        if not argument:
            return render_parse_error(
                msg="Missing arguments for demo_and_single_function"
            )

        arg_lower = argument.lower()
        try:
            if not isinstance(arg_lower, str):
                return render_parse_error(
                    msg="Invalid argument format. Expected a string. Example: function_name"
                )

            if arg_lower not in self.components_registry:
                return render_parse_error(
                    msg=f"Missing component for demo_and_single_function: {argument}"
                )

            component = self.components_registry[arg_lower]
            source_code = inspect.getsource(component)
            component_file_path = inspect.getfile(component)
            is_chart_demo = "/src/docs/library/charts/" in component_file_path

            return demo_and_code_single_file_wrapper(
                component(), source_code, is_chart_demo
            )

        except (ValueError, SyntaxError):
            return render_parse_error(
                msg="Error parsing arguments. Ensure they are in a valid format."
            )
