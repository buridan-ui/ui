import reflex as rx
from typing import Literal


class NavigationMenuPrimitive(rx.Component):
    """Base component for Navigation Menu components."""

    library = "@radix-ui/react-navigation-menu@1.2.14"

    alias = "NavigationMenuPrimitive"

    lib_dependencies = [
        "@radix-ui/primitive",
        "@radix-ui/react-collection",
        "@radix-ui/react-compose-refs",
        "@radix-ui/react-context",
        "@radix-ui/react-direction",
        "@radix-ui/react-dismissable-layer",
        "@radix-ui/react-id",
        "@radix-ui/react-presence",
        "@radix-ui/react-primitive",
        "@radix-ui/react-use-callback-ref",
        "@radix-ui/react-use-controllable-state",
        "@radix-ui/react-use-layout-effect",
        "@radix-ui/react-use-previous",
        "@radix-ui/react-visually-hidden",
    ]


class NavigationMenu(NavigationMenuPrimitive):
    """The root navigation menu component."""

    tag = "Root"

    alias = "NavigationMenuRoot"

    viewport: rx.Var[bool] = False

    value: rx.Var[str]

    default_value: rx.Var[str]

    on_value_change: rx.EventHandler[lambda value: [value]]

    dir: rx.Var[Literal["ltr", "rtl"]]

    orientation: rx.Var[Literal["horizontal", "vertical"]]

    delay_duration: rx.Var[int] = 0

    skip_delay_duration: rx.Var[int] = 0

    class_name: rx.Var[str] = (
        "group/navigation-menu relative flex max-w-max flex-1 items-center justify-center"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenu wrapper component."""
        return """
import * as NavigationMenuPrimitive from '@radix-ui/react-navigation-menu';

function NavigationMenu({ className, children, viewport = true, delayDuration = 0, skipDelayDuration = 0, ...props }) {
  return (
    <NavigationMenuPrimitive.Root
      data-slot="navigation-menu"
      data-viewport={viewport}
      className={className}
      delayDuration={delayDuration}
      skipDelayDuration={skipDelayDuration}
      {...props}
    >
      {children}
      {viewport && <NavigationMenuViewport />}
    </NavigationMenuPrimitive.Root>
  );
}
"""


class NavigationMenuList(NavigationMenuPrimitive):
    """The list container for navigation menu items."""

    tag = "List"

    alias = "NavigationMenuListPrimitive"

    class_name: rx.Var[str] = (
        "group flex flex-1 list-none items-center justify-center gap-1"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuList wrapper component."""
        return """
function NavigationMenuList({ className, ...props }) {
  return (
    <NavigationMenuPrimitive.List
      data-slot="navigation-menu-list"
      className={className}
      {...props}
    />
  );
}
"""


class NavigationMenuItem(NavigationMenuPrimitive):
    """Individual navigation menu item."""

    tag = "Item"

    alias = "NavigationMenuItemPrimitive"

    value: rx.Var[str]

    class_name: rx.Var[str] = "relative"

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuItem wrapper component."""
        return """
function NavigationMenuItem({ className, ...props }) {
  return (
    <NavigationMenuPrimitive.Item
      data-slot="navigation-menu-item"
      className={className}
      {...props}
    />
  );
}
"""


class NavigationMenuTrigger(NavigationMenuPrimitive):
    """Trigger button for navigation menu dropdown."""

    tag = "Trigger"

    alias = "NavigationMenuTriggerPrimitive"

    class_name: rx.Var[str] = (
        "group inline-flex h-9 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground disabled:pointer-events-none disabled:opacity-50 data-[state=open]:hover:bg-accent data-[state=open]:text-accent-foreground data-[state=open]:focus:bg-accent data-[state=open]:bg-accent/50 focus-visible:ring-ring/50 outline-none transition-[color,box-shadow] focus-visible:ring-[3px] focus-visible:outline-1"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuTrigger wrapper with chevron icon."""
        return """
function NavigationMenuTrigger({ className, children, ...props }) {
  return (
    <NavigationMenuPrimitive.Trigger
      data-slot="navigation-menu-trigger"
      className={className}
      {...props}
    >
      {children}{" "}
      <ChevronDown
        className="relative top-[1px] ml-1 size-3 transition duration-300 group-data-[state=open]:rotate-180"
        aria-hidden="true"
      />
    </NavigationMenuPrimitive.Trigger>
  );
}
"""


class NavigationMenuContent(NavigationMenuPrimitive):
    """Content container for navigation menu dropdown."""

    tag = "Content"

    alias = "NavigationMenuContentPrimitive"

    force_mount: rx.Var[bool]

    class_name: rx.Var[str] = (
        "absolute left-0 top-0 w-full md:w-auto data-[motion=from-end]:animate-[slideFromRight_250ms_ease] data-[motion=from-start]:animate-[slideFromLeft_250ms_ease] data-[motion=to-end]:animate-[slideToRight_250ms_ease] data-[motion=to-start]:animate-[slideToLeft_250ms_ease]"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuContent wrapper component."""
        return """
function NavigationMenuContent({ className, ...props }) {
  return (
    <NavigationMenuPrimitive.Content
      data-slot="navigation-menu-content"
      className={className}
      {...props}
    />
  );
}
"""


class NavigationMenuLink(NavigationMenuPrimitive):
    """Link component for navigation menu items."""

    tag = "Link"

    alias = "NavigationMenuLinkPrimitive"

    active: rx.Var[bool]

    href: rx.Var[str]

    on_select: rx.EventHandler[lambda e: [e]]

    class_name: rx.Var[str] = (
        "data-[active=true]:focus:bg-accent data-[active=true]:hover:bg-accent data-[active=true]:bg-accent/50 data-[active=true]:text-accent-foreground hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground focus-visible:ring-ring/50 [&_svg:not([class*='text-'])]:text-muted-foreground flex flex-col gap-1 rounded-sm p-2 text-sm transition-all outline-none focus-visible:ring-[3px] focus-visible:outline-1 [&_svg:not([class*='size-'])]:size-4"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuLink wrapper component."""
        return """
function NavigationMenuLink({ className, ...props }) {
  return (
    <NavigationMenuPrimitive.Link
      data-slot="navigation-menu-link"
      className={className}
      {...props}
    />
  );
}
"""


class NavigationMenuViewport(NavigationMenuPrimitive):
    """Viewport for rendering navigation menu content."""

    tag = "Viewport"

    alias = "NavigationMenuViewportPrimitive"

    force_mount: rx.Var[bool]

    class_name: rx.Var[str] = (
        "origin-top-center bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-90 relative mt-1.5 h-[var(--radix-navigation-menu-viewport-height)] w-full overflow-hidden rounded-md border shadow md:w-[var(--radix-navigation-menu-viewport-width)] transition-[width,height] duration-300 ease-in-out"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuViewport wrapper component."""
        return """
function NavigationMenuViewport({ className, ...props }) {
  return (
    <div className="absolute top-full left-0 isolate z-50 flex justify-center">
      <NavigationMenuPrimitive.Viewport
        data-slot="navigation-menu-viewport"
        className={className}
        {...props}
      />
    </div>
  );
}
"""


class NavigationMenuIndicator(NavigationMenuPrimitive):
    """Indicator showing the active menu item."""

    tag = "Indicator"

    alias = "NavigationMenuIndicatorPrimitive"

    force_mount: rx.Var[bool]

    class_name: rx.Var[str] = (
        "data-[state=visible]:animate-in data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:fade-in top-full z-[1] flex h-1.5 items-end justify-center overflow-hidden"
    )

    def _get_custom_code(self) -> str:
        """Add the NavigationMenuIndicator wrapper component."""
        return """
function NavigationMenuIndicator({ className, ...props }) {
  return (
    <NavigationMenuPrimitive.Indicator
      data-slot="navigation-menu-indicator"
      className={className}
      {...props}
    >
      <div className="bg-border relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm shadow-md" />
    </NavigationMenuPrimitive.Indicator>
  );
}
"""


navigation_menu = NavigationMenu.create
navigation_menu_list = NavigationMenuList.create
navigation_menu_item = NavigationMenuItem.create
navigation_menu_trigger = NavigationMenuTrigger.create
navigation_menu_content = NavigationMenuContent.create
navigation_menu_link = NavigationMenuLink.create
navigation_menu_viewport = NavigationMenuViewport.create
navigation_menu_indicator = NavigationMenuIndicator.create
