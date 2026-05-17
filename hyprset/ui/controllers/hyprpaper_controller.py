from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ...core.hyprpaper import (
    get_all_wallpapers,
    get_wp_by_name,
    get_wp_names,
    update_hyprpaper,
)
from ..dialogs import EditHyprpaper, InstallHyprStuff

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton

    class _Hyprpaper_Widgets(Protocol):
        hyprpaper_listWidget: QListWidget
        edit_wp_button: QPushButton
        hyprpaper_install_button: QPushButton

    _Base = _Hyprpaper_Widgets
else:
    _Base = object


# TODO
# Fix naming in hyprpaper_listWidget and update


class HyprpaperControllerMixin(_Base):
    def _setup_hyprpaper_tab(self):
        hyprpaper_names = get_wp_names(get_all_wallpapers())
        self.hyprpaper_listWidget.addItems(hyprpaper_names)
        self.hyprpaper_listWidget.itemDoubleClicked.connect(self._edit_hyprpaper)
        self.edit_wp_button.clicked.connect(
            lambda: self._edit_hyprpaper(self.hyprpaper_listWidget.currentItem())
        )
        self.hyprpaper_install_button.clicked.connect(self._install_hyprpaper)

    def _install_hyprpaper(self):
        dialog = InstallHyprStuff(parent=self, pkg="hyprpaper")
        dialog.center_on_parent()
        dialog.exec()

    def _edit_hyprpaper(self, item: QListWidgetItem):
        name = item.text()
        old_block = get_wp_by_name(name)
        if old_block is None:
            return

        dialog = EditHyprpaper(wp_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_hyprpaper(old_block, new_block)
            self.hyprpaper_listWidget.clear()
            self.hyprpaper_listWidget.addItems(get_wp_names(get_all_wallpapers()))
