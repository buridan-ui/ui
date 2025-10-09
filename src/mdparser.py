import reflex as rx
import re
import inspect
import os
import importlib
from typing import List, Dict, Callable
from src.wrappers.component.wrapper import component_wrapper_docs
from src import constants

markdown_component_map = {
    "h1": lambda t: rx.heading(t, class_name="text-2xl py-1", id=t),
    "h2": lambda t: rx.heading(t, class_name="text-xl py-1", id=t),
    "p": lambda t: rx.text(
        t,
        class_name="text-sm leading-6 pb-4",
    ),
    "li": lambda t: rx.list_item(
        rx.text(t, color=rx.color("slate", 11), class_name="text-sm"),
    ),
    "codeblock": lambda c, **p: rx.hstack(
        rx.code_block(
            c,
            width="100%",
            font_size="12px",
            language="python",
            wrap_long_lines=True,
            scrollbar_width="none",
            code_tag_props={
                "pre": "transparent",
                "background": "transparent",
            },
            custom_attrs={
                "background": "transparent !important",
                "pre": {"background": "transparent !important"},
                "code": {"background": "transparent !important"},
            },
            background="transparent !important",
            class_name="rounded-md !bg-transparent",
            border=f"1px dashed {rx.color('gray', 5)}",
        ),
        rx.el.button(
            rx.icon(tag="copy", size=13),
            cursor="pointer",
            position="absolute",
            right="15px",
            top="20px",
            on_click=[
                rx.toast("Command copied"),
                rx.set_clipboard(c),
            ],
        ),
        width="100%",
        align="center",
        position="relative",
    ),
    "a": lambda t, **p: rx.link(t, color=rx.color("accent", 8), **p),
}


class DelimiterParser:
    """Parser that can render components or display their source code."""

    def __init__(
        self,
        components_registry: Dict[str, Callable] | None = None,
        dynamic_load_dirs: List[str] | None = None,
    ):
        self.components_registry = components_registry or {}
        if dynamic_load_dirs:
            for directory in dynamic_load_dirs:
                self.components_registry.update(self._dynamic_load(directory))

    def _dynamic_load(self, directory: str) -> Dict[str, Callable]:
        """Dynamically loads components from a given directory."""
        registry = {}
        module_base_path = directory.replace("/", ".")

        if not os.path.isdir(directory):
            print(f"Warning: Dynamic load directory not found: {directory}")
            return {}

        for filename in os.listdir(directory):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module_path = f"{module_base_path}.{module_name}"

                try:
                    module = importlib.import_module(module_path)
                    for name, obj in inspect.getmembers(module):
                        if (
                            inspect.isfunction(obj) or inspect.isclass(obj)
                        ) and obj.__module__ == module.__name__:
                            registry[name] = obj
                except Exception as e:
                    print(f"jError loading components from module {module_path}: {e}")
        return registry

    def parse_and_render(self, content: str) -> List[rx.Component]:
        """Parse content with --component-- or --show_code(component)-- delimiters."""

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
                command = section["command"]
                argument = section["argument"]

                if command.lower() == constants.SHOW_CODE:
                    if argument and argument in self.components_registry:
                        source_code = inspect.getsource(
                            self.components_registry[argument]
                        )
                        md_code = f"```python\n{source_code}```"
                        components.append(
                            rx.markdown(
                                md_code,
                                component_map=markdown_component_map,
                                class_name="px-4",
                            )
                        )
                    else:
                        components.append(
                            rx.box(
                                f"Missing component for show_code: {argument}",
                                color="red",
                            )
                        )
                elif command.lower() == constants.SHOW_PAGE_CODE:
                    if argument and argument in self.components_registry:
                        component_func = self.components_registry[argument]
                        module = inspect.getmodule(component_func)
                        source_code = inspect.getsource(module)
                        md_code = f"```python\n{source_code}```"
                        components.append(
                            rx.markdown(
                                md_code,
                                component_map=markdown_component_map,
                                class_name="px-4",
                            )
                        )
                    else:
                        components.append(
                            rx.box(
                                f"Missing component for show_page_code: {argument}",
                                color="red",
                            )
                        )
                elif command.lower() == constants.SHOW_FILE_CONTENT:
                    if argument:
                        try:
                            filepath = argument.strip()
                            if filepath.startswith("@/"):
                                filepath = filepath[2:]
                            with open(filepath, "r") as f:
                                file_content = f.read()
                            language = ""
                            extension = os.path.splitext(filepath)[1]
                            if extension == ".css":
                                language = "css"
                            elif extension == ".py":
                                language = "python"
                            elif extension == ".js":
                                language = "javascript"
                            elif extension == ".ts":
                                language = "typescript"
                            elif extension == ".html":
                                language = "html"
                            md_code = f"```{language}\n{file_content}```"
                            components.append(
                                rx.markdown(
                                    md_code,
                                    component_map=markdown_component_map,
                                    class_name="px-4",
                                )
                            )
                        except FileNotFoundError:
                            components.append(
                                rx.box(
                                    f"File not found: {argument}",
                                    color="red",
                                )
                            )
                        except Exception as e:
                            components.append(
                                rx.box(
                                    f"Error reading file {argument}: {e}",
                                    color="red",
                                )
                            )
                    else:
                        components.append(
                            rx.box(
                                "Missing file path for show_file_content",
                                color="red",
                            )
                        )
                elif command.lower() == constants.COMPONENT_WRAPPER:
                    if argument and argument in self.components_registry:
                        component_func = self.components_registry[argument]
                        source_code = inspect.getsource(component_func)
                        component_instance = component_func()
                        components.append(
                            rx.el.div(
                                component_wrapper_docs(component_instance, source_code),
                                class_name="px-4 pb-6",
                            )
                        )
                    else:
                        components.append(
                            rx.box(
                                f"Missing component for component_wrapper: {argument}",
                                color="red",
                            )
                        )
                elif command.lower() in self.components_registry and argument is None:
                    components.append(self.components_registry[command.lower()]())
                else:
                    components.append(
                        rx.box(f"Unknown component or command: {command}", color="red")
                    )

        return components
