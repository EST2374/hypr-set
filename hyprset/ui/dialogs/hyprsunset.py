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


class EditHyprsunset(BaseDialog):
    def __init__(self, profile_block: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Profile" if profile_block else "Add Profile")
        self.original = profile_block
        self._build_ui(profile_block)
        self.resize(820, 300)

    @staticmethod
    def _parse(block: str) -> dict[str, str]:
        def find(key: str) -> str:
            m = re.search(rf"{key}\s*=\s*(\S+)", block)
            return m.group(1).strip() if m else ""

        return {
            "time": find("time"),
            "temperature": find("temperature"),
            "identity": find("identity"),
        }

    @staticmethod
    def _build_result(fields: dict[str, str]) -> str:
        lines = ["profile {"]
        if fields["time"]:
            lines.append(f"    time        = {fields['time']}")
        if fields["temperature"]:
            lines.append(f"    temperature = {fields['temperature']}")
        if fields["identity"]:
            lines.append(f"    identity    = {fields['identity']}")
        lines.append("}")
        return "\n".join(lines)

    def _build_ui(self, block: str):
        parsed = (
            self._parse(block)
            if block
            else {"time": "", "temperature": "", "identity": ""}
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields = {}

        field_defs = [
            ("Time", parsed["time"], "z.B. 20:00"),
            ("Temperature", parsed["temperature"], "z.B. 4000"),
            ("Identity", parsed["identity"], "true oder false"),
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
        return self._build_result(
            {
                "time": self._fields["Time"].text().strip(),
                "temperature": self._fields["Temperature"].text().strip(),
                "identity": self._fields["Identity"].text().strip(),
            }
        )
