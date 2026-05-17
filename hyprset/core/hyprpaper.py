import re

import hyprset.config as app_config


def get_all_wallpapers():
    try:
        with open(app_config.HYPRPAPER_FILE, "r") as f:
            text = f.read()
    except FileNotFoundError:
        return []

    pattern = r"wallpaper\s*\{.*?\}"
    all_blocks = re.findall(pattern, text, flags=re.DOTALL)

    wp_blocks = []
    for block in all_blocks:
        lines = block.splitlines()
        content_lines = [line.strip() for line in lines[1:] if line.strip()]
        if any(not line.startswith("#") for line in content_lines):
            wp_blocks.append(block)
    return wp_blocks


def get_wp_names(blocks: list[str]) -> list[str]:
    name_pattern = r"path\s*=\s*(\S+)"
    names = []
    for block in blocks:
        match = re.search(name_pattern, block)
        if match:
            names.append(match.group(1))
    return names


def get_wp_by_name(name: str) -> str | None:
    blocks = get_all_wallpapers()
    for block in blocks:
        match = re.search(r"path\s*=\s*(\S+)", block)
        if match and match.group(1) == name:
            return block
    return None


def update_hyprpaper(old_block: str, new_block: str) -> bool:
    try:
        with open(app_config.HYPRPAPER_FILE, "r") as f:
            content = f.read()

        if old_block not in content:
            return False

        content = content.replace(old_block, new_block, 1)

        with open(app_config.HYPRPAPER_FILE, "w") as f:
            f.write(content)

        return True
    except OSError:
        return False
