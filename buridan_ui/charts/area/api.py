import reflex as rx
from typing import Any, Dict, List, Optional, Union


class AreaChart:
    def __init__(self, data: List[Dict[str, Any]]):
        self._data = data
        self._x_key: Optional[str] = None
        self._show_y_axis = False
        self._y_axis_props: Dict[str, Any] = {}
        self._series: List[Dict[str, Any]] = []
        self._show_tooltip = True
        self._show_grid = True
        self._width: Union[int, str] = "100%"
        self._height: int = 250
        self._extra: Dict[str, Any] = {}
        self._components: List[Any] = []
        self._custom_legend: Optional[Dict[str, str]] = None
        self._legend_position: str = "bottom"

    def x(self, key: str) -> "AreaChart":
        self._x_key = key
        return self

    def series(
        self,
        key: str,
        color: str = "chart-1",
        stroke: Optional[str] = None,
        gradient: bool = False,
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
    ) -> "AreaChart":
        # Use rx.cond for conditional color formatting
        color_var = rx.cond(color.startswith("var("), color, f"var(--{color})")

        # Handle stroke with rx.cond
        stroke_final = (
            rx.cond(
                stroke is not None,
                rx.cond(stroke.startswith("var("), stroke, f"var(--{stroke})"),
                color_var,
            )
            if stroke is not None
            else color_var
        )

        # Handle gradient fill with rx.cond
        fill_value = rx.cond(gradient, f"url(#{key})", color_var)

        area_props = {
            "data_key": key,
            "stroke": stroke_final,
            "stroke_width": stroke_width or 1,
            "fill": fill_value,
            "type_": type_,
            "stack_id": stack_id,
            "x_axis_id": x_axis_id,
            "y_axis_id": y_axis_id,
            "dot": dot,
            "active_dot": active_dot,
            "connect_nulls": connect_nulls,
            "is_animation_active": rx.cond(
                is_animation_active is not None, is_animation_active, True
            )
            if is_animation_active is not None
            else True,
            "on_click": on_click,
            "_gradient": gradient,  # Store gradient flag for later use
        }

        # Store all props including None values - let Reflex handle filtering
        area_props.update(kwargs)
        self._series.append(area_props)
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
    ) -> "AreaChart":
        """
        Toggle Y-axis and customize its props.

        Args:
            show: Whether to show the Y-axis.
            axis_line: Show axis line.
            min_tick_gap: Minimum tick gap.
            tick_size: Tick size.
            tick_line: Show tick line.
            custom_attrs: Extra styling for tick labels.
            **kwargs: Any additional recharts.y_axis props.
        """
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

    def tooltip(self, show: bool = True) -> "AreaChart":
        self._show_tooltip = show
        return self

    def grid(self, show: bool = True) -> "AreaChart":
        self._show_grid = show
        return self

    def size(self, width: Union[int, str], height: int) -> "AreaChart":
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
    ) -> "AreaChart":
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

    def legend(self, labels: Dict[str, str], position: str = "bottom") -> "AreaChart":
        self._custom_legend = labels
        self._legend_position = position
        return self

    def add(self, *components: Any) -> "AreaChart":
        self._components.extend(components)
        return self

    def _create_gradient(self, series_data: Dict[str, Any]) -> rx.Component:
        """Create gradient definition for a series"""
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(
                stop_color=series_data["stroke"], offset="5%", stop_opacity=0.8
            ),
            rx.el.svg.stop(
                stop_color=series_data["stroke"], offset="95%", stop_opacity=0.1
            ),
            id=series_data["data_key"],
            x1=0,
            x2=0,
            y1=0,
            y2=1,
        )

    def _create_legend_item(self, series_data: Dict[str, Any]) -> rx.Component:
        """Create a legend item for a series"""
        return rx.hstack(
            rx.box(bg=series_data["stroke"], class_name="w-3 h-3 rounded-sm"),
            rx.text(
                rx.cond(
                    self._custom_legend is not None,
                    self._custom_legend.get(
                        series_data["data_key"], series_data["data_key"]
                    ),
                    series_data["data_key"],
                ),
                class_name="text-sm font-semibold",
                color=rx.color("slate", 11),
            ),
            spacing="2",
            align="center",
        )

    def __call__(self, **kwargs: Any) -> rx.Component:
        if not self._x_key:
            raise ValueError("X axis key must be set with `.x()` before rendering.")

        components = []

        # Create gradients for series that use them
        gradients = []
        for s in self._series:
            # Check if this series was configured with gradient=True
            if s.get("_gradient", False):
                gradients.append(self._create_gradient(s))

        # Add defs if we have gradients
        if gradients:
            components.append(rx.el.svg.defs(*gradients))

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

        # Add y-axis conditionally
        if self._show_y_axis:
            components.append(rx.recharts.y_axis(**self._y_axis_props))

        # Add all series areas
        for s in self._series:
            # Filter out None values for each series
            filtered_props = {k: v for k, v in s.items() if v is not None}
            components.append(rx.recharts.area(**filtered_props))

        # Add x-axis
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

        # Create the main chart
        chart = rx.recharts.area_chart(
            *components,
            data=self._data,
            width=self._width,
            height=self._height,
            **self._extra,
            **kwargs,
        )

        # Handle custom legend conditionally
        if self._custom_legend:
            legend_items = [self._create_legend_item(s) for s in self._series]
            legend = rx.hstack(
                *legend_items,
                class_name="justify-center gap-4 py-2",
            )

            return rx.cond(
                self._legend_position == "top",
                rx.box(legend, chart, class_name="w-full flex flex-col"),
                rx.box(chart, legend, class_name="w-full flex flex-col"),
            )

        return chart
