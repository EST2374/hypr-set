import glob
import os
import re

from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QColorDialog,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
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
