from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CONFIG_FILE = BASE_DIR / "hyprland.conf"
DEFAULT_CONFIG = BASE_DIR / "default_hyprland.conf"
REAL_CONFIG = Path.home() / ".config/hypr/hyprland.conf"
