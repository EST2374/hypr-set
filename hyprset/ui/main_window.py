import re
import webbrowser

from PySide6.QtCore import QProcess
from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QColorDialog, QMainWindow

from hyprset.config import CONFIG_FILE
from hyprset.core.keybindings import (
    get_general_keybindings,
    get_movement_keybindings,
    get_multimedia_keybindings,
    get_workspace_keybindings,
    update_keybinding,
)

from ..core.autostart import del_autostart, get_current_autostarts
from ..core.environments import del_env, get_current_env
from ..core.input import (
    follow_mouse_change,
    get_cur_follow_mouse,
    get_cur_item,
    get_kb_variants,
    write_setting_input,
)
from ..core.look import (
    change_bool_check,
    change_layout,
    get_cur_layout,
    get_cur_value,
    get_state_check,
    write_setting,
)
from ..core.monitor import (
    apply_monitor_settings,
    get_monitor_names,
    get_monitor_resolution,
)
from ..core.network import (
    build_wifi_scan_process,
    disconnect_wifi,
    parse_wifi_list,
    set_networking,
)
from ..styles import Theme, toggle_theme
from .dialogs import (
    AddEnvDialog,
    AddProgramDialog,
    AddScriptDialog,
    Connect_to_Wifi,
    EditKeybindingDialog,
    Update,
)
from .generated.ui_widget import Ui_Widget
from .toggle_switch import ToggleSwitch


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

        # TODO Overall
        # Default button
        # Set config file structure
        # Network config -> Wlan, DNS, ... / Bluetooth
        # Wallpaper (with preview ofc)
        # ?Users?
        # ?Update?
        # Keybindings improvement (delelet/add Buttons)

        # SideBar
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

        # Menu Bar
        self.quit_program.triggered.connect(QApplication.quit)
        self.actionHelp.triggered.connect(self.open_help)

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
        self.del_autostart_button.clicked.connect(self.del_selected_autostart)
        self.add_program_button.clicked.connect(self.add_new_autostart)
        self.add_script_button.clicked.connect(self.add_new_script)

        # Environment Settings
        self.current_env.addItems(get_current_env())
        self.add_env_button.clicked.connect(self.add_new_env)
        self.del_env_button.clicked.connect(self.del_selected_env)

        # Look and Feel
        LOOK_SETTINGS = {
            "gaps_in": "gaps_in_spinBox",
            "gaps_out": "gaps_out_spinBox",
            "border_size": "border_size_spinBox",
            "angle": "angle_spinBox",
            "rounding": "rounding_spin_box",
            "rounding_power": "rounding_power_spin_box",
            "active_opacity": "act_op_spin_box",
            "inactive_opacity": "inact_op_spin_box",
            "shadow_range": "shadow_range_spinbox",
            "shadow_render_power": "shadow_render_power_spinbox",
            "blur_size": "blur_size_spinBox",
            "blur_passes": "blur_passes_spinBox",
            "blur_vib": "blur_vib_doubleSpinBox",
            # TEST FOR INPUT
            "sensitivity": "mouse_sens_doubleSpinBox",
        }

        for setting, widget_attr in LOOK_SETTINGS.items():
            widget = getattr(self, widget_attr)
            widget.setValue(get_cur_value(setting))
            widget.valueChanged.connect(lambda val, s=setting: write_setting(s, val))

        self.set_color_1_button.clicked.connect(self.set_color_1)
        self.set_color_2_button.clicked.connect(self.set_color_2)
        self.shadow_color_button.clicked.connect(self.set_shadow_color)

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

        if get_state_check("blur_enable") == "true":
            self.blur_enable_checkBox.setCheckState(Qt.CheckState.Checked)
        self.blur_enable_checkBox.checkStateChanged.connect(
            lambda: change_bool_check("blur_enable")
        )
        if get_state_check("shadow_enable") == "true":
            self.shadow_enable_checkbox.setCheckState(Qt.CheckState.Checked)
        self.shadow_enable_checkbox.checkStateChanged.connect(
            lambda: change_bool_check("shadow_enable")
        )

        layouts = ["Dwindle", "Master", "Scrolling", "Monocle"]
        self.layout_comboBox.addItems(layouts)
        current = get_cur_layout()
        self.layout_comboBox.setCurrentText(current)
        self.layout_comboBox.currentTextChanged.connect(change_layout)

        # Input
        INPUT_SETTINGS = {
            "kb_layout": "kb_layout_comboBox",
            "kb_variant": "kb_variant_comboBox",
        }

        for setting_2, widget_attr_2 in INPUT_SETTINGS.items():
            widget_2 = getattr(self, widget_attr_2)
            widget_2.addItem(get_cur_item(setting_2))
            widget_2.currentTextChanged.connect(
                lambda val, s=setting_2: write_setting_input(s, val)
            )

        kb_layouts = ["us", "gb", "de", "fr", "es", "it", "br"]
        follow_mouse_options = ["Manual", "Automatic", "Semi-Automatic", "Locked"]
        self.kb_layout_comboBox.addItems(kb_layouts)
        self.kb_variant_comboBox.addItem("")
        self.kb_variant_comboBox.addItems(get_kb_variants())
        self.kb_layout_comboBox.currentTextChanged.connect(self.update_variant)
        self.follow_mouse_comboBox.addItems(follow_mouse_options)
        self.follow_mouse_comboBox.setCurrentText(get_cur_follow_mouse())
        self.follow_mouse_comboBox.currentTextChanged.connect(follow_mouse_change)
        self.mouse_sens_doubleSpinBox.setRange(-1.0, 1.0)

        # TODO
        # Sens and nat_scroll works, BUT
        # In wrong file (and glob_nat_scroll is directly below input (not quite so nice))
        if get_state_check("global_natural_scroll") == "true":
            self.mouse_natural_scroll_checkBox.setCheckState(Qt.CheckState.Checked)
        self.mouse_natural_scroll_checkBox.checkStateChanged.connect(
            lambda: change_bool_check("global_natural_scroll")
        )
        if get_state_check("natural_scroll_touchpad") == "true":
            self.touchpad_nat_scroll_checkbox.setCheckState(Qt.CheckState.Checked)
        self.touchpad_nat_scroll_checkbox.checkStateChanged.connect(
            lambda: change_bool_check("natural_scroll_touchpad")
        )

        # Keybindings
        self.general_list.addItems(get_general_keybindings())
        self.movement_list.addItems(get_movement_keybindings())
        self.workspaces_list.addItems(get_workspace_keybindings())
        self.multimedia_list.addItems(get_multimedia_keybindings())

        for list_widget in (
            self.general_list,
            self.movement_list,
            self.workspaces_list,
            self.multimedia_list,
        ):
            list_widget.itemDoubleClicked.connect(self._edit_keybinding)

        # Networking Tab
        self._networking_toggle = ToggleSwitch(self, active_color="#00b0ff")
        self._networking_toggle.setChecked(True)
        self._networking_toggle.stateChanged.connect(self._on_networking_toggled)

        self.network_layout.addWidget(self._networking_toggle)

        self._start_wifi_scan()
        self.wifi_refresh_button.clicked.connect(self._refresh_wifi)
        self.wifi_list.itemDoubleClicked.connect(self._open_wifi_connect_dialog)
        self.wifi_disconnect_button.clicked.connect(self._disconnect_selected)

        # Update Tab
        self.update_pushButton.clicked.connect(self.update_menu)

    # Help Button
    def open_help(self):
        webbrowser.open("https://github.com/EST2374/hypr-set")

    # Autostart add buttons
    def add_new_autostart(self):
        dialog = AddProgramDialog(self, on_added=self.current_autostart.addItem)
        dialog.center_on_parent()
        dialog.exec()

    def add_new_script(self):
        dialog = AddScriptDialog(self, on_added=self.current_autostart.addItem)
        dialog.center_on_parent()
        dialog.exec()

    def del_selected_autostart(self):
        current_row = self.current_autostart.currentRow()
        if current_row == -1:
            return
        item = self.current_autostart.currentItem()
        if del_autostart(item.text()):
            self.current_autostart.takeItem(current_row)

    def add_new_env(self):
        dialog = AddEnvDialog(self, on_added=self.current_env.addItem)
        dialog.center_on_parent()
        dialog.exec()

    # Environemnt
    def del_selected_env(self):
        current_row = self.current_env.currentRow()
        if current_row == -1:
            return
        item = self.current_env.currentItem()
        if del_env(item.text()):
            self.current_env.takeItem(current_row)

    # Look and Feel
    def set_color_1(self):
        self.pick_and_save_color(index=1)

    def set_color_2(self):
        self.pick_and_save_color(index=2)

    def set_shadow_color(self):
        self.pick_and_save_color(index=3)

    def pick_and_save_color(self, index):
        color = QColorDialog.getColor(
            QColor("white"),
            self,
            f"Border Color {index}",
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
                if line.strip().startswith(
                    "col.active_border"
                ) or line.strip().startswith("color"):
                    if index == 1:
                        line = re.sub(
                            r"(rgba\([0-9a-fA-F]+\))", new_rgba_string, line, count=1
                        )
                    elif index == 2:
                        pattern = r"(rgba\([0-9a-fA-F]+\)\s+)(rgba\([0-9a-fA-F]+\))"
                        line = re.sub(pattern, rf"\1{new_rgba_string}", line)

                    elif index == 3:
                        pattern = r"^\s*color\s*=.*"
                        line = re.sub(pattern, rf"\t\tcolor = {new_rgba_string}", line)

                    f.write(line)

                else:
                    f.write(line)

    # Input
    def update_variant(self):
        variants = get_kb_variants()
        self.kb_variant_comboBox.clear()
        self.kb_variant_comboBox.addItem("")
        self.kb_variant_comboBox.addItems(variants)

    # Keybindings
    def _edit_keybinding(self, item):
        dialog = EditKeybindingDialog(item.text(), parent=self)
        if dialog.exec() == EditKeybindingDialog.DialogCode.Accepted:
            new_line = dialog.get_result()
            if update_keybinding(item.text(), new_line):
                item.setText(new_line)

    # Networking
    def _start_wifi_scan(self):
        self._wifi_process = build_wifi_scan_process()
        self._wifi_process.finished.connect(self._handle_wifi_output)

    def _handle_wifi_output(self):
        process = self.sender()
        if isinstance(process, QProcess):
            raw_data = process.readAllStandardOutput().data()
            raw = bytes(raw_data).decode("utf-8")

            networks = parse_wifi_list(raw)
            self.wifi_list.clear()
            self.wifi_list.addItems(
                [f"{n['ssid']}  {n['signal']}  {n['security']}" for n in networks]
            )
            process.deleteLater()

    def _refresh_wifi(self):
        self.wifi_list.clear()
        self._start_wifi_scan()

    def connect_to_wifi(self):
        dialog = Connect_to_Wifi(ssid="", parent=self)
        dialog.center_on_parent()
        dialog.exec()

    def _open_wifi_connect_dialog(self, item):
        ssid = item.text().split("  ")[0]
        dialog = Connect_to_Wifi(ssid, parent=self)
        dialog.center_on_parent()
        dialog.exec()

    def _on_networking_toggled(self, state):
        def _done(ok):
            if not ok:
                return
            if state:
                self._start_wifi_scan()
            else:
                self.wifi_list.clear()

        set_networking(enabled=bool(state), on_done=_done)

    def _disconnect_selected(self):
        item = self.wifi_list.currentItem()
        if not item:
            return
        ssid = item.text().split("  ")[0]

        def _done(ok, msg):
            if ok:
                self._refresh_wifi()
            else:
                print(f"Disconnect failed: {msg}")

        disconnect_wifi(ssid, on_done=_done)

    def update_menu(self):
        dialog = Update(self)
        dialog.center_on_parent()
        dialog.exec()
