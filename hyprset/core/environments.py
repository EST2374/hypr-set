from hyprset.config import CONFIG_FILE


def get_current_env() -> list[str]:
    all_env = []

    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("env") and not line.startswith("#"):
                    command = line.split("=", 1)[-1].strip()
                    all_env.append(command)
        return all_env
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return all_env


def del_env(window):
    current_row = window.current_env.currentRow()
    if current_row != -1:
        item = window.current_env.takeItem(current_row)
        target = f"env = {item.text()}"
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()

        with open(CONFIG_FILE, "w") as f:
            for line in lines:
                if not line.strip().startswith(target):
                    f.write(line)
        del item
