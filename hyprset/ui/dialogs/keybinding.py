import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)

from .base import BaseDialog


class EditKeybindingDialog(BaseDialog):
    def __init__(self, bind_string: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Keybinding" if bind_string else "Add Keybinding")
        self.original = bind_string
        self._build_ui(bind_string)
        self.resize(820, 300)

    @staticmethod
    def _parse(bind_string: str) -> tuple[str, str, str]:
        m = re.match(
            r'hl\.bind\((.+?),\s*([\w.]+)\((".*?"|[^)]*)\)\s*\)',
            bind_string.strip(),
        )
        if not m:
            return "", "", ""
        keys = m.group(1).strip()
        action = m.group(2).strip()
        param = m.group(3).strip().strip('"')
        return keys, action, param

    @staticmethod
    def _build_result(keys: str, action: str, param: str) -> str:
        param_lua = f'"{param}"' if param else '""'
        return f'hl.bind({keys}", {action}({param_lua}))'

    def _build_ui(self, bind_string: str):
        keys, action, param = self._parse(bind_string) if bind_string else ("", "", "")

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields = {}

        field_defs = [
            (
                "Keys",
                keys,
                'e.g. mainMod .. " + SPACE"  or  mainMod .. " + CTRL + SPACE"',
            ),
            ("Action", action, "e.g. hl.dsp.exec_cmd"),
            ("Parameter", param, "e.g. walker-menu"),
        ]

        for label_text, default, placeholder in field_defs:
            row = QHBoxLayout()
            lbl = QLabel(f"{label_text}:")
            lbl.setFixedWidth(90)
            lbl.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            row.addWidget(lbl)
            edit = QLineEdit(default)
            edit.setPlaceholderText(placeholder)
            row.addWidget(edit)
            self._fields[label_text] = edit
            layout.addLayout(row)

        self._preview = QLabel()
        self._preview.setStyleSheet(
            "color: palette(mid); font-family: monospace; font-size: 11px;"
        )
        self._preview.setWordWrap(True)
        layout.addWidget(self._preview)

        for field in self._fields.values():
            field.textChanged.connect(self._update_preview)
        self._update_preview()

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _update_preview(self):
        self._preview.setText(f"  ↳  {self.get_result()}")

    def get_result(self) -> str:
        keys = self._fields["Keys"].text().strip()
        action = self._fields["Action"].text().strip()
        param = self._fields["Parameter"].text().strip()
        return self._build_result(keys, action, param)
