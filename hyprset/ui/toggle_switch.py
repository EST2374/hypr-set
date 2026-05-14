from PySide6.QtCore import (
    Property,
    QEasingCurve,
    QPropertyAnimation,
    QSize,
    Qt,
)
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QCheckBox


class ToggleSwitch(QCheckBox):
    def __init__(
        self,
        parent=None,
        width: int = 60,
        bg_color: str = "#777",
        active_color: str = "#00b0ff",
        circle_color: str = "#fff",
        animation_curve: QEasingCurve.Type = QEasingCurve.Type.OutBounce,
    ):
        super().__init__(parent)
        self.setFixedSize(width, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._bg_color = bg_color
        self._active_color = active_color
        self._circle_color = circle_color

        self._circle_pos = 3

        self._animation = QPropertyAnimation(self, b"circle_pos", self)
        self._animation.setEasingCurve(animation_curve)
        self._animation.setDuration(300)

        self.stateChanged.connect(self._start_animation)

    def _get_circle_pos(self):
        return self._circle_pos

    def _set_circle_pos(self, pos):
        self._circle_pos = pos
        self.update()

    circle_pos = Property(int, _get_circle_pos, _set_circle_pos)

    def _start_animation(self, state):
        self._animation.stop()
        end = self.width() - 26 if state else 3
        self._animation.setStartValue(self._circle_pos)
        self._animation.setEndValue(end)
        self._animation.start()

    def sizeHint(self):
        return QSize(60, 28)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        p.setPen(Qt.PenStyle.NoPen)

        track_color = QColor(self._active_color if self.isChecked() else self._bg_color)
        p.setBrush(track_color)
        p.drawRoundedRect(0, 0, self.width(), self.height(), 14, 14)

        p.setBrush(QColor(self._circle_color))
        p.drawEllipse(self._circle_pos, 3, 22, 22)

        p.end()
