import re
from curses import raw
from dataclasses import dataclass
from typing import Callable

from hyprset.config import CONFIG_FILE


@dataclass
class Setting:
    config_key: str
    pattern: str
    template: str
    type: Callable = int


@dataclass
class BoolSetting:
    config_key: str
    pattern: str
    template: str


SETTINGS: dict[str, Setting] = {
    "gaps_in": Setting("gaps_in", r"^\s*gaps_in\s*=.*", "\tgaps_in = {value}"),
    "gaps_out": Setting("gaps_out", r"^\s*gaps_out\s*=.*", "\tgaps_out = {value}"),
    "border_size": Setting(
        "border_size", r"^\s*border_size\s*=.*", "\tborder_size = {value}"
    ),
    "rounding": Setting("rounding", r"^\s*rounding\s*=.*", "\trounding = {value}"),
    "rounding_power": Setting(
        "rounding_power", r"^\s*rounding_power\s*=.*", "\trounding_power = {value}"
    ),
    "active_opacity": Setting(
        "active_opacity",
        r"^\s*active_opacity\s*=.*",
        "\tactive_opacity = {value}",
        float,
    ),
    "inactive_opacity": Setting(
        "inactive_opacity",
        r"^\s*inactive_opacity\s*=.*",
        "\tinactive_opacity = {value}",
        float,
    ),
    "angle": Setting(
        "angle", r"(\s*col\.active_border\s*=.*?)\d+deg", r"\g<1>{value}deg"
    ),
    "shadow_range": Setting("range", r"^\s*range\s*=.*", "\t\trange = {value}"),
    "shadow_render_power": Setting(
        "render_power", r"^\s*render_power\s*=.*", "\t\trender_power = {value}"
    ),
    "blur_size": Setting("size", r"^\s*size\s*=.*", "\t\tsize = {value}"),
    "blur_passes": Setting("passes", r"^\s*passes\s*=.*", "\t\tpasses = {value}"),
    "blur_vib": Setting(
        "vibrancy", r"^\s*vibrancy\s*=.*", "\t\tvibrancy = {value}", float
    ),
    # TEST FOR INPUT
    "sensitivity": Setting(
        "sensitivity", r"^\s*sensitivity\s*=.*", "\tsensitivity = {value}", float
    ),
}

BOOL_SETTINGS: dict[str, BoolSetting] = {
    "resize": BoolSetting(
        "resize_on_border",
        r"^\s*resize_on_border\s*=.*",
        "\tresize_on_border = {value}",
    ),
    "tearing": BoolSetting(
        "allow_tearing", r"^\s*allow_tearing\s*=.*", "\tallow_tearing = {value}"
    ),
    "blur_enable": BoolSetting(
        "blur_enable",
        r"(blur\s*\{[^}]*?enabled\s*=\s*)[^\s#]+",
        r"\g<1>{value}",
    ),
    "shadow_enable": BoolSetting(
        "shadow_a", r"(shadow\s*\{[^}]*?enabled\s*=\s*)[^\s#]+", r"\g<1>{value}"
    ),
    "global_natural_scroll": BoolSetting(
        "natural_scroll",
        r"(input\s*\{[^{]*?natural_scroll\s*=\s*)[^\s#]+",
        r"\g<1>{value}",
    ),
    "natural_scroll_touchpad": BoolSetting(
        "natural_scroll",
        r"(touchpad\s*\{[^}]*?natural_scroll\s*=\s*)[^\s#]+",
        r"\g<1>{value}",
    ),
}


def replace_in_config(pattern: str, new_line: str):
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)
    with open(CONFIG_FILE, "w") as f:
        f.write(new_content)


def get_cur_value(setting: str) -> int | float:
    s = SETTINGS[setting]
    try:
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if setting == "angle":
                    if "deg" in line:
                        return int(line.split()[-1].replace("deg", ""))
                elif line.startswith(s.config_key):
                    return s.type(line.split("=", 1)[-1].strip())
    except FileNotFoundError:
        return 0
    return 0


def get_state_check(setting: str) -> str:
    s = BOOL_SETTINGS[setting]
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()
            match = re.search(s.pattern, content, flags=re.MULTILINE)
            if match:
                full_match = match.group(0)
                return full_match.split("=", 1)[-1].strip()
    except FileNotFoundError:
        pass
    return "false"


def write_setting(setting: str, value: int | float):
    s = SETTINGS[setting]
    replace_in_config(s.pattern, s.template.format(value=value))


def change_bool_check(setting: str):
    s = BOOL_SETTINGS[setting]
    new_state = "false" if get_state_check(setting) == "true" else "true"
    replace_in_config(s.pattern, s.template.format(value=new_state))


def change_layout(layout_name: str):
    replace_in_config(r"^\s*layout\s*=.*", f"\tlayout = {layout_name.lower()}")


def get_cur_layout() -> str:
    try:
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("layout"):
                    return line.split("=", 1)[-1].strip().capitalize()
    except FileNotFoundError:
        pass
    return ""
