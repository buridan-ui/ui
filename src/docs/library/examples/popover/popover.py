import reflex as rx


def popover_root(*children, **props):
    """
    Root popover container.
    Uses Reflex's built-in popover component.
    """
    return rx.popover.root(*children, data_slot="popover", **props)


def popover_trigger(*children, **props):
    """Trigger element for the popover"""
    return rx.popover.trigger(*children, data_slot="popover-trigger", **props)


def popover_content(*children, class_name: str = "", **props):
    """
    Popover content container.
    Uses CSS variables from your shadcn theme.
    """
    base_classes = (
        "bg-[var(--popover)] text-[var(--popover-foreground)] "
        "data-[state=open]:animate-in data-[state=closed]:animate-out "
        "data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 "
        "data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 "
        "data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 "
        "data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 "
        "z-50 w-72 rounded-md border border-input dark:border-[var(--input)] p-4 shadow-md outline-none"
    )

    return rx.popover.content(
        *children,
        data_slot="popover-content",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
