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


class EditWindowRule(BaseDialog):
    def __init__(self, rule_block: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Window Rule" if rule_block else "Add Window Rule")
        self.original = rule_block
        self._build_ui(rule_block)
        self.resize(820, 420)

    @staticmethod
    def _parse(block: str) -> dict[str, str]:
        def find(key: str) -> str:
            m = re.search(rf'{key}\s*=\s*(".*?"|true|false|\{{[^}}]*\}}|\S+)', block)
            return m.group(1).strip().strip('"') if m else ""

        match_block = re.search(r"match\s*=\s*\{([^}]*)\}", block)
        match_str = match_block.group(1).strip() if match_block else ""

        return {
            "name": find("name"),
            "match": match_str,
            "float": find("float"),
            "animation": find("animation"),
            "size": find("size"),
        }

    @staticmethod
    def _build_result(fields: dict[str, str]) -> str:
        lines = ["hl.window_rule({"]

        if fields["name"]:
            lines.append(f'    name      = "{fields["name"]}",')
        if fields["match"]:
            lines.append(f"    match     = {{ {fields['match']} }},")
        if fields["float"]:
            lines.append(f"    float     = {fields['float']},")
        if fields["animation"]:
            lines.append(f'    animation = "{fields["animation"]}",')
        if fields["size"]:
            lines.append(f"    size      = {fields['size']},")

        lines.append("})")
        return "\n".join(lines)

    def _build_ui(self, block: str):
        parsed = (
            self._parse(block)
            if block
            else {
                "name": "",
                "match": "",
                "float": "",
                "animation": "",
                "size": "",
            }
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        self._fields = {}

        field_defs = [
            ("Name", parsed["name"], "z.B. fileManager"),
            ("Match", parsed["match"], 'z.B. class = "org.*"'),
            ("Float", parsed["float"], "true oder false"),
            ("Animation", parsed["animation"], "z.B. slide top"),
            ("Size", parsed["size"], "z.B. {1200, 700}"),
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
                "name": self._fields["Name"].text().strip(),
                "match": self._fields["Match"].text().strip(),
                "float": self._fields["Float"].text().strip(),
                "animation": self._fields["Animation"].text().strip(),
                "size": self._fields["Size"].text().strip(),
            }
        )
