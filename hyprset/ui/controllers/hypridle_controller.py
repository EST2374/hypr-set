from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ...core.hypridle import (
    add_listener,
    get_all_listeners,
    get_listeners_by_timeout,
    get_listeners_timeout,
    update_hypridle,
)
from ..dialogs import EditHypridle, InstallHyprStuff

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton

    class _Hyprsunset_Widgets(Protocol):
        hypridle_listWidget: QListWidget
        hypridle_add_button: QPushButton
        hypridle_edit_button: QPushButton
        hypridle_install_button: QPushButton
        hypridle_remove_button: QPushButton

    _Base = _Hyprsunset_Widgets
else:
    _Base = object

# TODO
# Remove button
# General block
# refresh th hyrpdile bg prcess


class HypridleControllerMixin(_Base):
    def _setup_hypridle_tab(self):
        profile_times = get_listeners_timeout(get_all_listeners())
        self.hypridle_listWidget.addItems(profile_times)
        self.hypridle_listWidget.itemDoubleClicked.connect(self._edit_hypridle)
        self.hypridle_edit_button.clicked.connect(
            lambda: self._edit_hypridle(self.hypridle_listWidget.currentItem())
        )
        self.hypridle_install_button.clicked.connect(self._install_hypridle)
        self.hypridle_add_button.clicked.connect(self._add_hyprdile_listeners)

    def _install_hypridle(self):
        dialog = InstallHyprStuff(parent=self, pkg="hypridle")
        dialog.center_on_parent()
        dialog.exec()

    def _add_hyprdile_listeners(self):
        dialog = EditHypridle(parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            add_listener(new_block)
            self.hypridle_listWidget.clear()
            self.hypridle_listWidget.addItems(
                get_listeners_timeout(get_all_listeners())
            )

    def _edit_hypridle(self, item: QListWidgetItem):
        name = item.text()
        old_block = get_listeners_by_timeout(name)
        if old_block is None:
            return

        dialog = EditHypridle(listener_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_hypridle(old_block, new_block)
            self.hypridle_listWidget.clear()
            self.hypridle_listWidget.addItems(
                get_listeners_timeout(get_all_listeners())
            )
