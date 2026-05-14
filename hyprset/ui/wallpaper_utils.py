from __future__ import annotations

import os
import subprocess
from typing import TYPE_CHECKING, Protocol

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QListWidget

    class _WallpaperWidget(Protocol):
        folder_label: QLabel
        choose_folder_button: QPushButton
        gallery: QListWidget
        listWidget: QListWidget
        wallpaper_page: QWidget

    _Base = _WallpaperWidget
else:
    _Base = object


from hyprset.config import DEFAULT_WP_PATH


class WallpaperMixin(_Base):
    def _setup_wallpaper_tab(self):
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

    # Improve for better memory
    def deload_wps(self):
        cur_item = self.listWidget.currentItem().text()
        if cur_item != "Wallpaper":
            self.gallery.clear()
