import re

import hyprset.config as app_config

DEFAULT_KEYBINDS: list[str] = [
    'hl.bind(mainMod .. " + Q", hl.dsp.exec_cmd(terminal))',
    'hl.bind(mainMod .. " + C", hl.dsp.window.close())',
    'hl.bind(mainMod .. " + M", hl.dsp.exec_cmd("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch \'hl.dsp.exit()\'"))',
    'hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(fileManager))',
    'hl.bind(mainMod .. " + V", hl.dsp.window.float({ action = "toggle" }))',
    'hl.bind(mainMod .. " + R", hl.dsp.exec_cmd(menu))',
    'hl.bind(mainMod .. " + P", hl.dsp.window.pseudo())',
    'hl.bind(mainMod .. " + J", hl.dsp.layout("togglesplit"))',
    'hl.bind(mainMod .. " + left", hl.dsp.focus({ direction = "left" }))',
    'hl.bind(mainMod .. " + right", hl.dsp.focus({ direction = "right" }))',
    'hl.bind(mainMod .. " + up", hl.dsp.focus({ direction = "up" }))',
    'hl.bind(mainMod .. " + down", hl.dsp.focus({ direction = "down" }))',
    'hl.bind(mainMod .. " + 1", hl.dsp.focus({ workspace = 1 }))',
    'hl.bind(mainMod .. " + 2", hl.dsp.focus({ workspace = 2 }))',
    'hl.bind(mainMod .. " + 3", hl.dsp.focus({ workspace = 3 }))',
    'hl.bind(mainMod .. " + 4", hl.dsp.focus({ workspace = 4 }))',
    'hl.bind(mainMod .. " + 5", hl.dsp.focus({ workspace = 5 }))',
    'hl.bind(mainMod .. " + 6", hl.dsp.focus({ workspace = 6 }))',
    'hl.bind(mainMod .. " + 7", hl.dsp.focus({ workspace = 7 }))',
    'hl.bind(mainMod .. " + 8", hl.dsp.focus({ workspace = 8 }))',
    'hl.bind(mainMod .. " + 9", hl.dsp.focus({ workspace = 9 }))',
    'hl.bind(mainMod .. " + 0", hl.dsp.focus({ workspace = 10 }))',
    'hl.bind(mainMod .. " + SHIFT + 1", hl.dsp.window.move({ workspace = 1 }))',
    'hl.bind(mainMod .. " + SHIFT + 2", hl.dsp.window.move({ workspace = 2 }))',
    'hl.bind(mainMod .. " + SHIFT + 3", hl.dsp.window.move({ workspace = 3 }))',
    'hl.bind(mainMod .. " + SHIFT + 4", hl.dsp.window.move({ workspace = 4 }))',
    'hl.bind(mainMod .. " + SHIFT + 5", hl.dsp.window.move({ workspace = 5 }))',
    'hl.bind(mainMod .. " + SHIFT + 6", hl.dsp.window.move({ workspace = 6 }))',
    'hl.bind(mainMod .. " + SHIFT + 7", hl.dsp.window.move({ workspace = 7 }))',
    'hl.bind(mainMod .. " + SHIFT + 8", hl.dsp.window.move({ workspace = 8 }))',
    'hl.bind(mainMod .. " + SHIFT + 9", hl.dsp.window.move({ workspace = 9 }))',
    'hl.bind(mainMod .. " + SHIFT + 0", hl.dsp.window.move({ workspace = 10 }))',
    'hl.bind(mainMod .. " + S", hl.dsp.workspace.toggle_special("magic"))',
    'hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:magic" }))',
    'hl.bind(mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))',
    'hl.bind(mainMod .. " + mouse_up", hl.dsp.focus({ workspace = "e-1" }))',
    'hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })',
    'hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })',
    'hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"), { locked = true, repeating = true })',
    'hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"), { locked = true, repeating = true })',
    'hl.bind("XF86AudioMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), { locked = true, repeating = true })',
    'hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"), { locked = true, repeating = true })',
    'hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%+"), { locked = true, repeating = true })',
    'hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%-"), { locked = true, repeating = true })',
    'hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true })',
    'hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })',
    'hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })',
    'hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })',
]


def get_keybindings_in_section(file_path: str) -> list[str]:
    binds = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("hl.bind") and not stripped.startswith("--"):
                    binds.append(stripped)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return binds


def all_binds() -> list[str]:
    return get_keybindings_in_section(str(app_config.CONFIG_FILE_LUA))


_WORKSPACE_RE = re.compile(r"hl\.dsp\.(focus|window\.move)\(\{ workspace")
_MOVEMENT_RE = re.compile(r"hl\.dsp\.focus\(\{ direction")
_MULTIMEDIA_RE = re.compile(r'hl\.bind\("XF86[\w]+".*\)')


def get_general_keybindings() -> list[str]:
    return [
        b
        for b in all_binds()
        if not _WORKSPACE_RE.search(b)
        and not _MOVEMENT_RE.search(b)
        and not _MULTIMEDIA_RE.search(b)
    ]


def get_movement_keybindings() -> list[str]:
    return [b for b in all_binds() if _MOVEMENT_RE.search(b)]


def get_workspace_keybindings() -> list[str]:
    return [b for b in all_binds() if _WORKSPACE_RE.search(b)]


def get_multimedia_keybindings() -> list[str]:
    return [b for b in all_binds() if _MULTIMEDIA_RE.search(b)]


def update_keybinding(old_line: str, new_line: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()

        if old_line not in content:
            return False

        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            f.write(content.replace(old_line, new_line, 1))

        return True
    except OSError as e:
        print(f"Error: {e}")
        return False


def add_keybinding(entry: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE_LUA, "a") as f:
            f.write(f"\n{entry}\n")
        return True
    except OSError as e:
        print(f"[add_keybinding] Error: {e}")
        return False


def del_keybinding(entry: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            lines = f.readlines()
        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            for line in lines:
                if line.strip() != entry.strip():
                    f.write(line)
        return True
    except OSError as e:
        print(f"Error: {e}")
        return False


def reset_to_defaults_keybindings() -> bool:
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            lines = f.readlines()

        new_lines = [line for line in lines if not line.strip().startswith("hl.bind")]
        new_lines.append("\n")
        for bind in DEFAULT_KEYBINDS:
            new_lines.append(bind + "\n")

        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            f.writelines(new_lines)

        return True
    except OSError as e:
        print(f"Error: {e}")
        return False
