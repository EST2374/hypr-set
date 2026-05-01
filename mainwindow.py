from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QPushButton, QStatusBar, QToolBar


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Hyprset")

        # MenuBar
        menu_bar = self.menuBar()
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Application")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_action)

        # ToolBar
        toolbar = QToolBar("My Main toolbar")
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        monitor_settings = QAction("Show Monitor Settings", self)
        monitor_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(monitor_settings)

        environment_settings = QAction("Show Environment Settings", self)
        environment_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(environment_settings)

        autostart_settings = QAction("Show Autostart Settings", self)
        autostart_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(autostart_settings)

        look_settings = QAction("Show Look Settings", self)
        look_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(look_settings)

        input_settings = QAction("Show Input Settings", self)
        input_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(input_settings)

        keybindings_settings = QAction("Show Keybindings Settings", self)
        keybindings_settings.triggered.connect(self.show_monitor_settings)
        toolbar.addAction(keybindings_settings)

    def quit_action(self):
        self.app.quit()

    def show_monitor_settings(self):
        pass

    def show_environment_settings(self):
        pass

    def show_autostart_settings(self):
        pass

    def show_look_settings(self):
        pass

    def show_input_settings(self):
        pass

    def show_keybindings_settings(self):
        pass
