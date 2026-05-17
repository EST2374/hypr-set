import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)

from hyprset.core.monitor import get_monitor_names

from .base import BaseDialog


class EditHyprpaper(BaseDialog):
    def __init__(self, wp_block: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Wallpaper")
        self.original = wp_block
        self._build_ui(wp_block)
        self.resize(820, 300)

    @staticmethod
    def _parse(block: str) -> dict[str, str]:
        def find(key: str) -> str:
            m = re.search(rf"{key}\s*=\s*(\S+)", block)
            return m.group(1).strip() if m else ""

        return {
            "monitor": find("monitor"),
            "path": find("path"),
            "fit_mode": find("fit_mode"),
        }

    @staticmethod
    def _build_result(fields: dict[str, str]) -> str:
        lines = ["wallpaper {"]
        if fields["monitor"]:
            lines.append(f"    monitor  = {fields['monitor']}")
        if fields["path"]:
            lines.append(f"    path     = {fields['path']}")
        if fields["fit_mode"]:
            lines.append(f"    fit_mode = {fields['fit_mode']}")
        lines.append("}")
        return "\n".join(lines)

    def _build_ui(self, block: str):
        parsed = (
            self._parse(block) if block else {"monitor": "", "path": "", "fit_mode": ""}
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields = {}

        field_defs = [
            ("Path", parsed["path"], "z.B. ~/wallpaper.jpg"),
            ("Fit Mode", parsed["fit_mode"], "z.B. cover"),
        ]

        monitor_row = QHBoxLayout()
        lbl = QLabel("Monitor:")
        lbl.setFixedWidth(90)
        lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        monitor_row.addWidget(lbl)
        self._monitor_combo = QComboBox()
        self._monitor_combo.addItems(get_monitor_names())
        if parsed["monitor"] in [
            self._monitor_combo.itemText(i) for i in range(self._monitor_combo.count())
        ]:
            self._monitor_combo.setCurrentText(parsed["monitor"])
        self._monitor_combo.currentTextChanged.connect(self._update_preview)
        monitor_row.addWidget(self._monitor_combo)
        layout.addLayout(monitor_row)
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
        return self._build_result(
            {
                "monitor": self._monitor_combo.currentText(),
                "path": self._fields["Path"].text().strip(),
                "fit_mode": self._fields["Fit Mode"].text().strip(),
            }
        )
