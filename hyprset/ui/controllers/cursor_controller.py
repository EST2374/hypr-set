from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from ...core.cursor import get_all_cursors, select_cursor

if TYPE_CHECKING:
    from PySide6.QtWidgets import (
        QFrame,
        QGridLayout,
        QLabel,
        QListWidget,
        QListWidgetItem,
        QPushButton,
    )

    class _Cursors__Widgets(Protocol):
        cursor_listWidget: QListWidget
        set_default_cursor_button: QPushButton
        select_cursor_button: QPushButton
        browse_cursor_button: QPushButton
        cursor_theme_name_label: QLabel
        cursor_preview_frame: QFrame
        cursor_grid_layout: QGridLayout

    _Base = _Cursors__Widgets
else:
    _Base = object


_PREVIEW_CURSORS: list[tuple[list[str], str]] = [
    (["left_ptr", "default", "arrow"], "Default"),
    (["hand2", "hand1", "pointer", "pointing_hand"], "Pointer"),
    (["xterm", "text", "ibeam"], "Text"),
    (["move", "fleur", "all-scroll"], "Move"),
    (["sb_h_double_arrow", "ew-resize", "col-resize", "h_double_arrow"], "H-Resize"),
    (["crossed_circle", "forbidden", "no-drop", "dnd_no_drop"], "No-Drop"),
]


def _extract_cursor_svg(theme_dir: Path, names: list[str]) -> str | None:
    hyprcursors = theme_dir / "hyprcursors"
    for name in names:
        hlc = hyprcursors / f"{name}.hlc"
        if not hlc.exists():
            continue
        try:
            with zipfile.ZipFile(hlc) as z:
                svgs = sorted(n for n in z.namelist() if n.endswith(".svg"))
                if not svgs:
                    continue
                data = z.read(svgs[0])
                tmp = tempfile.NamedTemporaryFile(
                    suffix=".svg", delete=False, prefix=f"hyprset_{name}_"
                )
                tmp.write(data)
                tmp.close()
                return tmp.name
        except Exception:
            continue
    return None


def _svg_to_pixmap(svg_path: str, size: int):
    from PySide6.QtCore import QSize
    from PySide6.QtGui import QPainter, QPixmap
    from PySide6.QtSvg import QSvgRenderer

    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(QSize(size, size))
    pixmap.fill(
        __import__("PySide6.QtCore", fromlist=["Qt"]).Qt.GlobalColor.transparent
    )
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    return pixmap


class CursorControllerMixin(_Base):
    def _setup_cursor_tab(self):
        self.cursor_listWidget.addItems(get_all_cursors())
        self.cursor_listWidget.itemDoubleClicked.connect(self._select_cursor)
        self.cursor_listWidget.currentTextChanged.connect(self._update_cursor_preview)
        self.select_cursor_button.clicked.connect(
            lambda: self._select_cursor(self.cursor_listWidget.currentItem())
        )

    def _select_cursor(self, item: QListWidgetItem):
        select_cursor(item.text())

    def _update_cursor_preview(self, theme_name: str):
        from PySide6.QtCore import Qt
        from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

        layout = self.cursor_grid_layout
        while (child := layout.takeAt(0)) is not None:
            if widget := child.widget():
                widget.deleteLater()

        self.cursor_theme_name_label.setText(theme_name)

        theme_dir = Path.home() / ".local/share/icons" / theme_name
        if not theme_dir.exists():
            theme_dir = Path("/usr/share/icons") / theme_name

        for idx, (aliases, label_text) in enumerate(_PREVIEW_CURSORS):
            row, col = divmod(idx, 2)

            svg_path = _extract_cursor_svg(theme_dir, aliases)

            name_label = QLabel(label_text)
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_label.setStyleSheet("font-size: 10px; color: #888;")

            icon = QLabel()
            icon.setFixedSize(48, 48)
            icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

            if svg_path:
                try:
                    pixmap = _svg_to_pixmap(svg_path, 48)
                    icon.setPixmap(pixmap)
                    icon.setToolTip(aliases[0])
                except Exception:
                    icon.setText("?")
                    icon.setStyleSheet("color: #555; font-size: 20px;")
            else:
                icon.setText("?")
                icon.setStyleSheet("color: #555; font-size: 20px;")
                icon.setToolTip(f"{aliases[0]} (not found)")

            cell = QWidget()
            cell_vl = QVBoxLayout(cell)
            cell_vl.setSpacing(2)
            cell_vl.setContentsMargins(4, 4, 4, 4)
            cell_vl.addWidget(icon, alignment=Qt.AlignmentFlag.AlignCenter)
            cell_vl.addWidget(name_label)

            layout.addWidget(cell, row, col)
