from __future__ import annotations

import glob
import os
import subprocess
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AppCategory:
    key: str
    label: str
    icon: str
    mime_types: list[str]
    primary_mime: str


CATEGORIES: list[AppCategory] = [
    AppCategory(
        key="browser",
        label="Web Browser",
        icon="web-browser",
        mime_types=["text/html", "x-scheme-handler/http", "x-scheme-handler/https"],
        primary_mime="x-scheme-handler/http",
    ),
    AppCategory(
        key="filemanager",
        label="File Manager",
        icon="system-file-manager",
        mime_types=["inode/directory"],
        primary_mime="inode/directory",
    ),
    AppCategory(
        key="terminal",
        label="Terminal",
        icon="utilities-terminal",
        mime_types=["application/x-terminal-emulator"],
        primary_mime="application/x-terminal-emulator",
    ),
    AppCategory(
        key="editor",
        label="Text Editor",
        icon="accessories-text-editor",
        mime_types=["text/plain", "text/x-readme"],
        primary_mime="text/plain",
    ),
    AppCategory(
        key="image",
        label="Image Viewer",
        icon="image-viewer",
        mime_types=[
            "image/png",
            "image/jpeg",
            "image/gif",
            "image/webp",
            "image/svg+xml",
        ],
        primary_mime="image/png",
    ),
    AppCategory(
        key="video",
        label="Video Player",
        icon="video-player",
        mime_types=[
            "video/mp4",
            "video/mkv",
            "video/x-matroska",
            "video/webm",
            "video/avi",
        ],
        primary_mime="video/mp4",
    ),
    AppCategory(
        key="audio",
        label="Music Player",
        icon="audio-player",
        mime_types=[
            "audio/mpeg",
            "audio/ogg",
            "audio/flac",
            "audio/x-wav",
            "audio/aac",
        ],
        primary_mime="audio/mpeg",
    ),
    AppCategory(
        key="pdf",
        label="PDF Viewer",
        icon="evince",
        mime_types=["application/pdf"],
        primary_mime="application/pdf",
    ),
]

CATEGORY_BY_KEY: dict[str, AppCategory] = {c.key: c for c in CATEGORIES}


@dataclass
class AppInfo:
    desktop_file: str
    name: str
    icon: str
    exec_cmd: str
    mime_types: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name


_DESKTOP_DIRS = [
    "/usr/share/applications",
    "/usr/local/share/applications",
    os.path.expanduser("~/.local/share/applications"),
]


def _parse_desktop_file(path: str) -> Optional[AppInfo]:
    fields: dict[str, str] = {}
    try:
        with open(path, errors="ignore") as f:
            in_entry = False
            for line in f:
                line = line.strip()
                if line == "[Desktop Entry]":
                    in_entry = True
                    continue
                if line.startswith("[") and in_entry:
                    break
                if in_entry and "=" in line:
                    k, v = line.split("=", 1)
                    fields[k.strip()] = v.strip()
    except OSError:
        return None

    name = fields.get("Name", "")
    exec_cmd = fields.get("Exec", "")
    no_display = fields.get("NoDisplay", "false").lower() == "true"
    hidden = fields.get("Hidden", "false").lower() == "true"
    app_type = fields.get("Type", "")

    if not name or not exec_cmd or no_display or hidden or app_type != "Application":
        return None

    mime_raw = fields.get("MimeType", "")
    mime_types = [m.strip() for m in mime_raw.split(";") if m.strip()]

    return AppInfo(
        desktop_file=os.path.basename(path),
        name=name,
        icon=fields.get("Icon", "application-x-executable"),
        exec_cmd=exec_cmd,
        mime_types=mime_types,
    )


def _get_all_apps() -> list[AppInfo]:
    seen: set[str] = set()
    apps: list[AppInfo] = []

    for directory in _DESKTOP_DIRS:
        for path in sorted(glob.glob(f"{directory}/*.desktop")):
            basename = os.path.basename(path)
            if basename in seen:
                continue
            seen.add(basename)
            info = _parse_desktop_file(path)
            if info:
                apps.append(info)

    apps.sort(key=lambda a: a.name.lower())
    return apps


def get_default_app(category: AppCategory) -> str:
    for mime in category.mime_types:
        try:
            result = subprocess.run(
                ["xdg-mime", "query", "default", mime],
                capture_output=True,
                text=True,
                timeout=3,
            )
            desktop = result.stdout.strip()
            if desktop:
                return desktop
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    return ""


def set_default_app(category: AppCategory, desktop_file: str) -> bool:
    success = True
    for mime in category.mime_types:
        try:
            result = subprocess.run(
                ["xdg-mime", "default", desktop_file, mime],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode != 0:
                success = False
        except (subprocess.TimeoutExpired, FileNotFoundError):
            success = False
    return success


def get_apps_for_category(category: AppCategory) -> list[AppInfo]:
    all_apps = _get_all_apps()
    mime_set = set(category.mime_types)

    _KEYWORD_FALLBACK: dict[str, list[str]] = {
        "terminal": [
            "terminal",
            "console",
            "alacritty",
            "kitty",
            "foot",
            "wezterm",
            "ghostty",
            "xterm",
            "urxvt",
            "tilix",
            "gnome-terminal",
        ],
        "filemanager": [
            "files",
            "manager",
            "nautilus",
            "dolphin",
            "thunar",
            "nemo",
            "pcmanfm",
            "ranger",
            "yazi",
        ],
    }

    if category.key in _KEYWORD_FALLBACK:
        keywords = _KEYWORD_FALLBACK[category.key]
        matched = []
        for app in all_apps:
            name_lower = app.name.lower()
            file_lower = app.desktop_file.lower()
            if (
                any(kw in name_lower for kw in keywords)
                or any(kw in file_lower for kw in keywords)
                or bool(mime_set & set(app.mime_types))
            ):
                matched.append(app)
        return matched

    matched = [a for a in all_apps if mime_set & set(a.mime_types)]

    return matched if matched else all_apps


def get_app_info(desktop_file: str) -> Optional[AppInfo]:
    for directory in _DESKTOP_DIRS:
        path = os.path.join(directory, desktop_file)
        if os.path.exists(path):
            return _parse_desktop_file(path)
    return None
