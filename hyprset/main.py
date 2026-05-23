#!/usr/bin/env python3

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from hyprset.core.monitor import set_default_monitors_in_config
from hyprset.styles import apply_theme, load_saved_theme
from hyprset.ui.main_window import Widget


def main():
    app = QApplication(sys.argv)
    set_default_monitors_in_config()
    apply_theme(app, load_saved_theme())
    app.setWindowIcon(QIcon("assets/logo.png"))

    window = Widget()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
