from hyprset.config import CONFIG_FILE


def get_current_autostarts() -> list[str]:
    all_autostart = []

    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("exec-once") and not line.startswith("#"):
                    command = line.split("=", 1)[-1].strip()
                    all_autostart.append(command)
        return all_autostart
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return all_autostart


def add_autostart(command: str) -> bool:
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if f"exec-once = {command}" in content:
            return False

        new_entry = f"exec-once = {command}\n"
        if "# Autostart end" in content:
            content = content.replace("# Autostart end", f"{new_entry}# Autostart end")
        else:
            content += new_entry

        with open(CONFIG_FILE, "w") as f:
            f.write(content)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False


def del_autostart(command: str) -> bool:
    target = f"exec-once = {command}"
    try:
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()

        new_lines = [l for l in lines if not l.strip() == target]

        if len(new_lines) == len(lines):
            return False

        with open(CONFIG_FILE, "w") as f:
            f.writelines(new_lines)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False
