import reflex as rx
from typing import Any, List, Literal


class VaulComponent(rx.Component):
    """Base component for Vaul drawer components."""

    library = "vaul@1.1.2"

    lib_dependencies = ["@radix-ui/react-dialog"]


class DrawerRoot(VaulComponent):
    """The root component for the drawer.

    This component manages the state of the drawer and provides context
    to all child components.
    """

    tag = "Drawer.Root"

    # Whether the drawer should be open by default
    default_open: rx.Var[bool]

    # Control the open state (controlled mode)
    open: rx.Var[bool]

    # Event handler called when the open state changes
    on_open_change: rx.EventHandler[lambda open: [open]]

    # Whether the drawer should be modal (default: True)
    modal: rx.Var[bool]

    # Direction of the drawer ("top", "bottom", "left", "right")
    direction: rx.Var[Literal["top", "bottom", "left", "right"]]

    # Whether the drawer should close when clicking outside
    dismiss_from_backdrop: rx.Var[bool]

    # Whether to prevent scrolling on the body when drawer is open
    should_scale_background: rx.Var[bool]

    # Custom scale for background when drawer is open
    scale_background: rx.Var[float]

    # Whether to prevent scroll restoration
    prevent_scroll_restoration: rx.Var[bool]

    # Snap points for the drawer (e.g., [0.2, 0.5, 1])
    snap_points: rx.Var[List[float]]

    # Whether to fade background from snap points
    fade_from_index: rx.Var[int]

    # Active snap point
    active_snap_point: rx.Var[float]

    # Event handler for snap point changes
    on_snap_point_change: rx.EventHandler[lambda point: [point]]

    # Whether nested drawers should scale
    nested: rx.Var[bool]

    # Event handler called when the drawer is closed
    on_close: rx.EventHandler[lambda: []]

    # Event handler called when a drag session starts
    on_drag_start: rx.EventHandler[lambda: []]

    # Event handler called when a drag session ends
    on_drag_end: rx.EventHandler[lambda: []]

    # Event handler called when the drawer is released
    on_release: rx.EventHandler[lambda: []]


class DrawerTrigger(VaulComponent):
    """The button that opens the drawer.

    This component is used to trigger the drawer to open.
    """

    tag = "Drawer.Trigger"

    # Make the trigger behave as a child component
    as_child: rx.Var[bool]


class DrawerPortal(VaulComponent):
    """Portal component to render drawer in a different part of the DOM.

    This component portals the drawer content to a different part of the DOM,
    typically at the end of the document body.
    """

    tag = "Drawer.Portal"

    # Custom container to portal into
    container: rx.Var[Any]


class DrawerOverlay(VaulComponent):
    """The overlay component that appears behind the drawer.

    This component creates a backdrop/overlay that appears behind the drawer
    when it's open.
    """

    tag = "Drawer.Overlay"

    # Make the overlay behave as a child component
    as_child: rx.Var[bool]


class DrawerContent(VaulComponent):
    """The main content container for the drawer.

    This component contains the actual content of the drawer.
    """

    tag = "Drawer.Content"

    # Make the content behave as a child component
    as_child: rx.Var[bool]

    # Event handler called when escape key is pressed
    on_escape_key_down: rx.EventHandler[lambda e: [e]]

    # Event handler called when pointer is pressed down outside
    on_pointer_down_outside: rx.EventHandler[lambda e: [e]]

    # Event handler called when clicked outside
    on_interact_outside: rx.EventHandler[lambda e: [e]]


class DrawerTitle(VaulComponent):
    """The title component for the drawer.

    This component is used to display the title of the drawer.
    It's important for accessibility.
    """

    tag = "Drawer.Title"

    # Make the title behave as a child component
    as_child: rx.Var[bool]


class DrawerDescription(VaulComponent):
    """The description component for the drawer.

    This component is used to display a description of the drawer.
    It's important for accessibility.
    """

    tag = "Drawer.Description"

    # Make the description behave as a child component
    as_child: rx.Var[bool]


class DrawerClose(VaulComponent):
    """The button that closes the drawer.

    This component is used to trigger the drawer to close.
    """

    tag = "Drawer.Close"

    # Make the close button behave as a child component
    as_child: rx.Var[bool]


class DrawerHandle(VaulComponent):
    """The handle component for the drawer.

    This component displays a drag handle for the drawer, typically
    shown at the top or bottom of the drawer content.
    """

    tag = "Drawer.Handle"

    # Make the handle behave as a child component
    as_child: rx.Var[bool]


# Convenience functions to create drawer components
drawer_root = DrawerRoot.create
drawer_trigger = DrawerTrigger.create
drawer_portal = DrawerPortal.create
drawer_overlay = DrawerOverlay.create
drawer_content = DrawerContent.create
drawer_title = DrawerTitle.create
drawer_description = DrawerDescription.create
drawer_close = DrawerClose.create
drawer_handle = DrawerHandle.create
