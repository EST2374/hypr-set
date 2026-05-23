from __future__ import annotations

from enum import Enum, auto
from pathlib import Path

from PySide6.QtCore import QSettings

_ASSETS_DIR = Path(__file__).parent.parent / "assets"

_THEME_FILES: dict[str, str] = {
    "dark": "style_dark.qss",
    "light": "style_light.qss",
    "mini_dark": "style_mini_dark.qss",
    "mini_light": "style_mini_light.qss",
}

_SETTINGS_ORG = "hyprset"
_SETTINGS_APP = "hyprset"
_SETTINGS_KEY = "ui/theme"
_DEFAULT_THEME_NAME = "DARK"


class Theme(Enum):
    SYSTEM = auto()
    DARK = auto()
    LIGHT = auto()
    MINI_DARK = auto()
    MINI_LIGHT = auto()


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
    if theme == Theme.SYSTEM:
        app.setStyleSheet("")  # type: ignore[attr-defined]
    else:
        qss = load_stylesheet(theme)
        app.setStyleSheet(qss)  # type: ignore[attr-defined]
    save_theme(theme)


def save_theme(theme: Theme) -> None:
    settings = QSettings(_SETTINGS_ORG, _SETTINGS_APP)
    settings.setValue(_SETTINGS_KEY, theme.name)


def load_saved_theme() -> Theme:
    settings = QSettings(_SETTINGS_ORG, _SETTINGS_APP)
    raw = settings.value(_SETTINGS_KEY, _DEFAULT_THEME_NAME)
    name = str(raw) if raw is not None else _DEFAULT_THEME_NAME
    try:
        return Theme[name]
    except KeyError:
        return Theme[_DEFAULT_THEME_NAME]


def current_theme_name(theme: Theme) -> str:
    return theme.name.replace("_", " ").title()
