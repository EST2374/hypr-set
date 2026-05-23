from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from PySide6.QtCore import QObject, QSize, QThread, QTimer, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox, QLabel, QPushButton

from ...core.default_apps import (
    CATEGORIES,
    AppCategory,
    get_apps_for_category,
    get_default_app,
    set_default_app,
)

if TYPE_CHECKING:

    class _DefaultAppsWidgets(Protocol):
        browser_combo: QComboBox
        filemanager_combo: QComboBox
        terminal_combo: QComboBox
        editor_combo: QComboBox
        image_combo: QComboBox
        video_combo: QComboBox
        audio_combo: QComboBox
        pdf_combo: QComboBox
        browser_apply_button: QPushButton
        filemanager_apply_button: QPushButton
        terminal_apply_button: QPushButton
        editor_apply_button: QPushButton
        image_apply_button: QPushButton
        video_apply_button: QPushButton
        audio_apply_button: QPushButton
        pdf_apply_button: QPushButton
        browser_status_label: QLabel
        filemanager_status_label: QLabel
        terminal_status_label: QLabel
        editor_status_label: QLabel
        image_status_label: QLabel
        video_status_label: QLabel
        audio_status_label: QLabel
        pdf_status_label: QLabel

    _Base = _DefaultAppsWidgets
else:
    _Base = object


_WIDGET_MAP: dict[str, tuple[str, str, str]] = {
    cat.key: (
        f"{cat.key}_combo",
        f"{cat.key}_apply_button",
        f"{cat.key}_status_label",
    )
    for cat in CATEGORIES
}


class _LoadWorker(QObject):
    finished = Signal(list)

    def run(self):
        results = []
        for cat in CATEGORIES:
            current = get_default_app(cat)
            apps = get_apps_for_category(cat)
            results.append((cat, current, apps))
        self.finished.emit(results)


class DefaultAppsControllerMixin(_Base):
    def _setup_default_apps_tab(self):
        for cat in CATEGORIES:
            _, btn_name, _ = _WIDGET_MAP[cat.key]
            btn: QPushButton = getattr(self, btn_name)
            btn.clicked.connect(lambda checked=False, c=cat: self._apply_default_app(c))
            btn.setEnabled(False)

        self._default_apps_load()

    def _default_apps_load(self):
        self._da_thread = QThread(cast(QObject, self))
        self._da_worker = _LoadWorker()
        self._da_worker.moveToThread(self._da_thread)
        self._da_thread.started.connect(self._da_worker.run)
        self._da_worker.finished.connect(self._on_default_apps_loaded)
        self._da_worker.finished.connect(self._da_thread.quit)
        self._da_thread.start()

    def _on_default_apps_loaded(self, results: list):
        for cat, current_desktop, apps in results:
            combo_name, btn_name, _ = _WIDGET_MAP[cat.key]
            combo: QComboBox = getattr(self, combo_name)
            btn: QPushButton = getattr(self, btn_name)

            label_name = f"label_{combo_name}"
            label: QLabel | None = getattr(self, label_name, None)
            if label is not None:
                cat_icon = QIcon.fromTheme(cat.icon)
                if not cat_icon.isNull():
                    label.setPixmap(cat_icon.pixmap(QSize(18, 18)))
                    label.setToolTip(cat.label)

            combo.blockSignals(True)
            combo.clear()

            current_index = -1

            if not current_desktop:
                combo.addItem("— not set —", None)

            for app in apps:
                app_icon = QIcon.fromTheme(app.icon)
                if not app_icon.isNull():
                    combo.addItem(app_icon, app.name, app.desktop_file)
                else:
                    combo.addItem(app.name, app.desktop_file)
                if app.desktop_file == current_desktop:
                    current_index = combo.count() - 1

            if current_index >= 0:
                combo.setCurrentIndex(current_index)
            elif current_desktop:
                combo.insertItem(0, f"[{current_desktop}]", current_desktop)
                combo.setCurrentIndex(0)

            combo.blockSignals(False)
            btn.setEnabled(True)

    def _apply_default_app(self, cat: AppCategory):
        combo_name, btn_name, status_name = _WIDGET_MAP[cat.key]
        combo: QComboBox = getattr(self, combo_name)
        btn: QPushButton = getattr(self, btn_name)
        status: QLabel = getattr(self, status_name)

        desktop_file = combo.currentData()
        if not desktop_file:
            return

        btn.setEnabled(False)
        status.setText("…")

        ok = set_default_app(cat, desktop_file)

        if ok:
            status.setStyleSheet("color: #4caf50;")
            status.setText("✓ Applied")
        else:
            status.setStyleSheet("color: #f44336;")
            status.setText("✗ Failed")

        btn.setEnabled(True)
        QTimer.singleShot(
            3000,
            lambda: (
                status.setText(""),
                status.setStyleSheet(""),
            ),
        )
