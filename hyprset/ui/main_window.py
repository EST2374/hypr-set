import os
import sys
import webbrowser

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication, QMainWindow

import hyprset.config as app_config

from ..styles import Theme, toggle_theme
from .controllers.autostart_and_env_controller import AutostartControllerMixin
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
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Sidebar
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

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

    def update_menu(self):
        from .dialogs import Update

        dialog = Update(self)
        dialog.center_on_parent()
        dialog.exec()
