import re

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
