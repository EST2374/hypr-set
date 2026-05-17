from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from hyprset.core.hyprsunset import (
    add_profile,
    get_all_profiles,
    get_profile_by_time,
    get_profiles_time,
    update_hyprsunset,
)

from ..dialogs import EditHyprsunset, InstallHyprStuff

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton

    class _Hyprsunset_Widgets(Protocol):
        hyprsunset_listWidget: QListWidget
        edit_hyprsunset_button: QPushButton
        install_hyprsunset_button: QPushButton
        add_hyprsunset_button: QPushButton

    _Base = _Hyprsunset_Widgets
else:
    _Base = object


# TODO
# remove button
# refresh th hyrpsunset bg prcess


class HyprsunsetControllerMixin(_Base):
    def _setup_hyprsunset_tab(self):
        profile_times = get_profiles_time(get_all_profiles())
        self.hyprsunset_listWidget.addItems(profile_times)
        self.hyprsunset_listWidget.itemDoubleClicked.connect(self._edit_hyprsunset)
        self.edit_hyprsunset_button.clicked.connect(
            lambda: self._edit_hyprsunset(self.hyprsunset_listWidget.currentItem())
        )
        self.install_hyprsunset_button.clicked.connect(self._install_hyprsunset)
        self.add_hyprsunset_button.clicked.connect(self._add_hyprsunset_profile)

    def _install_hyprsunset(self):
        dialog = InstallHyprStuff(parent=self, pkg="hyprsunset")
        dialog.center_on_parent()
        dialog.exec()

    def _add_hyprsunset_profile(self):
        dialog = EditHyprsunset(parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            add_profile(new_block)
            self.hyprsunset_listWidget.clear()
            self.hyprsunset_listWidget.addItems(get_profiles_time(get_all_profiles()))

    def _edit_hyprsunset(self, item: QListWidgetItem):
        name = item.text()
        old_block = get_profile_by_time(name)
        if old_block is None:
            return

        dialog = EditHyprsunset(profile_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_hyprsunset(old_block, new_block)
            self.hyprsunset_listWidget.clear()
            self.hyprsunset_listWidget.addItems(get_profiles_time(get_all_profiles()))
