import json
import re
import subprocess

from hyprset.config import CONFIG_FILE


def get_monitor_names() -> list[str]:
    try:
        result = subprocess.run(
            ["hyprctl", "monitors", "-j"],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(result.stdout)
        monitor_names = [monitor["name"] for monitor in data]
        return monitor_names
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
        return []


def get_monitor_resolution(mon_index: int) -> list[str]:
    try:
        result = subprocess.run(
            ["hyprctl", "monitors", "-j"],
            capture_output=True,
            text=True,
            check=True,
        )
        all_monitors = json.loads(result.stdout)
        available_modes = all_monitors[mon_index]["availableModes"]
        return available_modes
    except (subprocess.CalledProcessError, IndexError, KeyError) as e:
        print(f"Error fetching modes: {e}")
        return []


# TODO
# NEED TO BE FIXED (WRONG IMPEMENTATION)


def get_monitor_count() -> list[str]:
    try:
        result = subprocess.run(
            ["hyprctl", "monitors", "-j"],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(result.stdout)
        return []
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
        return []


def apply_monitor_settings(mon_name, mon_res, mon_pos, mon_scale):

    new_line = f"monitor = {mon_name},{mon_res},{mon_pos},{mon_scale}"

    pattern = r"^monitor\s*=.*"

    with open(CONFIG_FILE, "r") as file:
        content = file.read()

    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

    with open(CONFIG_FILE, "w") as file:
        file.write(new_content)


# TODO
# Mirror
# Rotation
# Enable/Disable
