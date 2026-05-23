import re
import shutil
import subprocess

import hyprset.config as app_config


def get_all_listeners():
    try:
        with open(app_config.HYPRIDLE_FILE, "r") as f:
            text = f.read()
    except FileNotFoundError:
        return []

    pattern = r"listener\s*\{.*?\}"
    all_blocks = re.findall(pattern, text, flags=re.DOTALL)

    listeners_blocks = []
    for block in all_blocks:
        lines = block.splitlines()
        content_lines = [line.strip() for line in lines[1:] if line.strip()]
        if any(not line.startswith("#") for line in content_lines):
            listeners_blocks.append(block)
    return listeners_blocks


def get_general_block() -> str | None:
    try:
        with open(app_config.HYPRIDLE_FILE, "r") as f:
            text = f.read()
    except FileNotFoundError:
        return None

    match = re.search(r"general\s*\{.*?\}", text, flags=re.DOTALL)
    return match.group(0) if match else None


def parse_general_block(block: str) -> dict[str, str]:
    def find(key: str) -> str:
        m = re.search(rf"^\s*{key}\s*=\s*(.+)$", block, flags=re.MULTILINE)
        return m.group(1).strip() if m else ""

    return {
        "lock_cmd": find("lock_cmd"),
        "before_sleep_cmd": find("before_sleep_cmd"),
        "after_sleep_cmd": find("after_sleep_cmd"),
    }


def build_general_block(fields: dict[str, str]) -> str:
    lines = ["general {"]
    if fields.get("lock_cmd"):
        lines.append(f"    lock_cmd         = {fields['lock_cmd']}")
    if fields.get("before_sleep_cmd"):
        lines.append(f"    before_sleep_cmd = {fields['before_sleep_cmd']}")
    if fields.get("after_sleep_cmd"):
        lines.append(f"    after_sleep_cmd  = {fields['after_sleep_cmd']}")
    lines.append("}")
    return "\n".join(lines)


def update_general_block(new_block: str) -> bool:
    try:
        with open(app_config.HYPRIDLE_FILE, "r") as f:
            content = f.read()

        match = re.search(r"general\s*\{.*?\}", content, flags=re.DOTALL)
        if match:
            content = content.replace(match.group(0), new_block, 1)
        else:
            content = new_block + "\n\n" + content

        with open(app_config.HYPRIDLE_FILE, "w") as f:
            f.write(content)
        return True
    except OSError:
        return False


def _format_timeout(seconds_str: str) -> str:
    try:
        s = int(seconds_str)
    except (ValueError, TypeError):
        return seconds_str
    if s < 60:
        return f"{s} s"
    if s < 3600:
        return f"{s // 60} min"
    h, rem = divmod(s, 3600)
    m = rem // 60
    return f"{h} h" if m == 0 else f"{h} h {m} min"


def extract_listener_timeout(block: str) -> str | None:
    m = re.search(r"^\s*timeout\s*=\s*(\S+)", block, flags=re.MULTILINE)
    return m.group(1) if m else None


_MAX_CMD_LEN = 48


def format_listener_label(block: str, index: int) -> str:
    timeout = extract_listener_timeout(block)
    on_timeout = re.search(r"^\s*on-timeout\s*=\s*(.+)$", block, flags=re.MULTILINE)

    parts: list[str] = [f"Listener {index}"]
    parts.append(_format_timeout(timeout) if timeout else "?")

    if on_timeout:
        cmd = on_timeout.group(1).strip()
        if cmd:
            parts.append(cmd if len(cmd) <= _MAX_CMD_LEN else cmd[: _MAX_CMD_LEN - 1] + "…")

    return "  ·  ".join(parts)


def get_listeners_timeout(blocks: list[str]) -> list[str]:
    profile_time = r"timeout\s*=\s*(\S+)"
    times = []
    for block in blocks:
        match = re.search(profile_time, block)
        if match:
            times.append(match.group(1))
    return times


def get_listeners_by_timeout(name: str) -> str | None:
    blocks = get_all_listeners()
    for block in blocks:
        match = re.search(r"timeout\s*=\s*(\S+)", block)
        if match and match.group(1) == name:
            return block
    return None


def add_listener(new_block: str) -> None:
    with open(app_config.HYPRIDLE_FILE, "a") as f:
        f.write("\n" + new_block + "\n")


def update_hypridle(old_block: str, new_block: str) -> bool:
    try:
        with open(app_config.HYPRIDLE_FILE, "r") as f:
            content = f.read()

        if old_block not in content:
            return False

        content = content.replace(old_block, new_block, 1)

        with open(app_config.HYPRIDLE_FILE, "w") as f:
            f.write(content)

        return True
    except OSError:
        return False


def remove_listener(block: str) -> bool:
    try:
        with open(app_config.HYPRIDLE_FILE, "r") as f:
            content = f.read()

        if block not in content:
            return False

        content = content.replace(block, "", 1)
        content = re.sub(r"\n{3,}", "\n\n", content)

        with open(app_config.HYPRIDLE_FILE, "w") as f:
            f.write(content)
        return True
    except OSError:
        return False


def restart_hypridle() -> bool:
    if not shutil.which("hypridle"):
        return False

    subprocess.run(["pkill", "-x", "hypridle"], capture_output=True)

    try:
        subprocess.Popen(
            ["hypridle"],
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except OSError:
        return False
