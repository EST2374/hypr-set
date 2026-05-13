import subprocess
from dataclasses import dataclass
from typing import Callable

import hyprset.config as app_config

from .config_utils import replace_in_config
from .look import _find_block_span, _read_value_in_block, _replace_key_in_block


@dataclass
class Setting:
    config_key: str
    pattern: str
    template: str
    type: Callable = str


SETTINGS_INPUT: dict[str, Setting] = {
    "kb_layout": Setting(
        "kb_layout", r"^\s*kb_layout\s*=.*", '\t\tkb_layout = "{value}",'
    ),
    "kb_variant": Setting(
        "kb_variant", r"^\s*kb_variant\s*=.*", '\t\tkb_variant = "{value}",'
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
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()

        span = _find_block_span(content, "input")
        if not span:
            return ""
        block_text = content[span[0] : span[1]]

        import re

        m = re.search(
            rf"\b{re.escape(s.config_key)}\s*=\s*\"?([^\s,\"\n]+)\"?", block_text
        )
        if m:
            return m.group(1)
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


def get_cur_follow_mouse() -> str:
    import re

    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()

        span = _find_block_span(content, "input")
        if not span:
            return ""
        block_text = content[span[0] : span[1]]

        m = re.search(r"\bfollow_mouse\s*=\s*(\d+)", block_text)
        if m:
            val = m.group(1)
            for name, code in FOLLOW_MOUSE.items():
                if code == val:
                    return name
    except FileNotFoundError:
        pass
    return ""


def follow_mouse_change(text: str):
    import re

    code = FOLLOW_MOUSE[text]
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    content = _replace_key_in_block(content, "input", "follow_mouse", code)

    with open(app_config.CONFIG_FILE_LUA, "w") as f:
        f.write(content)
