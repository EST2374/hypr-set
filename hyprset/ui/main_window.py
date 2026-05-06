import re

from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QColorDialog, QMainWindow

from hyprset.config import CONFIG_FILE, REAL_CONFIG

from ..core.autostart import del_autostart, get_current_autostarts
from ..core.environments import del_env, get_current_env
from ..core.look import (
    change_bool_check,
    change_layout,
    get_cur_layout,
    get_cur_value,
    get_state_check,
    set_gabs_in_box,
)
from ..core.monitor import (
    apply_monitor_settings,
    get_monitor_names,
    get_monitor_resolution,
)
from ..styles import Theme, toggle_theme
from .dialogs import AddEnvDialog, AddProgramDialog, AddScriptDialog
from .generated.ui_widget import Ui_Widget


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # Menu Bar
        # Set config file structure
        self.quit_program.triggered.connect(QApplication.quit)

        # Theme Switch
        self.dark_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.LIGHT)
        )
        self.light_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.DARK)
        )

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

        # Look and Feel
        self.gabs_in_spinBox.setValue(get_cur_value("gaps_in"))
        self.gaps_out_spinBox.setValue(get_cur_value("gaps_out"))
        self.border_size_spinBox.setValue(get_cur_value("border_size"))
        self.angle_spinBox.setValue(get_cur_value("angle"))
        self.gabs_in_spinBox.valueChanged.connect(
            lambda: set_gabs_in_box(self, "gaps_in")
        )
        self.gaps_out_spinBox.valueChanged.connect(
            lambda: set_gabs_in_box(self, "gaps_out")
        )
        self.border_size_spinBox.valueChanged.connect(
            lambda: set_gabs_in_box(self, "border_size")
        )
        self.angle_spinBox.valueChanged.connect(lambda: set_gabs_in_box(self, "angle"))
        self.set_color_1_button.clicked.connect(self.set_color_1)
        self.set_color_2_button.clicked.connect(self.set_color_2)
        if get_state_check("resize") == "true":
            self.resize_checkbox.setCheckState(Qt.CheckState.Checked)
        self.resize_checkbox.checkStateChanged.connect(
            lambda: change_bool_check("resize")
        )
        if get_state_check("tearing") == "true":
            self.allow_tearing_checkBox.setCheckState(Qt.CheckState.Checked)
        self.allow_tearing_checkBox.checkStateChanged.connect(
            lambda: change_bool_check("tearing")
        )
        layouts = ["Dwindle", "Master", "Scrolling", "Monocle"]
        self.layout_comboBox.addItems(layouts)
        current = get_cur_layout()
        self.layout_comboBox.setCurrentText(current)
        self.layout_comboBox.currentTextChanged.connect(lambda: change_layout(self))

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

    # Look and Feel
    def set_color_1(self):
        self.pick_and_save_color(index=1)

    def set_color_2(self):
        self.pick_and_save_color(index=2)

    def pick_and_save_color(self, index):
        color = QColorDialog.getColor(
            QColor("white"),
            self,
            f"Border Color {index} wählen",
            QColorDialog.ColorDialogOption.ShowAlphaChannel,
        )

        if color.isValid():
            new_hex = color.name().lstrip("#")
            new_rgba = f"rgba({new_hex}ee)"
            self.update_active_border(new_rgba, index)

    def update_active_border(self, new_rgba_string, index):
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()

        with open(CONFIG_FILE, "w") as f:
            for line in lines:
                if line.strip().startswith("col.active_border"):
                    if index == 1:
                        line = re.sub(
                            r"(rgba\([0-9a-fA-F]+\))", new_rgba_string, line, count=1
                        )
                    elif index == 2:
                        pattern = r"(rgba\([0-9a-fA-F]+\)\s+)(rgba\([0-9a-fA-F]+\))"
                        line = re.sub(pattern, rf"\1{new_rgba_string}", line)

                    f.write(line)
                else:
                    f.write(line)
