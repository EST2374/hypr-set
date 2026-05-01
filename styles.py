"""
styles.py — Hyprset stylesheet loader

Usage:
    from styles import load_stylesheet
    app.setStyleSheet(load_stylesheet())
"""

from pathlib import Path


def load_stylesheet(path: str | None = None) -> str:
    """Load and return the QSS stylesheet as a string.

    Args:
        path: Optional custom path to a .qss file.
              Defaults to style.qss next to this module.

    Returns:
        The stylesheet string, or an empty string if the file is not found.
    """
    qss_path = Path(path) if path else Path(__file__).parent / "style.qss"

    if not qss_path.exists():
        print(f"[styles] Warning: stylesheet not found at {qss_path}")
        return ""

    return qss_path.read_text(encoding="utf-8")
