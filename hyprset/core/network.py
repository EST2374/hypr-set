import re
import subprocess
from typing import Callable

from PySide6.QtCore import QProcess


def get_active_wifi_connections() -> list[dict]:
    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "NAME,TYPE,DEVICE", "connection", "show", "--active"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return []

    active: list[dict] = []
    for line in result.stdout.strip().splitlines():
        parts = re.split(r"(?<!\\):", line)
        parts = [p.replace(r"\:", ":") for p in parts]
        if len(parts) < 3:
            continue
        name, ctype, device = parts[0], parts[1], parts[2]
        if "wireless" not in ctype.lower() and "wifi" not in ctype.lower():
            continue
        active.append({"ssid": name, "device": device})
    return active


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


def set_wifi_radio(
    enabled: bool, on_done: Callable[[bool], None] | None = None
) -> None:
    state = "on" if enabled else "off"
    process = QProcess()

    def _finished(exit_code, _exit_status):
        if on_done:
            on_done(exit_code == 0)
        process.deleteLater()

    process.finished.connect(_finished)
    process.start("nmcli", ["radio", "wifi", state])


def is_wifi_radio_on() -> bool:
    try:
        result = subprocess.run(
            ["nmcli", "-t", "radio", "wifi"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return False
    return result.stdout.strip().lower() == "enabled"


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
