from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from hyprset.core.hyprsunset import (
    add_profile,
    extract_profile_time,
    format_profile_label,
    get_all_profiles,
    get_profile_by_time,
    remove_profile,
    restart_hyprsunset,
    update_hyprsunset,
)

from ..dialogs import EditHyprsunset, InstallHyprStuff
from ..notification import hyprland_notification

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QPushButton

    class _Hyprsunset_Widgets(Protocol):
        hyprsunset_listWidget: QListWidget
        edit_hyprsunset_button: QPushButton
        install_hyprsunset_button: QPushButton
        add_hyprsunset_button: QPushButton
        remove_hyprsunset_button: QPushButton

    _Base = _Hyprsunset_Widgets
else:
    _Base = object

_TIME_ROLE = Qt.ItemDataRole.UserRole


class HyprsunsetControllerMixin(_Base):
    def _setup_hyprsunset_tab(self):
        self._refresh_profile_list()
        self.hyprsunset_listWidget.itemDoubleClicked.connect(self._edit_hyprsunset)
        self.edit_hyprsunset_button.clicked.connect(
            lambda: self._edit_hyprsunset(self.hyprsunset_listWidget.currentItem())
        )
        self.install_hyprsunset_button.clicked.connect(self._install_hyprsunset)
        self.add_hyprsunset_button.clicked.connect(self._add_hyprsunset_profile)
        self.remove_hyprsunset_button.clicked.connect(self._remove_hyprsunset_profile)

    def _install_hyprsunset(self):
        dialog = InstallHyprStuff(parent=self, pkg="hyprsunset")
        dialog.center_on_parent()
        dialog.exec()
        hyprland_notification("Hyprsunset installed")

    def _refresh_profile_list(self):
        self.hyprsunset_listWidget.clear()
        for idx, block in enumerate(get_all_profiles(), start=1):
            item = QListWidgetItem(format_profile_label(block, idx))
            time_v = extract_profile_time(block)
            if time_v:
                item.setData(_TIME_ROLE, time_v)
            self.hyprsunset_listWidget.addItem(item)

    def _lookup_block(self, item: QListWidgetItem | None) -> str | None:
        if item is None:
            return None
        time_v = item.data(_TIME_ROLE)
        if not time_v:
            return None
        return get_profile_by_time(time_v)

    def _add_hyprsunset_profile(self):
        dialog = EditHyprsunset(parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            add_profile(new_block)
            self._refresh_profile_list()
            restart_hyprsunset()

    def _edit_hyprsunset(self, item: QListWidgetItem):
        old_block = self._lookup_block(item)
        if old_block is None:
            return

        dialog = EditHyprsunset(profile_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_hyprsunset(old_block, new_block)
            self._refresh_profile_list()
            restart_hyprsunset()

    def _remove_hyprsunset_profile(self):
        old_block = self._lookup_block(self.hyprsunset_listWidget.currentItem())
        if old_block is None:
            return
        if remove_profile(old_block):
            self._refresh_profile_list()
            restart_hyprsunset()
