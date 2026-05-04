import json
import re
import subprocess

from PySide6.QtWidgets import QWidget

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Monitor Settings
        # TODO For Multi Monitor Setup
        self.monitors_box.addItems(self.get_monitor_names())
        self.resolution_box.addItems(self.get_monitor_resolution())
        # self.position_box.addItems(self.get_monitor_count())
        # Needs to be fixed
        self.position_box.addItem("auto")
        self.scale_box.addItems(["1.0", "2.0"])
        self.apply_button.clicked.connect(self.apply_monitor_settings)

        # Environment Settings
        self.current_autostart.addItems(self.get_current_autostarts())
        self.del_autostart_button.clicked.connect(self.del_autostart)

    # Monitor Funcions
    def get_monitor_names(self) -> list[str]:
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

    def get_monitor_resolution(self) -> list[str]:
        try:
            mon_index = self.monitors_box.currentIndex()
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

    def get_monitor_count(self) -> list[str]:
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

    def apply_monitor_settings(self):
        mon_name = self.monitors_box.currentText()
        mon_res = self.resolution_box.currentText()
        mon_pos = self.position_box.currentText()
        mon_scale = self.scale_box.currentText()

        config_file = "/home/est/Work/hypr-set/hyprland.conf"

        new_line = f"monitor = {mon_name},{mon_res},{mon_pos},{mon_scale}"

        pattern = r"^monitor\s*=.*"

        with open(config_file, "r") as file:
            content = file.read()

        new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)

        with open(config_file, "w") as file:
            file.write(new_content)

    # Autostart Functions
    def get_current_autostarts(self) -> list[str]:
        all_autostart = []

        config_file = "/home/est/Work/hypr-set/hyprland.conf"

        try:
            with open(config_file, "r") as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("exec-once") and not line.startswith("#"):
                        command = line.split("=", 1)[-1].strip()
                        all_autostart.append(command)
            return all_autostart
        except FileNotFoundError:
            print(f"Error: {config_file} not found.")
            return all_autostart

    def del_autostart(self):
        config_file = "/home/est/Work/hypr-set/hyprland.conf"

        current_row = self.current_autostart.currentRow()
        if current_row != -1:
            item = self.current_autostart.takeItem(current_row)
            target = f"exec-once = {item.text()}"
            with open(config_file, "r") as f:
                lines = f.readlines()

            with open(config_file, "w") as f:
                for line in lines:
                    if not line.strip().startswith(target):
                        f.write(line)
            print(target)
            del item
