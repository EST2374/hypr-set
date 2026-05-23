import re
import shutil
import subprocess

import hyprset.config as app_config


def get_all_profiles():
    try:
        with open(app_config.HYPRSUNSET_FILE, "r") as f:
            text = f.read()
    except FileNotFoundError:
        return []

    pattern = r"profile\s*\{.*?\}"
    all_blocks = re.findall(pattern, text, flags=re.DOTALL)

    profile_blocks = []
    for block in all_blocks:
        lines = block.splitlines()
        content_lines = [line.strip() for line in lines[1:] if line.strip()]
        if any(not line.startswith("#") for line in content_lines):
            profile_blocks.append(block)
    return profile_blocks


def get_profiles_time(blocks: list[str]) -> list[str]:
    profile_time = r"time\s*=\s*(\S+)"
    times = []
    for block in blocks:
        match = re.search(profile_time, block)
        if match:
            times.append(match.group(1))
    return times


def get_profile_by_time(name: str) -> str | None:
    blocks = get_all_profiles()
    for block in blocks:
        match = re.search(r"time\s*=\s*(\S+)", block)
        if match and match.group(1) == name:
            return block
    return None


def add_profile(new_block: str) -> None:
    with open(app_config.HYPRSUNSET_FILE, "a") as f:
        f.write("\n" + new_block + "\n")


def update_hyprsunset(old_block: str, new_block: str) -> bool:
    try:
        with open(app_config.HYPRSUNSET_FILE, "r") as f:
            content = f.read()

        if old_block not in content:
            return False

        content = content.replace(old_block, new_block, 1)

        with open(app_config.HYPRSUNSET_FILE, "w") as f:
            f.write(content)

        return True
    except OSError:
        return False


def remove_profile(block: str) -> bool:
    try:
        with open(app_config.HYPRSUNSET_FILE, "r") as f:
            content = f.read()

        if block not in content:
            return False

        content = content.replace(block, "", 1)
        content = re.sub(r"\n{3,}", "\n\n", content)

        with open(app_config.HYPRSUNSET_FILE, "w") as f:
            f.write(content)
        return True
    except OSError:
        return False


def restart_hyprsunset() -> bool:
    if not shutil.which("hyprsunset"):
        return False

    subprocess.run(["pkill", "-x", "hyprsunset"], capture_output=True)

    try:
        subprocess.Popen(
            ["hyprsunset"],
            start_new_session=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except OSError:
        return False


def extract_profile_time(block: str) -> str | None:
    m = re.search(r"^\s*time\s*=\s*(\S+)", block, flags=re.MULTILINE)
    return m.group(1) if m else None


def format_profile_label(block: str, index: int) -> str:
    time_v = extract_profile_time(block)
    temp = re.search(r"^\s*temperature\s*=\s*(\S+)", block, flags=re.MULTILINE)
    identity = re.search(r"^\s*identity\s*=\s*(\S+)", block, flags=re.MULTILINE)

    parts: list[str] = [f"Profile {index}", time_v if time_v else "?"]

    if temp:
        parts.append(f"{temp.group(1)} K")
    elif identity and identity.group(1).strip().lower() == "true":
        parts.append("identity")

    return "  ·  ".join(parts)
