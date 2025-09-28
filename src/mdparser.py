import reflex as rx
import re
import inspect
from typing import List, Dict, Callable

markdown_component_map = {
    "h1": lambda t: rx.heading(t, class_name="text-3xl py-1", id=t),
    "h2": lambda t: rx.heading(t, class_name="text-2xl py-1", id=t),
}


class DelimiterParser:
    """Parser that can render components or display their source code."""

    def __init__(self, components_registry: Dict[str, Callable]):
        self.components_registry = components_registry

    def parse_and_render(self, content: str) -> List[rx.Component]:
        """Parse content with --component-- or --show_code(component)-- delimiters."""

        delimiter_pattern = r"--(\w+)(?:\((\w+)\))?--"
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
                    rx.markdown(section["value"], component_map=markdown_component_map)
                )
            elif section["type"] == "command":
                command = section["command"]
                argument = section["argument"]

                if command == "show_code":
                    if argument and argument in self.components_registry:
                        file_path = inspect.getfile(self.components_registry[argument])
                        with open(file_path, "r") as f:
                            source_code = f.read()
                        md_code = f"```python\n{source_code}```"
                        components.append(
                            rx.markdown(md_code, component_map=markdown_component_map)
                        )
                    else:
                        components.append(
                            rx.box(
                                f"Missing component for show_code: {argument}",
                                color="red",
                            )
                        )
                elif command in self.components_registry and argument is None:
                    components.append(self.components_registry[command]())
                else:
                    components.append(
                        rx.box(f"Unknown component or command: {command}", color="red")
                    )

        return components
