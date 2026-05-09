from PySide6.QtCore import QProcess


def parse_wifi_list(raw_output: str) -> list[dict]:
    networks = []
    for line in raw_output.strip().split("\n"):
        parts = line.split(":")
        if len(parts) >= 2:
            ssid = parts[0]
            signal = parts[1]
            security = parts[2] if len(parts) > 2 else "Open"
            if ssid:
                networks.append({"ssid": ssid, "signal": signal, "security": security})
    return networks


def build_wifi_scan_process() -> QProcess:
    process = QProcess()
    process.start("nmcli", ["-t", "-f", "SSID,BARS,SECURITY", "dev", "wifi"])
    return process


def set_networking(enabled: bool) -> None:
    """nmcli networking on/off"""
    state = "on" if enabled else "off"
    process = QProcess()
    process.start("nmcli", ["networking", state])
    process.waitForFinished(3000)


def disconnect_wifi(ssid: str) -> tuple[bool, str]:
    """Disconnect from a specific wifi network."""
    process = QProcess()
    process.start("nmcli", ["connection", "down", ssid])
    process.waitForFinished(5000)
    ok = process.exitCode() == 0
    msg = process.readAllStandardError().data().decode().strip()
    return ok, msg
