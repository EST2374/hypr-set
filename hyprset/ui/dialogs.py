import glob
import os
import re
import subprocess

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from hyprset.core.autostart import add_autostart
from hyprset.core.environments import add_env


class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def center_on_parent(self):
        p = self.parent()
        if isinstance(p, QWidget):
            parent_geo = p.frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)


class AddProgramDialog(BaseDialog):
    def __init__(self, parent=None, on_added=None):
        self._on_added = on_added
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

        if add_autostart(exec_cmd) and self._on_added:
            self._on_added(exec_cmd)
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


class AddScriptDialog(BaseDialog):
    def __init__(self, parent=None, on_added=None):
        self._on_added = on_added
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

    def add_script(self):
        new_script = self.script_edit_line.text()
        if not new_script:
            return
        if add_autostart(new_script) and self._on_added:
            self._on_added(new_script)
        self.accept()


class AddEnvDialog(BaseDialog):
    def __init__(self, parent=None, on_added=None):
        self._on_added = on_added
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

    def add_env(self):
        new_env = self.env_edit_line.text()
        if not new_env:
            return
        if add_env(new_env) and self._on_added:
            self._on_added(new_env)
        self.accept()


class Connect_to_Wifi(BaseDialog):
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
        out_data = self._process.readAllStandardOutput().data()
        err_data = self._process.readAllStandardError().data()

        output = bytes(out_data).decode("utf-8").strip()
        error = bytes(err_data).decode("utf-8").strip()

        if exit_code == 0:
            self.status_label.setText(f"Connected to {self.ssid}.")
        else:
            reason = error or output or "Unknown error"
            self.status_label.setText(f"Failed: {reason}")


class Update(BaseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update")
        self.resize(800, 300)

        self.list_programs = QListWidget()
        self.list_programs.addItems(self.get_updates())
        self.list_programs.itemDoubleClicked.connect(self.update_item)

        self.status_label = QLabel("")
        self.output_box = QListWidget()

        button_update_all = QPushButton("Update All")
        button_update_all.clicked.connect(self.update_all)

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_programs)
        layout.addWidget(button_update_all)
        layout.addWidget(self.status_label)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

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
            print(f"Unexpected return code: {e}")
            return []
        except FileNotFoundError:
            print("checkupdates not found")
            return []
        except Exception as e:
            print(f"Fehler: {e}")
            return []

    def update_all(self):
        self._run_pacman_command(["pkexec", "pacman", "-Syu", "--noconfirm"])

    def update_item(self, item):
        package_name = item.text().split()[0]
        self._run_pacman_command(
            ["pkexec", "pacman", "-Sy", package_name, "--noconfirm"]
        )

    def _run_pacman_command(self, cmd: list[str]):
        self.output_box.clear()
        self.status_label.setText("Running…")

        self._process = QProcess(self)
        self._process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)

        self._process.readyReadStandardOutput.connect(self._handle_output)
        self._process.finished.connect(self._handle_finished)
        self._process.errorOccurred.connect(self._handle_error)

        self._process.start(cmd[0], cmd[1:])

    def _handle_output(self):
        raw = self._process.readAllStandardOutput().data()
        text = bytes(raw).decode("utf-8", errors="replace").strip()
        for line in text.splitlines():
            if line:
                self.output_box.addItem(line)
                self.output_box.scrollToBottom()

    def _handle_finished(self, exit_code, exit_status):
        if exit_code == 0:
            self.status_label.setText("Finished.")
            self.refresh_list()
        else:
            self.status_label.setText(f"Error (exit code {exit_code}).")

    def _handle_error(self, error):
        errors = {
            QProcess.ProcessError.FailedToStart: "Process could not start (pkexec installed?)",
            QProcess.ProcessError.Crashed: "Process crashed.",
            QProcess.ProcessError.Timedout: "Timeout.",
        }
        msg = errors.get(error, "Error.")
        self.status_label.setText(msg)

    def refresh_list(self):
        self.list_programs.clear()
        self.list_programs.addItems(self.get_updates())


class EditKeybindingDialog(BaseDialog):
    BIND_TYPES = ["bind", "bindel", "bindl", "bindm", "binde", "bindr"]

    def __init__(self, bind_string: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Keybinding" if bind_string else "Add Keybinding")
        self.original = bind_string
        self._build_ui(bind_string)
        self.resize(800, 300)

    def _build_ui(self, bind_string: str):
        layout = QVBoxLayout(self)

        if bind_string:
            parts = [p.strip() for p in bind_string.split("=", 1)]
            bind_type = parts[0].strip()
            rest = parts[1] if len(parts) > 1 else ""
            tokens = [t.strip() for t in rest.split(",")]
        else:
            bind_type = "bind"
            tokens = []

        self._fields = {}

        type_row = QHBoxLayout()
        type_row.addWidget(QLabel("Typ:"))
        self._type_combo = QComboBox()
        self._type_combo.addItems(self.BIND_TYPES)
        self._type_combo.setCurrentText(
            bind_type if bind_type in self.BIND_TYPES else "bind"
        )
        type_row.addWidget(self._type_combo)
        layout.addLayout(type_row)

        field_defs = [
            ("Modifier", tokens[0] if len(tokens) > 0 else ""),
            ("Key", tokens[1] if len(tokens) > 1 else ""),
            ("Action", tokens[2] if len(tokens) > 2 else ""),
            ("Parameter", ", ".join(tokens[3:]) if len(tokens) > 3 else ""),
        ]

        for label_text, default in field_defs:
            row = QHBoxLayout()
            row.addWidget(QLabel(f"{label_text}:"))
            edit = QLineEdit(default)
            edit.setPlaceholderText(label_text)
            row.addWidget(edit)
            self._fields[label_text] = edit
            layout.addLayout(row)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_result(self) -> str:
        bind_type = self._type_combo.currentText()
        mod = self._fields["Modifier"].text().strip()
        key = self._fields["Key"].text().strip()
        action = self._fields["Action"].text().strip()
        params = self._fields["Parameter"].text().strip()

        parts = [mod, key, action]
        if params:
            parts.append(params)
        return f"{bind_type} = {', '.join(parts)}"
