import os
from random import randint

from ..wrappers.item import item

from .bar.v1 import barchart_v1
from .bar.v2 import barchart_v2
from .bar.v3 import barchart_v3
from .bar.v4 import barchart_v4


BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/pantry/"


def get_source(directory: str, filename: str):
    with open(os.path.join("buridan_ui", "charts", directory, filename), "r") as file:
        return file.read()


def create_export(func, directory, version):
    @item(f"{BASE_PATH}{directory}/v{version}.py", True)
    def export():
        return [func(), get_source(directory, f"v{version}.py"), randint(0, 100000)]

    return export


exports_config = {
    "bar": [
        create_export(barchart_v1, "bar", 1),
        create_export(barchart_v2, "bar", 2),
        create_export(barchart_v3, "bar", 3),
        create_export(barchart_v4, "bar", 4),
    ],
}
