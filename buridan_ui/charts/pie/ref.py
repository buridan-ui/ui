"""
Buridan UI Charts - API references for Pie Charts
"""

pie_chart_api = {
    "PieChart": {
        "description": "Instantiate the PieChart with data.",
        "arguments": {
            "data": {
                "type": "List[Dict[str, Any]]",
                "required": "True",
                "default": "None",
                "description": "The list of data points to be visualized.",
            }
        },
    },
    "values": {
        "description": "Set the data key for values and name key for labels.",
        "arguments": {
            "data_key": {
                "type": "str",
                "required": "True",
                "default": "None",
                "description": "The key used for the slice values.",
            },
            "name_key": {
                "type": "str",
                "required": "True",
                "default": "None",
                "description": "The key used for the slice names.",
            },
        },
    },
    "size": {
        "description": "Set the width and height of the chart.",
        "arguments": {
            "width": {
                "type": "Union[int, str]",
                "required": "True",
                "default": "'100%'",
                "description": "The chart width (e.g., '100%' or 500).",
            },
            "height": {
                "type": "int",
                "required": "True",
                "default": "250",
                "description": "The chart height in pixels.",
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
                "description": "Show tooltip when hovering over a slice.",
            }
        },
    },
    "colors": {
        "description": "Set fill colors for pie slices.",
        "arguments": {
            "palette": {
                "type": "List[str]",
                "required": "False",
                "default": "[]",
                "description": "A list of color strings (can be static or state-bound).",
            }
        },
    },
    "radius": {
        "description": "Set inner and outer radius for the pie.",
        "arguments": {
            "inner": {
                "type": "Optional[int]",
                "required": "False",
                "default": "None",
                "description": "Inner radius for doughnut effect.",
            },
            "outer": {
                "type": "Optional[int]",
                "required": "False",
                "default": "None",
                "description": "Outer radius (if customized).",
            },
        },
    },
    "label": {
        "description": "Toggle label display and configure label line.",
        "arguments": {
            "label": {
                "type": "Union[bool, Dict[str, Any]]",
                "required": "False",
                "default": "False",
                "description": "Enable default labels or provide props for label customization.",
            },
            "label_line": {
                "type": "Optional[bool]",
                "required": "False",
                "default": "None",
                "description": "Show or hide the line connecting labels to slices.",
            },
        },
    },
    "label_list": {
        "description": "Add a label list component to render labels inside the slices.",
        "arguments": {
            "**kwargs": {
                "type": "Any",
                "required": "False",
                "description": "Props to pass to `label_list`, e.g. `fill`, `class_name`, etc.",
            }
        },
    },
    "legend": {
        "description": "Add a custom legend below or above the chart.",
        "arguments": {
            "labels": {
                "type": "Dict[str, str]",
                "required": "True",
                "default": "None",
                "description": "Mapping of data keys to human-readable legend labels.",
            },
            "position": {
                "type": "Literal['top', 'bottom']",
                "required": "False",
                "default": "'bottom'",
                "description": "Position of the custom legend relative to the chart.",
            },
        },
    },
    "class_name": {
        "description": "Apply a custom class name to the pie component.",
        "arguments": {
            "class_name": {
                "type": "str",
                "required": "False",
                "default": "None",
                "description": "CSS class name for the pie chart.",
            }
        },
    },
    "config": {
        "description": "Add arbitrary Recharts props to the pie chart wrapper.",
        "arguments": {
            "**kwargs": {
                "type": "Any",
                "required": "False",
                "description": "Additional Recharts props like `sync_id`, `margin`, etc.",
            }
        },
    },
    "add": {
        "description": "Append extra custom components to the pie chart.",
        "arguments": {
            "*components": {
                "type": "Any",
                "required": "False",
                "description": "Any additional components to render inside the chart.",
            }
        },
    },
    "attrs": {
        "description": "Pass arbitrary attributes directly to the Pie component.",
        "arguments": {
            "**kwargs": {
                "type": "Any",
                "required": "False",
                "description": "Props to pass directly to the internal `<Pie />` component.",
            }
        },
    },
}
