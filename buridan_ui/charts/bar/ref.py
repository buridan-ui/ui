"""
Buridan UI Charts - API references for Bar Charts
"""

bar_chart_api = {
    "BarChart": {
        "description": "Instantiate the BarChart with data.",
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
        "description": "Set the X axis data key (category axis).",
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
        "description": "Add a data series (bar) to the chart.",
        "arguments": {
            "key": {
                "type": "str",
                "required": "True",
                "default": None,
                "description": "Data key for this bar series.",
            },
            "fill": {
                "type": "str",
                "required": "False",
                "default": "'chart-1'",
                "description": "Fill color (CSS variable or raw color).",
            },
            "stack_id": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "ID to stack bars together.",
            },
            "radius": {
                "type": "Optional[Union[int, List[int]]]",
                "required": "False",
                "default": "0",
                "description": "Corner radius of bars; can be int or list of 4 ints.",
            },
            "stroke": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Stroke color for bar outline.",
            },
            "stroke_width": {
                "type": "Optional[int]",
                "required": "False",
                "default": "1",
                "description": "Width of the bar stroke.",
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
    "y_axis": {
        "description": "Configure the Y axis (usually numeric).",
        "arguments": {
            "enabled": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show Y axis if True.",
            },
            "type_": {
                "type": "str",
                "required": "False",
                "default": "'number'",
                "description": "Axis type, typically 'number' or 'category'.",
            },
            "axis_line": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show axis line.",
            },
            "min_tick_gap": {
                "type": "int",
                "required": "False",
                "default": "50",
                "description": "Minimum gap between ticks.",
            },
            "tick_size": {
                "type": "int",
                "required": "False",
                "default": "10",
                "description": "Size of ticks.",
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
                "description": "Additional props for Y axis.",
            },
        },
    },
    "x_axis": {
        "description": "Configure the X axis (category axis).",
        "arguments": {
            "data_key": {
                "type": "str",
                "required": "False",
                "default": "None",
                "description": "Key for the X axis data.",
            },
            "type_": {
                "type": "str",
                "required": "False",
                "default": "'category'",
                "description": "Axis type, usually 'category'.",
            },
            "axis_line": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Show axis line.",
            },
            "tick_size": {
                "type": "int",
                "required": "False",
                "default": "10",
                "description": "Size of ticks.",
            },
            "tick_line": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Show tick lines.",
            },
            "interval": {
                "type": "Union[int, str]",
                "required": "False",
                "default": "None",
                "description": "Tick interval, e.g. 0, 1, or 'preserveStartEnd'.",
            },
            "custom_attrs": {
                "type": "Dict[str, Any]",
                "required": "False",
                "default": "None",
                "description": "Additional props for X axis.",
            },
        },
    },
    "tooltip": {
        "description": "Configure tooltip visibility and style.",
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
        "description": "Configure Cartesian grid visibility.",
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
        "description": "Set chart dimensions.",
        "arguments": {
            "width": {
                "type": "Union[int, str]",
                "required": "True",
                "default": "'100%'",
                "description": "Chart width (e.g., '100%' or int).",
            },
            "height": {
                "type": "int",
                "required": "True",
                "default": "250",
                "description": "Chart height in pixels.",
            },
        },
    },
    "layout": {
        "description": "Set chart layout orientation.",
        "arguments": {
            "layout": {
                "type": "str",
                "required": "False",
                "default": "'vertical'",
                "description": "Chart layout: 'vertical' or 'horizontal'.",
            }
        },
    },
    "margin": {
        "description": "Set chart margins.",
        "arguments": {
            "margin": {
                "type": "Dict[str, int]",
                "required": "False",
                "default": "None",
                "description": "Margin around chart (e.g., {'top': 10, 'left': 10}).",
            }
        },
    },
    "bar_size": {
        "description": "Set bar width.",
        "arguments": {
            "bar_size": {
                "type": "int",
                "required": "False",
                "default": "25",
                "description": "Width of bars in pixels.",
            }
        },
    },
    "bar_gap": {
        "description": "Set gap between bars.",
        "arguments": {
            "bar_gap": {
                "type": "int",
                "required": "False",
                "default": "4",
                "description": "Gap between bars in pixels.",
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
}
