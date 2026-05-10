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


def add_env(command: str) -> bool:
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if f"env = {command}" in content:
            return False

        new_entry = f"env = {command}\n"
        if "# Envirnonment end" in content:
            content = content.replace(
                "# Envirnonment end", f"{new_entry}# Envirnonment end"
            )
        else:
            content += new_entry

        with open(CONFIG_FILE, "w") as f:
            f.write(content)
        return True
    except OSError as e:
        print(f"Error writing config: {e}")
        return False


def del_env(entry: str) -> bool:
    target = f"env = {entry}"
    try:
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()
        with open(CONFIG_FILE, "w") as f:
            for line in lines:
                if not line.strip().startswith(target):
                    f.write(line)
        return True
    except Exception:
        return False
