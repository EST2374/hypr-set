from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from ...core.window_rule import (
    add_window_rule,
    delete_window_rule,
    get_all_window_rules,
    get_window_rule_by_name,
    get_window_rule_names,
    update_window_rule,
)
from ..dialogs import EditWindowRule

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget, QListWidgetItem, QPushButton

    class _WindowRuleWidgets(Protocol):
        add_window_rule_button: QPushButton
        delete_window_rule_button: QPushButton
        edit_window_rule_button: QPushButton
        window_rule_listWidget: QListWidget

    _Base = _WindowRuleWidgets
else:
    _Base = object


class WindowRuleControllerMixin(_Base):
    def _setup_windowrule_tab(self):
        window_rule_names = get_window_rule_names(get_all_window_rules())
        self.window_rule_listWidget.addItems(window_rule_names)
        self.edit_window_rule_button.clicked.connect(
            lambda: self._edit_window_rule(self.window_rule_listWidget.currentItem())
        )
        self.window_rule_listWidget.itemDoubleClicked.connect(self._edit_window_rule)
        self.add_window_rule_button.clicked.connect(self._add_window_rule)
        self.delete_window_rule_button.clicked.connect(self._delete_window_rule)

    def _add_window_rule(self):
        dialog = EditWindowRule(parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            add_window_rule(dialog.get_result())
            self._refresh_window_rules()

    def _refresh_window_rules(self):
        self.window_rule_listWidget.clear()
        self.window_rule_listWidget.addItems(
            get_window_rule_names(get_all_window_rules())
        )

    def _edit_window_rule(self, item: QListWidgetItem):
        name = item.text()
        old_block = get_window_rule_by_name(name)
        if old_block is None:
            return

        dialog = EditWindowRule(rule_block=old_block, parent=self)
        dialog.center_on_parent()
        if dialog.exec():
            new_block = dialog.get_result()
            update_window_rule(old_block, new_block)

    def _delete_window_rule(self):
        item = self.window_rule_listWidget.currentItem()
        if item is None:
            return
        block = get_window_rule_by_name(item.text())
        if block:
            delete_window_rule(block)
            self._refresh_window_rules()
