from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .base import BaseDialog

_ACTIONS: list[dict[str, Any]] = [
    {
        "label": "Run Program / Command",
        "lua_fn": "exec_cmd",
        "params": [
            ("cmd", "Command", "line", "e.g. alacritty  or  nautilus"),
        ],
    },
    {
        "label": "Close Window",
        "lua_fn": "window_close",
        "params": [],
    },
    {
        "label": "Float Toggle",
        "lua_fn": "window_float_toggle",
        "params": [],
    },
    {
        "label": "Focus Direction",
        "lua_fn": "focus_direction",
        "params": [
            ("direction", "Direction", "combo", ["left", "right", "up", "down"]),
        ],
    },
    {
        "label": "Go to Workspace",
        "lua_fn": "focus_workspace",
        "params": [
            (
                "workspace",
                "Workspace",
                "combo",
                [str(i) for i in range(1, 11)] + ["e+1", "e-1", "special:magic"],
            ),
        ],
    },
    {
        "label": "Move Window to Workspace",
        "lua_fn": "move_workspace",
        "params": [
            (
                "workspace",
                "Workspace",
                "combo",
                [str(i) for i in range(1, 11)] + ["special:magic"],
            ),
        ],
    },
    {
        "label": "Toggle Special Workspace",
        "lua_fn": "toggle_special",
        "params": [
            ("name", "Name", "line", "e.g. magic"),
        ],
    },
    {
        "label": "Layout Action",
        "lua_fn": "layout_action",
        "params": [
            (
                "action",
                "Action",
                "combo",
                [
                    "togglesplit",
                    "swapnext",
                    "swapprev",
                    "focusmaster",
                    "swapwithmaster",
                ],
            ),
        ],
    },
    {
        "label": "Drag Window (Mouse)",
        "lua_fn": "window_drag",
        "params": [],
    },
    {
        "label": "Resize Window (Mouse)",
        "lua_fn": "window_resize",
        "params": [],
    },
    {
        "label": "Custom Lua (Advanced)",
        "lua_fn": "custom",
        "params": [
            ("lua", "Lua action", "line", 'e.g. hl.dsp.exec_cmd("app")'),
        ],
    },
]

_ACTION_BY_LABEL: dict[str, dict] = {a["label"]: a for a in _ACTIONS}
_ACTION_BY_LUA: dict[str, dict] = {a["lua_fn"]: a for a in _ACTIONS}


def _build_lua(
    keys: str,
    action_def: dict,
    param_values: dict[str, str],
    opt_repeating: bool,
    opt_locked: bool,
) -> str:
    """Baut den vollständigen hl.bind(...)-Aufruf."""

    fn = action_def["lua_fn"]

    if fn == "exec_cmd":
        cmd = param_values.get("cmd", "")
        action_lua = f'hl.dsp.exec_cmd("{cmd}")'

    elif fn == "window_close":
        action_lua = "hl.dsp.window.close()"

    elif fn == "window_float_toggle":
        action_lua = 'hl.dsp.window.float({ action = "toggle" })'

    elif fn == "focus_direction":
        d = param_values.get("direction", "left")
        action_lua = f'hl.dsp.focus({{ direction = "{d}" }})'

    elif fn == "focus_workspace":
        ws = param_values.get("workspace", "1")
        if ws.lstrip("-+e").isdigit() or ws.startswith("e"):
            action_lua = f'hl.dsp.focus({{ workspace = "{ws}" }})'
        else:
            action_lua = f'hl.dsp.focus({{ workspace = "{ws}" }})'

    elif fn == "move_workspace":
        ws = param_values.get("workspace", "1")
        if ws.isdigit():
            action_lua = f"hl.dsp.window.move({{ workspace = {ws} }})"
        else:
            action_lua = f'hl.dsp.window.move({{ workspace = "{ws}" }})'

    elif fn == "toggle_special":
        name = param_values.get("name", "magic")
        action_lua = f'hl.dsp.workspace.toggle_special("{name}")'

    elif fn == "layout_action":
        act = param_values.get("action", "togglesplit")
        action_lua = f'hl.dsp.layout("{act}")'

    elif fn == "window_drag":
        action_lua = "hl.dsp.window.drag()"

    elif fn == "window_resize":
        action_lua = "hl.dsp.window.resize()"

    elif fn == "custom":
        action_lua = param_values.get("lua", "")

    else:
        action_lua = ""

    opts: list[str] = []
    if opt_repeating:
        opts.append("repeating = true")
    if opt_locked:
        opts.append("locked = true")

    opts_lua = ""
    if opts:
        opts_lua = ", { " + ", ".join(opts) + " }"

    return f"hl.bind({keys}, {action_lua}{opts_lua})"


@dataclass
class ParsedBind:
    keys: str = ""
    action_label: str = "Run Program / Command"
    params: dict[str, str] = field(default_factory=dict)
    repeating: bool = False
    locked: bool = False


def _parse_bind(lua: str) -> ParsedBind:
    """Versucht einen hl.bind()-String zurück ins Formular zu laden."""
    result = ParsedBind()
    lua = lua.strip()

    m_keys = re.match(r"hl\.bind\((.+?),\s*hl\.", lua)
    if not m_keys:
        m_raw = re.match(r"hl\.bind\((.+?),\s*(.+)\)", lua, re.DOTALL)
        if m_raw:
            result.keys = m_raw.group(1).strip()
            result.action_label = "Custom Lua (Advanced)"
            result.params["lua"] = m_raw.group(2).strip()
        return result

    result.keys = m_keys.group(1).strip()

    if "repeating = true" in lua:
        result.repeating = True
    if "locked = true" in lua:
        result.locked = True

    body = lua[m_keys.end() - len("hl.") :]

    if m := re.search(r'hl\.dsp\.exec_cmd\("([^"]+)"\)', body):
        result.action_label = "Run Program / Command"
        result.params["cmd"] = m.group(1)

    elif "hl.dsp.window.close()" in body:
        result.action_label = "Close Window"

    elif "hl.dsp.window.float" in body and "toggle" in body:
        result.action_label = "Float Toggle"

    elif m := re.search(r'hl\.dsp\.focus\(\{\s*direction\s*=\s*"(\w+)"', body):
        result.action_label = "Focus Direction"
        result.params["direction"] = m.group(1)

    elif m := re.search(r'hl\.dsp\.focus\(\{\s*workspace\s*=\s*"?([^"}\s]+)"?', body):
        result.action_label = "Go to Workspace"
        result.params["workspace"] = m.group(1)

    elif m := re.search(
        r'hl\.dsp\.window\.move\(\{\s*workspace\s*=\s*"?([^"}\s]+)"?', body
    ):
        result.action_label = "Move Window to Workspace"
        result.params["workspace"] = m.group(1)

    elif m := re.search(r'hl\.dsp\.workspace\.toggle_special\("([^"]+)"\)', body):
        result.action_label = "Toggle Special Workspace"
        result.params["name"] = m.group(1)

    elif m := re.search(r'hl\.dsp\.layout\("([^"]+)"\)', body):
        result.action_label = "Layout Action"
        result.params["action"] = m.group(1)

    elif "hl.dsp.window.drag()" in body:
        result.action_label = "Drag Window (Mouse)"

    elif "hl.dsp.window.resize()" in body:
        result.action_label = "Resize Window (Mouse)"

    else:
        result.action_label = "Custom Lua (Advanced)"
        m_custom = re.match(
            r"hl\.bind\([^,]+,\s*(.+?)(?:,\s*\{[^}]+\})?\s*\)$", lua, re.DOTALL
        )
        if m_custom:
            result.params["lua"] = m_custom.group(1).strip()

    return result


_MODIFIERS = [
    "",
    "SUPER",
    "CTRL",
    "ALT",
    "SHIFT",
    "SUPER + CTRL",
    "SUPER + ALT",
    "SUPER + SHIFT",
    "CTRL + ALT",
    "CTRL + SHIFT",
    "SUPER + CTRL + ALT",
]

_COMMON_KEYS = [
    "RETURN",
    "SPACE",
    "ESCAPE",
    "TAB",
    "BACKSPACE",
    "DELETE",
    "left",
    "right",
    "up",
    "down",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
    "PRIOR",
    "NEXT",
    "HOME",
    "END",
    "INSERT",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "plus",
    "minus",
    "equal",
    "slash",
    "backslash",
    "comma",
    "period",
    "mouse:272",
    "mouse:273",
    "mouse_down",
    "mouse_up",
    "XF86AudioRaiseVolume",
    "XF86AudioLowerVolume",
    "XF86AudioMute",
    "XF86AudioPlay",
    "XF86AudioPause",
    "XF86AudioNext",
    "XF86AudioPrev",
    "XF86MonBrightnessUp",
    "XF86MonBrightnessDown",
]


class KeyPicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self._mod_combo = QComboBox()
        self._mod_combo.addItems(_MODIFIERS)
        self._mod_combo.setEditable(True)
        self._mod_combo.setMinimumWidth(180)

        plus_label = QLabel("+")
        plus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        plus_label.setFixedWidth(16)

        self._key_combo = QComboBox()
        self._key_combo.addItems(_COMMON_KEYS)
        self._key_combo.setEditable(True)
        self._key_combo.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        layout.addWidget(self._mod_combo)
        layout.addWidget(plus_label)
        layout.addWidget(self._key_combo)

    def set_lua_keys(self, lua_keys: str):
        lua_keys = lua_keys.strip()

        if "mainMod" in lua_keys:
            m = re.search(r'mainMod\s*\.\.\s*"\s*\+\s*(.+)"', lua_keys)
            if m:
                rest = m.group(1).strip()
                parts = [p.strip() for p in rest.split("+")]
                if len(parts) == 1:
                    self._mod_combo.setCurrentText("SUPER")
                    self._key_combo.setCurrentText(parts[0])
                else:
                    extra_mods = " + ".join(parts[:-1])
                    self._mod_combo.setCurrentText(f"SUPER + {extra_mods}")
                    self._key_combo.setCurrentText(parts[-1])
        else:
            clean = lua_keys.strip('"')
            parts = [p.strip() for p in clean.split("+")]
            if len(parts) >= 2:
                mod = " + ".join(parts[:-1])
                key = parts[-1]
                self._mod_combo.setCurrentText(mod)
                self._key_combo.setCurrentText(key)
            elif len(parts) == 1:
                self._mod_combo.setCurrentText("")
                self._key_combo.setCurrentText(parts[0])

    def get_lua_keys(self) -> str:
        mod = self._mod_combo.currentText().strip()
        key = self._key_combo.currentText().strip()

        if not key:
            return '""'

        if "SUPER" in mod:
            rest = mod.replace("SUPER", "").strip().lstrip("+").strip()
            if rest:
                return f'mainMod .. " + {rest} + {key}"'
            return f'mainMod .. " + {key}"'
        elif mod:
            return f'"{mod} + {key}"'
        else:
            return f'"{key}"'

    def connect_changed(self, slot):
        self._mod_combo.currentTextChanged.connect(slot)
        self._key_combo.currentTextChanged.connect(slot)


class ParamPanel(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._panels: dict[str, tuple[QWidget, dict[str, QWidget]]] = {}

        for action in _ACTIONS:
            panel, widgets = self._make_panel(action)
            self._panels[action["label"]] = (panel, widgets)
            self.addWidget(panel)

    def _make_panel(self, action: dict) -> tuple[QWidget, dict[str, QWidget]]:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        widgets: dict[str, QWidget] = {}

        for key, label, wtype, spec in action["params"]:
            row = QHBoxLayout()
            lbl = QLabel(f"{label}:")
            lbl.setFixedWidth(90)
            lbl.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            row.addWidget(lbl)

            if wtype == "line":
                w = QLineEdit()
                w.setPlaceholderText(spec)
            elif wtype == "combo":
                w = QComboBox()
                w.setEditable(True)
                w.addItems(spec)
            else:
                w = QWidget()

            row.addWidget(w)
            widgets[key] = w
            layout.addLayout(row)

        if not action["params"]:
            lbl = QLabel("No additional parameters needed.")
            lbl.setStyleSheet("color: palette(mid); font-style: italic;")
            layout.addWidget(lbl)

        layout.addStretch()
        return panel, widgets

    def show_action(self, label: str):
        if label in self._panels:
            self.setCurrentWidget(self._panels[label][0])

    def get_values(self, label: str) -> dict[str, str]:
        if label not in self._panels:
            return {}
        _, widgets = self._panels[label]
        result = {}
        for key, w in widgets.items():
            if isinstance(w, QLineEdit):
                result[key] = w.text().strip()
            elif isinstance(w, QComboBox):
                result[key] = w.currentText().strip()
        return result

    def set_values(self, label: str, values: dict[str, str]):
        if label not in self._panels:
            return
        _, widgets = self._panels[label]
        for key, val in values.items():
            if key not in widgets:
                continue
            w = widgets[key]
            if isinstance(w, QLineEdit):
                w.setText(val)
            elif isinstance(w, QComboBox):
                idx = w.findText(val)
                if idx >= 0:
                    w.setCurrentIndex(idx)
                else:
                    w.setCurrentText(val)

    def connect_all_changed(self, slot):
        for _, (_, widgets) in self._panels.items():
            for w in widgets.values():
                if isinstance(w, QLineEdit):
                    w.textChanged.connect(slot)
                elif isinstance(w, QComboBox):
                    w.currentTextChanged.connect(slot)


class EditKeybindingDialog(BaseDialog):
    def __init__(self, bind_string: str = "", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Keybinding" if bind_string else "Add Keybinding")
        self.original = bind_string
        self._build_ui(bind_string)
        self.resize(640, 380)

    def _build_ui(self, bind_string: str):
        parsed = _parse_bind(bind_string) if bind_string else ParsedBind()

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        keys_row = QHBoxLayout()
        keys_lbl = QLabel("Keys:")
        keys_lbl.setFixedWidth(90)
        keys_lbl.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self._key_picker = KeyPicker()
        if parsed.keys:
            self._key_picker.set_lua_keys(parsed.keys)
        keys_row.addWidget(keys_lbl)
        keys_row.addWidget(self._key_picker)
        layout.addLayout(keys_row)

        action_row = QHBoxLayout()
        action_lbl = QLabel("Action:")
        action_lbl.setFixedWidth(90)
        action_lbl.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self._action_combo = QComboBox()
        self._action_combo.addItems([a["label"] for a in _ACTIONS])
        self._action_combo.setCurrentText(parsed.action_label)
        action_row.addWidget(action_lbl)
        action_row.addWidget(self._action_combo)
        layout.addLayout(action_row)

        self._param_panel = ParamPanel()
        self._param_panel.show_action(parsed.action_label)
        self._param_panel.set_values(parsed.action_label, parsed.params)
        self._param_panel.setFixedHeight(80)
        layout.addWidget(self._param_panel)

        opts_row = QHBoxLayout()
        opts_lbl = QLabel("Options:")
        opts_lbl.setFixedWidth(90)
        opts_lbl.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self._repeating_cb = QCheckBox("Repeating")
        self._locked_cb = QCheckBox("Locked (works on lockscreen)")
        self._repeating_cb.setChecked(parsed.repeating)
        self._locked_cb.setChecked(parsed.locked)
        opts_row.addWidget(opts_lbl)
        opts_row.addWidget(self._repeating_cb)
        opts_row.addSpacing(16)
        opts_row.addWidget(self._locked_cb)
        opts_row.addStretch()
        layout.addLayout(opts_row)

        self._preview = QLabel()
        self._preview.setStyleSheet(
            "color: palette(mid); font-family: monospace; font-size: 11px;"
            "padding: 4px; border-radius: 4px;"
        )
        self._preview.setWordWrap(True)
        layout.addWidget(self._preview)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self._action_combo.currentTextChanged.connect(self._on_action_changed)
        self._key_picker.connect_changed(self._update_preview)
        self._param_panel.connect_all_changed(self._update_preview)
        self._repeating_cb.checkStateChanged.connect(self._update_preview)
        self._locked_cb.checkStateChanged.connect(self._update_preview)

        self._update_preview()

    def _on_action_changed(self, label: str):
        self._param_panel.show_action(label)
        self._update_preview()

    def _update_preview(self, *_):
        self._preview.setText(f"  ↳  {self.get_result()}")

    def get_result(self) -> str:
        action_label = self._action_combo.currentText()
        action_def = _ACTION_BY_LABEL.get(action_label, _ACTIONS[0])
        param_values = self._param_panel.get_values(action_label)
        keys = self._key_picker.get_lua_keys()

        return _build_lua(
            keys=keys,
            action_def=action_def,
            param_values=param_values,
            opt_repeating=self._repeating_cb.isChecked(),
            opt_locked=self._locked_cb.isChecked(),
        )
