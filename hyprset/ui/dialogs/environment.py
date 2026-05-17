from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

import hyprset.config as app_config
from hyprset.core.environments import add_env

from .base import BaseDialog


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


class EditLineDialog(BaseDialog):
    def __init__(self, parent=None, on_added=None, widget=None):
        self._on_added = on_added
        self.item = widget
        super().__init__(parent)
        self.setWindowTitle("Edit Environment")
        self.resize(800, 300)

        env_label = QLabel("Edit Environment: ")
        self.env_edit_line = QLineEdit()
        self.env_edit_line.setText(self._on_added)
        button_apply = QPushButton("Apply")
        button_apply.clicked.connect(self.apply_new_env)

        layout_h = QHBoxLayout()
        layout_h.addWidget(env_label)
        layout_h.addWidget(self.env_edit_line)

        layout = QVBoxLayout()
        layout.addLayout(layout_h)
        layout.addWidget(button_apply)
        self.setLayout(layout)

    def apply_new_env(self):
        new_text = self.env_edit_line.text()
        old_text = self._on_added

        if self.item is not None and old_text is not None:
            self.item.setText(new_text)
            self._update_config(old_text, new_text)
            self.accept()
        else:
            pass

    def _update_config(self, old_entry: str, new_entry: str):
        old_line = f"hl.env({old_entry})\n"
        new_line = f"hl.env({new_entry})\n"

        try:
            with open(app_config.CONFIG_FILE_LUA, "r") as f:
                content = f.read()
            content = content.replace(old_line, new_line, 1)
            with open(app_config.CONFIG_FILE_LUA, "w") as f:
                f.write(content)
        except OSError as e:
            print(f"Error writing config: {e}")
