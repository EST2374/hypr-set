from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QColorDialog

import hyprset.config as app_config

from ...core.look import (
    BOOL_DEFAULTS,
    DEFAULTS,
    better_cur_enabled,
    better_cur_status,
    better_cur_value,
    change_angle_value,
    change_bool_lua,
    change_layout,
    get_angle,
    get_cur_layout,
    read_bool_lua,
    reset_to_defaults,
    write_setting_lua,
)
from ..constants import INPUT_SETTINGS, LOOK_SETTINGS

if TYPE_CHECKING:
    from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox, QPushButton

    class _LookWidgets(Protocol):
        set_color_1_button: QPushButton
        set_color_2_button: QPushButton
        shadow_color_button: QPushButton
        layout_comboBox: QComboBox
        resize_checkbox: QCheckBox
        allow_tearing_checkBox: QCheckBox
        blur_enable_checkBox: QCheckBox
        shadow_enable_checkbox: QCheckBox
        set_default_look_button: QPushButton
        # SpinBoxen aus LOOK_SETTINGS
        gaps_in_spinBox: QDoubleSpinBox
        gaps_out_spinBox: QDoubleSpinBox

    _Base = _LookWidgets
else:
    _Base = object


class LookControllerMixin(_Base):
    def _setup_look_tab(self):
        # SpinBoxen
        for setting, widget_attr in LOOK_SETTINGS.items():
            widget = getattr(self, widget_attr)
            if setting == "angle":
                widget.setValue(get_angle())
                widget.valueChanged.connect(lambda val: change_angle_value(val))
                continue
            widget.setValue(better_cur_value(setting))
            widget.valueChanged.connect(
                lambda val, s=setting: write_setting_lua(s, val)
            )

        # Color Buttons
        self.set_color_1_button.clicked.connect(self.set_color_1)
        self.set_color_2_button.clicked.connect(self.set_color_2)
        self.shadow_color_button.clicked.connect(self.set_shadow_color)

        # Checkbox
        self._setup_look_checkboxes()

        # Layout ComboBox
        layouts = ["Dwindle", "Master", "Scrolling", "Monocle"]
        self.layout_comboBox.addItems(layouts)
        self.layout_comboBox.setCurrentText(get_cur_layout())
        self.layout_comboBox.currentTextChanged.connect(change_layout)

        # Reset-Button
        self.set_default_look_button.clicked.connect(self._reset_look_to_defaults)

    def _setup_look_checkboxes(self):
        checks = {
            "resize_on_border": self.resize_checkbox,
            "allow_tearing": self.allow_tearing_checkBox,
        }
        enabled = {
            "blur": self.blur_enable_checkBox,
            "shadow": self.shadow_enable_checkbox,
        }
        bool_keys = {
            self.resize_checkbox: "resize",
            self.allow_tearing_checkBox: "tearing",
            self.blur_enable_checkBox: "blur_enable",
            self.shadow_enable_checkbox: "shadow_enable",
        }

        for lua_key, widget in checks.items():
            if better_cur_status(lua_key) == "true":
                widget.setCheckState(Qt.CheckState.Checked)

        for lua_key, widget in enabled.items():
            if better_cur_enabled(lua_key):
                widget.setCheckState(Qt.CheckState.Checked)

        for widget, bool_key in bool_keys.items():
            widget.checkStateChanged.connect(lambda _, k=bool_key: change_bool_lua(k))

    def _reload_look(self):
        for setting, widget_attr in LOOK_SETTINGS.items():
            widget = getattr(self, widget_attr)
            widget.blockSignals(True)
            widget.setValue(
                get_angle() if setting == "angle" else better_cur_value(setting)
            )
            widget.blockSignals(False)

        for lua_key, widget_attr in INPUT_SETTINGS.items():
            widget = getattr(self, widget_attr)
            widget.blockSignals(True)
            state = (
                Qt.CheckState.Checked
                if read_bool_lua(lua_key)
                else Qt.CheckState.Unchecked
            )
            widget.setCheckState(state)
            widget.blockSignals(False)

    def _reset_look_to_defaults(self):
        reset_to_defaults()

        for setting, widget_attr in LOOK_SETTINGS.items():
            if setting not in DEFAULTS:
                continue
            widget = getattr(self, widget_attr)
            widget.blockSignals(True)
            widget.setValue(DEFAULTS[setting])
            widget.blockSignals(False)

        for setting, widget_attr in INPUT_SETTINGS.items():
            widget = getattr(self, widget_attr)
            widget.blockSignals(True)
            state = (
                Qt.CheckState.Checked
                if BOOL_DEFAULTS.get(setting) == "true"
                else Qt.CheckState.Unchecked
            )
            widget.setCheckState(state)
            widget.blockSignals(False)

    def set_color_1(self):
        self._pick_and_save_color(index=1)

    def set_color_2(self):
        self._pick_and_save_color(index=2)

    def set_shadow_color(self):
        self._pick_and_save_color(index=3)

    def _pick_and_save_color(self, index):
        color = QColorDialog.getColor(
            QColor("white"),
            self,
            f"Border Color {index}",
            QColorDialog.ColorDialogOption.ShowAlphaChannel,
        )
        if not color.isValid():
            return

        new_hex = (
            f"{color.red():02x}{color.green():02x}{color.blue():02x}{color.alpha():02x}"
        )
        new_rgba = f"rgba({new_hex})"

        self._update_active_border(new_rgba, index=index)

    def _update_active_border(self, new_rgba_string, index):
        try:
            with open(app_config.CONFIG_FILE_LUA, "r") as f:
                content = f.read()
        except FileNotFoundError:
            return

        if index == 1:
            content = re.sub(
                r'(active_border\s*=\s*\{[^}]*colors\s*=\s*\{[^"]*")([^"]+)(")',
                rf"\g<1>{new_rgba_string}\g<3>",
                content,
                count=1,
                flags=re.DOTALL,
            )
        elif index == 2:
            content = re.sub(
                r'(active_border\s*=\s*\{[^}]*colors\s*=\s*\{[^"]*"[^"]*",\s*")([^"]+)(")',
                rf"\g<1>{new_rgba_string}\g<3>",
                content,
                count=1,
                flags=re.DOTALL,
            )
        elif index == 3:
            match = re.match(r"rgba\(([0-9a-fA-F]{8})\)", new_rgba_string)
            if match:
                rrggbbaa = match.group(1)
                lua_hex = f"0x{rrggbbaa[6:8]}{rrggbbaa[0:6]}"
                content = re.sub(
                    r"(shadow\s*=\s*\{[^}]*color\s*=\s*)([^\s,\n]+)",
                    rf"\g<1>{lua_hex}",
                    content,
                    count=1,
                    flags=re.DOTALL,
                )

        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            f.write(content)
