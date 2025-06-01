import os
import platform
from datetime import datetime, timedelta


def get_file_times(file_path):
    """Get directory meta data"""

    try:
        dir_stat = os.stat(file_path)
        if platform.system() == "Windows":
            creation_time = dir_stat.st_ctime
        else:
            try:
                creation_time = dir_stat.st_birthtime
            except AttributeError:
                creation_time = dir_stat.st_ctime  # fallback
    except Exception:
        creation_time = None

    # Scan files for latest modified time
    try:
        files = [
            os.path.join(file_path, f)
            for f in os.listdir(file_path)
            if os.path.isfile(os.path.join(file_path, f))
        ]

        latest_mtime = max(os.stat(f).st_mtime for f in files) if files else None
        file_count = len(files)
    except Exception:
        latest_mtime = None
        file_count = 0

    # Format results
    creation_str = (
        datetime.fromtimestamp(creation_time).strftime("%b %d, %Y")
        if isinstance(creation_time, (float, int))
        else "Not available"
    )
    modified_str = (
        datetime.fromtimestamp(latest_mtime).strftime("%b %d, %Y")
        if isinstance(latest_mtime, (float, int))
        else "Not available"
    )

    return [creation_str, modified_str, file_count]


def get_time_ago(past_time, current_time=None):
    """Convert a past datetime to a human-readable 'time ago' string"""
    if current_time is None:
        current_time = datetime.now()

    time_diff = current_time - past_time

    # Less than a minute
    if time_diff < timedelta(minutes=1):
        return "Updated just now"

    # Less than an hour
    if time_diff < timedelta(hours=1):
        minutes = time_diff.seconds // 60
        return f"Updated {minutes} minute{'s' if minutes != 1 else ''} ago"

    # Less than a day
    if time_diff < timedelta(days=1):
        hours = time_diff.seconds // 3600
        return f"Updated {hours} hour{'s' if hours != 1 else ''} ago"

    # Less than a month
    if time_diff < timedelta(days=30):
        days = time_diff.days
        return f"Updated {days} day{'s' if days != 1 else ''} ago"

    # Less than a year
    if time_diff < timedelta(days=365):
        months = time_diff.days // 30
        return f"Updated {months} month{'s' if months != 1 else ''} ago"

    # More than a year
    years = time_diff.days // 365
    return f"Updated {years} year{'s' if years != 1 else ''} ago"
