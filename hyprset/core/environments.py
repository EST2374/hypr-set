import re

import hyprset.config as app_config


def get_current_env() -> list[str]:
    all_env = []

    try:
        with open(app_config.CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("hl.env") and not line.startswith("--"):
                    inner = line.split("(", 1)[-1].split(")", 1)[0]
                    parts = re.findall(r'"([^"]*)"', inner)
                    if parts:
                        all_env.append(", ".join(f'"{p}"' for p in parts))
        return all_env
    except FileNotFoundError:
        print(f"Error: {app_config.CONFIG_FILE} not found.")
        return all_env


def add_env(command: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            content = f.read()

        entry_inner = command
        new_entry = f"hl.env({entry_inner})\n"

        if f"hl.env({entry_inner})" in content:
            return False

        pattern = r"(.*hl\.env\(.*\)\s*\n)(?![\s\S]*hl\.env)"
        match = re.search(pattern, content)
        if match:
            content = re.sub(pattern, r"\1" + new_entry, content)
        else:
            content += "\n" + new_entry

        with open(app_config.CONFIG_FILE, "w") as f:
            f.write(content)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False


def del_env(entry: str) -> bool:
    entry_normalized = re.sub(r"\s*,\s*", ",", entry)
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            lines = f.readlines()
        with open(app_config.CONFIG_FILE, "w") as f:
            for line in lines:
                inner = re.search(r"hl\.env\((.+)\)", line.strip())
                if inner:
                    inner_normalized = re.sub(r"\s*,\s*", ",", inner.group(1))
                    if inner_normalized == entry_normalized:
                        continue
                f.write(line)
        return True
    except Exception:
        return False
