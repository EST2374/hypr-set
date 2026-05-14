from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ...core.monitor import (
    apply_monitor_settings,
    get_cur_rotation,
    get_monitor_names,
    get_monitor_resolution,
    set_default_monitors_button,
)

ROTATION_OPTIONS = [
    "Normal",
    "90°",
    "180°",
    "270°",
    "flipped",
    "flipped + 90°",
    "flipped + 180°",
    "flipped + 270°",
]

if TYPE_CHECKING:
    from PySide6.QtWidgets import QComboBox, QPushButton

    class _MonitorWidgets(Protocol):
        monitors_box: QComboBox
        mirror_comboBox: QComboBox
        resolution_box: QComboBox
        rotation_comboBox: QComboBox
        position_box: QComboBox
        scale_box: QComboBox
        apply_button: QPushButton
        set_default_monitor_button: QPushButton

    _Base = _MonitorWidgets
else:
    _Base = object


class MonitorControllerMixin(_Base):
    def _setup_monitor_tab(self):
        monitor_names = get_monitor_names()

        self.monitors_box.addItems(monitor_names)
        self.mirror_comboBox.addItems(monitor_names)
        self.resolution_box.addItems(
            get_monitor_resolution(self.monitors_box.currentIndex())
        )
        self.rotation_comboBox.addItems(ROTATION_OPTIONS)
        self.position_box.addItem("auto")
        self.scale_box.addItems(["1.0", "2.0"])

        # Load current rotation
        self.rotation_comboBox.setCurrentText(
            get_cur_rotation(self.monitors_box.currentText())
        )

        self.monitors_box.currentIndexChanged.connect(self._on_monitor_changed)
        self.apply_button.clicked.connect(self._apply_monitor_settings)
        self.set_default_monitor_button.clicked.connect(set_default_monitors_button)

    def _on_monitor_changed(self, index):
        self.resolution_box.clear()
        self.resolution_box.addItems(get_monitor_resolution(index))
        self.rotation_comboBox.setCurrentText(
            get_cur_rotation(self.monitors_box.currentText())
        )

    def _apply_monitor_settings(self):
        apply_monitor_settings(
            self.monitors_box.currentText(),
            self.resolution_box.currentText(),
            self.position_box.currentText(),
            self.scale_box.currentText(),
            self.mirror_comboBox.currentText(),
            self.rotation_comboBox.currentText(),
        )
