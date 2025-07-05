import reflex as rx
from typing import Any, Dict, List, Optional, Union, Literal


class BarChart:
    def __init__(self, data: List[Dict[str, Any]]):
        self._data = data
        self._x_key: Optional[str] = None
        self._series: List[Dict[str, Any]] = []
        self._layout: Literal["horizontal", "vertical"] = "horizontal"
        self._width: Union[int, str] = "100%"
        self._height: int = 250
        self._extra: Dict[str, Any] = {}
        self._components: List[Any] = []
        self._custom_legend: Optional[Dict[str, str]] = None
        self._legend_position: str = "bottom"
        self._show_tooltip: bool = True
        self._show_grid: bool = True
        self._show_y_axis: bool = False
        self._y_axis_props: Dict[str, Any] = {}
        self._show_x_axis: bool = True
        self._x_axis_props: Dict[str, Any] = {}

    def x(self, key: str) -> "BarChart":
        self._x_key = key
        return self

    def layout(self, layout: Literal["horizontal", "vertical"]) -> "BarChart":
        self._layout = layout
        return self

    def series(
        self,
        key: str,
        fill: str = "chart-1",
        stack_id: Optional[str] = None,
        radius: Optional[Union[int, List[int]]] = None,
        label: Optional[Union[bool, Dict[str, Any]]] = None,
        is_animation_active: Optional[bool] = True,
        bar_size: Optional[int] = None,
        legend_type: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs: Any,
    ) -> "BarChart":
        # Handle fill color - add var() wrapper if not already present
        if fill.startswith("var("):
            fill_color = fill
        elif fill.startswith("#") or fill.startswith("rgb") or fill.startswith("hsl"):
            fill_color = fill
        else:
            fill_color = f"var(--{fill})"

        bar_props = {
            "data_key": key,
            "fill": fill_color,
            "stack_id": stack_id,
            "radius": radius,
            "label": label,
            "is_animation_active": is_animation_active,
            "bar_size": bar_size,
            "legend_type": legend_type,
            "name": name,
        }
        bar_props.update(kwargs)
        # Remove None values
        bar_props = {k: v for k, v in bar_props.items() if v is not None}
        self._series.append(bar_props)
        return self

    def x_axis(
        self,
        show: bool = True,
        type_: Optional[str] = None,
        data_key: Optional[str] = None,
        hide: bool = False,
        axis_line: bool = False,
        tick_size: Optional[int] = 10,
        tick_line: bool = False,
        custom_attrs: Optional[Dict[str, Any]] = None,
        interval: Optional[str] = "preserveStartEnd",
        **kwargs: Any,
    ) -> "BarChart":
        self._show_x_axis = show
        if show:
            props = {
                "data_key": data_key,
                "hide": hide,
                "type_": type_,
                "axis_line": axis_line,
                "tick_size": tick_size,
                "tick_line": tick_line,
                "custom_attrs": custom_attrs or {"fontSize": "12px"},
                "interval": interval,
            }

            # Add type_ only if specified
            if type_ is not None:
                props["type_"] = type_

            props.update(kwargs)
            self._x_axis_props = props
        return self

    def y_axis(
        self,
        show: bool = True,
        type_: Optional[str] = None,
        hide: bool = False,
        data_key: Optional[str] = None,
        axis_line: bool = False,
        min_tick_gap: Optional[int] = 5,
        tick_size: Optional[int] = 10,
        tick_line: bool = False,
        custom_attrs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> "BarChart":
        self._show_y_axis = show
        if show:
            props = {
                "hide": hide,
                "type_": type_,
                "data_key": data_key,
                "axis_line": axis_line,
                "min_tick_gap": min_tick_gap,
                "tick_size": tick_size,
                "tick_line": tick_line,
                "custom_attrs": custom_attrs or {"fontSize": "12px"},
            }

            # Add type_ only if specified
            if type_ is not None:
                props["type_"] = type_

            props.update(kwargs)
            self._y_axis_props = props
        return self

    def tooltip(self, show: bool = True) -> "BarChart":
        self._show_tooltip = show
        return self

    def grid(self, show: bool = True) -> "BarChart":
        self._show_grid = show
        return self

    def size(self, width: Union[int, str], height: int) -> "BarChart":
        self._width = width
        self._height = height
        return self

    def config(
        self,
        margin: Optional[Dict[str, int]] = None,
        stack_offset: Optional[str] = None,
        sync_id: Optional[str] = None,
        sync_method: Optional[str] = None,
        reverse_stack_order: Optional[bool] = None,
        bar_category_gap: Optional[Union[str, int]] = None,
        bar_gap: Optional[Union[str, int]] = None,
        max_bar_size: Optional[int] = None,
        **kwargs: Any,
    ) -> "BarChart":
        if margin is not None:
            self._extra["margin"] = margin
        if stack_offset is not None:
            self._extra["stack_offset"] = stack_offset
        if sync_id is not None:
            self._extra["sync_id"] = sync_id
        if sync_method is not None:
            self._extra["sync_method"] = sync_method
        if reverse_stack_order is not None:
            self._extra["reverse_stack_order"] = reverse_stack_order
        if bar_category_gap is not None:
            self._extra["bar_category_gap"] = bar_category_gap
        if bar_gap is not None:
            self._extra["bar_gap"] = bar_gap
        if max_bar_size is not None:
            self._extra["max_bar_size"] = max_bar_size

        self._extra.update(kwargs)
        return self

    def legend(self, labels: Dict[str, str], position: str = "bottom") -> "BarChart":
        self._custom_legend = labels
        self._legend_position = position
        return self

    def add(self, *components: Any) -> "BarChart":
        self._components.extend(components)
        return self

    def __call__(self, **kwargs: Any) -> rx.Component:
        if not self._x_key:
            raise ValueError("X axis key must be set with `.x()` before rendering.")

        if not self._series:
            raise ValueError(
                "At least one series must be added with `.series()` before rendering."
            )

        components = []

        # Add tooltip first (like in AreaChart)
        if self._show_tooltip:
            components.append(
                rx.recharts.tooltip(
                    is_animation_active=False,
                    separator="",
                    cursor=False,
                    item_style={
                        "color": "currentColor",
                        "display": "flex",
                        "paddingBottom": "0px",
                        "justifyContent": "space-between",
                        "textTransform": "capitalize",
                    },
                    label_style={"color": rx.color("slate", 10), "fontWeight": "500"},
                    content_style={
                        "background": rx.color_mode_cond(
                            "oklch(0.97 0.00 0)", "oklch(0.14 0.00 286)"
                        ),
                        "borderColor": rx.color("slate", 5),
                        "borderRadius": "5px",
                        "fontFamily": "IBM Plex Mono,ui-monospace,monospace",
                        "fontSize": "0.875rem",
                        "lineHeight": "1.25rem",
                        "fontWeight": "500",
                        "letterSpacing": "-0.01rem",
                        "minWidth": "8rem",
                        "width": "175px",
                        "padding": "0.375rem 0.625rem",
                        "position": "relative",
                    },
                )
            )

        # Add grid
        if self._show_grid:
            components.append(
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                )
            )

        # Add Y axis (like in AreaChart pattern)
        if self._show_y_axis:
            components.append(rx.recharts.y_axis(**self._y_axis_props))

        # Add bars (series) - CRITICAL: Add bars before X axis (like AreaChart adds areas before x_axis)
        for s in self._series:
            label_list = []
            if s.get("label") and isinstance(s["label"], dict):
                label_list.append(rx.recharts.label_list(**s["label"]))
            elif s.get("label") is True:
                label_list.append(rx.recharts.label_list())

            # Create bar component
            bar_props = {k: v for k, v in s.items() if k != "label"}
            components.append(rx.recharts.bar(*label_list, **bar_props))

        # Add X axis LAST (like in AreaChart)
        if self._show_x_axis:
            if self._x_axis_props:
                x_axis_props = dict(self._x_axis_props)
                # Set data_key to x_key if not explicitly provided
                if x_axis_props.get("data_key") is None:
                    x_axis_props["data_key"] = self._x_key
                components.append(rx.recharts.x_axis(**x_axis_props))
            else:
                # Default X axis
                components.append(
                    rx.recharts.x_axis(
                        data_key=self._x_key,
                        axis_line=False,
                        tick_size=10,
                        tick_line=False,
                        interval="preserveStartEnd",
                        custom_attrs={"fontSize": "12px"},
                    )
                )

        # Add any custom components
        components.extend(self._components)

        # Create the bar chart
        chart = rx.recharts.bar_chart(
            *components,
            data=self._data,
            layout=self._layout,
            width=self._width,
            height=self._height,
            **self._extra,
            **kwargs,
        )

        # Handle custom legend
        if self._custom_legend:
            legend_items = []
            for s in self._series:
                data_key = s["data_key"]
                label = self._custom_legend.get(data_key, data_key)
                legend_items.append(
                    rx.hstack(
                        rx.box(bg=s["fill"], class_name="w-3 h-3 rounded-sm"),
                        rx.text(
                            label,
                            class_name="text-sm font-semibold",
                            color=rx.color("slate", 11),
                        ),
                        spacing="2",
                        align="center",
                    )
                )

            legend = rx.hstack(
                *legend_items,
                class_name="justify-center gap-4 py-2",
            )

            return rx.box(
                *(
                    [legend, chart]
                    if self._legend_position == "top"
                    else [chart, legend]
                ),
                class_name="w-full flex flex-col",
            )

        return chart
