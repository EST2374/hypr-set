#!/usr/bin/env python3

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from hyprset.styles import load_stylesheet
from hyprset.ui.main_window import Widget


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())
    app.setWindowIcon(QIcon("assets/logo.png"))

    window = Widget()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
