import subprocess
from pathlib import Path

_ICON_DIRS = [
    Path.home() / ".local/share/icons",
    Path("/usr/share/icons"),
]


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
