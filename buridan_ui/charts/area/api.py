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
        color_var = f"var(--{color})" if not color.startswith("var(") else color
        stroke_final = (
            f"var(--{stroke})"
            if stroke and not stroke.startswith("var(")
            else (stroke or color_var)
        )

        area_props = {
            "data_key": key,
            "stroke": stroke_final,
            "stroke_width": stroke_width or 1,
            "fill": f"url(#{key})" if gradient else color_var,
            "type_": type_,
            "stack_id": stack_id,
            "x_axis_id": x_axis_id,
            "y_axis_id": y_axis_id,
            "dot": dot,
            "active_dot": active_dot,
            "connect_nulls": connect_nulls,
            "is_animation_active": is_animation_active
            if is_animation_active is not None
            else True,
            "on_click": on_click,
        }

        area_props = {k: v for k, v in area_props.items() if v is not None}
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

    def __call__(self, **kwargs: Any) -> rx.Component:
        if not self._x_key:
            raise ValueError("X axis key must be set with `.x()` before rendering.")

        gradients = []
        for s in self._series:
            if s.get("fill", "").startswith("url(#"):
                gradients.append(
                    rx.el.svg.linear_gradient(
                        rx.el.svg.stop(
                            stop_color=s["stroke"], offset="5%", stop_opacity=0.8
                        ),
                        rx.el.svg.stop(
                            stop_color=s["stroke"], offset="95%", stop_opacity=0.1
                        ),
                        id=s["data_key"],
                        x1=0,
                        x2=0,
                        y1=0,
                        y2=1,
                    )
                )

        defs = rx.el.svg.defs(*gradients) if gradients else None

        components = []
        if defs:
            components.append(defs)

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

        if self._show_grid:
            components.append(
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                )
            )

        if self._show_y_axis:
            components.append(rx.recharts.y_axis(**self._y_axis_props))

        for s in self._series:
            components.append(rx.recharts.area(**s))

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

        chart = rx.recharts.area_chart(
            *components,
            data=self._data,
            width=self._width,
            height=self._height,
            **self._extra,
            **kwargs,
        )

        if self._custom_legend:
            legend = rx.hstack(
                *[
                    rx.hstack(
                        rx.box(bg=s["stroke"], class_name="w-3 h-3 rounded-sm"),
                        rx.text(
                            self._custom_legend.get(s["data_key"], s["data_key"]),
                            class_name="text-sm font-semibold",
                            color=rx.color("slate", 11),
                        ),
                        spacing="2",
                        align="center",
                    )
                    for s in self._series
                ],
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
