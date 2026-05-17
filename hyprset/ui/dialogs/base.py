from PySide6.QtWidgets import (
    QDialog,
    QWidget,
)


class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def center_on_parent(self):
        p = self.parent()
        if isinstance(p, QWidget):
            parent_geo = p.frameGeometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y)
