# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(890, 716)
        self.actionThemes = QAction(Widget)
        self.actionThemes.setObjectName(u"actionThemes")
        self.dark_theme_button = QAction(Widget)
        self.dark_theme_button.setObjectName(u"dark_theme_button")
        self.light_theme_button = QAction(Widget)
        self.light_theme_button.setObjectName(u"light_theme_button")
        self.quit_program = QAction(Widget)
        self.quit_program.setObjectName(u"quit_program")
        self.centralwidget = QWidget(Widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Menu_settings = QTabWidget(self.centralwidget)
        self.Menu_settings.setObjectName(u"Menu_settings")
        self.Menu_settings.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu_settings.sizePolicy().hasHeightForWidth())
        self.Menu_settings.setSizePolicy(sizePolicy)
        self.Menu_settings.setMaximumSize(QSize(751, 571))
        self.monitor_tab = QWidget()
        self.monitor_tab.setObjectName(u"monitor_tab")
        self.verticalLayout_2 = QVBoxLayout(self.monitor_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.monitor_tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.monitors_box = QComboBox(self.monitor_tab)
        self.monitors_box.setObjectName(u"monitors_box")

        self.horizontalLayout.addWidget(self.monitors_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.monitor_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.resolution_box = QComboBox(self.monitor_tab)
        self.resolution_box.setObjectName(u"resolution_box")

        self.horizontalLayout_2.addWidget(self.resolution_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.monitor_tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.position_box = QComboBox(self.monitor_tab)
        self.position_box.setObjectName(u"position_box")

        self.horizontalLayout_3.addWidget(self.position_box)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.monitor_tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.scale_box = QComboBox(self.monitor_tab)
        self.scale_box.setObjectName(u"scale_box")

        self.horizontalLayout_4.addWidget(self.scale_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.apply_button = QPushButton(self.monitor_tab)
        self.apply_button.setObjectName(u"apply_button")

        self.verticalLayout_6.addWidget(self.apply_button)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.Menu_settings.addTab(self.monitor_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName(u"auto_tab")
        self.verticalLayout_5 = QVBoxLayout(self.auto_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.current_autostart = QListWidget(self.auto_tab)
        self.current_autostart.setObjectName(u"current_autostart")

        self.verticalLayout_3.addWidget(self.current_autostart)

        self.add_program_button = QPushButton(self.auto_tab)
        self.add_program_button.setObjectName(u"add_program_button")

        self.verticalLayout_3.addWidget(self.add_program_button)

        self.add_script_button = QPushButton(self.auto_tab)
        self.add_script_button.setObjectName(u"add_script_button")

        self.verticalLayout_3.addWidget(self.add_script_button)

        self.del_autostart_button = QPushButton(self.auto_tab)
        self.del_autostart_button.setObjectName(u"del_autostart_button")

        self.verticalLayout_3.addWidget(self.del_autostart_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.Menu_settings.addTab(self.auto_tab, "")
        self.env_tab = QWidget()
        self.env_tab.setObjectName(u"env_tab")
        self.verticalLayout_7 = QVBoxLayout(self.env_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.current_env = QListWidget(self.env_tab)
        self.current_env.setObjectName(u"current_env")

        self.verticalLayout_4.addWidget(self.current_env)

        self.add_env_button = QPushButton(self.env_tab)
        self.add_env_button.setObjectName(u"add_env_button")

        self.verticalLayout_4.addWidget(self.add_env_button)

        self.del_env_button = QPushButton(self.env_tab)
        self.del_env_button.setObjectName(u"del_env_button")

        self.verticalLayout_4.addWidget(self.del_env_button)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.Menu_settings.addTab(self.env_tab, "")
        self.look_tab = QWidget()
        self.look_tab.setObjectName(u"look_tab")
        self.Menu_settings.addTab(self.look_tab, "")
        self.input_tab = QWidget()
        self.input_tab.setObjectName(u"input_tab")
        self.Menu_settings.addTab(self.input_tab, "")
        self.keybinds_tab = QWidget()
        self.keybinds_tab.setObjectName(u"keybinds_tab")
        self.Menu_settings.addTab(self.keybinds_tab, "")
        self.windowrules_tab = QWidget()
        self.windowrules_tab.setObjectName(u"windowrules_tab")
        self.Menu_settings.addTab(self.windowrules_tab, "")

        self.horizontalLayout_10.addWidget(self.Menu_settings)

        Widget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Widget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 890, 19))
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menu_Application = QMenu(self.menubar)
        self.menu_Application.setObjectName(u"menu_Application")
        Widget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Widget)
        self.statusbar.setObjectName(u"statusbar")
        Widget.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menu_Application.menuAction())
        self.menuTheme.addSeparator()
        self.menuTheme.addSeparator()
        self.menuTheme.addAction(self.dark_theme_button)
        self.menuTheme.addAction(self.light_theme_button)
        self.menu_Application.addAction(self.quit_program)

        self.retranslateUi(Widget)

        self.Menu_settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hyprland Settings", None))
        self.actionThemes.setText(QCoreApplication.translate("Widget", u"Themes", None))
        self.dark_theme_button.setText(QCoreApplication.translate("Widget", u"Dark", None))
        self.light_theme_button.setText(QCoreApplication.translate("Widget", u"Light", None))
        self.quit_program.setText(QCoreApplication.translate("Widget", u"Quit", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Monitor: ", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Resolution", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Position", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Scale", None))
        self.apply_button.setText(QCoreApplication.translate("Widget", u"Apply", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.monitor_tab), QCoreApplication.translate("Widget", u"Monitor", None))
        self.add_program_button.setText(QCoreApplication.translate("Widget", u"Add Program", None))
        self.add_script_button.setText(QCoreApplication.translate("Widget", u"Add Script", None))
        self.del_autostart_button.setText(QCoreApplication.translate("Widget", u"Delete Autostart", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.auto_tab), QCoreApplication.translate("Widget", u"Autostart", None))
        self.add_env_button.setText(QCoreApplication.translate("Widget", u"Add Environment", None))
        self.del_env_button.setText(QCoreApplication.translate("Widget", u"Delete Environment", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.env_tab), QCoreApplication.translate("Widget", u"Environment", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.look_tab), QCoreApplication.translate("Widget", u"Look and Feel", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.input_tab), QCoreApplication.translate("Widget", u"Input", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.keybinds_tab), QCoreApplication.translate("Widget", u"Keybindings", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.windowrules_tab), QCoreApplication.translate("Widget", u"Window Rules", None))
        self.menuTheme.setTitle(QCoreApplication.translate("Widget", u"Themes", None))
        self.menu_Application.setTitle(QCoreApplication.translate("Widget", u"Application", None))
    # retranslateUi

