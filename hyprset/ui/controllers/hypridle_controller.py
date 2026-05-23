from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from ...core.hypridle import (
    add_listener,
    extract_listener_timeout,
    format_listener_label,
    get_all_listeners,
    get_general_block,
    get_listeners_by_timeout,
    remove_listener,
    restart_hypridle,
    update_general_block,
    update_hypridle,
)
from ..dialogs import EditHypridle, EditHypridleGeneral, InstallHyprStuff
from ..notification import hyprland_notification

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QPushButton

    class _Hyprsunset_Widgets(Protocol):
        hypridle_listWidget: QListWidget
        hypridle_add_button: QPushButton
        hypridle_edit_button: QPushButton
        hypridle_install_button: QPushButton
        hypridle_remove_button: QPushButton

    _Base = _Hyprsunset_Widgets
else:
    _Base = object

# Fix remove button (Claude made it KAPUTT!!!!)

_GENERAL_SENTINEL = "__general__"
_KIND_ROLE = Qt.ItemDataRole.UserRole
_TIMEOUT_ROLE = Qt.ItemDataRole.UserRole + 1


class HypridleControllerMixin(_Base):
    def _setup_hypridle_tab(self):
        self._refresh_listener_list()
        self.hypridle_listWidget.itemDoubleClicked.connect(self._edit_hypridle)
        self.hypridle_edit_button.clicked.connect(
            lambda: self._edit_hypridle(self.hypridle_listWidget.currentItem())
        )
        self.hypridle_install_button.clicked.connect(self._install_hypridle)
        self.hypridle_add_button.clicked.connect(self._add_hyprdile_listeners)
        self.hypridle_remove_button.clicked.connect(self._remove_hypridle_listener)

    def _install_hypridle(self):
        dialog = InstallHyprStuff(parent=self, pkg="hypridle")
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Hypridle installed")

    def _refresh_listener_list(self):
        self.hypridle_listWidget.clear()

        if get_general_block() is not None:
            general_item = QListWidgetItem("General Settings")
            general_item.setData(_KIND_ROLE, _GENERAL_SENTINEL)
            self.hypridle_listWidget.addItem(general_item)

        for idx, block in enumerate(get_all_listeners(), start=1):
            item = QListWidgetItem(format_listener_label(block, idx))
            item.setData(_KIND_ROLE, "listener")
            timeout = extract_listener_timeout(block)
            if timeout:
                item.setData(_TIMEOUT_ROLE, timeout)
            self.hypridle_listWidget.addItem(item)

    def _lookup_block(self, item: QListWidgetItem | None) -> str | None:
        if item is None or item.data(_KIND_ROLE) != "listener":
            return None
        timeout = item.data(_TIMEOUT_ROLE)
        if not timeout:
            return None
        return get_listeners_by_timeout(timeout)

    def _add_hyprdile_listeners(self):
        dialog = EditHypridle(parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            add_listener(new_block)
            hyprland_notification("Listener added")
            self._refresh_listener_list()
            restart_hypridle()

    def _edit_hypridle(self, item: QListWidgetItem):
        if item is None:
            return
        if item.data(_KIND_ROLE) == _GENERAL_SENTINEL:
            self._edit_general_block()
            return

        old_block = self._lookup_block(item)
        if old_block is None:
            return

        dialog = EditHypridle(listener_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_hypridle(old_block, new_block)
            self._refresh_listener_list()
            restart_hypridle()

        hyprland_notification("Listener edited")

    def _edit_general_block(self):
        current = get_general_block() or ""
        dialog = EditHypridleGeneral(general_block=current, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_general_block(new_block)
            self._refresh_listener_list()
            restart_hypridle()

    def _remove_hypridle_listener(self):
        old_block = self._lookup_block(self.hypridle_listWidget.currentItem())
        if old_block is None:
            return
        if remove_listener(old_block):
            self._refresh_listener_list()
            restart_hypridle()
        hyprland_notification("Listener removed")
