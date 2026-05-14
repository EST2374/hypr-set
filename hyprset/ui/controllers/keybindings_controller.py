from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from PySide6.QtWidgets import (
    QMessageBox,
)

from hyprset.core.keybindings import (
    add_keybinding,
    del_keybinding,
    get_general_keybindings,
    get_movement_keybindings,
    get_multimedia_keybindings,
    get_workspace_keybindings,
    reset_to_defaults_keybindings,
    update_keybinding,
)

from ..dialogs import EditKeybindingDialog

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QListWidget,
        QPushButton,
    )

    class _KeybindingsWidgets(Protocol):
        general_list: QListWidget
        movement_list: QListWidget
        workspaces_list: QListWidget
        multimedia_list: QListWidget
        general_add_button: QPushButton
        movement_add_button: QPushButton
        workspace_add_button: QPushButton
        multimedia_add_button: QPushButton
        delete_keybind_button: QPushButton
        delete_movement_button: QPushButton
        delete_workspace_button: QPushButton
        delete_multimedia_button: QPushButton
        set_default_general_keybind_button: QPushButton
        set_default_movement_button: QPushButton
        set_default_workspace_button: QPushButton
        set_default_multimedia_button: QPushButton

    _Base = _KeybindingsWidgets
else:
    _Base = object


class KeybindControllerMixin(_Base):
    def _setup_keybindings_tab(self):
        # Keybindings
        # TODO
        # Fix where Item gets into what list (Maybe make only general addable???)
        self.general_list.addItems(get_general_keybindings())
        self.movement_list.addItems(get_movement_keybindings())
        self.workspaces_list.addItems(get_workspace_keybindings())
        self.multimedia_list.addItems(get_multimedia_keybindings())

        for list_widget in (
            self.general_list,
            self.movement_list,
            self.workspaces_list,
            self.multimedia_list,
        ):
            list_widget.itemDoubleClicked.connect(self._edit_keybinding)

        KEYBIND_ADD_MAP = {
            self.general_add_button: self.general_list,
            self.movement_add_button: self.movement_list,
            self.workspace_add_button: self.workspaces_list,
            self.multimedia_add_button: self.multimedia_list,
        }

        KEYBIND_DELETE_MAP = {
            self.delete_keybind_button: self.general_list,
            self.delete_movement_button: self.movement_list,
            self.delete_workspace_button: self.workspaces_list,
            self.delete_multimedia_button: self.multimedia_list,
        }

        for button, list_widget in KEYBIND_DELETE_MAP.items():
            button.clicked.connect(
                lambda checked=False, lw=list_widget: self.del_selected_keybinding(lw)
            )

        for button, list_widget in KEYBIND_ADD_MAP.items():
            button.clicked.connect(
                lambda checked=False, lw=list_widget: self.add_keybinding()
            )

        for set_default_keybind_button in (
            self.set_default_general_keybind_button,
            self.set_default_movement_button,
            self.set_default_workspace_button,
            self.set_default_multimedia_button,
        ):
            set_default_keybind_button.clicked.connect(self.set_default_keybinds_config)

    def _edit_keybinding(self, item):
        dialog = EditKeybindingDialog(item.text(), parent=self)
        if dialog.exec() == EditKeybindingDialog.DialogCode.Accepted:
            new_line = dialog.get_result()
            if update_keybinding(item.text(), new_line):
                item.setText(new_line)

    def add_keybinding(self):
        dialog = EditKeybindingDialog(parent=self)
        dialog.center_on_parent()
        if dialog.exec() == EditKeybindingDialog.DialogCode.Accepted:
            new_line = dialog.get_result()
            if add_keybinding(new_line):
                self._reload_keybinding_lists()

    def set_default_keybinds_config(self):
        reply = QMessageBox.question(
            self,
            "Reset to Defaults",
            "Are you sure you want to reset all keybindings to default?\nThis cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            if reset_to_defaults_keybindings():
                self._reload_keybinding_lists()

    def del_selected_keybinding(self, list_widget):
        current_row = list_widget.currentRow()
        if current_row == -1:
            return
        item = list_widget.currentItem()
        if del_keybinding(item.text()):
            list_widget.takeItem(current_row)

    def _reload_keybinding_lists(self):
        self.general_list.clear()
        self.movement_list.clear()
        self.workspaces_list.clear()
        self.multimedia_list.clear()
        self.general_list.addItems(get_general_keybindings())
        self.movement_list.addItems(get_movement_keybindings())
        self.workspaces_list.addItems(get_workspace_keybindings())
        self.multimedia_list.addItems(get_multimedia_keybindings())

    def _reload_keybindings(self):
        self._reload_keybinding_lists()
