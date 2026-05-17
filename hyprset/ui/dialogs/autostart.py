import glob
import os
import re

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
)

from hyprset.core.autostart import add_autostart

from .base import BaseDialog


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
