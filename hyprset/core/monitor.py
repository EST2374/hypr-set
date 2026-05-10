import json
import re
import subprocess

from hyprset.config import CONFIG_FILE


def get_monitor_data() -> list | None:
    try:
        result = subprocess.run(
            ["hyprctl", "monitors", "-j"],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"An error occurred: {e}")
        return None


def get_monitor_names() -> list[str]:
    data = get_monitor_data()
    if data is None:
        return []
    return [monitor["name"] for monitor in data]


def get_monitor_resolution(mon_index: int) -> list[str]:
    data = get_monitor_data()
    if data is None:
        return []
    try:
        return data[mon_index]["availableModes"]
    except (IndexError, KeyError) as e:
        print(f"Error fetching modes: {e}")
        return []


# TODO
# NEED TO BE FIXED (WRONG IMPEMENTATION)
# MONITOR POS


def get_monitor_count() -> int:
    data = get_monitor_data()
    return len(data) if data is not None else 0


def set_default_monitors_in_config():
    data = get_monitor_data()
    if data is None:
        return

    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        lines_to_add = []
        for monitor in data:
            name = monitor["name"]
            if not re.search(
                rf"^monitor\s*=\s*{re.escape(name)}", content, re.MULTILINE
            ):
                lines_to_add.append(f"monitor = {name},auto,auto,1.0")

        if not lines_to_add:
            return

        new_entries = "\n".join(lines_to_add) + "\n"
        new_content = re.sub(
            r"(# Monitor begin\n)(.*?)(# Monitor end)",
            rf"\1\2{new_entries}\3",
            content,
            flags=re.DOTALL,
        )

        with open(CONFIG_FILE, "w") as f:
            f.write(new_content)

    except OSError as e:
        print(f"Error writing config: {e}")


def apply_monitor_settings(mon_name, mon_res, mon_pos, mon_scale):

    new_line = f"monitor = {mon_name},{mon_res},{mon_pos},{mon_scale}"

    pattern = rf"^monitor\s*=\s*{re.escape(mon_name)}.*"

    with open(CONFIG_FILE, "r") as file:
        content = file.read()

    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

    with open(CONFIG_FILE, "w") as file:
        file.write(new_content)


def set_default_monitors_button():
    data = get_monitor_data()
    if data is None:
        return
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        lines_to_add = []
        for monitor in data:
            name = monitor["name"]
            lines_to_add.append(f"monitor = {name},auto,auto,1.0")

        new_entries = "\n".join(lines_to_add) + "\n" if lines_to_add else ""

        new_content = re.sub(
            r"(# Monitor begin\n).*?(# Monitor end)",
            rf"\g<1>{new_entries}\2",
            content,
            flags=re.DOTALL,
        )

        with open(CONFIG_FILE, "w") as f:
            f.write(new_content)
    except OSError as e:
        print(f"Error writing config: {e}")


# TODO
# Mirror
# Rotation
# Enable/Disable
