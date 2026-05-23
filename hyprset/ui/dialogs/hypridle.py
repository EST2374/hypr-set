import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)

from ...core.hypridle import build_general_block, parse_general_block
from .base import BaseDialog


class EditHypridle(BaseDialog):
    def __init__(self, listener_block: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Listener" if listener_block else "Add Listener")
        self.original = listener_block
        self._build_ui(listener_block)
        self.resize(820, 340)

    @staticmethod
    def _parse(block: str) -> dict[str, str]:
        def find(key: str) -> str:
            m = re.search(rf"{key}\s*=\s*(.+)", block)
            return m.group(1).strip() if m else ""

        return {
            "timeout": find("timeout"),
            "on_timeout": find("on-timeout"),
            "on_resume": find("on-resume"),
        }

    @staticmethod
    def _build_result(fields: dict[str, str]) -> str:
        lines = ["listener {"]
        if fields["timeout"]:
            lines.append(f"    timeout    = {fields['timeout']}")
        if fields["on_timeout"]:
            lines.append(f"    on-timeout = {fields['on_timeout']}")
        if fields["on_resume"]:
            lines.append(f"    on-resume  = {fields['on_resume']}")
        lines.append("}")
        return "\n".join(lines)

    def _build_ui(self, block: str):
        parsed = (
            self._parse(block)
            if block
            else {"timeout": "", "on_timeout": "", "on_resume": ""}
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields = {}

        field_defs = [
            ("Timeout", parsed["timeout"], "z.B. 300"),
            ("On-Timeout", parsed["on_timeout"], "z.B. loginctl lock-session"),
            ("On-Resume", parsed["on_resume"], "z.B. brightnessctl -r"),
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
                "timeout": self._fields["Timeout"].text().strip(),
                "on_timeout": self._fields["On-Timeout"].text().strip(),
                "on_resume": self._fields["On-Resume"].text().strip(),
            }
        )


class EditHypridleGeneral(BaseDialog):
    def __init__(self, general_block: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit General Settings")
        self.resize(820, 280)
        self._build_ui(general_block)

    def _build_ui(self, block: str):
        parsed = (
            parse_general_block(block)
            if block
            else {"lock_cmd": "", "before_sleep_cmd": "", "after_sleep_cmd": ""}
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields: dict[str, QLineEdit] = {}

        field_defs = [
            ("lock_cmd", parsed["lock_cmd"], "z.B. pidof hyprlock || hyprlock"),
            (
                "before_sleep_cmd",
                parsed["before_sleep_cmd"],
                "z.B. loginctl lock-session",
            ),
            (
                "after_sleep_cmd",
                parsed["after_sleep_cmd"],
                "z.B. hyprctl dispatch dpms on",
            ),
        ]

        for key, default, placeholder in field_defs:
            row = QHBoxLayout()
            lbl = QLabel(f"{key}:")
            lbl.setFixedWidth(140)
            lbl.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            row.addWidget(lbl)
            edit = QLineEdit(default)
            edit.setPlaceholderText(placeholder)
            row.addWidget(edit)
            self._fields[key] = edit
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
        self._preview.setText(self.get_result())

    def get_result(self) -> str:
        return build_general_block(
            {key: edit.text().strip() for key, edit in self._fields.items()}
        )
