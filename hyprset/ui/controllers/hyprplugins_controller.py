from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ..dialogs.hyprplugin import HyprPluginManager

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton

    class _Hyprplugin_Widgets(Protocol):
        plugins_list: QListWidget
        enable_button: QPushButton
        disable_button: QPushButton

    _Base = _Hyprplugin_Widgets
else:
    _Base = object


# Better overview and repo install


class HyprpluginControllerMixin(_Base):
    def _setup_hyprplugin_tab(self):
        self.enable_button.clicked.connect(
            lambda: self._enable_plugins(self.plugins_list.currentItem())
        )
        self.disable_button.clicked.connect(
            lambda: self._disable_plugins(self.plugins_list.currentItem())
        )

    def _enable_plugins(self, item: QListWidgetItem):
        plugin = str(item.text()).lower()
        dialog = HyprPluginManager(parent=self, plugin=f"{plugin}", mode="enable")
        dialog.center_on_parent()
        dialog.exec()

    def _disable_plugins(self, item: QListWidgetItem):
        plugin = str(item.text()).lower()
        dialog = HyprPluginManager(parent=self, plugin=f"{plugin}", mode="disable")
        dialog.center_on_parent()
        dialog.exec()
