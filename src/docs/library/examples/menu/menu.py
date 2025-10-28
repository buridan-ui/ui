import reflex as rx
from typing import Literal


def dropdown_menu_root(*children, **props):
    """Root dropdown menu container"""
    return rx.menu.root(*children, data_slot="dropdown-menu", **props)


def dropdown_menu_trigger(*children, **props):
    """Trigger button for the dropdown menu"""
    return rx.menu.trigger(*children, data_slot="dropdown-menu-trigger", **props)


def dropdown_menu_content(*children, class_name: str = "", **props):
    """
    Dropdown menu content container.
    Uses CSS variables from your shadcn theme.
    """
    base_classes = (
        "bg--popover text-popover-foreground "
        "data-[state=open]:animate-in data-[state=closed]:animate-out "
        "data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 "
        "data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 "
        "data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 "
        "data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 "
        "z-50 min-w-[8rem] overflow-x-hidden overflow-y-auto rounded-md border border-input dark:border-[var(--input)] p-1 shadow-md"
    )

    return rx.menu.content(
        *children,
        data_slot="dropdown-menu-content",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_item(
    *children,
    variant: Literal["default", "destructive"] = "default",
    inset: bool = False,
    disabled: bool = False,
    class_name: str = "",
    **props,
):
    """Dropdown menu item with optional variant styling"""
    base_classes = (
        "focus:bg-[var(--accent)] focus:text-[var(--accent-foreground)] "
        "data-[variant=destructive]:text-[var(--destructive)] "
        "data-[variant=destructive]:focus:bg-[var(--destructive)]/10 "
        "dark:data-[variant=destructive]:focus:bg-[var(--destructive)]/20 "
        "data-[variant=destructive]:focus:text-[var(--destructive)] "
        "[&_svg:not([class*='text-'])]:text-[var(--muted-foreground)] "
        "relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm "
        "outline-none select-none "
        "data-[disabled]:pointer-events-none data-[disabled]:opacity-50 "
        + ("pl-8 " if inset else "")
        + "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    )

    return rx.menu.item(
        *children,
        data_slot="dropdown-menu-item",
        data_variant=variant,
        data_inset=inset,
        disabled=disabled,
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_label(*children, inset: bool = False, class_name: str = "", **props):
    """Label/header for menu sections"""
    base_classes = "px-2 py-1.5 text-sm font-medium " + ("pl-8" if inset else "")

    return rx.el.div(
        *children,
        data_slot="dropdown-menu-label",
        data_inset=inset,
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_separator(class_name: str = "", **props):
    """Separator line between menu items"""
    base_classes = "bg-input -mx-1 my-1 h-px"

    return rx.menu.separator(
        data_slot="dropdown-menu-separator",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_shortcut(*children, class_name: str = "", **props):
    """Keyboard shortcut display"""
    base_classes = "text-[var(--muted-foreground)] ml-auto text-xs tracking-widest"

    return rx.el.span(
        *children,
        data_slot="dropdown-menu-shortcut",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_sub_trigger(
    *children, inset: bool = False, class_name: str = "", **props
):
    """Trigger for submenu"""
    base_classes = (
        "focus:bg-[var(--accent)] focus:text-[var(--accent-foreground)] "
        "data-[state=open]:bg-[var(--accent)] data-[state=open]:text-[var(--accent-foreground)] "
        "[&_svg:not([class*='text-'])]:text-[var(--muted-foreground)] "
        "flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-none select-none "
        + ("pl-8 " if inset else "")
        + "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    )

    return rx.menu.sub_trigger(
        *children,
        data_slot="dropdown-menu-sub-trigger",
        data_inset=inset,
        class_name=f"[&_.rt-BaseMenuSubTriggerIcon.rt-DropdownMenuSubtriggerIcon]:!size-2 [&_.rt-BaseMenuSubTriggerIcon.rt-DropdownMenuSubtriggerIcon]:!shrink-0 {base_classes} {class_name}".strip(),
        **props,
    )


def dropdown_menu_sub_content(*children, class_name: str = "", **props):
    """Submenu content container"""
    base_classes = (
        "bg-[var(--popover)] text-[var(--popover-foreground)] "
        "data-[state=open]:animate-in data-[state=closed]:animate-out "
        "data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 "
        "data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 "
        "z-50 min-w-[8rem] overflow-hidden rounded-md border border-input p-1 shadow-lg border dark:border-[var(--input)]"
    )

    return rx.menu.sub_content(
        *children,
        data_slot="dropdown-menu-sub-content",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
