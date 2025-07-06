import reflex as rx
from typing import Any, Dict, List, Optional, Union, Literal


class PieChart:
    def __init__(self, data: List[Dict[str, Any]]):
        self._data = data
        self._data_key: Optional[str] = None
        self._name_key: Optional[str] = None
        self._width: Union[int, str] = "100%"
        self._height: int = 250
        self._tooltip: bool = True
        self._colors: List[str] = []
        self._cells: Optional[List[Any]] = None
        self._inner_radius: Optional[int] = None
        self._outer_radius: Optional[int] = None
        self._label: Union[bool, Dict[str, Any]] = False
        self._label_line: Optional[bool] = None
        self._legend_labels: Optional[Dict[str, str]] = None
        self._legend_position: Literal["top", "bottom"] = "bottom"
        self._extra: Dict[str, Any] = {}
        self._custom_attrs: Dict[str, Any] = {}
        self._class_name: Optional[str] = None
        self._components: List[Any] = []
        self.label_list_props: Optional[Dict[str, Any]] = None

    def values(self, data_key: str, name_key: str) -> "PieChart":
        self._data_key = data_key
        self._name_key = name_key
        return self

    def size(self, width: Union[int, str], height: int) -> "PieChart":
        self._width = width
        self._height = height
        return self

    def tooltip(self, show: bool = True) -> "PieChart":
        self._tooltip = show
        return self

    def colors(self, palette: List[str]) -> "PieChart":
        self._colors = palette
        return self

    def radius(
        self, inner: Optional[int] = None, outer: Optional[int] = None
    ) -> "PieChart":
        self._inner_radius = inner
        self._outer_radius = outer
        return self

    def label(
        self, label: Union[bool, Dict[str, Any]], label_line: Optional[bool] = None
    ) -> "PieChart":
        self._label = label
        self._label_line = label_line
        return self

    def legend(
        self, labels: Dict[str, str], position: Literal["top", "bottom"] = "bottom"
    ) -> "PieChart":
        self._legend_labels = labels
        self._legend_position = position
        return self

    def config(self, **kwargs: Any) -> "PieChart":
        self._extra.update(kwargs)
        return self

    def class_name(self, class_name: str) -> "PieChart":
        self._class_name = class_name
        return self

    def add(self, *components: Any) -> "PieChart":
        self._components.extend(components)
        return self

    def attrs(self, **kwargs: Any) -> "PieChart":
        self._custom_attrs.update(kwargs)
        return self

    def label_list(self, **kwargs):
        self.label_list_props = kwargs
        return self

    def _create_color_cells(self) -> List[rx.Component]:
        """Create color cells reactively using rx.foreach"""
        # Instead of checking if not self._colors, we'll always return the rx.foreach
        # and let it handle empty lists gracefully
        return [rx.foreach(self._colors, lambda color: rx.recharts.cell(fill=color))]

    def _create_pie_children(self) -> List[rx.Component]:
        """Create pie children components reactively"""
        pie_children = []

        # Add label list if present
        if self.label_list_props is not None:
            pie_children.append(rx.recharts.label_list(**self.label_list_props))

        # Handle label dict case - need to use rx.cond for state variables
        if isinstance(self._label, dict):
            pie_children.append(rx.recharts.label_list(**self._label))

        # Add color cells
        color_cells = self._create_color_cells()
        pie_children.extend(color_cells)

        return pie_children

    def _create_pie_props(self) -> Dict[str, Any]:
        """Create pie properties, handling state variables properly"""
        pie_props = {
            "data": self._data,
            "data_key": self._data_key,
            "name_key": self._name_key,
            "stroke": "0",
        }

        # Add optional properties only if they're not None
        if self._inner_radius is not None:
            pie_props["inner_radius"] = self._inner_radius
        if self._outer_radius is not None:
            pie_props["outer_radius"] = self._outer_radius
        if self._class_name is not None:
            pie_props["class_name"] = self._class_name
        if self._label_line is not None:
            pie_props["label_line"] = self._label_line

        # Handle label - use rx.cond for state variables
        if isinstance(self._label, bool):
            pie_props["label"] = self._label
        else:
            pie_props["label"] = True

        # Add custom attributes
        for key, value in self._custom_attrs.items():
            pie_props[key] = value

        return pie_props

    def _create_legend(self, chart: rx.Component) -> rx.Component:
        """Create legend with proper reactive handling"""
        if not self._legend_labels:
            return chart

        # For the legend to work properly with state variables, we need to create
        # a combined data structure that can be iterated over with rx.foreach
        # The best approach is to create legend items statically if possible,
        # or use a state variable that combines colors and labels

        legend_items = []

        # If we have static colors and labels, create them statically
        if isinstance(self._colors, list) and isinstance(self._legend_labels, dict):
            colors = self._colors
            labels = list(self._legend_labels.values())

            for i, color in enumerate(colors):
                label = labels[i] if i < len(labels) else color
                legend_items.append(
                    rx.hstack(
                        rx.box(bg=color, class_name="w-3 h-3 rounded-sm"),
                        rx.text(
                            label,
                            class_name="text-sm font-semibold",
                            color=rx.color("slate", 11),
                        ),
                        spacing="2",
                        align="center",
                    )
                )
        else:
            # If colors or labels are state variables, we need a different approach
            # Create a simple legend that just uses the colors
            def create_legend_item_from_color(color):
                return rx.hstack(
                    rx.box(bg=color, class_name="w-3 h-3 rounded-sm"),
                    rx.text(
                        color,  # Use color as fallback label
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    spacing="2",
                    align="center",
                )

            legend_items = [rx.foreach(self._colors, create_legend_item_from_color)]

        legend = rx.hstack(
            *legend_items, class_name="justify-center gap-4 py-2 flex flex-wrap"
        )

        return rx.box(
            *([legend, chart] if self._legend_position == "top" else [chart, legend]),
            class_name="w-full flex flex-col",
        )

    def __call__(self, **kwargs: Any) -> rx.Component:
        if not self._data_key or not self._name_key:
            raise ValueError("Both data_key and name_key must be set via `.values()`")

        # Create pie children components
        pie_children = self._create_pie_children()

        # Create pie properties
        pie_props = self._create_pie_props()

        # Create chart components
        chart_components = []

        # Add tooltip if enabled
        if self._tooltip:
            chart_components.append(
                rx.recharts.tooltip(
                    is_animation_active=False,
                    separator="",
                    cursor=False,
                    item_style={
                        "color": "currentColor",
                        "display": "flex",
                        "justifyContent": "space-between",
                        "paddingBottom": "0px",
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

        # Add the main pie component
        chart_components.append(rx.recharts.pie(*pie_children, **pie_props))

        # Add any additional components
        chart_components.extend(self._components)

        # Create the main chart
        chart = rx.recharts.pie_chart(
            *chart_components,
            data=self._data,
            width=self._width,
            height=self._height,
            **self._extra,
            **kwargs,
        )

        # Handle legend
        return self._create_legend(chart)
