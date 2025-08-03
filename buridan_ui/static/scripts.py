import os

from buridan_ui.config import LOCAL_BASE_CHART_PATH, LOCAL_BASE_PANTRY_PATH
from buridan_ui.wrappers.base.utils.meta import get_file_times


def count_python_files_in_folder(folder_name) -> int:
    """Get the total number of files in a folder"""
    total_files = 0

    for _dirpath, _dirnames, filenames in os.walk(folder_name):
        total_files += len(
            [
                f
                for f in filenames
                if f.endswith(".py")
                and f != "__init__.py"
                and f != "api.py"
                and f != "ref.py"
            ]
        )

    return total_files


def get_directory_meta_data():
    from buridan_ui.export import ExportConfig

    config = ExportConfig()
    charts, pantry = {}, {}

    # Get the chart directories metadata
    for directory in config.CHARTS.keys():
        full_path = os.path.join(LOCAL_BASE_CHART_PATH, directory, "")
        charts[directory] = get_file_times(full_path)

    # Get the pantry directories metadata
    for directory in config.COMPONENTS.keys():
        full_path = os.path.join(LOCAL_BASE_PANTRY_PATH, directory, "")
        pantry[directory] = get_file_times(full_path)

    # Write the metadata to static/meta.py
    with open("buridan_ui/static/meta.py", "w") as file:
        file.write(f"""ChartMetaData = {charts}\nPantryMetaData = {pantry}\n""")


if __name__ == "__main__":
    get_directory_meta_data()
