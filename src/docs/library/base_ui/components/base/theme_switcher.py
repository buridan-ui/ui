"""Theme switcher component."""

from reflex.components.component import Component
from reflex.components.core.cond import cond
from reflex.components.el import Button, Div
from reflex.style import LiteralColorMode, color_mode, set_color_mode

from ...icons.hugeicon import hi
from ...utils.twmerge import cn


def theme_switcher_item(mode: LiteralColorMode, icon: str) -> Component:
    """Create a theme switcher item button for a specific mode."""
    active_cn = "text-foreground shadow-sm bg-background"
    unactive_cn = "hover:text-foreground text-muted-foreground"
    return Button.create(
        hi(icon, class_name="shrink-0", size=14),
        on_click=set_color_mode(mode),
        class_name=(
            "flex items-center cursor-pointer justify-center rounded-md transition-color size-6",
            cond(mode == color_mode, active_cn, unactive_cn),
        ),
        aria_label=f"Switch to {mode} mode",
    )


def theme_switcher(class_name: str = "") -> Component:
    """Theme switcher component."""
    return Div.create(
        theme_switcher_item("system", "ComputerIcon"),
        theme_switcher_item("light", "Sun01Icon"),
        theme_switcher_item("dark", "Moon02Icon"),
        class_name=cn(
            "flex flex-row items-center bg-secondary p-1 rounded-md w-fit",
            class_name,
        ),
    )
