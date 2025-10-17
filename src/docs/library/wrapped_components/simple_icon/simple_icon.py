"""Simple Icon component wrapper for @icons-pack/react-simple-icons."""

import reflex as rx
from reflex.utils.imports import ImportVar


class SimpleIcon(rx.Component):
    """Simple Icon component wrapper for @icons-pack/react-simple-icons."""

    library = "@icons-pack/react-simple-icons"

    tag = "SiReact"

    color: rx.Var[str]

    size: rx.Var[int | str]

    @classmethod
    def create(cls, icon_name: str, **props):
        """Create a SimpleIcon component.

        Args:
            icon_name: The icon component name (e.g., "SiReact", "SiGithub", "SiPython")
            **props: Additional props like size, color

        Returns:
            The component instance.
        """
        instance = super().create(**props)
        instance.tag = icon_name
        return instance

    def add_imports(self) -> rx.ImportDict:
        """Add the specific icon import."""
        if self.library is None:
            exception = "Library must be set to use SimpleIcon"
            raise ValueError(exception)
        return {
            self.library: ImportVar(
                tag=self.tag,
                is_default=False,
            )
        }


def simple_icon(icon_name: str, **props) -> rx.Component:
    """Create a simple icon component.

    Args:
        icon_name: The Simple Icons component name (e.g., "SiGithub")
        **props: Additional props like size, color

    Returns:
        The SimpleIcon component.
    """
    return SimpleIcon.create(icon_name, **props)
