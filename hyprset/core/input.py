import re
import subprocess
from dataclasses import dataclass
from typing import Callable

from hyprset.config import CONFIG_FILE

from .config_utils import replace_in_config


@dataclass
class Setting:
    config_key: str
    pattern: str
    template: str
    type: Callable = str


SETTINGS_INPUT: dict[str, Setting] = {
    "kb_layout": Setting("kb_layout", r"^\s*kb_layout\s*=.*", "\tkb_layout = {value}"),
    "kb_variant": Setting(
        "kb_variant", r"^\s*kb_variant\s*=.*", "\tkb_variant = {value}"
    ),
}

FOLLOW_MOUSE: dict[str, str] = {
    "Manual": "0",
    "Automatic": "1",
    "Semi-Automatic": "2",
    "Locked": "3",
}


def write_setting_input(setting: str, value: str):
    s = SETTINGS_INPUT[setting]
    replace_in_config(s.pattern, s.template.format(value=value))


def get_cur_item(setting: str) -> str:
    s = SETTINGS_INPUT[setting]
    try:
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith(s.config_key):
                    return s.type(line.split("=", 1)[-1].strip())
    except FileNotFoundError:
        return ""
    return ""


def get_kb_variants() -> list[str]:
    try:
        kb_layout = get_cur_item("kb_layout")
        result = subprocess.run(
            ["localectl", "list-x11-keymap-variants", f"{kb_layout}"],
            capture_output=True,
            text=True,
            check=True,
        )
        variants = result.stdout.strip().split("\n")
        return [v for v in variants if v]
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return []


def get_cur_follow_mouse():
    try:
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("follow_mouse"):
                    val = line.split("=", 1)[-1].strip()

                    for name, code in FOLLOW_MOUSE.items():
                        if code == val:
                            return name
    except FileNotFoundError:
        return ""
    return ""


def follow_mouse_change(text):
    code = FOLLOW_MOUSE[text]
    replace_in_config(r"^\s*follow_mouse\s*=.*", f"\tfollow_mouse = {code}")
