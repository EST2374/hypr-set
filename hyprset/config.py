from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CONFIG_FILE = BASE_DIR / "examples/hyprland.conf"
CONFIG_FILE_LUA = Path.home() / ".config/hypr/hyprland.lua"
HYPRSUNSET_FILE = Path.home() / ".config/hypr/hyprsunset.conf"
HYPRLOCK_FILE = Path.home() / ".config/hypr/hyprlock.conf"
HYPRPAPER_FILE = Path.home() / ".config/hypr/hyprpaper.conf"
HYPRIDLE_FILE = Path.home() / ".config/hypr/hypridle.conf"
DEFAULT_CONFIG = BASE_DIR / "examples/default_hyprland.conf"
REAL_CONFIG = Path.home() / ".config/hypr/hyprland.conf"
DEFAULT_WP_PATH = Path.home() / "Pictures"
