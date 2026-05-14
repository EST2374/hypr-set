from PySide6.QtWidgets import QFileDialog

import hyprset.config as app_config

CONFIG_MAPPINGS = [
    {
        "setting_name": "CONFIG_FILE",
        "settings_key": "last_config_path",
        "label_attr": "current_config_path_label",
        "button_attr": "choose_config_file_button",
        "title": "Select Hyprland Config",
        "needs_full_reload": True,
    },
    {
        "setting_name": "HYPRSUNSET_FILE",
        "settings_key": "last_hyprsunset_path",
        "label_attr": "hyprsunset_file_label",
        "button_attr": "choose_hypersunset_button",
        "title": "Select Hyprsunset Config",
        "needs_full_reload": False,
    },
    {
        "setting_name": "HYPRLOCK_FILE",
        "settings_key": "last_hyprlock_path",
        "label_attr": "cur_hyprlock_file_label",
        "button_attr": "choose_hyprlock_button",
        "title": "Select Hyprlock Config",
        "needs_full_reload": False,
    },
    {
        "setting_name": "HYPRPAPER_FILE",
        "settings_key": "last_hyprpaper_path",
        "label_attr": "cur_hyprpaper_file_label",
        "button_attr": "choose_hyperpaper_file_button",
        "title": "Select Hyprpaper Config",
        "needs_full_reload": False,
    },
    {
        "setting_name": "HYPRIDLE_FILE",
        "settings_key": "last_hypridle_path",
        "label_attr": "cur_hypridle_label",
        "button_attr": "choose_hypridle_button",
        "title": "Select Hypridle Config",
        "needs_full_reload": False,
    },
]


class SettingsManager:
    def __init__(self, widget):
        from PySide6.QtCore import QSettings

        self._widget = widget
        self._qs = QSettings("HyprsetProject", "HyprsetApp")

    def load_saved_paths(self):
        for m in CONFIG_MAPPINGS:
            default = str(getattr(app_config, m["setting_name"]))
            saved = str(self._qs.value(m["settings_key"], default))

            setattr(app_config, m["setting_name"], saved)
            getattr(self._widget, m["label_attr"]).setText(saved)
            getattr(self._widget, m["button_attr"]).clicked.connect(
                lambda _, mapping=m: self.handle_browse(mapping)
            )

    def handle_browse(self, mapping):
        current = str(getattr(app_config, mapping["setting_name"]))

        file_path, _ = QFileDialog.getOpenFileName(
            self._widget,
            mapping["title"],
            current,
            "Config Files (*.conf *.lua)",
        )

        if not file_path:
            return

        setattr(app_config, mapping["setting_name"], file_path)
        self._qs.setValue(mapping["settings_key"], file_path)
        getattr(self._widget, mapping["label_attr"]).setText(file_path)

        if mapping["needs_full_reload"]:
            try:
                self._widget.reload_ui()
            except KeyError as e:
                print(f"Fehler beim Laden der UI: Key {e} nicht gefunden.")

    def get_saved(self, settings_key, fallback=""):
        return str(self._qs.value(settings_key, fallback))
