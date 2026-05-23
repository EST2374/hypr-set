import os
import shutil
import tempfile

from PySide6.QtCore import QProcess, QProcessEnvironment, Qt
from PySide6.QtWidgets import (
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
)

from .base import BaseDialog


class HyprPluginManager(BaseDialog):
    def __init__(self, parent=None, plugin=None, mode=None):
        super().__init__(parent)
        self.setWindowTitle("Enabling / Disabling Hyprplugin")
        self.resize(500, 250)
        self.plugin_name = plugin
        self.plugin_mode = mode

        self._tmp_dir = None

        cmd_label = QLabel(f"<code>hyprpm {self.plugin_mode} {self.plugin_name}</code>")
        cmd_label.setTextFormat(Qt.TextFormat.RichText)

        self.status_label = QLabel("")
        self.output_box = QListWidget()

        label_insatall_button = str(self.plugin_mode).capitalize()
        self._install_button = QPushButton(f"{label_insatall_button}")
        self._install_button.clicked.connect(self._run_install)

        layout = QVBoxLayout(self)
        layout.addWidget(cmd_label)
        layout.addWidget(self._install_button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

    def _run_install(self):
        password, ok = QInputDialog.getText(
            self,
            f"Enabling {self.plugin_name}",
            "Enter your Password",
            QLineEdit.EchoMode.Password,
        )

        if not ok or not password:
            self.status_label.setText("Quit installation.")
            return

        self._install_button.setEnabled(False)
        self.output_box.clear()
        self.status_label.setText("Installing…")

        self._process = QProcess(self)
        self._process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)

        self._tmp_dir = tempfile.mkdtemp()
        wrapper_path = os.path.join(self._tmp_dir, "sudo")

        with open(wrapper_path, "w") as f:
            f.write('#!/bin/sh\necho "$HYPRSET_PASS" | /usr/bin/sudo -S "$@"\n')
        os.chmod(wrapper_path, 0o755)

        env = QProcessEnvironment.systemEnvironment()
        env.insert("HYPRSET_PASS", password)

        original_path = env.value("PATH")
        env.insert("PATH", f"{self._tmp_dir}:{original_path}")

        self._process.setProcessEnvironment(env)

        self._process.readyReadStandardOutput.connect(self._handle_output)
        self._process.finished.connect(self._handle_finished)
        self._process.errorOccurred.connect(self._handle_error)

        self._process.start(
            "hyprpm",
            [f"{self.plugin_mode}", f"{self.plugin_name}"],
        )

        env.remove("HYPRSET_PASS")

    def _handle_output(self):
        raw = self._process.readAllStandardOutput().data()
        text = bytes(raw).decode("utf-8", errors="replace").strip()
        for line in text.splitlines():
            if line:
                self.output_box.addItem(line)
                self.output_box.scrollToBottom()

    def _cleanup(self):
        if self._tmp_dir and os.path.exists(self._tmp_dir):
            try:
                shutil.rmtree(self._tmp_dir)
            except OSError:
                pass
            self._tmp_dir = None

    def _handle_finished(self, exit_code, _exit_status):
        self._cleanup()
        if exit_code == 0:
            self.status_label.setText(f"{self.plugin_name} enabled.")
        else:
            self.status_label.setText(f"Error (exit code {exit_code}).")
            self._install_button.setEnabled(True)

    def _handle_error(self, error):
        self._cleanup()
        errors = {
            QProcess.ProcessError.FailedToStart: "Process could not start (hyprpm installed?)",
            QProcess.ProcessError.Crashed: "Process crashed.",
            QProcess.ProcessError.Timedout: "Timeout.",
        }
        self.status_label.setText(errors.get(error, "Unknown error."))
        self._install_button.setEnabled(True)
