import hyprset.config as app_config


def create_autostart_block():
    template = '\nhl.on("hyprland.start", function ()\nend)\n'
    try:
        with open(app_config.CONFIG_FILE, "a") as f:
            f.write(template)
        return True
    except OSError:
        return False


def uncomment_autostart_block() -> bool:
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            lines = f.readlines()

        in_block = False
        new_lines = []

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("--") and 'hl.on("hyprland.start"' in stripped:
                in_block = True
                new_lines.append(line.replace("-- ", "", 1).replace("--", "", 1))
                continue

            if in_block:
                if stripped.startswith("--"):
                    new_lines.append(line.replace("-- ", "", 1).replace("--", "", 1))
                else:
                    in_block = False
                    new_lines.append(line)
            else:
                new_lines.append(line)

        with open(app_config.CONFIG_FILE, "w") as f:
            f.writelines(new_lines)
        return True

    except OSError as e:
        print(f"Error writing config: {e}")
        return False


def get_current_autostarts() -> list[str]:
    all_autostart = []

    try:
        with open(app_config.CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("hl.exec_cmd") and not line.startswith("--"):
                    command = line.split("(", 1)[-1].split(")", 1)[0].strip(" \"'")
                    all_autostart.append(command)
        return all_autostart
    except FileNotFoundError:
        print(f"Error: {app_config.CONFIG_FILE} not found.")
        return all_autostart


def is_autostart_initialized() -> bool:
    search_string = 'hl.on("hyprland.start"'
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            for line in f:
                clean_line = line.strip()
                if search_string in clean_line and not clean_line.startswith("--"):
                    return True
        return False
    except FileNotFoundError:
        return False


def is_autostart_commented_out() -> bool:
    search_string = 'hl.on("hyprland.start"'
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            for line in f:
                clean_line = line.strip()
                if search_string in clean_line and clean_line.startswith("--"):
                    return True
        return False
    except FileNotFoundError:
        return False


def add_autostart(command: str) -> bool:
    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            content = f.read()

        if f"hl.exec_cmd({command})" in content:
            return False

        new_entry = f'\thl.exec_cmd("{command}")\n'
        if "end)" in content:
            content = content.replace("end)", f"{new_entry}end)")
        else:
            content += new_entry

        with open(app_config.CONFIG_FILE, "w") as f:
            f.write(content)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False


def del_autostart(command: str) -> bool:
    clean_cmd = command.strip(" \"'")

    target1 = f'hl.exec_cmd("{clean_cmd}")'
    target2 = f"hl.exec_cmd({clean_cmd})"
    targets = [target1, target2]

    try:
        with open(app_config.CONFIG_FILE, "r") as f:
            lines = f.readlines()

        new_lines = [l for l in lines if l.strip() not in targets]

        if len(new_lines) == len(lines):
            return False

        with open(app_config.CONFIG_FILE, "w") as f:
            f.writelines(new_lines)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False
