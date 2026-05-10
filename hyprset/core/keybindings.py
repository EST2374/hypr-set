import re

from hyprset.config import CONFIG_FILE


def get_keybindings_in_section(section_begin: str, section_end: str) -> list[str]:
    result = []
    inside = False

    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                stripped = line.strip()

                if stripped == section_begin:
                    inside = True
                    continue

                if stripped == section_end:
                    inside = False
                    continue

                if (
                    inside
                    and stripped.startswith("bind")
                    and not stripped.startswith("#")
                ):
                    clean = re.sub(r"\s+#.*$", "", stripped)
                    result.append(clean)

            return result

    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found.")
        return result


def get_general_keybindings() -> list[str]:
    return get_keybindings_in_section("# Keybindings begin", "# Keybindings end")


def get_movement_keybindings() -> list[str]:
    return get_keybindings_in_section("# keymove begin", "# keymove end")


def get_workspace_keybindings() -> list[str]:
    return get_keybindings_in_section("# keyworkspace begin", "# keyworkspace end")


def get_multimedia_keybindings() -> list[str]:
    return get_keybindings_in_section("# keymultimedia begin", "# keymultimedia end")


def update_keybinding(old_line: str, new_line: str) -> bool:
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()

        if old_line not in content:
            return False

        with open(CONFIG_FILE, "w") as f:
            f.write(content.replace(old_line, new_line, 1))

        return True
    except OSError as e:
        print(f"Error: {e}")
        return False
