import re
from typing import Callable

from PySide6.QtCore import QProcess


def parse_wifi_list(raw_output: str) -> list[dict]:
    networks = []
    for line in raw_output.strip().split("\n"):
        parts = re.split(r"(?<!\\):", line)
        parts = [p.replace(r"\:", ":") for p in parts]
        if len(parts) >= 2 and parts[0]:
            networks.append(
                {
                    "ssid": parts[0],
                    "signal": parts[1],
                    "security": parts[2].strip() if len(parts) > 2 else "",
                }
            )
    return networks


def build_wifi_scan_process() -> QProcess:
    process = QProcess()
    process.start("nmcli", ["-t", "-f", "SSID,BARS,SECURITY", "dev", "wifi"])
    return process


def set_networking(
    enabled: bool, on_done: Callable[[bool], None] | None = None
) -> None:
    state = "on" if enabled else "off"
    process = QProcess()

    def _finished(exit_code, _exit_status):
        if on_done:
            on_done(exit_code == 0)
        process.deleteLater()

    process.finished.connect(_finished)
    process.start("nmcli", ["networking", state])


def disconnect_wifi(
    ssid: str, on_done: Callable[[bool, str], None] | None = None
) -> None:
    process = QProcess()

    def _finished(exit_code, _exit_status):
        ok = exit_code == 0
        msg = (
            bytes(process.readAllStandardError().data())
            .decode("utf-8", errors="replace")
            .strip()
        )
        if on_done:
            on_done(ok, msg)
        process.deleteLater()

    process.finished.connect(_finished)
    process.start("nmcli", ["connection", "down", ssid])
