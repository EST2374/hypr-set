from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ...core.autostart import (
    create_autostart_block,
    del_autostart,
    get_current_autostarts,
    is_autostart_commented_out,
    is_autostart_initialized,
    uncomment_autostart_block,
)
from ...core.environments import del_env, get_current_env
from ..dialogs import AddEnvDialog, AddProgramDialog, AddScriptDialog, EditLineDialog
from ..notification import hyprland_notification

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QPushButton

    class _Autostart_and_Environment_Widgets(Protocol):
        current_autostart: QListWidget
        del_autostart_button: QPushButton
        add_program_button: QPushButton
        add_script_button: QPushButton
        current_env: QListWidget
        add_env_button: QPushButton
        del_env_button: QPushButton

    _Base = _Autostart_and_Environment_Widgets
else:
    _Base = object


class AutostartControllerMixin(_Base):
    def _setup_autostart_tab(self):
        # Autostart Settings
        self._ensure_autostart_initialized()
        self.current_autostart.addItems(get_current_autostarts())
        self.del_autostart_button.clicked.connect(self.del_selected_autostart)
        self.add_program_button.clicked.connect(self.add_new_autostart)
        self.add_script_button.clicked.connect(self.add_new_script)

        # Environment Settings
        self.current_env.addItems(get_current_env())
        self.add_env_button.clicked.connect(self.add_new_env)
        self.del_env_button.clicked.connect(self.del_selected_env)
        self.current_env.itemDoubleClicked.connect(self.edit_env)

    def _ensure_autostart_initialized(self):
        if is_autostart_initialized():
            return
        if is_autostart_commented_out():
            uncomment_autostart_block()
        else:
            create_autostart_block()

    def add_new_autostart(self):
        dialog = AddProgramDialog(self, on_added=self.current_autostart.addItem)
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Autostart Program added")

    def add_new_script(self):
        dialog = AddScriptDialog(self, on_added=self.current_autostart.addItem)
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Autostart Script added")

    def del_selected_autostart(self):
        current_row = self.current_autostart.currentRow()
        if current_row == -1:
            return
        item = self.current_autostart.currentItem()
        if del_autostart(item.text()):
            self.current_autostart.takeItem(current_row)
        hyprland_notification("Autostart removed")

    def add_new_env(self):
        dialog = AddEnvDialog(self, on_added=self.current_env.addItem)
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Environment added")

    # Environemnt
    def del_selected_env(self):
        current_row = self.current_env.currentRow()
        if current_row == -1:
            return
        item = self.current_env.currentItem()
        if del_env(item.text()):
            self.current_env.takeItem(current_row)
        hyprland_notification("Environment removed")

    def edit_env(self):
        curren_item = self.current_env.currentItem()
        dialog = EditLineDialog(
            self,
            on_added=curren_item.text(),
            widget=curren_item,
        )
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Environment edited")

    def _reload_autostart(self):
        self.current_autostart.clear()
        self.current_autostart.addItems(get_current_autostarts())
        self.current_env.clear()
        self.current_env.addItems(get_current_env())
