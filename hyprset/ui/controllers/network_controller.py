from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QHBoxLayout, QListWidget

from ...core.network import (
    build_wifi_scan_process,
    disconnect_wifi,
    parse_wifi_list,
    set_networking,
)
from ..dialogs import (
    Connect_to_Wifi,
)
from ..toggle_switch import ToggleSwitch

if TYPE_CHECKING:
    from PySide6.QtWidgets import QPushButton

    class _NetworkWidgets(Protocol):
        network_layout: QHBoxLayout
        wifi_refresh_button: QPushButton
        wifi_list: QListWidget
        wifi_disconnect_button: QPushButton

    _Base = _NetworkWidgets
else:
    _Base = object


class NetworkControllerMixin(_Base):
    def _setup_network_tab(self):
        # Networking Tab
        # TODO
        # For different Security stuff
        self._networking_toggle = ToggleSwitch(self, active_color="#00b0ff")
        self._networking_toggle.setChecked(True)
        self._networking_toggle.stateChanged.connect(self._on_networking_toggled)

        self.network_layout.addWidget(self._networking_toggle)

        self._start_wifi_scan()
        self.wifi_refresh_button.clicked.connect(self._refresh_wifi)
        self.wifi_list.itemDoubleClicked.connect(self._open_wifi_connect_dialog)
        self.wifi_disconnect_button.clicked.connect(self._disconnect_selected)

    def _start_wifi_scan(self):
        self._wifi_process = build_wifi_scan_process()
        self._wifi_process.finished.connect(self._handle_wifi_output)

    def _handle_wifi_output(self):
        process = self.sender()
        if isinstance(process, QProcess):
            raw_data = process.readAllStandardOutput().data()
            raw = bytes(raw_data).decode("utf-8")

            networks = parse_wifi_list(raw)
            self.wifi_list.clear()
            self.wifi_list.addItems(
                [f"{n['ssid']}  {n['signal']}  {n['security']}" for n in networks]
            )
            process.deleteLater()

    def _refresh_wifi(self):
        self.wifi_list.clear()
        self._start_wifi_scan()

    def connect_to_wifi(self):
        dialog = Connect_to_Wifi(ssid="", parent=self)
        dialog.center_on_parent()
        dialog.exec()

    def _open_wifi_connect_dialog(self, item):
        ssid = item.text().split("  ")[0]
        dialog = Connect_to_Wifi(ssid, parent=self)
        dialog.center_on_parent()
        dialog.exec()

    def _on_networking_toggled(self, state):
        def _done(ok):
            if not ok:
                return
            if state:
                self._start_wifi_scan()
            else:
                self.wifi_list.clear()

        set_networking(enabled=bool(state), on_done=_done)

    def _disconnect_selected(self):
        item = self.wifi_list.currentItem()
        if not item:
            return
        ssid = item.text().split("  ")[0]

        def _done(ok, msg):
            if ok:
                self._refresh_wifi()
            else:
                print(f"Disconnect failed: {msg}")

        disconnect_wifi(ssid, on_done=_done)
