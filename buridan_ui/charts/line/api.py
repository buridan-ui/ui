import reflex as rx
from typing import Any, Dict, List, Optional, Union


class LineChart:
    def __init__(self, data: List[Dict[str, Any]]):
        self._data = data
        self._x_key: Optional[str] = None
        self._show_y_axis = False
        self._y_axis_props: Dict[str, Any] = {}
        self._show_x_axis: bool = True
        self._x_axis_props: Dict[str, Any] = {}
        self._series: List[Dict[str, Any]] = []
        self._show_tooltip = True
        self._show_grid = True
        self._width: Union[int, str] = "100%"
        self._height: int = 250
        self._extra: Dict[str, Any] = {}
        self._components: List[Any] = []
        self._custom_legend: Optional[Dict[str, str]] = None
        self._legend_position: str = "bottom"

    def x(self, key: str) -> "LineChart":
        self._x_key = key
        return self

    def series(
        self,
        key: str,
        color: str = "chart-1",
        stroke: Optional[str] = None,
        type_: Optional[str] = None,
        stack_id: Optional[str] = None,
        x_axis_id: Optional[Union[str, int]] = None,
        y_axis_id: Optional[Union[str, int]] = None,
        dot: Optional[bool] = None,
        active_dot: Optional[bool] = None,
        stroke_width: Optional[int] = None,
        connect_nulls: Optional[bool] = None,
        is_animation_active: Optional[bool] = None,
        on_click: Optional[Any] = None,
        **kwargs: Any,
    ) -> "LineChart":
        # Use rx.cond to handle color variable logic reactively
        color_var = rx.cond(color.startswith("var("), color, f"var(--{color})")

        # Handle stroke logic reactively
        stroke_final = (
            rx.cond(
                stroke is None,
                color_var,
                rx.cond(stroke.startswith("var("), stroke, f"var(--{stroke})"),
            )
            if stroke is not None
            else color_var
        )

        line_props = {
            "data_key": key,
            "stroke": stroke_final,
            "stroke_width": stroke_width or 1,
            "type_": type_,
            "stack_id": stack_id,
            "x_axis_id": x_axis_id,
            "y_axis_id": y_axis_id,
            "dot": dot,
            "active_dot": active_dot,
            "connect_nulls": connect_nulls,
            "is_animation_active": rx.cond(
                is_animation_active is None, True, is_animation_active
            )
            if is_animation_active is not None
            else True,
            "on_click": on_click,
        }

        # Store the series config - we'll filter None values in __call__
        self._series.append(
            {
                "config": line_props,
                "kwargs": kwargs,
                "key": key,
            }
        )
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
    ) -> "LineChart":
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
            props.update(kwargs)
            self._x_axis_props = props
        return self

    def y_axis(
        self,
        show: bool = True,
        axis_line: bool = False,
        min_tick_gap: Optional[int] = 50,
        tick_size: Optional[int] = 10,
        tick_line: bool = False,
        custom_attrs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> "LineChart":
        self._show_y_axis = show
        if show:
            props = {
                "axis_line": axis_line,
                "min_tick_gap": min_tick_gap,
                "tick_size": tick_size,
                "tick_line": tick_line,
                "custom_attrs": custom_attrs or {"fontSize": "12px"},
            }
            props.update(kwargs)
            self._y_axis_props = props
        return self

    def tooltip(self, show: bool = True) -> "LineChart":
        self._show_tooltip = show
        return self

    def grid(self, show: bool = True) -> "LineChart":
        self._show_grid = show
        return self

    def size(self, width: Union[int, str], height: int) -> "LineChart":
        self._width = width
        self._height = height
        return self

    def config(
        self,
        sync_id: Optional[str] = None,
        layout: Optional[str] = None,
        margin: Optional[Dict[str, int]] = None,
        stack_offset: Optional[str] = None,
        sync_method: Optional[str] = None,
        reverse_stack_order: Optional[bool] = None,
        **kwargs: Any,
    ) -> "LineChart":
        if sync_id is not None:
            self._extra["sync_id"] = sync_id
        if layout is not None:
            self._extra["layout"] = layout
        if margin is not None:
            self._extra["margin"] = margin
        if stack_offset is not None:
            self._extra["stack_offset"] = stack_offset
        if sync_method is not None:
            self._extra["sync_method"] = sync_method
        if reverse_stack_order is not None:
            self._extra["reverse_stack_order"] = reverse_stack_order

        self._extra.update(kwargs)
        return self

    def legend(self, labels: Dict[str, str], position: str = "bottom") -> "LineChart":
        self._custom_legend = labels
        self._legend_position = position
        return self

    def add(self, *components: Any) -> "LineChart":
        self._components.extend(components)
        return self

    def _create_series_component(self, series_config: Dict[str, Any]) -> rx.Component:
        """Create a single series component with proper None filtering"""
        config = series_config["config"]
        kwargs = series_config["kwargs"]

        # Filter out None values reactively
        filtered_props = {}
        for key, value in config.items():
            if value is not None:
                filtered_props[key] = value

        # Add kwargs
        filtered_props.update(kwargs)

        # Handle labels if present
        label_list = []
        if filtered_props.get("label"):
            if isinstance(filtered_props["label"], dict):
                label_list.append(rx.recharts.label_list(**filtered_props["label"]))
            elif filtered_props["label"] is True:
                label_list.append(rx.recharts.label_list())
            # Remove label from props since it's handled separately
            filtered_props.pop("label", None)

        return rx.recharts.line(*label_list, **filtered_props)

    def __call__(self, **kwargs: Any) -> rx.Component:
        if not self._x_key:
            raise ValueError("X axis key must be set with `.x()` before rendering.")

        # Build components list
        components = []

        # Add custom components first
        components.extend(self._components)

        # Add tooltip conditionally
        if self._show_tooltip:
            components.append(
                rx.recharts.graphing_tooltip(
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

        # Add grid conditionally
        if self._show_grid:
            components.append(
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                )
            )

        # Add Y axis conditionally
        if self._show_y_axis:
            components.append(rx.recharts.y_axis(**self._y_axis_props))

        # Add series components
        for series_config in self._series:
            components.append(self._create_series_component(series_config))

        # Add X axis conditionally
        if self._show_x_axis:
            x_axis_props = dict(self._x_axis_props)
            x_axis_props.setdefault("data_key", self._x_key)
            x_axis_props.setdefault("axis_line", False)
            x_axis_props.setdefault("tick_size", 10)
            x_axis_props.setdefault("tick_line", False)
            x_axis_props.setdefault("interval", "preserveStartEnd")
            x_axis_props.setdefault("custom_attrs", {"fontSize": "12px"})
            components.append(rx.recharts.x_axis(**x_axis_props))

        # Create the main chart
        chart = rx.recharts.line_chart(
            *components,
            data=self._data,
            width=self._width,
            height=self._height,
            **self._extra,
            **kwargs,
        )

        # Handle custom legend
        if self._custom_legend:
            legend_items = []
            for series_config in self._series:
                key = series_config["key"]
                stroke = series_config["config"]["stroke"]
                label = self._custom_legend.get(key, key)

                legend_items.append(
                    rx.hstack(
                        rx.box(bg=stroke, class_name="w-3 h-3 rounded-sm"),
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
