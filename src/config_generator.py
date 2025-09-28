from pathlib import Path
from functools import lru_cache
import datetime


def get_formatted_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%b %d, %Y")


@lru_cache(maxsize=1)
def get_component_config():
    """
    Scans the 'src/charts' and 'src/pantry' directories to dynamically generate
    a configuration for all components, including routes and metadata. The result is cached.
    """
    config = {}
    base_paths = [Path("src/charts"), Path("src/pantry")]

    for base_path in base_paths:
        if not base_path.exists():
            continue

        for component_dir in sorted(base_path.iterdir()):
            if not component_dir.is_dir() or component_dir.name.startswith("__"):
                continue

            versions = sorted(list(component_dir.glob("v[0-9]*.py")))
            if not versions:
                continue

            # Get creation and modification times
            timestamps = [p.stat().st_mtime for p in versions]
            creation_time = min(timestamps) if timestamps else 0
            last_update_time = max(timestamps) if timestamps else 0

            component_name = component_dir.name
            group = base_path.name

            display_name = component_name.replace("_", " ").replace("-", " ").title()

            url_prefix = f"/{group}"
            url_slug = component_name.replace("_", "-")

            if group == "charts":
                display_name += " Charts"
                url = f"{url_prefix}/{url_slug}-charts"
            else:
                url = f"{url_prefix}/{url_slug}"

            id_prefix = component_name

            config[display_name] = {
                "url": url,
                "id_prefix": id_prefix,
                "quantity": len(versions),
                "group": group.title(),
                "dir": component_name,
                "meta": [
                    get_formatted_date(creation_time),
                    get_formatted_date(last_update_time),
                    len(versions),
                ],
            }
    return config
