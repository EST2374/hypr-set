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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(976, 733)
        self.actionThemes = QAction(Widget)
        self.actionThemes.setObjectName(u"actionThemes")
        self.dark_theme_button = QAction(Widget)
        self.dark_theme_button.setObjectName(u"dark_theme_button")
        self.light_theme_button = QAction(Widget)
        self.light_theme_button.setObjectName(u"light_theme_button")
        self.quit_program = QAction(Widget)
        self.quit_program.setObjectName(u"quit_program")
        self.actionRefresh = QAction(Widget)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionHelp = QAction(Widget)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(Widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Settings_Menu = QTabWidget(self.centralwidget)
        self.Settings_Menu.setObjectName(u"Settings_Menu")
        self.Settings_Menu.setTabPosition(QTabWidget.TabPosition.West)
        self.Settings_Menu.setTabShape(QTabWidget.TabShape.Rounded)
        self.Settings_Menu.setDocumentMode(False)
        self.hyprland_tab = QWidget()
        self.hyprland_tab.setObjectName(u"hyprland_tab")
        self.horizontalLayout_14 = QHBoxLayout(self.hyprland_tab)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Hyprland_Menu_Settings = QTabWidget(self.hyprland_tab)
        self.Hyprland_Menu_Settings.setObjectName(u"Hyprland_Menu_Settings")
        self.Hyprland_Menu_Settings.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hyprland_Menu_Settings.sizePolicy().hasHeightForWidth())
        self.Hyprland_Menu_Settings.setSizePolicy(sizePolicy)
        self.monitor_tab = QWidget()
        self.monitor_tab.setObjectName(u"monitor_tab")
        self.verticalLayout_2 = QVBoxLayout(self.monitor_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.monitor_tab_layout = QVBoxLayout()
        self.monitor_tab_layout.setObjectName(u"monitor_tab_layout")
        self.monitor_settings_layout = QVBoxLayout()
        self.monitor_settings_layout.setObjectName(u"monitor_settings_layout")
        self.monitor_name_layout = QHBoxLayout()
        self.monitor_name_layout.setObjectName(u"monitor_name_layout")
        self.monitor_name_label = QLabel(self.monitor_tab)
        self.monitor_name_label.setObjectName(u"monitor_name_label")

        self.monitor_name_layout.addWidget(self.monitor_name_label)

        self.monitors_box = QComboBox(self.monitor_tab)
        self.monitors_box.setObjectName(u"monitors_box")

        self.monitor_name_layout.addWidget(self.monitors_box)


        self.monitor_settings_layout.addLayout(self.monitor_name_layout)

        self.monitor_res_layout = QHBoxLayout()
        self.monitor_res_layout.setObjectName(u"monitor_res_layout")
        self.monitor_res_label = QLabel(self.monitor_tab)
        self.monitor_res_label.setObjectName(u"monitor_res_label")

        self.monitor_res_layout.addWidget(self.monitor_res_label)

        self.resolution_box = QComboBox(self.monitor_tab)
        self.resolution_box.setObjectName(u"resolution_box")

        self.monitor_res_layout.addWidget(self.resolution_box)


        self.monitor_settings_layout.addLayout(self.monitor_res_layout)

        self.monitor_pos_layout = QHBoxLayout()
        self.monitor_pos_layout.setObjectName(u"monitor_pos_layout")
        self.monitor_pos_label = QLabel(self.monitor_tab)
        self.monitor_pos_label.setObjectName(u"monitor_pos_label")

        self.monitor_pos_layout.addWidget(self.monitor_pos_label)

        self.position_box = QComboBox(self.monitor_tab)
        self.position_box.setObjectName(u"position_box")

        self.monitor_pos_layout.addWidget(self.position_box)


        self.monitor_settings_layout.addLayout(self.monitor_pos_layout)

        self.monitor_scale_layout = QHBoxLayout()
        self.monitor_scale_layout.setObjectName(u"monitor_scale_layout")
        self.monitor_scale_label = QLabel(self.monitor_tab)
        self.monitor_scale_label.setObjectName(u"monitor_scale_label")

        self.monitor_scale_layout.addWidget(self.monitor_scale_label)

        self.scale_box = QComboBox(self.monitor_tab)
        self.scale_box.setObjectName(u"scale_box")

        self.monitor_scale_layout.addWidget(self.scale_box)


        self.monitor_settings_layout.addLayout(self.monitor_scale_layout)


        self.monitor_tab_layout.addLayout(self.monitor_settings_layout)

        self.apply_button = QPushButton(self.monitor_tab)
        self.apply_button.setObjectName(u"apply_button")

        self.monitor_tab_layout.addWidget(self.apply_button)


        self.verticalLayout_2.addLayout(self.monitor_tab_layout)

        self.Hyprland_Menu_Settings.addTab(self.monitor_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName(u"auto_tab")
        self.verticalLayout_5 = QVBoxLayout(self.auto_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.auto_hyprland_layout = QHBoxLayout()
        self.auto_hyprland_layout.setObjectName(u"auto_hyprland_layout")
        self.auto_hyprland_layout_2 = QVBoxLayout()
        self.auto_hyprland_layout_2.setObjectName(u"auto_hyprland_layout_2")
        self.current_autostart = QListWidget(self.auto_tab)
        self.current_autostart.setObjectName(u"current_autostart")

        self.auto_hyprland_layout_2.addWidget(self.current_autostart)

        self.add_program_button = QPushButton(self.auto_tab)
        self.add_program_button.setObjectName(u"add_program_button")

        self.auto_hyprland_layout_2.addWidget(self.add_program_button)

        self.add_script_button = QPushButton(self.auto_tab)
        self.add_script_button.setObjectName(u"add_script_button")

        self.auto_hyprland_layout_2.addWidget(self.add_script_button)

        self.del_autostart_button = QPushButton(self.auto_tab)
        self.del_autostart_button.setObjectName(u"del_autostart_button")

        self.auto_hyprland_layout_2.addWidget(self.del_autostart_button)


        self.auto_hyprland_layout.addLayout(self.auto_hyprland_layout_2)


        self.verticalLayout_5.addLayout(self.auto_hyprland_layout)

        self.Hyprland_Menu_Settings.addTab(self.auto_tab, "")
        self.env_tab = QWidget()
        self.env_tab.setObjectName(u"env_tab")
        self.verticalLayout_7 = QVBoxLayout(self.env_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.env_hyprland_layout = QVBoxLayout()
        self.env_hyprland_layout.setObjectName(u"env_hyprland_layout")
        self.current_env = QListWidget(self.env_tab)
        self.current_env.setObjectName(u"current_env")

        self.env_hyprland_layout.addWidget(self.current_env)

        self.add_env_button = QPushButton(self.env_tab)
        self.add_env_button.setObjectName(u"add_env_button")

        self.env_hyprland_layout.addWidget(self.add_env_button)

        self.del_env_button = QPushButton(self.env_tab)
        self.del_env_button.setObjectName(u"del_env_button")

        self.env_hyprland_layout.addWidget(self.del_env_button)


        self.verticalLayout_7.addLayout(self.env_hyprland_layout)

        self.Hyprland_Menu_Settings.addTab(self.env_tab, "")
        self.look_tab = QWidget()
        self.look_tab.setObjectName(u"look_tab")
        self.layoutWidget = QWidget(self.look_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 60, 311, 411))
        self.general_look_layout = QVBoxLayout(self.layoutWidget)
        self.general_look_layout.setObjectName(u"general_look_layout")
        self.general_look_layout.setContentsMargins(0, 0, 0, 0)
        self.gaps_in_layout = QHBoxLayout()
        self.gaps_in_layout.setObjectName(u"gaps_in_layout")
        self.gaps_in_label = QLabel(self.layoutWidget)
        self.gaps_in_label.setObjectName(u"gaps_in_label")

        self.gaps_in_layout.addWidget(self.gaps_in_label)

        self.gabs_in_spinBox = QSpinBox(self.layoutWidget)
        self.gabs_in_spinBox.setObjectName(u"gabs_in_spinBox")

        self.gaps_in_layout.addWidget(self.gabs_in_spinBox)


        self.general_look_layout.addLayout(self.gaps_in_layout)

        self.gaps_out_layout = QHBoxLayout()
        self.gaps_out_layout.setObjectName(u"gaps_out_layout")
        self.gaps_out_layout_2 = QLabel(self.layoutWidget)
        self.gaps_out_layout_2.setObjectName(u"gaps_out_layout_2")

        self.gaps_out_layout.addWidget(self.gaps_out_layout_2)

        self.gaps_out_spinBox = QSpinBox(self.layoutWidget)
        self.gaps_out_spinBox.setObjectName(u"gaps_out_spinBox")

        self.gaps_out_layout.addWidget(self.gaps_out_spinBox)


        self.general_look_layout.addLayout(self.gaps_out_layout)

        self.border_size_layout = QHBoxLayout()
        self.border_size_layout.setObjectName(u"border_size_layout")
        self.border_size_label = QLabel(self.layoutWidget)
        self.border_size_label.setObjectName(u"border_size_label")

        self.border_size_layout.addWidget(self.border_size_label)

        self.border_size_spinBox = QSpinBox(self.layoutWidget)
        self.border_size_spinBox.setObjectName(u"border_size_spinBox")

        self.border_size_layout.addWidget(self.border_size_spinBox)


        self.general_look_layout.addLayout(self.border_size_layout)

        self.border_col_1_layout = QHBoxLayout()
        self.border_col_1_layout.setObjectName(u"border_col_1_layout")
        self.border_col_1_label = QLabel(self.layoutWidget)
        self.border_col_1_label.setObjectName(u"border_col_1_label")

        self.border_col_1_layout.addWidget(self.border_col_1_label)

        self.set_color_1_button = QPushButton(self.layoutWidget)
        self.set_color_1_button.setObjectName(u"set_color_1_button")

        self.border_col_1_layout.addWidget(self.set_color_1_button)


        self.general_look_layout.addLayout(self.border_col_1_layout)

        self.border_col_2_layout = QHBoxLayout()
        self.border_col_2_layout.setObjectName(u"border_col_2_layout")
        self.border_col_2_label = QLabel(self.layoutWidget)
        self.border_col_2_label.setObjectName(u"border_col_2_label")

        self.border_col_2_layout.addWidget(self.border_col_2_label)

        self.set_color_2_button = QPushButton(self.layoutWidget)
        self.set_color_2_button.setObjectName(u"set_color_2_button")

        self.border_col_2_layout.addWidget(self.set_color_2_button)


        self.general_look_layout.addLayout(self.border_col_2_layout)

        self.angle_border_layout = QHBoxLayout()
        self.angle_border_layout.setObjectName(u"angle_border_layout")
        self.angle_label = QLabel(self.layoutWidget)
        self.angle_label.setObjectName(u"angle_label")

        self.angle_border_layout.addWidget(self.angle_label)

        self.angle_spinBox = QSpinBox(self.layoutWidget)
        self.angle_spinBox.setObjectName(u"angle_spinBox")
        self.angle_spinBox.setMaximum(360)

        self.angle_border_layout.addWidget(self.angle_spinBox)


        self.general_look_layout.addLayout(self.angle_border_layout)

        self.resize_checkbox = QCheckBox(self.layoutWidget)
        self.resize_checkbox.setObjectName(u"resize_checkbox")

        self.general_look_layout.addWidget(self.resize_checkbox)

        self.allow_tearing_checkBox = QCheckBox(self.layoutWidget)
        self.allow_tearing_checkBox.setObjectName(u"allow_tearing_checkBox")

        self.general_look_layout.addWidget(self.allow_tearing_checkBox)

        self.layout_hyprland_layout = QHBoxLayout()
        self.layout_hyprland_layout.setObjectName(u"layout_hyprland_layout")
        self.layout_hyprland_label = QLabel(self.layoutWidget)
        self.layout_hyprland_label.setObjectName(u"layout_hyprland_label")

        self.layout_hyprland_layout.addWidget(self.layout_hyprland_label)

        self.layout_comboBox = QComboBox(self.layoutWidget)
        self.layout_comboBox.setObjectName(u"layout_comboBox")

        self.layout_hyprland_layout.addWidget(self.layout_comboBox)


        self.general_look_layout.addLayout(self.layout_hyprland_layout)

        self.label = QLabel(self.look_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 220, 91, 41))
        self.label_2 = QLabel(self.look_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 150, 151, 61))
        self.label_3 = QLabel(self.look_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 110, 101, 41))
        self.label_4 = QLabel(self.look_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 280, 91, 41))
        self.Hyprland_Menu_Settings.addTab(self.look_tab, "")
        self.input_tab = QWidget()
        self.input_tab.setObjectName(u"input_tab")
        self.Hyprland_Menu_Settings.addTab(self.input_tab, "")
        self.keybinds_tab = QWidget()
        self.keybinds_tab.setObjectName(u"keybinds_tab")
        self.Hyprland_Menu_Settings.addTab(self.keybinds_tab, "")
        self.windowrules_tab = QWidget()
        self.windowrules_tab.setObjectName(u"windowrules_tab")
        self.verticalLayout_9 = QVBoxLayout(self.windowrules_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Hyprland_Menu_Settings.addTab(self.windowrules_tab, "")

        self.horizontalLayout_14.addWidget(self.Hyprland_Menu_Settings)

        self.Settings_Menu.addTab(self.hyprland_tab, "")
        self.network_tab = QWidget()
        self.network_tab.setObjectName(u"network_tab")
        self.Settings_Menu.addTab(self.network_tab, "")
        self.wallpaper_tab = QWidget()
        self.wallpaper_tab.setObjectName(u"wallpaper_tab")
        self.Settings_Menu.addTab(self.wallpaper_tab, "")
        self.update_tab = QWidget()
        self.update_tab.setObjectName(u"update_tab")
        self.Settings_Menu.addTab(self.update_tab, "")

        self.horizontalLayout_10.addWidget(self.Settings_Menu)

        Widget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Widget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 976, 19))
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
        self.menu_Application.addAction(self.actionHelp)

        self.retranslateUi(Widget)

        self.Settings_Menu.setCurrentIndex(0)
        self.Hyprland_Menu_Settings.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hyprland Settings", None))
        self.actionThemes.setText(QCoreApplication.translate("Widget", u"Themes", None))
        self.dark_theme_button.setText(QCoreApplication.translate("Widget", u"Dark", None))
        self.light_theme_button.setText(QCoreApplication.translate("Widget", u"Light", None))
        self.quit_program.setText(QCoreApplication.translate("Widget", u"Quit", None))
        self.actionRefresh.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.actionHelp.setText(QCoreApplication.translate("Widget", u"Help", None))
        self.monitor_name_label.setText(QCoreApplication.translate("Widget", u"Monitor: ", None))
        self.monitor_res_label.setText(QCoreApplication.translate("Widget", u"Resolution", None))
        self.monitor_pos_label.setText(QCoreApplication.translate("Widget", u"Position", None))
        self.monitor_scale_label.setText(QCoreApplication.translate("Widget", u"Scale", None))
        self.apply_button.setText(QCoreApplication.translate("Widget", u"Apply", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.monitor_tab), QCoreApplication.translate("Widget", u"Monitor", None))
        self.add_program_button.setText(QCoreApplication.translate("Widget", u"Add Program", None))
        self.add_script_button.setText(QCoreApplication.translate("Widget", u"Add Script", None))
        self.del_autostart_button.setText(QCoreApplication.translate("Widget", u"Delete Autostart", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.auto_tab), QCoreApplication.translate("Widget", u"Autostart", None))
        self.add_env_button.setText(QCoreApplication.translate("Widget", u"Add Environment", None))
        self.del_env_button.setText(QCoreApplication.translate("Widget", u"Delete Environment", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.env_tab), QCoreApplication.translate("Widget", u"Environment", None))
        self.gaps_in_label.setText(QCoreApplication.translate("Widget", u"Gaps in: ", None))
        self.gaps_out_layout_2.setText(QCoreApplication.translate("Widget", u"Gaps out: ", None))
        self.border_size_label.setText(QCoreApplication.translate("Widget", u"Border size: ", None))
        self.border_col_1_label.setText(QCoreApplication.translate("Widget", u"Border color (1): ", None))
        self.set_color_1_button.setText(QCoreApplication.translate("Widget", u"Set color 1", None))
        self.border_col_2_label.setText(QCoreApplication.translate("Widget", u"Border color (2): ", None))
        self.set_color_2_button.setText(QCoreApplication.translate("Widget", u"Set color 2", None))
        self.angle_label.setText(QCoreApplication.translate("Widget", u"Angle: ", None))
        self.resize_checkbox.setText(QCoreApplication.translate("Widget", u"Resize on border", None))
        self.allow_tearing_checkBox.setText(QCoreApplication.translate("Widget", u"Allow tearing", None))
        self.layout_hyprland_label.setText(QCoreApplication.translate("Widget", u"Layout:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Active opacity", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Rounding power", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Rounding", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Inactive opacity", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.look_tab), QCoreApplication.translate("Widget", u"Look and Feel", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.input_tab), QCoreApplication.translate("Widget", u"Input", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.keybinds_tab), QCoreApplication.translate("Widget", u"Keybindings", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.windowrules_tab), QCoreApplication.translate("Widget", u"Window Rules", None))
        self.Settings_Menu.setTabText(self.Settings_Menu.indexOf(self.hyprland_tab), QCoreApplication.translate("Widget", u"Hyprland", None))
        self.Settings_Menu.setTabText(self.Settings_Menu.indexOf(self.network_tab), QCoreApplication.translate("Widget", u"Network", None))
        self.Settings_Menu.setTabText(self.Settings_Menu.indexOf(self.wallpaper_tab), QCoreApplication.translate("Widget", u"Wallpaper", None))
        self.Settings_Menu.setTabText(self.Settings_Menu.indexOf(self.update_tab), QCoreApplication.translate("Widget", u"Update", None))
        self.menuTheme.setTitle(QCoreApplication.translate("Widget", u"Themes", None))
        self.menu_Application.setTitle(QCoreApplication.translate("Widget", u"Application", None))
    # retranslateUi

