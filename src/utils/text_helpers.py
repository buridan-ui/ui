import re


def slugify(text: str) -> str:
    """Converts text to a URL-friendly slug."""
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text.lower()
