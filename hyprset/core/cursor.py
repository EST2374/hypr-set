import re
import subprocess
from pathlib import Path

import hyprset.config as app_config

_ICON_DIRS = [
    Path.home() / ".local/share/icons",
    Path("/usr/share/icons"),
]

# TODO
# Reload environments list


def get_all_cursors() -> list[str]:
    seen: set[str] = set()
    cursors: list[str] = []

    for icon_dir in _ICON_DIRS:
        if not icon_dir.exists():
            continue
        for manifest in icon_dir.rglob("manifest.hl"):
            theme_dir = manifest.parent
            if not (theme_dir / "hyprcursors").is_dir():
                continue
            name = theme_dir.name
            if name not in seen:
                seen.add(name)
                cursors.append(name)

    return sorted(cursors)


def select_cursor(selected_cursor: str):
    try:
        subprocess.run(
            ["hyprctl", "setcursor", selected_cursor, "24"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None


def set_default_cursor(selected_cursor: str):
    config_path = Path(app_config.CONFIG_FILE_LUA)
    env_line = f'hl.env("HYPRCURSOR_THEME", "{selected_cursor}")'

    try:
        content = config_path.read_text()
    except FileNotFoundError:
        print("File not found")
        return

    pattern = r'hl\.env\("HYPRCURSOR_THEME",\s*"[^"]*"\)'

    if re.search(pattern, content):
        content = re.sub(pattern, env_line, content)
    else:
        size_match = re.search(r'(hl\.env\("HYPRCURSOR_SIZE",[^\n]*\n)', content)
        if size_match:
            insert_at = size_match.end()
            content = content[:insert_at] + env_line + "\n" + content[insert_at:]
        else:
            content += f"\n{env_line}\n"

    config_path.write_text(content)
