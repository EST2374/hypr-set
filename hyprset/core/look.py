import re

import hyprset.config as app_config

from .config_utils import replace_in_config

# TODO
# ADD INACTIVE COLOR BUTTON

DEFAULTS: dict[str, int | float] = {
    "gaps_in": 5,
    "gaps_out": 20,
    "border_size": 2,
    "rounding": 10,
    "rounding_power": 2,
    "active_opacity": 1.0,
    "inactive_opacity": 1.0,
    "angle": 45,
    "shadow_range": 4,
    "shadow_render_power": 3,
    "blur_size": 3,
    "blur_passes": 1,
    "blur_vib": 0.1696,
}

BOOL_DEFAULTS: dict[str, str] = {
    "resize": "false",
    "tearing": "false",
    "blur_enable": "true",
    "shadow_enable": "true",
}


LUA_SETTING_MAP: dict[str, tuple[str, str]] = {
    "gaps_in": ("general", "gaps_in"),
    "gaps_out": ("general", "gaps_out"),
    "border_size": ("general", "border_size"),
    "rounding": ("decoration", "rounding"),
    "rounding_power": ("decoration", "rounding_power"),
    "active_opacity": ("decoration", "active_opacity"),
    "inactive_opacity": ("decoration", "inactive_opacity"),
    "shadow_range": ("shadow", "range"),
    "shadow_render_power": ("shadow", "render_power"),
    "blur_size": ("blur", "size"),
    "blur_passes": ("blur", "passes"),
    "blur_vib": ("blur", "vibrancy"),
    "sensitivity": ("input", "sensitivity"),
}

LUA_BOOL_MAP: dict[str, tuple[str, str]] = {
    "resize": ("general", "resize_on_border"),
    "tearing": ("general", "allow_tearing"),
    "blur_enable": ("blur", "enabled"),
    "shadow_enable": ("shadow", "enabled"),
    "global_natural_scroll": ("input", "natural_scroll"),
    "natural_scroll_touchpad": ("touchpad", "natural_scroll"),
}


def _find_block_span(content: str, block_name: str) -> tuple[int, int] | None:
    pattern = rf"\b{re.escape(block_name)}\s*=\s*\{{"
    m = re.search(pattern, content)
    if not m:
        return None

    brace_start = m.end() - 1
    depth = 0

    for i, ch in enumerate(content[brace_start:], start=brace_start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return (m.start(), i + 1)

    return None


def _replace_key_in_block(content: str, block: str, lua_key: str, new_value) -> str:
    span = _find_block_span(content, block)
    if not span:
        return content

    start, end = span
    block_text = content[start:end]

    new_block = re.sub(
        rf"(\b{re.escape(lua_key)}\s*=\s*)[^\s,\n]+(,?)",
        rf"\g<1>{new_value}\g<2>",
        block_text,
        count=1,
    )

    return content[:start] + new_block + content[end:]


def _read_value_in_block(block: str, lua_key: str) -> str | None:
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return None

    span = _find_block_span(content, block)
    if not span:
        return None

    block_text = content[span[0] : span[1]]
    m = re.search(rf"\b{re.escape(lua_key)}\s*=\s*([^\s,\n]+)", block_text)
    if m:
        return m.group(1).strip('"')
    return None


def _read_bool_lua(block: str, key: str) -> bool:
    value = _read_value_in_block(block, key)
    return value == "true"


def better_cur_value(setting: str) -> int | float:
    if setting not in LUA_SETTING_MAP:
        return 0.0
    block, lua_key = LUA_SETTING_MAP[setting]
    value = _read_value_in_block(block, lua_key)
    if value is None:
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def better_cur_status(setting: str) -> str:
    LUA_STATUS_MAP = {
        "resize_on_border": ("general", "resize_on_border"),
        "allow_tearing": ("general", "allow_tearing"),
    }
    if setting not in LUA_STATUS_MAP:
        return ""
    block, lua_key = LUA_STATUS_MAP[setting]
    return _read_value_in_block(block, lua_key) or ""


def better_cur_enabled(block: str) -> bool:
    return _read_bool_lua(block, "enabled")


def read_bool_lua(setting: str) -> bool:
    if setting not in LUA_BOOL_MAP:
        return False
    block, lua_key = LUA_BOOL_MAP[setting]
    return _read_bool_lua(block, lua_key)


def get_angle() -> int:
    value = _read_value_in_block("active_border", "angle")
    try:
        return int(value) if value is not None else 45
    except ValueError:
        return 45


def change_angle_value(value: int):
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    content = _replace_key_in_block(content, "active_border", "angle", value)

    with open(app_config.CONFIG_FILE_LUA, "w") as f:
        f.write(content)


def change_layout(layout_name: str):
    replace_in_config(r"^\s*layout\s*=.*", f'\t\tlayout = "{layout_name.lower()}"')


def change_inactive_border_col(new_color: str):
    replace_in_config(
        r"^\s*inactive_border\s*=.*", f'\t\t\tinactive_border = "{new_color}"'
    )


def get_cur_layout() -> str:
    value = _read_value_in_block("general", "layout")
    return value.strip('"').capitalize() if value else ""


def write_setting_lua(setting: str, value: int | float):
    if setting not in LUA_SETTING_MAP:
        return

    block, lua_key = LUA_SETTING_MAP[setting]

    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    content = _replace_key_in_block(content, block, lua_key, value)

    with open(app_config.CONFIG_FILE_LUA, "w") as f:
        f.write(content)


def change_bool_lua(setting: str):
    if setting not in LUA_BOOL_MAP:
        return

    block, lua_key = LUA_BOOL_MAP[setting]
    current = _read_bool_lua(block, lua_key)
    new_value = "false" if current else "true"

    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return

    content = _replace_key_in_block(content, block, lua_key, new_value)

    with open(app_config.CONFIG_FILE_LUA, "w") as f:
        f.write(content)


def reset_to_defaults():
    for setting, value in DEFAULTS.items():
        write_setting_lua(setting, value)
    for setting in BOOL_DEFAULTS:
        block, lua_key = LUA_BOOL_MAP[setting]
        current = _read_bool_lua(block, lua_key)
        target = BOOL_DEFAULTS[setting] == "true"
        if current != target:
            change_bool_lua(setting)
