from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import Qt

from ...core.input import (
    follow_mouse_change,
    get_cur_follow_mouse,
    get_cur_item,
    get_kb_variants,
    write_setting_input,
)
from ...core.look import change_bool_lua, read_bool_lua
from ..constants import INPUT_SETTINGS

if TYPE_CHECKING:
    from PySide6.QtWidgets import QCheckBox, QComboBox, QDoubleSpinBox

    class _InputWidgets(Protocol):
        kb_layout_comboBox: QComboBox
        kb_variant_comboBox: QComboBox
        follow_mouse_comboBox: QComboBox
        mouse_sens_doubleSpinBox: QDoubleSpinBox
        touchpad_nat_scroll_checkbox: QCheckBox
        mouse_natural_scroll_checkBox: QCheckBox

    _Base = _InputWidgets
else:
    _Base = object


class InputControllerMixin(_Base):
    def _setup_input_tab(self):
        # Input
        for setting_2, widget_attr_2 in INPUT_SETTINGS.items():
            widget_2 = getattr(self, widget_attr_2)
            widget_2.addItem(get_cur_item(setting_2))
            widget_2.currentTextChanged.connect(
                lambda val, s=setting_2: write_setting_input(s, val)
            )

        kb_layouts = ["us", "gb", "de", "fr", "es", "it", "br"]
        follow_mouse_options = ["Manual", "Automatic", "Semi-Automatic", "Locked"]
        self.kb_layout_comboBox.addItems(kb_layouts)
        self.kb_variant_comboBox.addItem("")
        self.kb_variant_comboBox.addItems(get_kb_variants())
        self.kb_layout_comboBox.currentTextChanged.connect(self.update_variant)
        self.follow_mouse_comboBox.addItems(follow_mouse_options)
        self.follow_mouse_comboBox.setCurrentText(get_cur_follow_mouse())
        self.follow_mouse_comboBox.currentTextChanged.connect(follow_mouse_change)
        self.mouse_sens_doubleSpinBox.setRange(-1.0, 1.0)

        if read_bool_lua("global_natural_scroll"):
            self.mouse_natural_scroll_checkBox.setCheckState(Qt.CheckState.Checked)
        self.mouse_natural_scroll_checkBox.checkStateChanged.connect(
            lambda: change_bool_lua("global_natural_scroll")
        )
        if read_bool_lua("natural_scroll_touchpad"):
            self.touchpad_nat_scroll_checkbox.setCheckState(Qt.CheckState.Checked)
        self.touchpad_nat_scroll_checkbox.checkStateChanged.connect(
            lambda: change_bool_lua("natural_scroll_touchpad")
        )

    def update_variant(self):
        variants = get_kb_variants()
        self.kb_variant_comboBox.clear()
        self.kb_variant_comboBox.addItem("")
        self.kb_variant_comboBox.addItems(variants)

    def _reload_input(self):
        self.follow_mouse_comboBox.setCurrentText(get_cur_follow_mouse())
