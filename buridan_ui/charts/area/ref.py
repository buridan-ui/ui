"""
Buridan UI Charts - API references for Area Charts
"""

area_chart_api = {
    "AreaChart": {
        "description": "Instantiate the AreaChart with data.",
        "arguments": {
            "data": {
                "type": "List[Dict[str, Any]]",
                "required": "True",
                "default": None,
                "description": "The list of data points to be plotted.",
            }
        },
    },
    "x": {
        "description": "Set the XAxis data key.",
        "arguments": {
            "key": {
                "type": "str",
                "required": "True",
                "default": None,
                "description": "The key in data to use for the X axis.",
            }
        },
    },
    "series": {
        "description": "Add a data series to the area chart.",
        "arguments": {
            "key": {
                "type": "str",
                "required": "True",
                "default": None,
                "description": "Data key for this series.",
            },
            "color": {
                "type": "str",
                "required": "False",
                "default": "'chart-1'",
                "description": "Fill color (CSS variable or raw color).",
            },
            "stroke": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Stroke color override (defaults to color).",
            },
            "gradient": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Use gradient fill instead of solid color.",
            },
            "type_": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Type of the area curve (e.g., 'monotone').",
            },
            "stack_id": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "ID for stacking series.",
            },
            "x_axis_id": {
                "type": "Optional[Union[str, int]]",
                "required": "False",
                "default": "None",
                "description": "X axis ID to use.",
            },
            "y_axis_id": {
                "type": "Optional[Union[str, int]]",
                "required": "False",
                "default": "None",
                "description": "Y axis ID to use.",
            },
            "dot": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "None",
                "description": "Whether to show dots on data points.",
            },
            "active_dot": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "None",
                "description": "Whether to highlight active dots.",
            },
            "stroke_width": {
                "type": "Optional[int]",
                "required": "False",
                "default": "1",
                "description": "Width of the stroke.",
            },
            "connect_nulls": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "None",
                "description": "Connect null data points.",
            },
            "is_animation_active": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "True",
                "description": "Enable animation.",
            },
            "on_click": {
                "type": "Optional[Any]",
                "required": "False",
                "default": "None",
                "description": "Click event handler.",
            },
        },
    },
    "tooltip": {
        "description": "Toggle tooltip visibility.",
        "arguments": {
            "show": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Show tooltip if True.",
            }
        },
    },
    "grid": {
        "description": "Toggle grid visibility.",
        "arguments": {
            "show": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Show grid if True.",
            }
        },
    },
    "size": {
        "description": "Set chart size.",
        "arguments": {
            "width": {
                "type": "Union[int, str]",
                "required": "True",
                "default": "100%",
                "description": "Width of the chart (e.g., '100%' or int).",
            },
            "height": {
                "type": "int",
                "required": "True",
                "default": 250,
                "description": "Height of the chart in pixels.",
            },
        },
    },
    "config": {
        "description": "Additional config for the area chart.",
        "arguments": {
            "sync_id": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Sync multiple charts with the same ID.",
            },
            "layout": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Chart layout: 'horizontal' or 'vertical'.",
            },
            "margin": {
                "type": "Optional[Dict[str, int]]",
                "required": "False",
                "default": "None",
                "description": "Margin around chart as dict (e.g., {'top': 10, 'left': 10}).",
            },
            "stack_offset": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Stack offset type, e.g., 'expand'.",
            },
            "sync_method": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Sync method, e.g., 'index'.",
            },
            "reverse_stack_order": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "None",
                "description": "Reverse stacking order.",
            },
        },
    },
    "add": {
        "description": "Add extra recharts components manually.",
        "arguments": {
            "components": {
                "type": "Any",
                "required": "False",
                "default": "None",
                "description": "One or more recharts components.",
            }
        },
    },
    "legend": {
        "description": "Configure custom legend labels and position.",
        "arguments": {
            "labels": {
                "type": "Dict[str, str]",
                "required": "True",
                "default": None,
                "description": "Mapping of series key to legend label text.",
            },
            "position": {
                "type": "str",
                "required": "False",
                "default": "'bottom'",
                "description": "Legend position: 'top' or 'bottom'.",
            },
        },
    },
    "y_axis": {
        "description": "Enable or disable Y axis with optional style overrides.",
        "arguments": {
            "enabled": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Set True to show Y axis.",
            },
            "axis_line": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show Y axis line.",
            },
            "min_tick_gap": {
                "type": "int",
                "required": "False",
                "default": "50",
                "description": "Minimum gap between Y axis ticks.",
            },
            "tick_size": {
                "type": "int",
                "required": "False",
                "default": "10",
                "description": "Size of Y axis ticks.",
            },
            "tick_line": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show tick lines.",
            },
            "custom_attrs": {
                "type": "Dict[str, Any]",
                "required": "False",
                "default": "None",
                "description": "Additional custom attributes for Y axis.",
            },
        },
    },
}
