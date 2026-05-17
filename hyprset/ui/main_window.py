import os
import sys
import webbrowser
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow

import hyprset.config as app_config

from ..styles import Theme, toggle_theme
from .controllers.autostart_and_env_controller import AutostartControllerMixin
from .controllers.cursor_controller import CursorControllerMixin
from .controllers.hypridle_controller import HypridleControllerMixin
from .controllers.hyprpaper_controller import HyprpaperControllerMixin
from .controllers.hyprsunset_controller import HyprsunsetControllerMixin
from .controllers.input_controller import InputControllerMixin
from .controllers.keybindings_controller import KeybindControllerMixin
from .controllers.look_controller import LookControllerMixin
from .controllers.monitor_controller import MonitorControllerMixin
from .controllers.network_controller import NetworkControllerMixin
from .controllers.window_rule_controller import WindowRuleControllerMixin
from .dialogs import Update
from .generated.ui_widget import Ui_Widget
from .settings_manager import SettingsManager
from .wallpaper_utils import WallpaperMixin

# TODO Overall
# Make it for the LUA conf (90% complete)
# Network config -> Wlan, DNS, ... / Bluetooth (Make for more securtity settings)
# Wallpaper works but memory heavy
# ?Users?
# Update better and more reliable
# Hyprland Plugin manager
# Hyprsunset usw integrate
# load custom config
# UI reload after a new config
# Statusbar and tooltips for the user
# Add Font and Cursor settings


class Widget(
    QMainWindow,
    Ui_Widget,
    LookControllerMixin,
    InputControllerMixin,
    KeybindControllerMixin,
    NetworkControllerMixin,
    AutostartControllerMixin,
    MonitorControllerMixin,
    WallpaperMixin,
    WindowRuleControllerMixin,
    HyprpaperControllerMixin,
    HyprsunsetControllerMixin,
    HypridleControllerMixin,
    CursorControllerMixin,
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Sidebar
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listWidget.currentRowChanged.connect(self._on_sidebar_changed)

        # Menu bar
        self.quit_program.triggered.connect(QApplication.quit)
        self.actionHelp.triggered.connect(self.open_help)
        self.actionRestart.triggered.connect(self.trigger_restart)

        # Theme
        self.dark_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.LIGHT)
        )
        self.light_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.DARK)
        )

        # Config Paths
        self._settings_manager = SettingsManager(self)
        self._settings_manager.load_saved_paths()

        # Init Tabs
        self._setup_monitor_tab()
        self._setup_autostart_tab()
        self._setup_look_tab()
        self._setup_input_tab()
        self._setup_keybindings_tab()
        self._setup_windowrule_tab()
        self._setup_network_tab()
        self._setup_wallpaper_tab()
        self._setup_hyprpaper_tab()
        self._setup_hyprsunset_tab()
        self._setup_hypridle_tab()
        self._setup_cursor_tab()

        # Update Button
        self.update_pushButton.clicked.connect(self.update_menu)

    # UI Relaod
    def reload_ui(self):
        self._reload_look()
        self._reload_input()
        self._reload_keybindings()
        self._reload_autostart()

    # Globals
    def open_help(self):
        webbrowser.open("https://github.com/EST2374/hypr-set")

    def trigger_restart(self):
        QApplication.quit()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def _on_sidebar_changed(self, index: int):
        if index == 2:
            self._ensure_hyprpaper_conf()

    def _ensure_hyprpaper_conf(self):
        from ..core.monitor import get_monitor_names

        path = Path(app_config.HYPRPAPER_FILE)
        if path.exists():
            return

        monitors = get_monitor_names()
        if not monitors:
            monitors = [""]

        lines = []
        for name in monitors:
            lines.append(
                f"wallpaper {{\n"
                f"    monitor  = {name}\n"
                f"    path     = \n"
                f"    fit_mode = cover\n"
                f"}}\n"
            )

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines))

    def update_menu(self):
        dialog = Update(self)
        dialog.center_on_parent()
        dialog.exec()
