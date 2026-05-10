import re

from hyprset.config import CONFIG_FILE


def replace_in_config(pattern: str, new_line: str):
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    new_content = re.sub(pattern, new_line, content, flags=re.MULTILINE)
    with open(CONFIG_FILE, "w") as f:
        f.write(new_content)
