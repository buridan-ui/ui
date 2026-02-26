import re
from pathlib import Path

# Provide the themes from shadcn/ui #
# by downloading the raw file and cleaning the TypeScript exports and variables #
THEMES_FILE = Path("scripts/themes.json")
OUTPUT_CSS = Path("assets/css/themes.css")

text = THEMES_FILE.read_text()
lines = [
    "/* Generated from https://github.com/shadcn-ui/ui/blob/main/apps/v4/registry/themes.ts */\n"
]

# Split by theme objects manually
theme_splits = re.split(r"\},\s*\{", text)


def extract_vars_from_lines(lines_list):
    var_lines = []
    for line in lines_list:
        line = line.strip().rstrip(",")
        if not line:
            continue
        # Match key: value (quoted or unquoted)
        m = re.match(r'["]?([\w-]+)["]?\s*:\s*["]?(.+?)["]?$', line)
        if m:
            key, val = m.groups()
            var_lines.append(f"  --{key}: {val};")
    return var_lines


for theme_text in theme_splits:
    # Extract theme name
    name_match = re.search(r'name\s*:\s*"([^"]+)"', theme_text)
    if not name_match:
        continue
    name = name_match.group(1)

    # Extract light block lines
    light_lines = []
    dark_lines = []

    in_light = False
    in_dark = False
    brace_count = 0

    for line in theme_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("light: {"):
            in_light = True
            brace_count = 1
            continue
        elif stripped.startswith("dark: {"):
            in_dark = True
            brace_count = 1
            continue

        # Track braces to know when block ends
        if in_light or in_dark:
            brace_count += line.count("{")
            brace_count -= line.count("}")
            if brace_count == 0:
                in_light = False
                in_dark = False
                continue
            if in_light:
                light_lines.append(line)
            if in_dark:
                dark_lines.append(line)

    # Write light CSS
    if light_lines:
        lines.append(f".{name} {{")
        lines.extend(extract_vars_from_lines(light_lines))
        lines.append("}\n")

    # Write dark CSS
    if dark_lines:
        lines.append(f".{name}-dark {{")
        lines.extend(extract_vars_from_lines(dark_lines))
        lines.append("}\n")

OUTPUT_CSS.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_CSS.write_text("\n".join(lines))
print(f"Wrote {OUTPUT_CSS}")
