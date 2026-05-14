import re

import hyprset.config as app_config

# TODO
# Imporve the dialog
# Add Buttona and delete


def get_all_window_rules():
    with open(app_config.CONFIG_FILE_LUA, "r") as f:
        text = f.read()

    pattern = r"hl\.window_rule\(\{.*?\}\)"
    all_blocks = re.findall(pattern, text, flags=re.DOTALL)

    active_blocks = []
    for block in all_blocks:
        lines = block.splitlines()
        content_lines = [l.strip() for l in lines[1:] if l.strip()]
        if any(not l.startswith("--") for l in content_lines):
            active_blocks.append(block)

    return active_blocks


def get_window_rule_names(blocks: list[str]) -> list[str]:
    name_pattern = r'name\s*=\s*"([^"]+)"'
    names = []
    for block in blocks:
        match = re.search(name_pattern, block)
        if match:
            names.append(match.group(1))
    return names


def get_window_rule_by_name(name: str) -> str | None:
    blocks = get_all_window_rules()
    for block in blocks:
        match = re.search(r'name\s*=\s*"([^"]+)"', block)
        if match and match.group(1) == name:
            return block
    return None


def update_window_rule(old_block: str, new_block: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE_LUA, "r") as f:
            content = f.read()

        if old_block not in content:
            print("update_window_rule: old block not found")
            return False

        content = content.replace(old_block, new_block, 1)

        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            f.write(content)

        return True
    except OSError as e:
        print(f"update_window_rule: Error: {e}")
        return False
