from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from PySide6.QtCore import QObject, QProcess, Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QLabel,
    QListView,
    QListWidget,
    QVBoxLayout,
)

from ...core.bluetooth import (
    build_bluetooth_scan_process,
    connect_bluetooth,
    disconnect_bluetooth,
    get_connected_bluetooth_devices,
    is_bluetooth_radio_on,
    parse_bluetooth_list,
    set_bluetooth_radio,
)
from ..notification import hyprland_notification
from ..toggle_switch import ToggleSwitch

if TYPE_CHECKING:
    from PySide6.QtWidgets import QPushButton

    class _BluetoothWidgets(Protocol):
        bluetooth_tab_layout: QVBoxLayout
        bluetooth_scan_button: QPushButton
        bluetooth_connect_button: QPushButton
        bluetooth_list: QListWidget
        bluetooth_disconnect_button: QPushButton
        current_bluetooth_list: QListWidget

    _Base = _BluetoothWidgets
else:
    _Base = object


class BluetoothControllerMixin(_Base):
    def _setup_bluetooth_tab(self):
        self._build_bluetooth_toggle_row()
        self._bluetooth_devices: list[dict] = []
        self._bluetooth_seen_macs: set[str] = set()

        self.current_bluetooth_list.setFlow(QListView.Flow.LeftToRight)
        self.current_bluetooth_list.setWrapping(False)
        self.current_bluetooth_list.setFixedHeight(36)
        self.current_bluetooth_list.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.current_bluetooth_list.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self._refresh_active_bluetooth()
        if self._bluetooth_toggle.isChecked():
            self._start_bluetooth_scan()

        self.bluetooth_scan_button.clicked.connect(self._scan_bluetooth)
        self.bluetooth_connect_button.clicked.connect(
            lambda: self._connect_selected(self.bluetooth_list.currentItem())
        )
        self.bluetooth_list.itemDoubleClicked.connect(self._connect_selected)
        self.bluetooth_disconnect_button.clicked.connect(self._disconnect_selected)

    def _start_bluetooth_scan(self):
        self.bluetooth_scan_button.setEnabled(False)
        self.bluetooth_scan_button.setText("Scanning…")
        self._bluetooth_process = build_bluetooth_scan_process()
        self._bluetooth_process.finished.connect(self._handle_bluetooth_output)

    def _handle_bluetooth_output(self):
        added = 0
        process = cast(QObject, self).sender()
        if isinstance(process, QProcess):
            raw_data = process.readAllStandardOutput().data()
            raw = bytes(raw_data).decode("utf-8")

            new_devices = parse_bluetooth_list(raw)
            for d in new_devices:
                if d["mac"] in self._bluetooth_seen_macs:
                    continue
                self._bluetooth_seen_macs.add(d["mac"])
                self._bluetooth_devices.append(d)
                self.bluetooth_list.addItem(f"{d['name']}  {d['mac']}")
                added += 1
            process.deleteLater()

        self.bluetooth_scan_button.setEnabled(True)
        self.bluetooth_scan_button.setText("Scan")
        if added:
            hyprland_notification(f"Found {added} new device(s)")

    def _scan_bluetooth(self):
        if not self._bluetooth_toggle.isChecked():
            hyprland_notification("Bluetooth is off")
            return
        if hasattr(self, "_bluetooth_process"):
            try:
                if self._bluetooth_process.state() != QProcess.ProcessState.NotRunning:
                    return
            except RuntimeError:
                pass
        self._refresh_active_bluetooth()
        self._start_bluetooth_scan()

    def _build_bluetooth_toggle_row(self):
        label = QLabel("Bluetooth")
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self._bluetooth_toggle = ToggleSwitch(self, active_color="#00b0ff")
        self._bluetooth_toggle.setChecked(is_bluetooth_radio_on())
        self._bluetooth_toggle.stateChanged.connect(self._on_bluetooth_toggled)

        row = QHBoxLayout()
        row.setContentsMargins(8, 0, 8, 0)
        row.addWidget(label)
        row.addStretch()
        row.addWidget(self._bluetooth_toggle)

        self.bluetooth_tab_layout.insertLayout(0, row)

    def _refresh_active_bluetooth(self):
        self.current_bluetooth_list.clear()
        active = get_connected_bluetooth_devices()
        if not active:
            self.current_bluetooth_list.addItem("Not connected")
            return
        for d in active:
            self.current_bluetooth_list.addItem(f"{d['name']}  ({d['mac']})")

    def _refresh_bluetooth(self):
        self.bluetooth_list.clear()
        self._bluetooth_devices = []
        self._refresh_active_bluetooth()
        if self._bluetooth_toggle.isChecked():
            self._start_bluetooth_scan()

    def _connect_selected(self, item):
        if item is None:
            return
        text = item.text()
        parts = text.rsplit("  ", 1)
        if len(parts) != 2:
            return
        mac = parts[1].strip()

        def _done(ok, msg):
            if ok:
                self._refresh_active_bluetooth()
                hyprland_notification("Bluetooth connected")
            else:
                print(f"Bluetooth connect failed: {msg}")
                hyprland_notification("Bluetooth connect failed")

        connect_bluetooth(mac, on_done=_done)

    def _on_bluetooth_toggled(self, state):
        if not state and hasattr(self, "_bluetooth_process"):
            try:
                self._bluetooth_process.kill()
            except RuntimeError:
                pass

        def _done(ok):
            if not ok:
                return
            if state:
                self._start_bluetooth_scan()
            else:
                self.bluetooth_list.clear()
                self._bluetooth_devices = []
            self._refresh_active_bluetooth()

        set_bluetooth_radio(enabled=bool(state), on_done=_done)
        if not state:
            self.bluetooth_list.clear()
            self._bluetooth_devices = []
            self._bluetooth_seen_macs.clear()
            hyprland_notification("Bluetooth OFF")
        else:
            hyprland_notification("Bluetooth ON")

    def _disconnect_selected(self):
        item = self.current_bluetooth_list.currentItem()
        if not item:
            return
        text = item.text()
        if "(" not in text or ")" not in text:
            return
        mac = text.rsplit("(", 1)[1].rstrip(")").strip()

        def _done(ok, msg):
            if ok:
                self._refresh_bluetooth()
            else:
                print(f"Disconnect failed: {msg}")

        disconnect_bluetooth(mac, on_done=_done)
        hyprland_notification("Disconnected")
