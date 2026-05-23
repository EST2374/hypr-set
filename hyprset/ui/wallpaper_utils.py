from __future__ import annotations

import os
from typing import TYPE_CHECKING, Protocol, cast

from PySide6.QtCore import QProcess, QSize, Qt
from PySide6.QtGui import QIcon, QImageReader, QPixmap
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from hyprset.config import DEFAULT_WP_PATH

from ..core.monitor import get_monitor_names

if TYPE_CHECKING:

    class _WallpaperWidget(Protocol):
        folder_label: QLabel
        choose_folder_button: QPushButton
        gallery: QListWidget
        listWidget: QListWidget
        wallpaper_page: QWidget
        wp_monitor_comboBox: QComboBox

    _Base = _WallpaperWidget
else:
    _Base = object


_THUMB_SIZE = QSize(250, 150)
_IMAGE_EXTS = (".png", ".jpg", ".jpeg")


def _load_thumbnail(path: str) -> QIcon:
    reader = QImageReader(path)
    reader.setAutoTransform(True)
    orig = reader.size()
    if orig.isValid() and not orig.isEmpty():
        scaled = orig.scaled(_THUMB_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        reader.setScaledSize(scaled)
    image = reader.read()
    if image.isNull():
        return QIcon()
    return QIcon(QPixmap.fromImage(image))


class WallpaperMixin(_Base):
    def _setup_wallpaper_tab(self):
        self._wp_loaded_path: str | None = None

        wp = str(DEFAULT_WP_PATH)
        self.setup_wallpaper_gallery()
        self.folder_label.setText(wp)
        self.choose_folder_button.clicked.connect(self.browse_wallpaper_folder)
        self.gallery.itemDoubleClicked.connect(self.apply_wallpaper)
        self.listWidget.currentItemChanged.connect(self._on_sidebar_changed_wp)
        self.wp_monitor_comboBox.addItems(get_monitor_names())

    def setup_wallpaper_gallery(self):
        self.gallery.setViewMode(QListWidget.ViewMode.IconMode)
        self.gallery.setIconSize(_THUMB_SIZE)
        self.gallery.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.gallery.setSpacing(10)
        self.gallery.setUniformItemSizes(True)

        layout = self.wallpaper_page.layout()
        if layout is not None:
            layout.addWidget(self.gallery)
        else:
            layout = QVBoxLayout(self.wallpaper_page)
            layout.addWidget(self.gallery)

    def load_images_from_path(self, wp_path: str):
        if not os.path.isdir(wp_path):
            return
        self.gallery.setUpdatesEnabled(False)
        try:
            self.gallery.clear()
            for filename in sorted(os.listdir(wp_path)):
                if not filename.lower().endswith(_IMAGE_EXTS):
                    continue
                full_path = os.path.join(wp_path, filename)
                item = QListWidgetItem(_load_thumbnail(full_path), filename)
                item.setData(Qt.ItemDataRole.UserRole, full_path)
                self.gallery.addItem(item)
        finally:
            self.gallery.setUpdatesEnabled(True)
        self._wp_loaded_path = wp_path

    def browse_wallpaper_folder(self):
        wp = str(DEFAULT_WP_PATH)
        folder_path = QFileDialog.getExistingDirectory(
            cast(QWidget, self),
            "Select Wallpaper Folder",
            wp,
            QFileDialog.Option.ShowDirsOnly,
        )
        if folder_path:
            self.load_images_from_path(folder_path)
            self.folder_label.setText(folder_path)

    def apply_wallpaper(self, item):
        full_path = item.data(Qt.ItemDataRole.UserRole) or os.path.join(
            self.folder_label.text(), item.text()
        )
        mon_name = self.wp_monitor_comboBox.currentText()
        proc = QProcess(cast(QWidget, self))
        proc.finished.connect(lambda *_: proc.deleteLater())
        proc.start("hyprctl", ["hyprpaper", "wallpaper", f"{mon_name},{full_path}"])

    def _on_sidebar_changed_wp(self):
        item = self.listWidget.currentItem()
        if item is None or item.text() != "Wallpaper":
            return
        current = self.folder_label.text() or str(DEFAULT_WP_PATH)
        if self._wp_loaded_path != current:
            self.load_images_from_path(current)
