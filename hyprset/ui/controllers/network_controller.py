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

from ...core.network import (
    build_wifi_scan_process,
    disconnect_wifi,
    get_active_wifi_connections,
    is_wifi_radio_on,
    parse_wifi_list,
    set_wifi_radio,
)
from ..dialogs import Connect_to_Wifi
from ..notification import hyprland_notification
from ..toggle_switch import ToggleSwitch

if TYPE_CHECKING:
    from PySide6.QtWidgets import QPushButton

    class _NetworkWidgets(Protocol):
        wifi_tab_layout: QVBoxLayout
        wifi_refresh_button: QPushButton
        wifi_connect_button: QPushButton
        wifi_list: QListWidget
        wifi_disconnect_button: QPushButton
        current_connection_label: QLabel
        current_connection_list: QListWidget

    _Base = _NetworkWidgets
else:
    _Base = object


class NetworkControllerMixin(_Base):
    def _setup_network_tab(self):
        self._build_wifi_toggle_row()

        self._networks: list[dict] = []

        self.current_connection_list.setFlow(QListView.Flow.LeftToRight)
        self.current_connection_list.setWrapping(False)
        self.current_connection_list.setFixedHeight(36)
        self.current_connection_list.setHorizontalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.current_connection_list.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self._refresh_active_connection()
        if self._networking_toggle.isChecked():
            self._start_wifi_scan()
        self.wifi_refresh_button.clicked.connect(self._refresh_wifi)
        self.wifi_connect_button.clicked.connect(
            lambda: self._open_wifi_connect_dialog(self.wifi_list.currentItem())
        )
        self.wifi_list.itemDoubleClicked.connect(self._open_wifi_connect_dialog)
        self.wifi_disconnect_button.clicked.connect(self._disconnect_selected)

    def _build_wifi_toggle_row(self):
        label = QLabel("Wi-Fi")
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self._networking_toggle = ToggleSwitch(self, active_color="#00b0ff")
        self._networking_toggle.setChecked(is_wifi_radio_on())
        self._networking_toggle.stateChanged.connect(self._on_wifi_toggled)

        row = QHBoxLayout()
        row.setContentsMargins(8, 0, 8, 0)
        row.addWidget(label)
        row.addStretch()
        row.addWidget(self._networking_toggle)

        self.wifi_tab_layout.insertLayout(0, row)

    def _refresh_active_connection(self):
        self.current_connection_list.clear()
        active = get_active_wifi_connections()
        if not active:
            self.current_connection_list.addItem("Not connected")
            return
        for c in active:
            self.current_connection_list.addItem(f"{c['ssid']}  ({c['device']})")

    def _start_wifi_scan(self):
        self._wifi_process = build_wifi_scan_process()
        self._wifi_process.finished.connect(self._handle_wifi_output)

    def _handle_wifi_output(self):
        process = cast(QObject, self).sender()
        if isinstance(process, QProcess):
            raw_data = process.readAllStandardOutput().data()
            raw = bytes(raw_data).decode("utf-8")

            self._networks = parse_wifi_list(raw)
            self.wifi_list.clear()
            self.wifi_list.addItems(
                [f"{n['ssid']}  {n['signal']}  {n['security']}" for n in self._networks]
            )
            process.deleteLater()

    def _refresh_wifi(self):
        self.wifi_list.clear()
        self._networks = []
        self._refresh_active_connection()
        if self._networking_toggle.isChecked():
            self._start_wifi_scan()

    def _open_wifi_connect_dialog(self, item):
        if item is None:
            return
        ssid = item.text().split("  ")[0]
        security = next(
            (n["security"] for n in self._networks if n["ssid"] == ssid), ""
        )
        dialog = Connect_to_Wifi(ssid, security=security, parent=self)
        dialog.center_on_parent()
        dialog.finished.connect(lambda _: self._refresh_active_connection())
        dialog.exec()

    def connect_to_wifi(self):
        dialog = Connect_to_Wifi(ssid="", parent=self)
        dialog.center_on_parent()
        dialog.finished.connect(lambda _: self._refresh_active_connection())
        dialog.exec()

    def _on_wifi_toggled(self, state):
        if not state and hasattr(self, "_wifi_process"):
            try:
                self._wifi_process.kill()
            except RuntimeError:
                pass

        def _done(ok):
            if not ok:
                return
            if state:
                self._start_wifi_scan()
            else:
                self.wifi_list.clear()
                self._networks = []
            self._refresh_active_connection()

        set_wifi_radio(enabled=bool(state), on_done=_done)
        if not state:
            hyprland_notification("Wifi OFF")
        else:
            hyprland_notification("Wifi ON")

    def _disconnect_selected(self):
        item = self.current_connection_list.currentItem()
        if not item:
            return
        ssid = item.text().split("  ")[0]

        def _done(ok, msg):
            if ok:
                self._refresh_wifi()
            else:
                print(f"Disconnect failed: {msg}")

        disconnect_wifi(ssid, on_done=_done)
        hyprland_notification("Disconnected")
