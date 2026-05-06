# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(1074, 846)
        self.actionThemes = QAction(Widget)
        self.actionThemes.setObjectName("actionThemes")
        self.dark_theme_button = QAction(Widget)
        self.dark_theme_button.setObjectName("dark_theme_button")
        self.light_theme_button = QAction(Widget)
        self.light_theme_button.setObjectName("light_theme_button")
        self.quit_program = QAction(Widget)
        self.quit_program.setObjectName("quit_program")
        self.actionRefresh = QAction(Widget)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionHelp = QAction(Widget)
        self.actionHelp.setObjectName("actionHelp")
        self.centralwidget = QWidget(Widget)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Settings_Menu = QTabWidget(self.centralwidget)
        self.Settings_Menu.setObjectName("Settings_Menu")
        self.Settings_Menu.setTabPosition(QTabWidget.TabPosition.West)
        self.Settings_Menu.setTabShape(QTabWidget.TabShape.Rounded)
        self.Settings_Menu.setDocumentMode(False)
        self.hyprland_tab = QWidget()
        self.hyprland_tab.setObjectName("hyprland_tab")
        self.horizontalLayout_14 = QHBoxLayout(self.hyprland_tab)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Hyprland_Menu_Settings = QTabWidget(self.hyprland_tab)
        self.Hyprland_Menu_Settings.setObjectName("Hyprland_Menu_Settings")
        self.Hyprland_Menu_Settings.setEnabled(True)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Hyprland_Menu_Settings.sizePolicy().hasHeightForWidth()
        )
        self.Hyprland_Menu_Settings.setSizePolicy(sizePolicy)
        self.monitor_tab = QWidget()
        self.monitor_tab.setObjectName("monitor_tab")
        self.verticalLayout_2 = QVBoxLayout(self.monitor_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.monitor_tab_layout = QVBoxLayout()
        self.monitor_tab_layout.setObjectName("monitor_tab_layout")
        self.monitor_settings_layout = QVBoxLayout()
        self.monitor_settings_layout.setObjectName("monitor_settings_layout")
        self.monitor_name_layout = QHBoxLayout()
        self.monitor_name_layout.setObjectName("monitor_name_layout")
        self.monitor_name_label = QLabel(self.monitor_tab)
        self.monitor_name_label.setObjectName("monitor_name_label")

        self.monitor_name_layout.addWidget(self.monitor_name_label)

        self.monitors_box = QComboBox(self.monitor_tab)
        self.monitors_box.setObjectName("monitors_box")

        self.monitor_name_layout.addWidget(self.monitors_box)

        self.monitor_settings_layout.addLayout(self.monitor_name_layout)

        self.monitor_res_layout = QHBoxLayout()
        self.monitor_res_layout.setObjectName("monitor_res_layout")
        self.monitor_res_label = QLabel(self.monitor_tab)
        self.monitor_res_label.setObjectName("monitor_res_label")

        self.monitor_res_layout.addWidget(self.monitor_res_label)

        self.resolution_box = QComboBox(self.monitor_tab)
        self.resolution_box.setObjectName("resolution_box")

        self.monitor_res_layout.addWidget(self.resolution_box)

        self.monitor_settings_layout.addLayout(self.monitor_res_layout)

        self.monitor_pos_layout = QHBoxLayout()
        self.monitor_pos_layout.setObjectName("monitor_pos_layout")
        self.monitor_pos_label = QLabel(self.monitor_tab)
        self.monitor_pos_label.setObjectName("monitor_pos_label")

        self.monitor_pos_layout.addWidget(self.monitor_pos_label)

        self.position_box = QComboBox(self.monitor_tab)
        self.position_box.setObjectName("position_box")

        self.monitor_pos_layout.addWidget(self.position_box)

        self.monitor_settings_layout.addLayout(self.monitor_pos_layout)

        self.monitor_scale_layout = QHBoxLayout()
        self.monitor_scale_layout.setObjectName("monitor_scale_layout")
        self.monitor_scale_label = QLabel(self.monitor_tab)
        self.monitor_scale_label.setObjectName("monitor_scale_label")

        self.monitor_scale_layout.addWidget(self.monitor_scale_label)

        self.scale_box = QComboBox(self.monitor_tab)
        self.scale_box.setObjectName("scale_box")

        self.monitor_scale_layout.addWidget(self.scale_box)

        self.monitor_settings_layout.addLayout(self.monitor_scale_layout)

        self.monitor_tab_layout.addLayout(self.monitor_settings_layout)

        self.apply_button = QPushButton(self.monitor_tab)
        self.apply_button.setObjectName("apply_button")

        self.monitor_tab_layout.addWidget(self.apply_button)

        self.verticalLayout_2.addLayout(self.monitor_tab_layout)

        self.Hyprland_Menu_Settings.addTab(self.monitor_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName("auto_tab")
        self.verticalLayout_5 = QVBoxLayout(self.auto_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.auto_hyprland_layout = QHBoxLayout()
        self.auto_hyprland_layout.setObjectName("auto_hyprland_layout")
        self.auto_hyprland_layout_2 = QVBoxLayout()
        self.auto_hyprland_layout_2.setObjectName("auto_hyprland_layout_2")
        self.current_autostart = QListWidget(self.auto_tab)
        self.current_autostart.setObjectName("current_autostart")

        self.auto_hyprland_layout_2.addWidget(self.current_autostart)

        self.add_program_button = QPushButton(self.auto_tab)
        self.add_program_button.setObjectName("add_program_button")

        self.auto_hyprland_layout_2.addWidget(self.add_program_button)

        self.add_script_button = QPushButton(self.auto_tab)
        self.add_script_button.setObjectName("add_script_button")

        self.auto_hyprland_layout_2.addWidget(self.add_script_button)

        self.del_autostart_button = QPushButton(self.auto_tab)
        self.del_autostart_button.setObjectName("del_autostart_button")

        self.auto_hyprland_layout_2.addWidget(self.del_autostart_button)

        self.auto_hyprland_layout.addLayout(self.auto_hyprland_layout_2)

        self.verticalLayout_5.addLayout(self.auto_hyprland_layout)

        self.Hyprland_Menu_Settings.addTab(self.auto_tab, "")
        self.env_tab = QWidget()
        self.env_tab.setObjectName("env_tab")
        self.verticalLayout_7 = QVBoxLayout(self.env_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.env_hyprland_layout = QVBoxLayout()
        self.env_hyprland_layout.setObjectName("env_hyprland_layout")
        self.current_env = QListWidget(self.env_tab)
        self.current_env.setObjectName("current_env")

        self.env_hyprland_layout.addWidget(self.current_env)

        self.add_env_button = QPushButton(self.env_tab)
        self.add_env_button.setObjectName("add_env_button")

        self.env_hyprland_layout.addWidget(self.add_env_button)

        self.del_env_button = QPushButton(self.env_tab)
        self.del_env_button.setObjectName("del_env_button")

        self.env_hyprland_layout.addWidget(self.del_env_button)

        self.verticalLayout_7.addLayout(self.env_hyprland_layout)

        self.Hyprland_Menu_Settings.addTab(self.env_tab, "")
        self.look_tab = QWidget()
        self.look_tab.setObjectName("look_tab")
        self.look_outer_layout = QVBoxLayout(self.look_tab)
        self.look_outer_layout.setSpacing(12)
        self.look_outer_layout.setContentsMargins(12, 12, 12, 12)
        self.look_outer_layout.setObjectName("look_outer_layout")
        self.look_grid_layout = QGridLayout()
        self.look_grid_layout.setObjectName("look_grid_layout")
        self.look_grid_layout.setHorizontalSpacing(12)
        self.look_grid_layout.setVerticalSpacing(12)
        self.general_group = QGroupBox(self.look_tab)
        self.general_group.setObjectName("general_group")
        self.general_form_layout = QFormLayout(self.general_group)
        self.general_form_layout.setObjectName("general_form_layout")
        self.general_form_layout.setLabelAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.general_form_layout.setHorizontalSpacing(12)
        self.general_form_layout.setVerticalSpacing(8)
        self.gaps_in_label = QLabel(self.general_group)
        self.gaps_in_label.setObjectName("gaps_in_label")

        self.general_form_layout.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.gaps_in_label
        )

        self.gabs_in_spinBox = QSpinBox(self.general_group)
        self.gabs_in_spinBox.setObjectName("gabs_in_spinBox")

        self.general_form_layout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.gabs_in_spinBox
        )

        self.gaps_out_layout_2 = QLabel(self.general_group)
        self.gaps_out_layout_2.setObjectName("gaps_out_layout_2")

        self.general_form_layout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.gaps_out_layout_2
        )

        self.gaps_out_spinBox = QSpinBox(self.general_group)
        self.gaps_out_spinBox.setObjectName("gaps_out_spinBox")

        self.general_form_layout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.gaps_out_spinBox
        )

        self.border_size_label = QLabel(self.general_group)
        self.border_size_label.setObjectName("border_size_label")

        self.general_form_layout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.border_size_label
        )

        self.border_size_spinBox = QSpinBox(self.general_group)
        self.border_size_spinBox.setObjectName("border_size_spinBox")

        self.general_form_layout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.border_size_spinBox
        )

        self.border_col_1_label = QLabel(self.general_group)
        self.border_col_1_label.setObjectName("border_col_1_label")

        self.general_form_layout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.border_col_1_label
        )

        self.set_color_1_button = QPushButton(self.general_group)
        self.set_color_1_button.setObjectName("set_color_1_button")

        self.general_form_layout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.set_color_1_button
        )

        self.border_col_2_label = QLabel(self.general_group)
        self.border_col_2_label.setObjectName("border_col_2_label")

        self.general_form_layout.setWidget(
            4, QFormLayout.ItemRole.LabelRole, self.border_col_2_label
        )

        self.set_color_2_button = QPushButton(self.general_group)
        self.set_color_2_button.setObjectName("set_color_2_button")

        self.general_form_layout.setWidget(
            4, QFormLayout.ItemRole.FieldRole, self.set_color_2_button
        )

        self.angle_label = QLabel(self.general_group)
        self.angle_label.setObjectName("angle_label")

        self.general_form_layout.setWidget(
            5, QFormLayout.ItemRole.LabelRole, self.angle_label
        )

        self.angle_spinBox = QSpinBox(self.general_group)
        self.angle_spinBox.setObjectName("angle_spinBox")
        self.angle_spinBox.setMaximum(360)

        self.general_form_layout.setWidget(
            5, QFormLayout.ItemRole.FieldRole, self.angle_spinBox
        )

        self.resize_checkbox = QCheckBox(self.general_group)
        self.resize_checkbox.setObjectName("resize_checkbox")

        self.general_form_layout.setWidget(
            6, QFormLayout.ItemRole.SpanningRole, self.resize_checkbox
        )

        self.allow_tearing_checkBox = QCheckBox(self.general_group)
        self.allow_tearing_checkBox.setObjectName("allow_tearing_checkBox")

        self.general_form_layout.setWidget(
            7, QFormLayout.ItemRole.SpanningRole, self.allow_tearing_checkBox
        )

        self.layout_hyprland_label = QLabel(self.general_group)
        self.layout_hyprland_label.setObjectName("layout_hyprland_label")

        self.general_form_layout.setWidget(
            8, QFormLayout.ItemRole.LabelRole, self.layout_hyprland_label
        )

        self.layout_comboBox = QComboBox(self.general_group)
        self.layout_comboBox.setObjectName("layout_comboBox")

        self.general_form_layout.setWidget(
            8, QFormLayout.ItemRole.FieldRole, self.layout_comboBox
        )

        self.look_grid_layout.addWidget(self.general_group, 0, 0, 1, 1)

        self.decoration_group = QGroupBox(self.look_tab)
        self.decoration_group.setObjectName("decoration_group")
        self.decoration_form_layout = QFormLayout(self.decoration_group)
        self.decoration_form_layout.setObjectName("decoration_form_layout")
        self.decoration_form_layout.setLabelAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.decoration_form_layout.setHorizontalSpacing(12)
        self.decoration_form_layout.setVerticalSpacing(8)
        self.rounding_label = QLabel(self.decoration_group)
        self.rounding_label.setObjectName("rounding_label")

        self.decoration_form_layout.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.rounding_label
        )

        self.rounding_spin_box = QSpinBox(self.decoration_group)
        self.rounding_spin_box.setObjectName("rounding_spin_box")

        self.decoration_form_layout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.rounding_spin_box
        )

        self.rounding_power_label = QLabel(self.decoration_group)
        self.rounding_power_label.setObjectName("rounding_power_label")

        self.decoration_form_layout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.rounding_power_label
        )

        self.rounding_power_spin_box = QSpinBox(self.decoration_group)
        self.rounding_power_spin_box.setObjectName("rounding_power_spin_box")

        self.decoration_form_layout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.rounding_power_spin_box
        )

        self.active_op_label = QLabel(self.decoration_group)
        self.active_op_label.setObjectName("active_op_label")

        self.decoration_form_layout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.active_op_label
        )

        self.act_op_spin_box = QSpinBox(self.decoration_group)
        self.act_op_spin_box.setObjectName("act_op_spin_box")

        self.decoration_form_layout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.act_op_spin_box
        )

        self.inact_op_label = QLabel(self.decoration_group)
        self.inact_op_label.setObjectName("inact_op_label")

        self.decoration_form_layout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.inact_op_label
        )

        self.inact_op_spin_box = QSpinBox(self.decoration_group)
        self.inact_op_spin_box.setObjectName("inact_op_spin_box")

        self.decoration_form_layout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.inact_op_spin_box
        )

        self.look_grid_layout.addWidget(self.decoration_group, 0, 1, 1, 1)

        self.shadow_group = QGroupBox(self.look_tab)
        self.shadow_group.setObjectName("shadow_group")
        self.shadow_form_layout = QFormLayout(self.shadow_group)
        self.shadow_form_layout.setObjectName("shadow_form_layout")
        self.shadow_form_layout.setLabelAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.shadow_form_layout.setHorizontalSpacing(12)
        self.shadow_form_layout.setVerticalSpacing(8)
        self.shadow_enable_checkbox = QCheckBox(self.shadow_group)
        self.shadow_enable_checkbox.setObjectName("shadow_enable_checkbox")
        self.shadow_enable_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.shadow_form_layout.setWidget(
            0, QFormLayout.ItemRole.SpanningRole, self.shadow_enable_checkbox
        )

        self.shadow_range_label = QLabel(self.shadow_group)
        self.shadow_range_label.setObjectName("shadow_range_label")

        self.shadow_form_layout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.shadow_range_label
        )

        self.shadow_range_spinbox = QSpinBox(self.shadow_group)
        self.shadow_range_spinbox.setObjectName("shadow_range_spinbox")

        self.shadow_form_layout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.shadow_range_spinbox
        )

        self.shadow_render_power_label = QLabel(self.shadow_group)
        self.shadow_render_power_label.setObjectName("shadow_render_power_label")

        self.shadow_form_layout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.shadow_render_power_label
        )

        self.shadow_range_power_spinbox = QSpinBox(self.shadow_group)
        self.shadow_range_power_spinbox.setObjectName("shadow_range_power_spinbox")

        self.shadow_form_layout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.shadow_range_power_spinbox
        )

        self.shadow_label_2 = QLabel(self.shadow_group)
        self.shadow_label_2.setObjectName("shadow_label_2")

        self.shadow_form_layout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.shadow_label_2
        )

        self.shadow_color_button = QPushButton(self.shadow_group)
        self.shadow_color_button.setObjectName("shadow_color_button")

        self.shadow_form_layout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.shadow_color_button
        )

        self.look_grid_layout.addWidget(self.shadow_group, 1, 0, 1, 1)

        self.blur_group = QGroupBox(self.look_tab)
        self.blur_group.setObjectName("blur_group")
        self.blur_form_layout = QFormLayout(self.blur_group)
        self.blur_form_layout.setObjectName("blur_form_layout")
        self.blur_form_layout.setLabelAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.blur_form_layout.setHorizontalSpacing(12)
        self.blur_form_layout.setVerticalSpacing(8)
        self.blur_enable_checkBox = QCheckBox(self.blur_group)
        self.blur_enable_checkBox.setObjectName("blur_enable_checkBox")

        self.blur_form_layout.setWidget(
            0, QFormLayout.ItemRole.SpanningRole, self.blur_enable_checkBox
        )

        self.blur_size_label = QLabel(self.blur_group)
        self.blur_size_label.setObjectName("blur_size_label")

        self.blur_form_layout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.blur_size_label
        )

        self.blur_size_spinBox = QSpinBox(self.blur_group)
        self.blur_size_spinBox.setObjectName("blur_size_spinBox")

        self.blur_form_layout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.blur_size_spinBox
        )

        self.blur_passes_label = QLabel(self.blur_group)
        self.blur_passes_label.setObjectName("blur_passes_label")

        self.blur_form_layout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.blur_passes_label
        )

        self.blur_passes_spinBox = QSpinBox(self.blur_group)
        self.blur_passes_spinBox.setObjectName("blur_passes_spinBox")

        self.blur_form_layout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.blur_passes_spinBox
        )

        self.blur_vibrancy_label = QLabel(self.blur_group)
        self.blur_vibrancy_label.setObjectName("blur_vibrancy_label")

        self.blur_form_layout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.blur_vibrancy_label
        )

        self.blur_vib_doubleSpinBox = QDoubleSpinBox(self.blur_group)
        self.blur_vib_doubleSpinBox.setObjectName("blur_vib_doubleSpinBox")

        self.blur_form_layout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.blur_vib_doubleSpinBox
        )

        self.look_grid_layout.addWidget(self.blur_group, 1, 1, 1, 1)

        self.look_outer_layout.addLayout(self.look_grid_layout)

        self.Hyprland_Menu_Settings.addTab(self.look_tab, "")
        self.input_tab = QWidget()
        self.input_tab.setObjectName("input_tab")
        self.Hyprland_Menu_Settings.addTab(self.input_tab, "")
        self.keybinds_tab = QWidget()
        self.keybinds_tab.setObjectName("keybinds_tab")
        self.Hyprland_Menu_Settings.addTab(self.keybinds_tab, "")
        self.windowrules_tab = QWidget()
        self.windowrules_tab.setObjectName("windowrules_tab")
        self.verticalLayout_9 = QVBoxLayout(self.windowrules_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Hyprland_Menu_Settings.addTab(self.windowrules_tab, "")

        self.horizontalLayout_14.addWidget(self.Hyprland_Menu_Settings)

        self.Settings_Menu.addTab(self.hyprland_tab, "")
        self.network_tab = QWidget()
        self.network_tab.setObjectName("network_tab")
        self.Settings_Menu.addTab(self.network_tab, "")
        self.wallpaper_tab = QWidget()
        self.wallpaper_tab.setObjectName("wallpaper_tab")
        self.Settings_Menu.addTab(self.wallpaper_tab, "")
        self.update_tab = QWidget()
        self.update_tab.setObjectName("update_tab")
        self.Settings_Menu.addTab(self.update_tab, "")

        self.horizontalLayout_10.addWidget(self.Settings_Menu)

        Widget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Widget)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1074, 19))
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        self.menu_Application = QMenu(self.menubar)
        self.menu_Application.setObjectName("menu_Application")
        Widget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Widget)
        self.statusbar.setObjectName("statusbar")
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
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", "Hyprland Settings", None)
        )
        self.actionThemes.setText(QCoreApplication.translate("Widget", "Themes", None))
        self.dark_theme_button.setText(
            QCoreApplication.translate("Widget", "Dark", None)
        )
        self.light_theme_button.setText(
            QCoreApplication.translate("Widget", "Light", None)
        )
        self.quit_program.setText(QCoreApplication.translate("Widget", "Quit", None))
        self.actionRefresh.setText(
            QCoreApplication.translate("Widget", "Refresh", None)
        )
        self.actionHelp.setText(QCoreApplication.translate("Widget", "Help", None))
        self.monitor_name_label.setText(
            QCoreApplication.translate("Widget", "Monitor: ", None)
        )
        self.monitor_res_label.setText(
            QCoreApplication.translate("Widget", "Resolution", None)
        )
        self.monitor_pos_label.setText(
            QCoreApplication.translate("Widget", "Position", None)
        )
        self.monitor_scale_label.setText(
            QCoreApplication.translate("Widget", "Scale", None)
        )
        self.apply_button.setText(QCoreApplication.translate("Widget", "Apply", None))
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.monitor_tab),
            QCoreApplication.translate("Widget", "Monitor", None),
        )
        self.add_program_button.setText(
            QCoreApplication.translate("Widget", "Add Program", None)
        )
        self.add_script_button.setText(
            QCoreApplication.translate("Widget", "Add Script", None)
        )
        self.del_autostart_button.setText(
            QCoreApplication.translate("Widget", "Delete Autostart", None)
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.auto_tab),
            QCoreApplication.translate("Widget", "Autostart", None),
        )
        self.add_env_button.setText(
            QCoreApplication.translate("Widget", "Add Environment", None)
        )
        self.del_env_button.setText(
            QCoreApplication.translate("Widget", "Delete Environment", None)
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.env_tab),
            QCoreApplication.translate("Widget", "Environment", None),
        )
        self.general_group.setTitle(
            QCoreApplication.translate("Widget", "General Settings", None)
        )
        self.gaps_in_label.setText(
            QCoreApplication.translate("Widget", "Gaps in:", None)
        )
        self.gaps_out_layout_2.setText(
            QCoreApplication.translate("Widget", "Gaps out:", None)
        )
        self.border_size_label.setText(
            QCoreApplication.translate("Widget", "Border size:", None)
        )
        self.border_col_1_label.setText(
            QCoreApplication.translate("Widget", "Border color (1):", None)
        )
        self.set_color_1_button.setText(
            QCoreApplication.translate("Widget", "Set color 1", None)
        )
        self.border_col_2_label.setText(
            QCoreApplication.translate("Widget", "Border color (2):", None)
        )
        self.set_color_2_button.setText(
            QCoreApplication.translate("Widget", "Set color 2", None)
        )
        self.angle_label.setText(QCoreApplication.translate("Widget", "Angle:", None))
        self.resize_checkbox.setText(
            QCoreApplication.translate("Widget", "Resize on border", None)
        )
        self.allow_tearing_checkBox.setText(
            QCoreApplication.translate("Widget", "Allow tearing", None)
        )
        self.layout_hyprland_label.setText(
            QCoreApplication.translate("Widget", "Layout:", None)
        )
        self.decoration_group.setTitle(
            QCoreApplication.translate("Widget", "Decoration Settings", None)
        )
        self.rounding_label.setText(
            QCoreApplication.translate("Widget", "Rounding:", None)
        )
        self.rounding_power_label.setText(
            QCoreApplication.translate("Widget", "Rounding power:", None)
        )
        self.active_op_label.setText(
            QCoreApplication.translate("Widget", "Active opacity:", None)
        )
        self.inact_op_label.setText(
            QCoreApplication.translate("Widget", "Inactive opacity:", None)
        )
        self.shadow_group.setTitle(
            QCoreApplication.translate("Widget", "Shadow Settings", None)
        )
        self.shadow_enable_checkbox.setText(
            QCoreApplication.translate("Widget", "Enable", None)
        )
        self.shadow_range_label.setText(
            QCoreApplication.translate("Widget", "Range:", None)
        )
        self.shadow_render_power_label.setText(
            QCoreApplication.translate("Widget", "Render power:", None)
        )
        self.shadow_label_2.setText(
            QCoreApplication.translate("Widget", "Color:", None)
        )
        self.shadow_color_button.setText(
            QCoreApplication.translate("Widget", "Set shadow color", None)
        )
        self.blur_group.setTitle(
            QCoreApplication.translate("Widget", "Blur Settings", None)
        )
        self.blur_enable_checkBox.setText(
            QCoreApplication.translate("Widget", "Enable", None)
        )
        self.blur_size_label.setText(
            QCoreApplication.translate("Widget", "Size:", None)
        )
        self.blur_passes_label.setText(
            QCoreApplication.translate("Widget", "Passes:", None)
        )
        self.blur_vibrancy_label.setText(
            QCoreApplication.translate("Widget", "Vibrancy:", None)
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.look_tab),
            QCoreApplication.translate("Widget", "Look and Feel", None),
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.input_tab),
            QCoreApplication.translate("Widget", "Input", None),
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.keybinds_tab),
            QCoreApplication.translate("Widget", "Keybindings", None),
        )
        self.Hyprland_Menu_Settings.setTabText(
            self.Hyprland_Menu_Settings.indexOf(self.windowrules_tab),
            QCoreApplication.translate("Widget", "Window Rules", None),
        )
        self.Settings_Menu.setTabText(
            self.Settings_Menu.indexOf(self.hyprland_tab),
            QCoreApplication.translate("Widget", "Hyprland", None),
        )
        self.Settings_Menu.setTabText(
            self.Settings_Menu.indexOf(self.network_tab),
            QCoreApplication.translate("Widget", "Network", None),
        )
        self.Settings_Menu.setTabText(
            self.Settings_Menu.indexOf(self.wallpaper_tab),
            QCoreApplication.translate("Widget", "Wallpaper", None),
        )
        self.Settings_Menu.setTabText(
            self.Settings_Menu.indexOf(self.update_tab),
            QCoreApplication.translate("Widget", "Update", None),
        )
        self.menuTheme.setTitle(QCoreApplication.translate("Widget", "Themes", None))
        self.menu_Application.setTitle(
            QCoreApplication.translate("Widget", "Application", None)
        )

    # retranslateUi
