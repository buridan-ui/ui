"""
Buridan UI Charts - API references for Line Charts
"""

line_chart_api = {
    "LineChart": {
        "description": "Instantiate the LineChart with data.",
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
        "description": "Add a data series to the line chart.",
        "arguments": {
            "key": {
                "type": "str",
                "required": "True",
                "default": None,
                "description": "Data key for this series.",
            },
            "stroke": {
                "type": "str",
                "required": "False",
                "default": "'var(--chart-1)'",
                "description": "Stroke color.",
            },
            "stroke_width": {
                "type": "int",
                "required": "False",
                "default": 2,
                "description": "Line thickness.",
            },
            "type_": {
                "type": "str",
                "required": "False",
                "default": "'natural'",
                "description": "Line type (e.g., 'monotone', 'linear').",
            },
            "dot": {
                "type": "Union[bool, str]",
                "required": "False",
                "default": "False",
                "description": "Show dots on data points.",
            },
            "is_animation_active": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Enable line animation.",
            },
            "stack_id": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "ID for stacking lines.",
            },
            "name": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Custom legend name.",
            },
            "legend_type": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Legend symbol shape.",
            },
            "label": {
                "type": "Union[bool, Dict[str, Any]]",
                "required": "False",
                "default": "None",
                "description": "Show value labels.",
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
                "default": "'100%'",
                "description": "Chart width.",
            },
            "height": {
                "type": "int",
                "required": "True",
                "default": 250,
                "description": "Chart height in pixels.",
            },
        },
    },
    "config": {
        "description": "Additional config for the line chart.",
        "arguments": {
            "sync_id": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Sync charts by ID.",
            },
            "layout": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Layout direction (horizontal or vertical).",
            },
            "margin": {
                "type": "Optional[Dict[str, int]]",
                "required": "False",
                "default": "None",
                "description": "Outer chart margins.",
            },
            "sync_method": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Sync method, e.g., 'index'.",
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
                "description": "Extra Recharts elements.",
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
                "description": "Series key to legend label mapping.",
            },
            "position": {
                "type": "str",
                "required": "False",
                "default": "'bottom'",
                "description": "Legend position ('top' or 'bottom').",
            },
        },
    },
    "y_axis": {
        "description": "Enable or disable Y axis with optional style overrides.",
        "arguments": {
            "show": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show Y axis.",
            },
            "type_": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Axis scale type.",
            },
            "data_key": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Data key for Y axis.",
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
                "default": 5,
                "description": "Min gap between ticks.",
            },
            "tick_size": {
                "type": "int",
                "required": "False",
                "default": 10,
                "description": "Tick size.",
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
                "description": "Extra attributes.",
            },
        },
    },
    "x_axis": {
        "description": "Enable or disable X axis with optional style overrides.",
        "arguments": {
            "show": {
                "type": "bool",
                "required": "False",
                "default": "True",
                "description": "Show X axis.",
            },
            "type_": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Axis scale type.",
            },
            "data_key": {
                "type": "Optional[str]",
                "required": "False",
                "default": "None",
                "description": "Data key for X axis.",
            },
            "axis_line": {
                "type": "bool",
                "required": "False",
                "default": "False",
                "description": "Show axis line.",
            },
            "tick_size": {
                "type": "int",
                "required": "False",
                "default": 10,
                "description": "Tick size.",
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
                "default": "{'fontSize': '12px'}",
                "description": "Extra X axis attributes.",
            },
            "interval": {
                "type": "Optional[str]",
                "required": "False",
                "default": "'preserveStartEnd'",
                "description": "Tick interval policy.",
            },
        },
    },
}
