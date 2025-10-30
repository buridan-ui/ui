"""Custom toggle component."""

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for toggle components."""

    ROOT = "p-1.5 inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium hover:bg-muted hover:text-muted-foreground disabled:pointer-events-none disabled:opacity-50 data-[pressed]:bg-accent data-[pressed]:text-accent-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] outline-none transition-[color,box-shadow] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive whitespace-nowrap"


class ToggleBaseComponent(BaseUIComponent):
    """Base component for toggle components."""

    library = f"{PACKAGE_NAME}/toggle"

    @property
    def import_var(self):
        """Return the import variable for the toggle component."""
        return ImportVar(tag="Toggle", package_path="", install=False)


class Toggle(ToggleBaseComponent):
    """A two-state button that can be on or off. Renders a <button> element."""

    tag = "Toggle"

    # A unique string that identifies the toggle when used inside a toggle group.
    value: Var[str]

    # Whether the toggle button is currently pressed. This is the uncontrolled counterpart of pressed. Defaults to False.
    default_pressed: Var[bool]

    # Whether the toggle button is currently pressed. This is the controlled counterpart of default_pressed.
    pressed: Var[bool]

    # Callback fired when the pressed state is changed.
    on_pressed_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the toggle component."""
        props["data-slot"] = "toggle"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


toggle = Toggle.create
