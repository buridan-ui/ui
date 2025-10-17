"""Typed component wrapper for react-typed."""

import reflex as rx
from reflex.utils.imports import ImportVar


class Typed(rx.Component):
    """Typed component for typewriter animation effects."""

    # Use the maintained fork instead of the buggy react-typed
    library = "react-typed"
    tag = "ReactTyped"

    # Core props
    strings: rx.Var[list[str]]
    type_speed: rx.Var[int]
    back_speed: rx.Var[int]
    back_delay: rx.Var[int]
    start_delay: rx.Var[int]
    loop: rx.Var[bool]
    loop_count: rx.Var[int]
    show_cursor: rx.Var[bool]
    cursor_char: rx.Var[str]
    smart_backspace: rx.Var[bool]
    shuffle: rx.Var[bool]
    fade_out: rx.Var[bool]
    fade_out_delay: rx.Var[int]
    stopped: rx.Var[bool]

    @classmethod
    def create(cls, **props):
        """Create a Typed component.

        Args:
            **props: Component props like strings, type_speed, etc.

        Returns:
            The component instance.
        """
        return super().create(**props)

    def add_imports(self) -> rx.ImportDict:
        """Add the Typed component import."""
        return {self.library: ImportVar(tag=self.tag, is_default=False)}


def typed(**props) -> rx.Component:
    """Create a typewriter animation component.

    NOTE: This uses react-typed-component (maintained fork).
    Install with: npm install react-typed-component

    Args:
        strings: List of strings to type out
        type_speed: Typing speed in milliseconds (default: 0)
        back_speed: Backspacing speed in milliseconds (default: 0)
        back_delay: Time before backspacing in milliseconds (default: 700)
        start_delay: Time before typing starts in milliseconds (default: 0)
        loop: Whether to loop the animation (default: False)
        loop_count: Number of times to loop, 0 = infinite (default: 0)
        show_cursor: Show blinking cursor (default: True)
        cursor_char: Character to use for cursor (default: "|")
        smart_backspace: Only backspace what doesn't match previous string (default: True)
        shuffle: Shuffle the strings (default: False)
        fade_out: Fade out instead of backspace (default: False)
        fade_out_delay: Delay before fade out in milliseconds (default: 500)
        stopped: Stop the animation (default: False)
        **props: Additional component props

    Returns:
        The Typed component.
    """
    return Typed.create(**props)
