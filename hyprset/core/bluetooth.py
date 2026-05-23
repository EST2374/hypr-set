import re
import subprocess
from typing import Callable

from PySide6.QtCore import QProcess

_MAC_LIKE = re.compile(r"^[0-9A-F]{2}([:-][0-9A-F]{2}){5}$", re.IGNORECASE)


def get_connected_bluetooth_devices() -> list[dict]:
    try:
        result = subprocess.run(
            ["bluetoothctl", "devices", "Connected"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        return []

    connected: list[dict] = []
    for line in result.stdout.strip().splitlines():
        match = re.match(r"Device\s+(\S+)\s+(.*)", line)
        if match:
            connected.append({"mac": match.group(1), "name": match.group(2)})
    return connected


def _is_meaningful_name(name: str, mac: str) -> bool:
    if not name:
        return False
    name = name.strip()
    if not name:
        return False
    if _MAC_LIKE.match(name):
        return False
    if name.lower() == mac.lower():
        return False
    if name.replace(":", "").replace("-", "").lower() == mac.replace(":", "").lower():
        return False
    if not any(c.isalpha() for c in name):
        return False
    return True


def parse_bluetooth_list(raw_output: str) -> list[dict]:
    devices = []
    seen = set()
    for line in raw_output.strip().split("\n"):
        match = re.search(r"Device\s+([0-9A-F:]{17})\s+(.*)", line, re.IGNORECASE)
        if not match:
            continue
        mac = match.group(1)
        name = match.group(2).strip()
        if mac in seen:
            continue
        if not _is_meaningful_name(name, mac):
            continue
        seen.add(mac)
        devices.append({"mac": mac, "name": name})
    return devices


def build_bluetooth_scan_process(timeout: int = 8) -> QProcess:
    process = QProcess()
    process.start("bluetoothctl", ["--timeout", str(timeout), "scan", "on"])
    return process


def set_bluetooth_radio(
    enabled: bool, on_done: Callable[[bool], None] | None = None
) -> None:
    state = "on" if enabled else "off"
    process = QProcess()

    def _finished(exit_code, _exit_status):
        if on_done:
            on_done(exit_code == 0)
        process.deleteLater()

    process.finished.connect(_finished)
    process.start("bluetoothctl", ["power", state])


def is_bluetooth_radio_on() -> bool:
    try:
        result = subprocess.run(
            ["bluetoothctl", "show"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        return False
    for line in result.stdout.splitlines():
        if "Powered:" in line:
            return "yes" in line.lower()
    return False


def disconnect_bluetooth(
    mac: str, on_done: Callable[[bool, str], None] | None = None
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
    process.start("bluetoothctl", ["disconnect", mac])


def connect_bluetooth(
    mac: str, on_done: Callable[[bool, str], None] | None = None
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
    process.start("bluetoothctl", ["connect", mac])
