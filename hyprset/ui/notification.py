import subprocess


def hyprland_notification(message: str):
    try:
        subprocess.run(
            ["hyprctl", "notify", "2", "5000", "0", f"{message}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None
