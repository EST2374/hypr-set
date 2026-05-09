import glob
import os
import re
import subprocess

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from hyprset.config import CONFIG_FILE


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

        new_line = f"exec-once = {exec_cmd}"

        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if "# Autostart end" in content:
            content = content.replace("# Autostart end", f"{new_line}\n# Autostart end")
        else:
            content += f"\n{new_line}"

        with open(CONFIG_FILE, "w") as f:
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

        new_line = f"exec-once = {new_script}"

        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if "# Autostart end" in content:
            content = content.replace("# Autostart end", f"{new_line}\n# Autostart end")
        else:
            content += f"\n{new_line}"

        with open(CONFIG_FILE, "w") as f:
            f.write(content)

        parent = self.parent()
        if parent and hasattr(parent, "current_autostart"):
            parent.current_autostart.addItem(new_script)

        self.accept()


class AddEnvDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Environment")
        self.resize(800, 300)

        env_label = QLabel("Add Environment: ")
        self.env_edit_line = QLineEdit()
        button_add = QPushButton("Add")
        button_add.clicked.connect(self.add_env)

        layout_h = QHBoxLayout()
        layout_h.addWidget(env_label)
        layout_h.addWidget(self.env_edit_line)

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

    def add_env(self):
        new_env = self.env_edit_line.text()

        new_line = f"env = {new_env}"

        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if "# Envirnonment end" in content:
            content = content.replace(
                "# Envirnonment end", f"{new_line}\n# Envirnonment end"
            )
        else:
            content += f"\n{new_line}"

        with open(CONFIG_FILE, "w") as f:
            f.write(content)

        parent = self.parent()
        if parent and hasattr(parent, "current_autostart"):
            parent.current_env.addItem(new_env)

        self.accept()


class PickColorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose color")
        self.resize(300, 100)

        layout = QVBoxLayout(self)
        self.setLayout(layout)


class Connect_to_Wifi(QDialog):
    def __init__(self, ssid: str, parent=None):
        super().__init__(parent)
        self.ssid = ssid
        self.setWindowTitle(f"Connect to {ssid}")
        self.resize(400, 160)

        connect_label = QLabel(f"Connecting to: <b>{ssid}</b>")

        password_label = QLabel("Password:")
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit.setPlaceholderText("Leave empty for open networks")

        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_line_edit)

        self.show_password = QCheckBox("Show password")
        self.show_password.toggled.connect(self.toggle_password_visibility)

        self.status_label = QLabel("")

        connect_button = QPushButton("Connect")
        connect_button.clicked.connect(self.connect_to_wifi)

        main_layout = QVBoxLayout()
        main_layout.addWidget(connect_label)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.show_password)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(connect_button)
        self.setLayout(main_layout)

    def center_on_parent(self):
        if self.parent():
            parent_geo = self.parent().frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)

    def toggle_password_visibility(self, is_checked):
        mode = QLineEdit.EchoMode.Normal if is_checked else QLineEdit.EchoMode.Password
        self.password_line_edit.setEchoMode(mode)

    def connect_to_wifi(self):
        password = self.password_line_edit.text().strip()

        args = ["dev", "wifi", "connect", self.ssid]
        if password:
            args += ["password", password]

        self._process = QProcess(self)
        self._process.finished.connect(self._handle_result)
        self._process.start("nmcli", args)
        self.status_label.setText("Connecting…")

    def _handle_result(self, exit_code):
        output = self._process.readAllStandardOutput().data().decode().strip()
        error = self._process.readAllStandardError().data().decode().strip()

        if exit_code == 0:
            self.status_label.setText(f"Connected to {self.ssid}.")
        else:
            reason = error or output or "Unknown error"
            self.status_label.setText(f"Failed: {reason}")


class Update(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update")
        self.resize(800, 300)

        self.list_programs = QListWidget()
        self.list_programs.addItems(self.get_updates())
        self.list_programs.itemDoubleClicked.connect(self.update_item)

        button_update_all = QPushButton("Update All")
        button_update_all.clicked.connect(self.update_all)

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_programs)
        layout.addWidget(button_update_all)
        self.setLayout(layout)

    def center_on_parent(self):
        if self.parent():
            parent_geo = self.parent().frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)

    def get_updates(self) -> list[str]:
        updates_list = []
        try:
            result = subprocess.run(
                ["checkupdates"],
                capture_output=True,
                text=True,
                check=True,
            )
            updates_list = result.stdout.splitlines()
            return updates_list
        except subprocess.CalledProcessError as e:
            if e.returncode == 2:
                return []
            print(f"An error occurred: {e}")
            return []

    def update_all(self):
        cmd = ["pkexec", "pacman", "-Syu", "--noconfirm"]
        self._run_pacman_command(cmd, "System Update")

    def update_item(self, item):
        package_name = item.text().split()[0]
        cmd = ["pkexec", "pacman", "-S", package_name, "--noconfirm"]
        self._run_pacman_command(cmd, f"Update {package_name}")

    def _run_pacman_command(self, cmd, title):
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            info = QMessageBox()
            info.resize(800, 300)
            info.information(self, title, f"Finished!\n\n{result.stdout[-500:]}")
            self.refresh_list()

        except subprocess.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else "Error."
            QMessageBox.critical(self, "Error", f"Details:\n{error_msg}")

    def refresh_list(self):
        self.list_programs.clear()
        self.list_programs.addItems(self.get_updates())
