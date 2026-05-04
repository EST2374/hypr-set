import glob
import json
import os
import re
import subprocess

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

from ui_widget import Ui_Widget


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Menu Bar
        self.quit_program.triggered.connect(QApplication.quit)

        # TODO
        # Make Theme Switcher

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
        self.add_program_button.clicked.connect(self.add_new_autostart)
        self.add_script_button.clicked.connect(self.add_new_script)

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
            del item

    def add_new_autostart(self):
        dialog = AddProgramDialog(self)
        dialog.center_on_parent()
        dialog.exec()

    def add_new_script(self):
        dialog = AddScriptDialog(self)
        dialog.center_on_parent()
        dialog.exec()


class AddProgramDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Autostart Program")
        self.resize(800, 300)

        self.list_programs = QListWidget()
        self.list_programs.addItems(self.get_programs())

        button_add = QPushButton("Add")
        button_add.clicked.connect(self.add_program)

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_programs)
        layout.addWidget(button_add)
        self.setLayout(layout)

    def center_on_parent(self):
        if self.parent():
            parent_geo = self.parent().frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)

    def add_program(self):
        selected_item = self.list_programs.currentItem()
        if not selected_item:
            return

        selected_name = selected_item.text()

        apps = self.get_installed_apps()
        exec_cmd = next(
            (app["exec"] for app in apps if app["name"] == selected_name), None
        )

        if not exec_cmd:
            return

        exec_cmd = re.sub(r"%\w", "", exec_cmd).strip()

        config_file = "/home/est/Work/hypr-set/hyprland.conf"
        new_line = f"exec-once = {exec_cmd}"

        with open(config_file, "r") as f:
            content = f.read()

        if "# Autostart end" in content:
            content = content.replace("# Autostart end", f"{new_line}\n# Autostart end")
        else:
            content += f"\n{new_line}"

        with open(config_file, "w") as f:
            f.write(content)

        parent = self.parent()
        if parent and hasattr(parent, "current_autostart"):
            parent.current_autostart.addItem(exec_cmd)

        self.accept()

    def get_installed_apps(self):
        desktop_dirs = [
            "/usr/share/applications",
            "/usr/local/share/applications",
            os.path.expanduser("~/.local/share/applications"),
        ]

        apps = []
        for directory in desktop_dirs:
            for path in glob.glob(f"{directory}/*.desktop"):
                with open(path, "r", errors="ignore") as f:
                    name, exec_cmd, no_display = None, None, False
                    for line in f:
                        if line.startswith("Name=") and name is None:
                            name = line.strip().split("=", 1)[1]
                        if line.startswith("Exec=") and exec_cmd is None:
                            exec_cmd = line.strip().split("=", 1)[1]
                        if line.startswith("NoDisplay=true"):
                            no_display = True
                    if name and not no_display:
                        apps.append({"name": name, "exec": exec_cmd})

        return sorted(apps, key=lambda x: x["name"])

    def get_programs(self) -> list[str]:
        apps = self.get_installed_apps()
        names = [app["name"] for app in apps]
        return names


class AddScriptDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Autostart Script")
        self.resize(800, 300)

        script_label = QLabel("Add script: ")
        self.script_edit_line = QLineEdit()
        button_add = QPushButton("Add")
        button_add.clicked.connect(self.add_script)

        layout_h = QHBoxLayout()
        layout_h.addWidget(script_label)
        layout_h.addWidget(self.script_edit_line)

        layout = QVBoxLayout()
        layout.addLayout(layout_h)
        layout.addWidget(button_add)
        self.setLayout(layout)

    def center_on_parent(self):
        if self.parent():
            parent_geo = self.parent().frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)

    def add_script(self):
        new_script = self.script_edit_line.text()

        config_file = "/home/est/Work/hypr-set/hyprland.conf"
        new_line = f"exec-once = {new_script}"

        with open(config_file, "r") as f:
            content = f.read()

        if "# Autostart end" in content:
            content = content.replace("# Autostart end", f"{new_line}\n# Autostart end")
        else:
            content += f"\n{new_line}"

        with open(config_file, "w") as f:
            f.write(content)

        parent = self.parent()
        if parent and hasattr(parent, "current_autostart"):
            parent.current_autostart.addItem(new_script)

        self.accept()
