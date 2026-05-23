from PySide6.QtCore import QProcess, Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from .base import BaseDialog


class Connect_to_Wifi(BaseDialog):
    _PERSONAL = "personal"
    _ENTERPRISE = "enterprise"
    _OPEN = "open"

    def __init__(self, ssid: str, security: str = "", parent=None):
        super().__init__(parent)
        self.ssid = ssid
        self._security_type = self._classify(security)

        self.setWindowTitle(f"Connect to {ssid}")
        self.resize(420, 200)
        self._build_ui()

    @staticmethod
    def _classify(security: str) -> str:
        s = security.upper()
        if "802.1X" in s or "EAP" in s:
            return Connect_to_Wifi._ENTERPRISE
        if any(k in s for k in ("WPA", "WEP", "SAE")):
            return Connect_to_Wifi._PERSONAL
        return Connect_to_Wifi._OPEN

    def _toggle_pw_visibility(self, checked: bool):
        mode = QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        self._password_edit.setEchoMode(mode)
        if hasattr(self, "_eap_password_edit"):
            self._eap_password_edit.setEchoMode(mode)

    def _build_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.addWidget(QLabel(f"Connecting to: <b>{self.ssid}</b>"))

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        if self._security_type == self._ENTERPRISE:
            self._build_enterprise(form)
        elif self._security_type == self._PERSONAL:
            self._build_personal(form)
        else:
            form.addRow(QLabel("Open network — no credentials required."))

        main_layout.addLayout(form)

        if self._security_type != self._OPEN:
            self._show_pw_cb = QCheckBox("Show password")
            self._show_pw_cb.toggled.connect(self._toggle_pw_visibility)
            main_layout.addWidget(self._show_pw_cb)

        self._status_label = QLabel("")
        main_layout.addWidget(self._status_label)

        self._connect_btn = QPushButton("Connect")
        self._connect_btn.clicked.connect(self._connect)
        main_layout.addWidget(self._connect_btn)

    def _build_personal(self, form: QFormLayout):
        self._password_edit = QLineEdit()
        self._password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self._password_edit.setPlaceholderText("WiFi password")
        form.addRow("Password:", self._password_edit)

    def _build_enterprise(self, form: QFormLayout):
        self._eap_combo = QComboBox()
        self._eap_combo.addItems(["PEAP", "TTLS", "TLS", "LEAP", "FAST", "PWD"])
        form.addRow("EAP Method:", self._eap_combo)

        self._phase2_combo = QComboBox()
        self._phase2_combo.addItems(["mschapv2", "mschap", "pap", "chap", "gtc"])
        self._phase2_row_label = QLabel("Phase 2:")
        form.addRow("Phase 2:", self._phase2_combo)

        self._eap_combo.currentTextChanged.connect(self._on_eap_changed)

        self._anonymous_identity_edit = QLineEdit()
        self._anonymous_identity_edit.setPlaceholderText(
            "optional: anonymous@domain (sent in clear)"
        )
        form.addRow("Anonymous Identity:", self._anonymous_identity_edit)

        self._username_edit = QLineEdit()
        self._username_edit.setPlaceholderText("username")
        form.addRow("Username:", self._username_edit)

        self._domain_edit = QLineEdit()
        self._domain_edit.setPlaceholderText("optional: domain (e.g. example.com)")
        form.addRow("Domain:", self._domain_edit)

        self._eap_password_edit = QLineEdit()
        self._eap_password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self._eap_password_edit.setPlaceholderText("password")
        form.addRow("Password:", self._eap_password_edit)

        self._ca_cert_edit = QLineEdit()
        self._ca_cert_edit.setPlaceholderText("optional: /path/to/ca.crt")
        form.addRow("CA Cert:", self._ca_cert_edit)

        self.resize(460, 380)

    def _on_eap_changed(self, method: str):
        has_phase2 = method in ("PEAP", "TTLS", "FAST")
        self._phase2_combo.setVisible(has_phase2)

    def _connect(self):
        self._connect_btn.setEnabled(False)
        self._status_label.setText("Connecting…")

        self._process = QProcess(self)
        self._process.finished.connect(self._handle_result)

        if self._security_type == self._ENTERPRISE:
            self._start_enterprise()
        elif self._security_type == self._PERSONAL:
            self._start_personal()
        else:
            self._start_open()

    def _start_personal(self):
        password = self._password_edit.text().strip()
        args = ["dev", "wifi", "connect", self.ssid]
        if password:
            args += ["password", password]
        self._process.start("nmcli", args)

    def _start_open(self):
        self._process.start("nmcli", ["dev", "wifi", "connect", self.ssid])

    def _start_enterprise(self):
        eap = self._eap_combo.currentText().lower()
        username = self._username_edit.text().strip()
        domain = self._domain_edit.text().strip()
        anonymous_identity = self._anonymous_identity_edit.text().strip()
        password = self._eap_password_edit.text().strip()
        phase2 = (
            self._phase2_combo.currentText() if self._phase2_combo.isVisible() else ""
        )
        ca_cert = self._ca_cert_edit.text().strip()

        identity = f"{username}@{domain}" if domain else username

        add_args = [
            "connection",
            "add",
            "type",
            "wifi",
            "con-name",
            self.ssid,
            "ssid",
            self.ssid,
            "wifi-sec.key-mgmt",
            "wpa-eap",
            "802-1x.eap",
            eap,
            "802-1x.identity",
            identity,
            "802-1x.password",
            password,
        ]
        if anonymous_identity:
            add_args += ["802-1x.anonymous-identity", anonymous_identity]
        if phase2:
            add_args += ["802-1x.phase2-auth", phase2]
        if ca_cert:
            add_args += ["802-1x.ca-cert", ca_cert]

        add_proc = QProcess(self)
        add_proc.finished.connect(lambda code, _: self._bring_up_enterprise(code))
        add_proc.start("nmcli", add_args)
        self._add_proc = add_proc

    def _bring_up_enterprise(self, add_exit_code: int):
        if add_exit_code != 0:
            err = (
                bytes(self._add_proc.readAllStandardError().data())
                .decode("utf-8", errors="replace")
                .strip()
            )
            reason = err or "unknown error"
            self._status_label.setText(f"Failed to add profile: {reason}")
            self._connect_btn.setEnabled(True)
            return
        self._process.start("nmcli", ["connection", "up", self.ssid])

    def _handle_result(self, exit_code: int, _exit_status):
        out = (
            bytes(self._process.readAllStandardOutput().data()).decode("utf-8").strip()
        )
        err = bytes(self._process.readAllStandardError().data()).decode("utf-8").strip()

        if exit_code == 0:
            self._status_label.setText(f"Connected to {self.ssid}.")
        else:
            reason = err or out or "Unknown error"
            self._status_label.setText(f"Failed: {reason}")
            self._connect_btn.setEnabled(True)
