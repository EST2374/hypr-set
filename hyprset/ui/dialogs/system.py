import subprocess

from PySide6.QtCore import QProcess, Qt
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
)

from .base import BaseDialog


class Update(BaseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update")
        self.resize(800, 300)

        self.list_programs = QListWidget()
        self.list_programs.addItems(self.get_updates())
        self.list_programs.itemDoubleClicked.connect(self.update_item)

        self.status_label = QLabel("")
        self.output_box = QListWidget()

        button_update_all = QPushButton("Update All")
        button_update_all.clicked.connect(self.update_all)

        layout = QVBoxLayout(self)
        layout.addWidget(self.list_programs)
        layout.addWidget(button_update_all)
        layout.addWidget(self.status_label)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

    def get_updates(self) -> list[str]:
        updates_list = []
        try:
            result = subprocess.run(
                ["checkupdates"],
                capture_output=True,
                text=True,
                check=True,
            )
            updates_list = result.stdout.splitlines()
            return updates_list
        except subprocess.CalledProcessError as e:
            if e.returncode == 2:
                return []
            print(f"Unexpected return code: {e}")
            return []
        except FileNotFoundError:
            print("checkupdates not found")
            return []
        except Exception as e:
            print(f"Fehler: {e}")
            return []

    def update_all(self):
        self._run_pacman_command(["pkexec", "pacman", "-Syu", "--noconfirm"])

    def update_item(self, item):
        package_name = item.text().split()[0]
        self._run_pacman_command(
            ["pkexec", "pacman", "-Sy", package_name, "--noconfirm"]
        )

    def _run_pacman_command(self, cmd: list[str]):
        self.output_box.clear()
        self.status_label.setText("Running…")

        self._process = QProcess(self)
        self._process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)

        self._process.readyReadStandardOutput.connect(self._handle_output)
        self._process.finished.connect(self._handle_finished)
        self._process.errorOccurred.connect(self._handle_error)

        self._process.start(cmd[0], cmd[1:])

    def _handle_output(self):
        raw = self._process.readAllStandardOutput().data()
        text = bytes(raw).decode("utf-8", errors="replace").strip()
        for line in text.splitlines():
            if line:
                self.output_box.addItem(line)
                self.output_box.scrollToBottom()

    def _handle_finished(self, exit_code, exit_status):
        if exit_code == 0:
            self.status_label.setText("Finished.")
            self.refresh_list()
        else:
            self.status_label.setText(f"Error (exit code {exit_code}).")

    def _handle_error(self, error):
        errors = {
            QProcess.ProcessError.FailedToStart: "Process could not start (pkexec installed?)",
            QProcess.ProcessError.Crashed: "Process crashed.",
            QProcess.ProcessError.Timedout: "Timeout.",
        }
        msg = errors.get(error, "Error.")
        self.status_label.setText(msg)

    def refresh_list(self):
        self.list_programs.clear()
        self.list_programs.addItems(self.get_updates())


class InstallHyprStuff(BaseDialog):
    def __init__(self, parent=None, pkg=None):
        super().__init__(parent)
        self.setWindowTitle("Install Hyprpaper")
        self.resize(500, 250)
        self.pkg_name = pkg

        info_label = QLabel(f"{self.pkg_name} is not installed. Install it now?")
        cmd_label = QLabel(f"<code>sudo pacman -S {self.pkg_name}</code>")
        cmd_label.setTextFormat(Qt.TextFormat.RichText)

        self.status_label = QLabel("")
        self.output_box = QListWidget()

        self._install_button = QPushButton("Install")
        self._install_button.clicked.connect(self._run_install)

        layout = QVBoxLayout(self)
        layout.addWidget(info_label)
        layout.addWidget(cmd_label)
        layout.addWidget(self._install_button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

    def _run_install(self):
        self._install_button.setEnabled(False)
        self.output_box.clear()
        self.status_label.setText("Installing…")

        self._process = QProcess(self)
        self._process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self._process.readyReadStandardOutput.connect(self._handle_output)
        self._process.finished.connect(self._handle_finished)
        self._process.errorOccurred.connect(self._handle_error)
        self._process.start(
            "pkexec", ["pacman", "-S", f"{self.pkg_name}", "--noconfirm"]
        )

    def _handle_output(self):
        raw = self._process.readAllStandardOutput().data()
        text = bytes(raw).decode("utf-8", errors="replace").strip()
        for line in text.splitlines():
            if line:
                self.output_box.addItem(line)
                self.output_box.scrollToBottom()

    def _handle_finished(self, exit_code, _exit_status):
        if exit_code == 0:
            self.status_label.setText(f"{self.pkg_name} installed successfully.")
        else:
            self.status_label.setText(f"Error (exit code {exit_code}).")
            self._install_button.setEnabled(True)

    def _handle_error(self, error):
        errors = {
            QProcess.ProcessError.FailedToStart: "Process could not start (pkexec installed?)",
            QProcess.ProcessError.Crashed: "Process crashed.",
            QProcess.ProcessError.Timedout: "Timeout.",
        }
        self.status_label.setText(errors.get(error, "Unknown error."))
        self._install_button.setEnabled(True)
