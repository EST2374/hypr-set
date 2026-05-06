from __future__ import annotations

from enum import Enum, auto
from pathlib import Path

_ASSETS_DIR = Path(__file__).parent.parent / "assets"

_THEME_FILES: dict[str, str] = {
    "dark": "style_dark.qss",
    "light": "style_light.qss",
}


class Theme(Enum):
    DARK = auto()
    LIGHT = auto()


def load_stylesheet(
    theme: Theme = Theme.DARK,
    *,
    custom_path: str | Path | None = None,
) -> str:

    if custom_path is not None:
        qss_path = Path(custom_path)
    else:
        filename = _THEME_FILES[theme.name.lower()]
        qss_path = _ASSETS_DIR / filename

    if not qss_path.exists():
        print(f"[styles] Warning: stylesheet not found at {qss_path}")
        return ""

    return qss_path.read_text(encoding="utf-8")


def apply_theme(app: object, theme: Theme = Theme.DARK) -> None:
    qss = load_stylesheet(theme)
    app.setStyleSheet(qss)  # type: ignore[attr-defined]


def current_theme_name(theme: Theme) -> str:
    return theme.name.capitalize()


def toggle_theme(app, current_theme: Theme) -> Theme:
    next_theme = Theme.LIGHT if current_theme == Theme.DARK else Theme.DARK
    apply_theme(app, next_theme)
    return next_theme
