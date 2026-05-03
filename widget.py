import json
import subprocess

from PySide6.QtWidgets import QWidget

from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Monitor Settings
        self.monitors_box.addItems(self.get_monitor_names())
        self.resolution_box.addItems(self.get_monitor_resolution())
        self.position_box.addItems(self.get_monitor_count())

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
