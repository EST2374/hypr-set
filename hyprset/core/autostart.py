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


def del_autostart(window):
    current_row = window.current_autostart.currentRow()
    if current_row != -1:
        item = window.current_autostart.takeItem(current_row)
        target = f"exec-once = {item.text()}"
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()

        with open(CONFIG_FILE, "w") as f:
            for line in lines:
                if not line.strip().startswith(target):
                    f.write(line)
        del item
