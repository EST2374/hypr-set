import os
import re
import subprocess
import sys
import webbrowser

from PySide6.QtCore import QProcess, QSettings, QSize, Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QColorDialog,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
)

import hyprset.config as app_config
from hyprset.config import DEFAULT_WP_PATH
from hyprset.core.keybindings import (
    add_keybinding,
    del_keybinding,
    get_general_keybindings,
    get_movement_keybindings,
    get_multimedia_keybindings,
    get_workspace_keybindings,
    reset_to_defaults_keybindings,
    update_keybinding,
)

from ..core.autostart import (
    create_autostart_block,
    del_autostart,
    get_current_autostarts,
    is_autostart_commented_out,
    is_autostart_initialized,
    uncomment_autostart_block,
)
from ..core.environments import del_env, get_current_env
from ..core.input import (
    follow_mouse_change,
    get_cur_follow_mouse,
    get_cur_item,
    get_kb_variants,
    write_setting_input,
)
from ..core.look import (
    BOOL_DEFAULTS,
    DEFAULTS,
    better_cur_enabled,
    better_cur_status,
    better_cur_value,
    change_angle_value,
    change_bool_lua,
    change_layout,
    get_angle,
    get_cur_layout,
    read_bool_lua,
    write_setting_lua,
)
from ..core.monitor import (
    apply_monitor_settings,
    get_cur_rotation,
    get_monitor_names,
    get_monitor_resolution,
    set_default_monitors_button,
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
    "sensitivity": "mouse_sens_doubleSpinBox",
}

INPUT_SETTINGS = {
    "kb_layout": "kb_layout_comboBox",
    "kb_variant": "kb_variant_comboBox",
}


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hyprland Settings")

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

        # SideBar
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)

        # Menu Bar
        self.quit_program.triggered.connect(QApplication.quit)
        self.actionHelp.triggered.connect(self.open_help)
        self.actionRestart.triggered.connect(self.trigger_restart)

        # Theme Switch
        self.dark_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.LIGHT)
        )
        self.light_theme_button.triggered.connect(
            lambda: toggle_theme(self, Theme.DARK)
        )

        # Config File Settings
        # TODO
        # Set the new values correct (Maybe a small mistake with main file???)
        # Config Buttons
        self.config_mappings = [
            {
                "button": self.choose_config_file_button,
                "setting_name": "CONFIG_FILE",
                "label": self.current_config_path_label,
                "title": "Select Hyprland Config",
                "needs_full_reload": True,
            },
            {
                "button": self.choose_hypersunset_button,
                "setting_name": "HYPRSUNSET_FILE",
                "label": self.hyprsunset_file_label,
                "title": "Select Hyprsunset Config",
                "needs_full_reload": False,
            },
            {
                "button": self.choose_hyprlock_button,
                "setting_name": "HYPRLOCK_FILE",
                "label": self.cur_hyprlock_file_label,
                "title": "Select Hyprlock Config",
                "needs_full_reload": False,
            },
            {
                "button": self.choose_hyperpaper_file_button,
                "setting_name": "HYPRPAPER_FILE",
                "label": self.cur_hyprpaper_file_label,
                "title": "Select Hyprpaper Config",
                "needs_full_reload": False,
            },
            {
                "button": self.choose_hypridle_button,
                "setting_name": "HYPRIDLE_FILE",
                "label": self.cur_hypridle_label,
                "title": "Select Hypridle Config",
                "needs_full_reload": False,
            },
        ]

        # TODO
        # Make less dry
        self.settings = QSettings("HyprsetProject", "HyprsetApp")
        saved_path = str(
            self.settings.value("last_config_path", str(app_config.CONFIG_FILE))
        )
        saved_path_hyprsunset = str(
            self.settings.value("last_hyprsunset_path", str(app_config.HYPRSUNSET_FILE))
        )
        saved_path_hyprlock = str(
            self.settings.value("last_hyprlock_path", str(app_config.HYPRLOCK_FILE))
        )
        saved_path_hyprpaper = str(
            self.settings.value("last_hyprpaper_path", str(app_config.HYPRPAPER_FILE))
        )
        saved_path_hypridle = str(
            self.settings.value("last_hypridle_path", str(app_config.HYPRIDLE_FILE))
        )
        app_config.CONFIG_FILE = saved_path
        app_config.HYPRSUNSET_FILE = saved_path_hyprsunset
        app_config.HYPRLOCK_FILE = saved_path_hyprlock
        app_config.HYPRPAPER_FILE = saved_path_hyprpaper
        app_config.HYPRIDLE_FILE = saved_path_hypridle
        self.current_config_path_label.setText(saved_path)
        self.hyprsunset_file_label.setText(saved_path_hyprsunset)
        self.cur_hyprlock_file_label.setText(saved_path_hyprlock)
        self.cur_hyprpaper_file_label.setText(saved_path_hyprpaper)
        self.cur_hypridle_label.setText(saved_path_hypridle)
        for item in self.config_mappings:
            item["button"].clicked.connect(lambda _, m=item: self.handle_browse(m))

        # Monitor Settings
        # TODO
        # Enable / Disable
        rotation_options = [
            "Normal",
            "90°",
            "180°",
            "270°",
            "flipped",
            "flipped + 90°",
            "flipped + 180°",
            "flipped + 270°",
        ]
        self.monitors_box.addItems(get_monitor_names())
        self.resolution_box.addItems(
            get_monitor_resolution(self.monitors_box.currentIndex())
        )
        self.mirror_comboBox.addItems(get_monitor_names())
        self.rotation_comboBox.addItems(rotation_options)
        self.position_box.addItem("auto")
        self.scale_box.addItems(["1.0", "2.0"])
        self.apply_button.clicked.connect(
            lambda: apply_monitor_settings(
                self.monitors_box.currentText(),
                self.resolution_box.currentText(),
                self.position_box.currentText(),
                self.scale_box.currentText(),
                self.mirror_comboBox.currentText(),
                self.rotation_comboBox.currentText(),
            )
        )
        self.set_default_monitor_button.clicked.connect(
            lambda: set_default_monitors_button()
        )
        self.rotation_comboBox.setCurrentText(
            get_cur_rotation(self.monitors_box.currentText())
        )

        # Autostart Settings
        self._ensure_autostart_initialized()
        self.current_autostart.addItems(get_current_autostarts())
        self.del_autostart_button.clicked.connect(self.del_selected_autostart)
        self.add_program_button.clicked.connect(self.add_new_autostart)
        self.add_script_button.clicked.connect(self.add_new_script)

        # Environment Settings
        self.current_env.addItems(get_current_env())
        self.add_env_button.clicked.connect(self.add_new_env)
        self.del_env_button.clicked.connect(self.del_selected_env)

        # Look and Feel
        for setting, widget_attr in LOOK_SETTINGS.items():
            widget = getattr(self, widget_attr)
            if setting == "angle":
                widget.setValue(get_angle())
                widget.valueChanged.connect(lambda val: change_angle_value(val))
                continue
            widget.setValue(better_cur_value(setting))
            widget.valueChanged.connect(
                lambda val, s=setting: write_setting_lua(s, val)
            )

        self.set_color_1_button.clicked.connect(self.set_color_1)
        self.set_color_2_button.clicked.connect(self.set_color_2)
        self.shadow_color_button.clicked.connect(self.set_shadow_color)

        # TODO
        # Make less dry
        if better_cur_status("resize_on_border") == "true":
            self.resize_checkbox.setCheckState(Qt.CheckState.Checked)
        self.resize_checkbox.checkStateChanged.connect(
            lambda: change_bool_lua("resize")
        )
        if better_cur_status("allow_tearing") == "true":
            self.allow_tearing_checkBox.setCheckState(Qt.CheckState.Checked)
        self.allow_tearing_checkBox.checkStateChanged.connect(
            lambda: change_bool_lua("tearing")
        )

        if better_cur_enabled("blur"):
            self.blur_enable_checkBox.setCheckState(Qt.CheckState.Checked)
        self.blur_enable_checkBox.checkStateChanged.connect(
            lambda: change_bool_lua("blur_enable")
        )
        if better_cur_enabled("shadow"):
            self.shadow_enable_checkbox.setCheckState(Qt.CheckState.Checked)
        self.shadow_enable_checkbox.checkStateChanged.connect(
            lambda: change_bool_lua("shadow_enable")
        )

        layouts = ["Dwindle", "Master", "Scrolling", "Monocle"]
        self.layout_comboBox.addItems(layouts)
        current = get_cur_layout()
        self.layout_comboBox.setCurrentText(current)
        self.layout_comboBox.currentTextChanged.connect(change_layout)
        self.set_default_look_button.clicked.connect(self._reset_look_to_defaults)

        # Input
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

        if read_bool_lua("global_natural_scroll"):
            self.mouse_natural_scroll_checkBox.setCheckState(Qt.CheckState.Checked)
        self.mouse_natural_scroll_checkBox.checkStateChanged.connect(
            lambda: change_bool_lua("global_natural_scroll")
        )
        if read_bool_lua("natural_scroll_touchpad"):
            self.touchpad_nat_scroll_checkbox.setCheckState(Qt.CheckState.Checked)
        self.touchpad_nat_scroll_checkbox.checkStateChanged.connect(
            lambda: change_bool_lua("natural_scroll_touchpad")
        )

        # Keybindings
        # TODO
        # Fix where Item gets into what list (Maybe make only general addable???)
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

        KEYBIND_ADD_MAP = {
            self.general_add_button: self.general_list,
            self.movement_add_button: self.movement_list,
            self.workspace_add_button: self.workspaces_list,
            self.multimedia_add_button: self.multimedia_list,
        }

        KEYBIND_DELETE_MAP = {
            self.delete_keybind_button: self.general_list,
            self.delete_movement_button: self.movement_list,
            self.delete_workspace_button: self.workspaces_list,
            self.delete_multimedia_button: self.multimedia_list,
        }

        for button, list_widget in KEYBIND_DELETE_MAP.items():
            button.clicked.connect(
                lambda checked=False, lw=list_widget: self.del_selected_keybinding(lw)
            )

        for button, list_widget in KEYBIND_ADD_MAP.items():
            button.clicked.connect(
                lambda checked=False, lw=list_widget: self.add_keybinding()
            )

        for set_default_keybind_button in (
            self.set_default_general_keybind_button,
            self.set_default_movement_button,
            self.set_default_workspace_button,
            self.set_default_multimedia_button,
        ):
            set_default_keybind_button.clicked.connect(self.set_default_keybinds_config)

        # Networking Tab
        # TODO
        # For different Security stuff
        self._networking_toggle = ToggleSwitch(self, active_color="#00b0ff")
        self._networking_toggle.setChecked(True)
        self._networking_toggle.stateChanged.connect(self._on_networking_toggled)

        self.network_layout.addWidget(self._networking_toggle)

        self._start_wifi_scan()
        self.wifi_refresh_button.clicked.connect(self._refresh_wifi)
        self.wifi_list.itemDoubleClicked.connect(self._open_wifi_connect_dialog)
        self.wifi_disconnect_button.clicked.connect(self._disconnect_selected)

        # Wallpaper Tab
        # TODO
        # Should Remove "old" Pictures (small error)
        # Select and apply Wallpaper (Kinda done, lil switching wallpaper bug)
        # Better Memory handling
        # Delete Wallpaper
        wp = str(DEFAULT_WP_PATH)
        self.setup_wallpaper_gallery()
        self.load_images_from_path(wp)
        self.folder_label.setText(wp)
        self.choose_folder_button.clicked.connect(self.browse_wallpaper_folder)
        self.gallery.itemDoubleClicked.connect(self.apply_wallpaper)
        self.listWidget.currentItemChanged.connect(self.deload_wps)

        # Update Tab
        self.update_pushButton.clicked.connect(self.update_menu)

    # Improve for better memory
    def deload_wps(self):
        cur_item = self.listWidget.currentItem().text()
        if cur_item != "Wallpaper":
            self.gallery.clear()

    # Update UI
    def reload_ui(self):
        # Look spinboxes
        for setting, widget_attr in LOOK_SETTINGS.items():
            widget = getattr(self, widget_attr)
            widget.blockSignals(True)
            if setting == "angle":
                widget.setValue(get_angle())
            else:
                widget.setValue(better_cur_value(setting))
            widget.blockSignals(False)

        # Bools
        if read_bool_lua("resize"):
            self.resize_checkbox.setCheckState(Qt.CheckState.Checked)
        if read_bool_lua("tearing"):
            self.allow_tearing_checkBox.setCheckState(Qt.CheckState.Checked)
        if read_bool_lua("blur_enable"):
            self.blur_enable_checkBox.setCheckState(Qt.CheckState.Checked)
        if read_bool_lua("shadow_enable"):
            self.shadow_enable_checkbox.setCheckState(Qt.CheckState.Checked)
        if read_bool_lua("global_natural_scroll"):
            self.mouse_natural_scroll_checkBox.setCheckState(Qt.CheckState.Checked)
        self.mouse_natural_scroll_checkBox.checkStateChanged.connect(
            lambda: change_bool_lua("global_natural_scroll")
        )
        if read_bool_lua("natural_scroll_touchpad"):
            self.touchpad_nat_scroll_checkbox.setCheckState(Qt.CheckState.Checked)
        self.touchpad_nat_scroll_checkbox.checkStateChanged.connect(
            lambda: change_bool_lua("natural_scroll_touchpad")
        )

        # Keybindings
        self._reload_keybinding_lists()

        # Autostart / Env
        self.current_autostart.clear()
        self.current_autostart.addItems(get_current_autostarts())
        self.current_env.clear()
        self.current_env.addItems(get_current_env())

        # Input
        self.follow_mouse_comboBox.setCurrentText(get_cur_follow_mouse())

    # Help Button
    def open_help(self):
        webbrowser.open("https://github.com/EST2374/hypr-set")

    # Config File
    def handle_browse(self, mapping):
        current_path = str(getattr(app_config, mapping["setting_name"]))

        file_path, _ = QFileDialog.getOpenFileName(
            self, mapping["title"], current_path, "Config Files (*.conf *.lua)"
        )

        if file_path:
            setattr(app_config, mapping["setting_name"], file_path)

            setting_key = mapping["setting_name"].lower().replace("_file", "")
            save_key = f"last_{setting_key}_path"

            self.settings.setValue(save_key, file_path)

            mapping["label"].setText(file_path)

            if mapping.get("needs_full_reload", True):
                try:
                    self.reload_ui()
                except KeyError as e:
                    print(f"Fehler beim Laden der UI: Key {e} nicht gefunden.")
            else:
                print(f"Pfad für {setting_key} aktualisiert.")

    # Menu buttons
    def trigger_restart(self):
        QApplication.quit()
        os.execl(sys.executable, sys.executable, *sys.argv)

    # Autostart add buttons
    def _ensure_autostart_initialized(self):
        if is_autostart_initialized():
            return
        if is_autostart_commented_out():
            uncomment_autostart_block()
        else:
            create_autostart_block()

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

        if not color.isValid():
            return

        new_hex = (
            f"{color.red():02x}{color.green():02x}{color.blue():02x}{color.alpha():02x}"
        )
        new_rgba = f"rgba({new_hex})"

        if index == 1:
            self.update_active_border(new_rgba, index=1)
        elif index == 2:
            self.update_active_border(new_rgba, index=2)
        elif index == 3:
            self.update_active_border(new_rgba, index=3)

    def update_active_border(self, new_rgba_string, index):
        try:
            with open(app_config.CONFIG_FILE_LUA, "r") as f:
                content = f.read()
        except FileNotFoundError:
            return

        if index == 1:
            # Replaces the first color
            content = re.sub(
                r'(active_border\s*=\s*\{[^}]*colors\s*=\s*\{[^"]*")([^"]+)(")',
                rf"\g<1>{new_rgba_string}\g<3>",
                content,
                count=1,
                flags=re.DOTALL,
            )
        elif index == 2:
            # Replaces the second color
            content = re.sub(
                r'(active_border\s*=\s*\{[^}]*colors\s*=\s*\{[^"]*"[^"]*",\s*")([^"]+)(")',
                rf"\g<1>{new_rgba_string}\g<3>",
                content,
                count=1,
                flags=re.DOTALL,
            )
        elif index == 3:
            # Shadow color
            match = re.match(r"rgba\(([0-9a-fA-F]{8})\)", new_rgba_string)
            if match:
                rrggbbaa = match.group(1)
                aa = rrggbbaa[6:8]
                rgb = rrggbbaa[0:6]
                lua_hex = f"0x{aa}{rgb}"
                content = re.sub(
                    r"(shadow\s*=\s*\{[^}]*color\s*=\s*)([^\s,\n]+)",
                    rf"\g<1>{lua_hex}",
                    content,
                    count=1,
                    flags=re.DOTALL,
                )

        with open(app_config.CONFIG_FILE_LUA, "w") as f:
            f.write(content)

    # TODO
    # Make it work :(
    def _reset_look_to_defaults(self):

        for setting, widget_attr in LOOK_SETTINGS.items():
            if setting in DEFAULTS:
                widget = getattr(self, widget_attr)
                widget.blockSignals(True)
                widget.setValue(DEFAULTS[setting])
                widget.blockSignals(False)

        BOOL_WIDGET_MAP = {
            "resize": self.resize_checkbox,
            "tearing": self.allow_tearing_checkBox,
            "blur_enable": self.blur_enable_checkBox,
            "shadow_enable": self.shadow_enable_checkbox,
        }
        for setting, widget in BOOL_WIDGET_MAP.items():
            widget.blockSignals(True)
            state = (
                Qt.CheckState.Checked
                if BOOL_DEFAULTS[setting] == "true"
                else Qt.CheckState.Unchecked
            )
            widget.setCheckState(state)
            widget.blockSignals(False)

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

    def add_keybinding(self):
        dialog = EditKeybindingDialog(parent=self)
        dialog.center_on_parent()
        if dialog.exec() == EditKeybindingDialog.DialogCode.Accepted:
            new_line = dialog.get_result()
            if add_keybinding(new_line):
                self._reload_keybinding_lists()

    def set_default_keybinds_config(self):
        reply = QMessageBox.question(
            self,
            "Reset to Defaults",
            "Are you sure you want to reset all keybindings to default?\nThis cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            if reset_to_defaults_keybindings():
                self._reload_keybinding_lists()

    def del_selected_keybinding(self, list_widget):
        current_row = list_widget.currentRow()
        if current_row == -1:
            return
        item = list_widget.currentItem()
        if del_keybinding(item.text()):
            list_widget.takeItem(current_row)

    def _reload_keybinding_lists(self):
        self.general_list.clear()
        self.movement_list.clear()
        self.workspaces_list.clear()
        self.multimedia_list.clear()
        self.general_list.addItems(get_general_keybindings())
        self.movement_list.addItems(get_movement_keybindings())
        self.workspaces_list.addItems(get_workspace_keybindings())
        self.multimedia_list.addItems(get_multimedia_keybindings())

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

    # Wallpaper
    def setup_wallpaper_gallery(self):
        self.gallery.setViewMode(QListWidget.ViewMode.IconMode)
        self.gallery.setIconSize(QSize(250, 150))
        self.gallery.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.gallery.setSpacing(10)

        layout = self.wallpaper_page.layout()
        if layout is not None:
            layout.addWidget(self.gallery)
        else:
            layout = QVBoxLayout(self.wallpaper_page)
            layout.addWidget(self.gallery)

    def load_images_from_path(self, wp_path: str):
        if os.path.exists(wp_path):
            for filename in os.listdir(wp_path):
                if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    full_path = os.path.join(wp_path, filename)
                    item = QListWidgetItem(QIcon(full_path), filename)
                    item.setData(Qt.ItemDataRole.UserRole, full_path)
                    self.gallery.addItem(item)

    def browse_wallpaper_folder(self):
        wp = str(DEFAULT_WP_PATH)
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Wallpaper Folder",
            wp,
            QFileDialog.Option.ShowDirsOnly,
        )

        if folder_path:
            self.load_images_from_path(folder_path)
            self.folder_label.setText(folder_path)

    def apply_wallpaper(self, item):
        try:
            full_path = f"{self.folder_label.text()}/{item.text()}"
            subprocess.run(
                ["hyprctl", "hyprpaper", "wallpaper", f",{full_path}"],
                capture_output=True,
                text=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return None
