#!/usr/bin/env python3

import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow
from styles import load_stylesheet

app = QApplication(sys.argv)
app.setStyleSheet(load_stylesheet())

window = MainWindow(app)

window.show()
app.exec()
