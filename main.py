#!/usr/bin/env python3

import sys

from PySide6.QtWidgets import QApplication

from styles import load_stylesheet
from widget import Widget

app = QApplication(sys.argv)
app.setStyleSheet(load_stylesheet())

window = Widget()

window.show()
app.exec()
