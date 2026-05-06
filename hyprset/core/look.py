import re

from hyprset.config import CONFIG_FILE, REAL_CONFIG


def get_cur_value(setting: str) -> int:
    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if setting == "angle":
                    if "deg" in line:
                        value_part = line.split("=", 1)[-1].strip().split()[-1]
                        return int(value_part.replace("deg", ""))

                if setting == "gaps_in":
                    if line.startswith("gaps_in"):
                        value = line.split("=", 1)[-1].strip()
                        return int(value)

                if setting == "gaps_out":
                    if line.startswith("gaps_out"):
                        value = line.split("=", 1)[-1].strip()
                        return int(value)

                if setting == "border_size":
                    if line.startswith("border_size"):
                        value = line.split("=", 1)[-1].strip()
                        return int(value)

        return 0
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return 45


def set_gabs_in_box(self, setting: str):

    new_line = ""
    pattern = ""

    if setting == "angle":
        number = self.angle_spinBox.value()
        pattern = r"(\s*col\.active_border\s*=.*?)\d+deg"
        new_line = rf"\g<1>{number}deg"

    elif setting == "gaps_in":
        number = self.gabs_in_spinBox.value()
        pattern = r"^\s*gaps_in\s*=.*"
        new_line = f"\tgaps_in = {number}"

    elif setting == "gaps_out":
        number = self.gaps_out_spinBox.value()
        pattern = r"^\s*gaps_out\s*=.*"
        new_line = f"\tgaps_out = {number}"

    elif setting == "border_size":
        number = self.border_size_spinBox.value()
        pattern = r"^\s*border_size\s*=.*"
        new_line = f"\tborder_size = {number}"

    with open(CONFIG_FILE, "r") as file:
        content = file.read()

    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

    with open(CONFIG_FILE, "w") as file:
        file.write(new_content)


def change_bool_check(setting: str):
    new_line = ""
    pattern = ""

    if setting == "resize":
        state = get_state_check("resize")
        if state == "true":
            state = "false"
        else:
            state = "true"

        pattern = r"^\s*resize_on_border\s*=.*"
        new_line = f"\tresize_on_border = {state}"

    elif setting == "tearing":
        state = get_state_check("tearing")
        if state == "true":
            state = "false"
        else:
            state = "true"

        pattern = r"^\s*allow_tearing\s*=.*"
        new_line = f"\tallow_tearing = {state}"

    with open(CONFIG_FILE, "r") as file:
        content = file.read()

    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

    with open(CONFIG_FILE, "w") as file:
        file.write(new_content)


def get_state_check(setting: str):
    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if setting == "resize":
                    if line.startswith("resize_on_border"):
                        value = line.split("=", 1)[-1].strip()
                        return value
                if setting == "tearing":
                    if line.startswith("allow_tearing"):
                        value = line.split("=", 1)[-1].strip()
                        return value
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return "false"


def change_layout(self):
    new_layout = self.layout_comboBox.currentText().lower()

    pattern = r"^\s*layout\s*=.*"
    new_line = f"\tlayout = {new_layout}"

    with open(CONFIG_FILE, "r") as file:
        content = file.read()

    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

    with open(CONFIG_FILE, "w") as file:
        file.write(new_content)


def get_cur_layout() -> str:
    value = ""
    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("layout"):
                    value = line.split("=", 1)[-1].strip()

        return value.capitalize()
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return ""
