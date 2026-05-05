from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from ..core.autostart import del_autostart, get_current_autostarts
from ..core.environments import del_env, get_current_env
from ..core.monitor import (
    apply_monitor_settings,
    get_monitor_names,
    get_monitor_resolution,
)
from .dialogs import AddEnvDialog, AddProgramDialog, AddScriptDialog
from .generated.ui_widget import Ui_Widget


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Menu Bar
        # TODO
        # Theme Switch
        # Refresh Button
        self.quit_program.triggered.connect(QApplication.quit)

        # Monitor Settings
        self.monitors_box.addItems(get_monitor_names())
        self.resolution_box.addItems(
            get_monitor_resolution(self.monitors_box.currentIndex())
        )
        self.position_box.addItem("auto")
        self.scale_box.addItems(["1.0", "2.0"])
        self.apply_button.clicked.connect(
            lambda: apply_monitor_settings(
                self.monitors_box.currentText(),
                self.resolution_box.currentText(),
                self.position_box.currentText(),
                self.scale_box.currentText(),
            )
        )

        # Autostart Settings
        self.current_autostart.addItems(get_current_autostarts())
        self.del_autostart_button.clicked.connect(lambda: del_autostart(self))
        self.add_program_button.clicked.connect(self.add_new_autostart)
        self.add_script_button.clicked.connect(self.add_new_script)

        # Environment Settings
        self.current_env.addItems(get_current_env())
        self.add_env_button.clicked.connect(self.add_new_env)
        self.del_env_button.clicked.connect(lambda: del_env(self))

    # Autostart add buttons
    def add_new_autostart(self):
        dialog = AddProgramDialog(self)
        dialog.center_on_parent()
        dialog.exec()

    def add_new_script(self):
        dialog = AddScriptDialog(self)
        dialog.center_on_parent()
        dialog.exec()

    def add_new_env(self):
        dialog = AddEnvDialog(self)
        dialog.center_on_parent()
        dialog.exec()
