"""React CountUp component wrapper for react-countup."""

import reflex as rx


class CountUp(rx.Component):
    """CountUp component for animated number counting."""

    library = "react-countup"
    tag = "CountUp"
    is_default = True

    start: rx.Var[int | float]
    end: rx.Var[int | float]
    duration: rx.Var[int | float]
    decimals: rx.Var[int]
    decimal: rx.Var[str]
    prefix: rx.Var[str]
    suffix: rx.Var[str]
    separator: rx.Var[str]
    delay: rx.Var[int | float]
    enable_scroll_spy: rx.Var[bool]
    scroll_spy_delay: rx.Var[int]
    scroll_spy_once: rx.Var[bool]
    preserve_value: rx.Var[bool]
    use_easing: rx.Var[bool]
    easingFn: rx.Var[str]

    @classmethod
    def create(cls, **props):
        """Create a CountUp component.

        Args:
            **props: Component props

        Returns:
            The component instance.
        """
        return super().create(**props)


def count_up(**props) -> rx.Component:
    """Create an animated number counting component.

    NOTE: This uses react-countup package.
    Install with: npm install react-countup

    Args:
        start: Starting number (default: 0)
        end: Ending number (required)
        duration: Animation duration in seconds (default: 2)
        decimals: Number of decimal places (default: 0)
        decimal: Decimal character (default: ".")
        prefix: Text before number (e.g., "$")
        suffix: Text after number (e.g., "+", "%")
        separator: Thousands separator (default: ",")
        delay: Delay before animation starts in seconds (default: 0)
        enable_scroll_spy: Start animation when scrolled into view (default: False)
        scroll_spy_delay: Delay for scroll spy in ms (default: 0)
        scroll_spy_once: Only trigger scroll spy once (default: False)
        preserve_value: Preserve previous value on props change (default: False)
        use_easing: Use easing animation (default: True)
        **props: Additional component props

    Returns:
        The CountUp component.

    Example:
        count_up(end=1000, duration=2.5, prefix="$", separator=",")
    """
    return CountUp.create(**props)
