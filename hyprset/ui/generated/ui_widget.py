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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(835, 679)
        self.dark_theme_button = QAction(Widget)
        self.dark_theme_button.setObjectName(u"dark_theme_button")
        self.light_theme_button = QAction(Widget)
        self.light_theme_button.setObjectName(u"light_theme_button")
        self.quit_program = QAction(Widget)
        self.quit_program.setObjectName(u"quit_program")
        self.actionHelp = QAction(Widget)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionRestart = QAction(Widget)
        self.actionRestart.setObjectName(u"actionRestart")
        self.centralwidget = QWidget(Widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(160, 0))
        self.listWidget.setMaximumSize(QSize(160, 16777215))
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.listWidget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.hyprland_page = QWidget()
        self.hyprland_page.setObjectName(u"hyprland_page")
        self.verticalLayout = QVBoxLayout(self.hyprland_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Hyprland_Menu_Settings = QTabWidget(self.hyprland_page)
        self.Hyprland_Menu_Settings.setObjectName(u"Hyprland_Menu_Settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Hyprland_Menu_Settings.sizePolicy().hasHeightForWidth())
        self.Hyprland_Menu_Settings.setSizePolicy(sizePolicy1)
        self.monitor_tab = QWidget()
        self.monitor_tab.setObjectName(u"monitor_tab")
        self.monitor_outer_vl = QVBoxLayout(self.monitor_tab)
        self.monitor_outer_vl.setSpacing(16)
        self.monitor_outer_vl.setObjectName(u"monitor_outer_vl")
        self.monitor_outer_vl.setContentsMargins(24, 24, 24, 24)
        self.monitor_group = QGroupBox(self.monitor_tab)
        self.monitor_group.setObjectName(u"monitor_group")
        self.monitor_form_layout = QFormLayout(self.monitor_group)
        self.monitor_form_layout.setObjectName(u"monitor_form_layout")
        self.monitor_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.monitor_form_layout.setHorizontalSpacing(16)
        self.monitor_form_layout.setVerticalSpacing(12)
        self.monitor_form_layout.setContentsMargins(20, 24, 20, 20)
        self.monitor_name_label = QLabel(self.monitor_group)
        self.monitor_name_label.setObjectName(u"monitor_name_label")

        self.monitor_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.monitor_name_label)

        self.monitors_box = QComboBox(self.monitor_group)
        self.monitors_box.setObjectName(u"monitors_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.monitors_box.sizePolicy().hasHeightForWidth())
        self.monitors_box.setSizePolicy(sizePolicy2)

        self.monitor_form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.monitors_box)

        self.monitor_res_label = QLabel(self.monitor_group)
        self.monitor_res_label.setObjectName(u"monitor_res_label")

        self.monitor_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.monitor_res_label)

        self.resolution_box = QComboBox(self.monitor_group)
        self.resolution_box.setObjectName(u"resolution_box")
        sizePolicy2.setHeightForWidth(self.resolution_box.sizePolicy().hasHeightForWidth())
        self.resolution_box.setSizePolicy(sizePolicy2)

        self.monitor_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.resolution_box)

        self.monitor_pos_label = QLabel(self.monitor_group)
        self.monitor_pos_label.setObjectName(u"monitor_pos_label")

        self.monitor_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.monitor_pos_label)

        self.position_box = QComboBox(self.monitor_group)
        self.position_box.setObjectName(u"position_box")
        sizePolicy2.setHeightForWidth(self.position_box.sizePolicy().hasHeightForWidth())
        self.position_box.setSizePolicy(sizePolicy2)

        self.monitor_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.position_box)

        self.monitor_scale_label = QLabel(self.monitor_group)
        self.monitor_scale_label.setObjectName(u"monitor_scale_label")

        self.monitor_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.monitor_scale_label)

        self.scale_box = QComboBox(self.monitor_group)
        self.scale_box.setObjectName(u"scale_box")
        sizePolicy2.setHeightForWidth(self.scale_box.sizePolicy().hasHeightForWidth())
        self.scale_box.setSizePolicy(sizePolicy2)

        self.monitor_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.scale_box)

        self.mirror_label = QLabel(self.monitor_group)
        self.mirror_label.setObjectName(u"mirror_label")

        self.monitor_form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.mirror_label)

        self.mirror_comboBox = QComboBox(self.monitor_group)
        self.mirror_comboBox.addItem("")
        self.mirror_comboBox.setObjectName(u"mirror_comboBox")

        self.monitor_form_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.mirror_comboBox)

        self.rotation_comboBox = QComboBox(self.monitor_group)
        self.rotation_comboBox.setObjectName(u"rotation_comboBox")

        self.monitor_form_layout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.rotation_comboBox)

        self.rotation_label = QLabel(self.monitor_group)
        self.rotation_label.setObjectName(u"rotation_label")

        self.monitor_form_layout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.rotation_label)


        self.monitor_outer_vl.addWidget(self.monitor_group)

        self.monitor_apply_hl = QHBoxLayout()
        self.monitor_apply_hl.setObjectName(u"monitor_apply_hl")
        self.set_default_monitor_button = QPushButton(self.monitor_tab)
        self.set_default_monitor_button.setObjectName(u"set_default_monitor_button")
        self.set_default_monitor_button.setMinimumSize(QSize(120, 34))

        self.monitor_apply_hl.addWidget(self.set_default_monitor_button)

        self.monitor_apply_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.monitor_apply_hl.addItem(self.monitor_apply_spacer)

        self.apply_button = QPushButton(self.monitor_tab)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setMinimumSize(QSize(140, 36))

        self.monitor_apply_hl.addWidget(self.apply_button)


        self.monitor_outer_vl.addLayout(self.monitor_apply_hl)

        self.monitor_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.monitor_outer_vl.addItem(self.monitor_bottom_spacer)

        self.Hyprland_Menu_Settings.addTab(self.monitor_tab, "")
        self.auto_tab = QWidget()
        self.auto_tab.setObjectName(u"auto_tab")
        self.auto_outer_vl = QVBoxLayout(self.auto_tab)
        self.auto_outer_vl.setSpacing(16)
        self.auto_outer_vl.setObjectName(u"auto_outer_vl")
        self.auto_outer_vl.setContentsMargins(24, 24, 24, 24)
        self.autostart_group = QGroupBox(self.auto_tab)
        self.autostart_group.setObjectName(u"autostart_group")
        self.autostart_inner_vl = QVBoxLayout(self.autostart_group)
        self.autostart_inner_vl.setSpacing(12)
        self.autostart_inner_vl.setObjectName(u"autostart_inner_vl")
        self.autostart_inner_vl.setContentsMargins(16, 24, 16, 16)
        self.current_autostart = QListWidget(self.autostart_group)
        self.current_autostart.setObjectName(u"current_autostart")

        self.autostart_inner_vl.addWidget(self.current_autostart)

        self.auto_btn_hl = QHBoxLayout()
        self.auto_btn_hl.setSpacing(8)
        self.auto_btn_hl.setObjectName(u"auto_btn_hl")
        self.add_program_button = QPushButton(self.autostart_group)
        self.add_program_button.setObjectName(u"add_program_button")
        self.add_program_button.setMinimumSize(QSize(0, 34))

        self.auto_btn_hl.addWidget(self.add_program_button)

        self.add_script_button = QPushButton(self.autostart_group)
        self.add_script_button.setObjectName(u"add_script_button")
        self.add_script_button.setMinimumSize(QSize(0, 34))

        self.auto_btn_hl.addWidget(self.add_script_button)

        self.auto_btn_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.auto_btn_hl.addItem(self.auto_btn_spacer)

        self.del_autostart_button = QPushButton(self.autostart_group)
        self.del_autostart_button.setObjectName(u"del_autostart_button")
        self.del_autostart_button.setMinimumSize(QSize(0, 34))

        self.auto_btn_hl.addWidget(self.del_autostart_button)


        self.autostart_inner_vl.addLayout(self.auto_btn_hl)


        self.auto_outer_vl.addWidget(self.autostart_group)

        self.auto_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.auto_outer_vl.addItem(self.auto_bottom_spacer)

        self.Hyprland_Menu_Settings.addTab(self.auto_tab, "")
        self.env_tab = QWidget()
        self.env_tab.setObjectName(u"env_tab")
        self.env_outer_vl = QVBoxLayout(self.env_tab)
        self.env_outer_vl.setSpacing(16)
        self.env_outer_vl.setObjectName(u"env_outer_vl")
        self.env_outer_vl.setContentsMargins(24, 24, 24, 24)
        self.env_group = QGroupBox(self.env_tab)
        self.env_group.setObjectName(u"env_group")
        self.env_inner_vl = QVBoxLayout(self.env_group)
        self.env_inner_vl.setSpacing(12)
        self.env_inner_vl.setObjectName(u"env_inner_vl")
        self.env_inner_vl.setContentsMargins(16, 24, 16, 16)
        self.current_env = QListWidget(self.env_group)
        self.current_env.setObjectName(u"current_env")

        self.env_inner_vl.addWidget(self.current_env)

        self.env_btn_hl = QHBoxLayout()
        self.env_btn_hl.setSpacing(8)
        self.env_btn_hl.setObjectName(u"env_btn_hl")
        self.add_env_button = QPushButton(self.env_group)
        self.add_env_button.setObjectName(u"add_env_button")
        self.add_env_button.setMinimumSize(QSize(0, 34))

        self.env_btn_hl.addWidget(self.add_env_button)

        self.env_btn_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.env_btn_hl.addItem(self.env_btn_spacer)

        self.del_env_button = QPushButton(self.env_group)
        self.del_env_button.setObjectName(u"del_env_button")
        self.del_env_button.setMinimumSize(QSize(0, 34))

        self.env_btn_hl.addWidget(self.del_env_button)


        self.env_inner_vl.addLayout(self.env_btn_hl)


        self.env_outer_vl.addWidget(self.env_group)

        self.env_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.env_outer_vl.addItem(self.env_bottom_spacer)

        self.Hyprland_Menu_Settings.addTab(self.env_tab, "")
        self.look_tab = QWidget()
        self.look_tab.setObjectName(u"look_tab")
        self.look_scroll_vl = QVBoxLayout(self.look_tab)
        self.look_scroll_vl.setSpacing(0)
        self.look_scroll_vl.setObjectName(u"look_scroll_vl")
        self.look_scroll_vl.setContentsMargins(0, 0, 0, 0)
        self.look_scroll_area = QScrollArea(self.look_tab)
        self.look_scroll_area.setObjectName(u"look_scroll_area")
        self.look_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.look_scroll_area.setWidgetResizable(True)
        self.look_scroll_contents = QWidget()
        self.look_scroll_contents.setObjectName(u"look_scroll_contents")
        self.look_scroll_contents.setGeometry(QRect(0, 0, 471, 678))
        self.look_contents_vl = QVBoxLayout(self.look_scroll_contents)
        self.look_contents_vl.setSpacing(16)
        self.look_contents_vl.setObjectName(u"look_contents_vl")
        self.look_contents_vl.setContentsMargins(24, 24, 24, 24)
        self.look_row1_hl = QHBoxLayout()
        self.look_row1_hl.setSpacing(16)
        self.look_row1_hl.setObjectName(u"look_row1_hl")
        self.general_group = QGroupBox(self.look_scroll_contents)
        self.general_group.setObjectName(u"general_group")
        self.general_form_layout = QFormLayout(self.general_group)
        self.general_form_layout.setObjectName(u"general_form_layout")
        self.general_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.general_form_layout.setHorizontalSpacing(16)
        self.general_form_layout.setVerticalSpacing(12)
        self.general_form_layout.setContentsMargins(16, 24, 16, 16)
        self.gaps_in_label = QLabel(self.general_group)
        self.gaps_in_label.setObjectName(u"gaps_in_label")

        self.general_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.gaps_in_label)

        self.gaps_in_spinBox = QSpinBox(self.general_group)
        self.gaps_in_spinBox.setObjectName(u"gaps_in_spinBox")
        sizePolicy2.setHeightForWidth(self.gaps_in_spinBox.sizePolicy().hasHeightForWidth())
        self.gaps_in_spinBox.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.gaps_in_spinBox)

        self.gaps_out_label = QLabel(self.general_group)
        self.gaps_out_label.setObjectName(u"gaps_out_label")

        self.general_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.gaps_out_label)

        self.gaps_out_spinBox = QSpinBox(self.general_group)
        self.gaps_out_spinBox.setObjectName(u"gaps_out_spinBox")
        sizePolicy2.setHeightForWidth(self.gaps_out_spinBox.sizePolicy().hasHeightForWidth())
        self.gaps_out_spinBox.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.gaps_out_spinBox)

        self.border_size_label = QLabel(self.general_group)
        self.border_size_label.setObjectName(u"border_size_label")

        self.general_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.border_size_label)

        self.border_size_spinBox = QSpinBox(self.general_group)
        self.border_size_spinBox.setObjectName(u"border_size_spinBox")
        sizePolicy2.setHeightForWidth(self.border_size_spinBox.sizePolicy().hasHeightForWidth())
        self.border_size_spinBox.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.border_size_spinBox)

        self.border_col_1_label = QLabel(self.general_group)
        self.border_col_1_label.setObjectName(u"border_col_1_label")

        self.general_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.border_col_1_label)

        self.set_color_1_button = QPushButton(self.general_group)
        self.set_color_1_button.setObjectName(u"set_color_1_button")
        sizePolicy2.setHeightForWidth(self.set_color_1_button.sizePolicy().hasHeightForWidth())
        self.set_color_1_button.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.set_color_1_button)

        self.border_col_2_label = QLabel(self.general_group)
        self.border_col_2_label.setObjectName(u"border_col_2_label")

        self.general_form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.border_col_2_label)

        self.set_color_2_button = QPushButton(self.general_group)
        self.set_color_2_button.setObjectName(u"set_color_2_button")
        sizePolicy2.setHeightForWidth(self.set_color_2_button.sizePolicy().hasHeightForWidth())
        self.set_color_2_button.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.set_color_2_button)

        self.angle_label = QLabel(self.general_group)
        self.angle_label.setObjectName(u"angle_label")

        self.general_form_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.angle_label)

        self.angle_spinBox = QSpinBox(self.general_group)
        self.angle_spinBox.setObjectName(u"angle_spinBox")
        sizePolicy2.setHeightForWidth(self.angle_spinBox.sizePolicy().hasHeightForWidth())
        self.angle_spinBox.setSizePolicy(sizePolicy2)
        self.angle_spinBox.setMaximum(360)

        self.general_form_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.angle_spinBox)

        self.layout_hyprland_label = QLabel(self.general_group)
        self.layout_hyprland_label.setObjectName(u"layout_hyprland_label")

        self.general_form_layout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.layout_hyprland_label)

        self.layout_comboBox = QComboBox(self.general_group)
        self.layout_comboBox.setObjectName(u"layout_comboBox")
        sizePolicy2.setHeightForWidth(self.layout_comboBox.sizePolicy().hasHeightForWidth())
        self.layout_comboBox.setSizePolicy(sizePolicy2)

        self.general_form_layout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.layout_comboBox)

        self.resize_checkbox = QCheckBox(self.general_group)
        self.resize_checkbox.setObjectName(u"resize_checkbox")

        self.general_form_layout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.resize_checkbox)

        self.allow_tearing_checkBox = QCheckBox(self.general_group)
        self.allow_tearing_checkBox.setObjectName(u"allow_tearing_checkBox")

        self.general_form_layout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.allow_tearing_checkBox)


        self.look_row1_hl.addWidget(self.general_group)

        self.decoration_group = QGroupBox(self.look_scroll_contents)
        self.decoration_group.setObjectName(u"decoration_group")
        self.decoration_form_layout = QFormLayout(self.decoration_group)
        self.decoration_form_layout.setObjectName(u"decoration_form_layout")
        self.decoration_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.decoration_form_layout.setHorizontalSpacing(16)
        self.decoration_form_layout.setVerticalSpacing(12)
        self.decoration_form_layout.setContentsMargins(16, 24, 16, 16)
        self.rounding_label = QLabel(self.decoration_group)
        self.rounding_label.setObjectName(u"rounding_label")

        self.decoration_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.rounding_label)

        self.rounding_spin_box = QSpinBox(self.decoration_group)
        self.rounding_spin_box.setObjectName(u"rounding_spin_box")
        sizePolicy2.setHeightForWidth(self.rounding_spin_box.sizePolicy().hasHeightForWidth())
        self.rounding_spin_box.setSizePolicy(sizePolicy2)

        self.decoration_form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.rounding_spin_box)

        self.rounding_power_label = QLabel(self.decoration_group)
        self.rounding_power_label.setObjectName(u"rounding_power_label")

        self.decoration_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.rounding_power_label)

        self.rounding_power_spin_box = QSpinBox(self.decoration_group)
        self.rounding_power_spin_box.setObjectName(u"rounding_power_spin_box")
        sizePolicy2.setHeightForWidth(self.rounding_power_spin_box.sizePolicy().hasHeightForWidth())
        self.rounding_power_spin_box.setSizePolicy(sizePolicy2)

        self.decoration_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.rounding_power_spin_box)

        self.active_op_label = QLabel(self.decoration_group)
        self.active_op_label.setObjectName(u"active_op_label")

        self.decoration_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.active_op_label)

        self.act_op_spin_box = QDoubleSpinBox(self.decoration_group)
        self.act_op_spin_box.setObjectName(u"act_op_spin_box")
        sizePolicy2.setHeightForWidth(self.act_op_spin_box.sizePolicy().hasHeightForWidth())
        self.act_op_spin_box.setSizePolicy(sizePolicy2)
        self.act_op_spin_box.setDecimals(1)
        self.act_op_spin_box.setMinimum(0.000000000000000)
        self.act_op_spin_box.setMaximum(1.000000000000000)
        self.act_op_spin_box.setSingleStep(0.100000000000000)

        self.decoration_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.act_op_spin_box)

        self.inact_op_label = QLabel(self.decoration_group)
        self.inact_op_label.setObjectName(u"inact_op_label")

        self.decoration_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.inact_op_label)

        self.inact_op_spin_box = QDoubleSpinBox(self.decoration_group)
        self.inact_op_spin_box.setObjectName(u"inact_op_spin_box")
        sizePolicy2.setHeightForWidth(self.inact_op_spin_box.sizePolicy().hasHeightForWidth())
        self.inact_op_spin_box.setSizePolicy(sizePolicy2)
        self.inact_op_spin_box.setDecimals(1)
        self.inact_op_spin_box.setMinimum(0.000000000000000)
        self.inact_op_spin_box.setMaximum(1.000000000000000)
        self.inact_op_spin_box.setSingleStep(0.100000000000000)

        self.decoration_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.inact_op_spin_box)


        self.look_row1_hl.addWidget(self.decoration_group)


        self.look_contents_vl.addLayout(self.look_row1_hl)

        self.look_row2_hl = QHBoxLayout()
        self.look_row2_hl.setSpacing(16)
        self.look_row2_hl.setObjectName(u"look_row2_hl")
        self.shadow_group = QGroupBox(self.look_scroll_contents)
        self.shadow_group.setObjectName(u"shadow_group")
        self.shadow_form_layout = QFormLayout(self.shadow_group)
        self.shadow_form_layout.setObjectName(u"shadow_form_layout")
        self.shadow_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.shadow_form_layout.setHorizontalSpacing(16)
        self.shadow_form_layout.setVerticalSpacing(12)
        self.shadow_form_layout.setContentsMargins(16, 24, 16, 16)
        self.shadow_enable_checkbox = QCheckBox(self.shadow_group)
        self.shadow_enable_checkbox.setObjectName(u"shadow_enable_checkbox")

        self.shadow_form_layout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.shadow_enable_checkbox)

        self.shadow_range_label = QLabel(self.shadow_group)
        self.shadow_range_label.setObjectName(u"shadow_range_label")

        self.shadow_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.shadow_range_label)

        self.shadow_range_spinbox = QSpinBox(self.shadow_group)
        self.shadow_range_spinbox.setObjectName(u"shadow_range_spinbox")
        sizePolicy2.setHeightForWidth(self.shadow_range_spinbox.sizePolicy().hasHeightForWidth())
        self.shadow_range_spinbox.setSizePolicy(sizePolicy2)

        self.shadow_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.shadow_range_spinbox)

        self.shadow_render_power_label = QLabel(self.shadow_group)
        self.shadow_render_power_label.setObjectName(u"shadow_render_power_label")

        self.shadow_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.shadow_render_power_label)

        self.shadow_render_power_spinbox = QSpinBox(self.shadow_group)
        self.shadow_render_power_spinbox.setObjectName(u"shadow_render_power_spinbox")
        sizePolicy2.setHeightForWidth(self.shadow_render_power_spinbox.sizePolicy().hasHeightForWidth())
        self.shadow_render_power_spinbox.setSizePolicy(sizePolicy2)

        self.shadow_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.shadow_render_power_spinbox)

        self.shadow_label_2 = QLabel(self.shadow_group)
        self.shadow_label_2.setObjectName(u"shadow_label_2")

        self.shadow_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.shadow_label_2)

        self.shadow_color_button = QPushButton(self.shadow_group)
        self.shadow_color_button.setObjectName(u"shadow_color_button")
        sizePolicy2.setHeightForWidth(self.shadow_color_button.sizePolicy().hasHeightForWidth())
        self.shadow_color_button.setSizePolicy(sizePolicy2)

        self.shadow_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.shadow_color_button)


        self.look_row2_hl.addWidget(self.shadow_group)

        self.blur_group = QGroupBox(self.look_scroll_contents)
        self.blur_group.setObjectName(u"blur_group")
        self.blur_form_layout = QFormLayout(self.blur_group)
        self.blur_form_layout.setObjectName(u"blur_form_layout")
        self.blur_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.blur_form_layout.setHorizontalSpacing(16)
        self.blur_form_layout.setVerticalSpacing(12)
        self.blur_form_layout.setContentsMargins(16, 24, 16, 16)
        self.blur_enable_checkBox = QCheckBox(self.blur_group)
        self.blur_enable_checkBox.setObjectName(u"blur_enable_checkBox")

        self.blur_form_layout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.blur_enable_checkBox)

        self.blur_size_label = QLabel(self.blur_group)
        self.blur_size_label.setObjectName(u"blur_size_label")

        self.blur_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.blur_size_label)

        self.blur_size_spinBox = QSpinBox(self.blur_group)
        self.blur_size_spinBox.setObjectName(u"blur_size_spinBox")
        sizePolicy2.setHeightForWidth(self.blur_size_spinBox.sizePolicy().hasHeightForWidth())
        self.blur_size_spinBox.setSizePolicy(sizePolicy2)

        self.blur_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.blur_size_spinBox)

        self.blur_passes_label = QLabel(self.blur_group)
        self.blur_passes_label.setObjectName(u"blur_passes_label")

        self.blur_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.blur_passes_label)

        self.blur_passes_spinBox = QSpinBox(self.blur_group)
        self.blur_passes_spinBox.setObjectName(u"blur_passes_spinBox")
        sizePolicy2.setHeightForWidth(self.blur_passes_spinBox.sizePolicy().hasHeightForWidth())
        self.blur_passes_spinBox.setSizePolicy(sizePolicy2)

        self.blur_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.blur_passes_spinBox)

        self.blur_vibrancy_label = QLabel(self.blur_group)
        self.blur_vibrancy_label.setObjectName(u"blur_vibrancy_label")

        self.blur_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.blur_vibrancy_label)

        self.blur_vib_doubleSpinBox = QDoubleSpinBox(self.blur_group)
        self.blur_vib_doubleSpinBox.setObjectName(u"blur_vib_doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.blur_vib_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.blur_vib_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.blur_vib_doubleSpinBox.setDecimals(4)

        self.blur_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.blur_vib_doubleSpinBox)


        self.look_row2_hl.addWidget(self.blur_group)


        self.look_contents_vl.addLayout(self.look_row2_hl)

        self.look_default_hl = QHBoxLayout()
        self.look_default_hl.setSpacing(8)
        self.look_default_hl.setObjectName(u"look_default_hl")
        self.set_default_look_button = QPushButton(self.look_scroll_contents)
        self.set_default_look_button.setObjectName(u"set_default_look_button")
        self.set_default_look_button.setMinimumSize(QSize(120, 34))

        self.look_default_hl.addWidget(self.set_default_look_button)

        self.look_default_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.look_default_hl.addItem(self.look_default_spacer)


        self.look_contents_vl.addLayout(self.look_default_hl)

        self.look_bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.look_contents_vl.addItem(self.look_bottom_spacer)

        self.look_scroll_area.setWidget(self.look_scroll_contents)

        self.look_scroll_vl.addWidget(self.look_scroll_area)

        self.Hyprland_Menu_Settings.addTab(self.look_tab, "")
        self.input_tab = QWidget()
        self.input_tab.setObjectName(u"input_tab")
        self.input_outer_vl = QVBoxLayout(self.input_tab)
        self.input_outer_vl.setSpacing(16)
        self.input_outer_vl.setObjectName(u"input_outer_vl")
        self.input_outer_vl.setContentsMargins(24, 24, 24, 24)
        self.input_row1_hl = QHBoxLayout()
        self.input_row1_hl.setSpacing(16)
        self.input_row1_hl.setObjectName(u"input_row1_hl")
        self.keyboard_groupBox = QGroupBox(self.input_tab)
        self.keyboard_groupBox.setObjectName(u"keyboard_groupBox")
        self.keyboard_form_layout = QFormLayout(self.keyboard_groupBox)
        self.keyboard_form_layout.setObjectName(u"keyboard_form_layout")
        self.keyboard_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.keyboard_form_layout.setHorizontalSpacing(16)
        self.keyboard_form_layout.setVerticalSpacing(12)
        self.keyboard_form_layout.setContentsMargins(16, 24, 16, 16)
        self.kb_layout_label = QLabel(self.keyboard_groupBox)
        self.kb_layout_label.setObjectName(u"kb_layout_label")

        self.keyboard_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kb_layout_label)

        self.kb_layout_comboBox = QComboBox(self.keyboard_groupBox)
        self.kb_layout_comboBox.setObjectName(u"kb_layout_comboBox")
        sizePolicy2.setHeightForWidth(self.kb_layout_comboBox.sizePolicy().hasHeightForWidth())
        self.kb_layout_comboBox.setSizePolicy(sizePolicy2)

        self.keyboard_form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kb_layout_comboBox)

        self.kb_variant_label = QLabel(self.keyboard_groupBox)
        self.kb_variant_label.setObjectName(u"kb_variant_label")

        self.keyboard_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.kb_variant_label)

        self.kb_variant_comboBox = QComboBox(self.keyboard_groupBox)
        self.kb_variant_comboBox.setObjectName(u"kb_variant_comboBox")
        sizePolicy2.setHeightForWidth(self.kb_variant_comboBox.sizePolicy().hasHeightForWidth())
        self.kb_variant_comboBox.setSizePolicy(sizePolicy2)

        self.keyboard_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.kb_variant_comboBox)

        self.kb_model_label = QLabel(self.keyboard_groupBox)
        self.kb_model_label.setObjectName(u"kb_model_label")

        self.keyboard_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.kb_model_label)

        self.kb_model_comboBox = QComboBox(self.keyboard_groupBox)
        self.kb_model_comboBox.setObjectName(u"kb_model_comboBox")
        sizePolicy2.setHeightForWidth(self.kb_model_comboBox.sizePolicy().hasHeightForWidth())
        self.kb_model_comboBox.setSizePolicy(sizePolicy2)

        self.keyboard_form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.kb_model_comboBox)

        self.kb_options_label = QLabel(self.keyboard_groupBox)
        self.kb_options_label.setObjectName(u"kb_options_label")

        self.keyboard_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kb_options_label)

        self.kb_options_comboBox = QComboBox(self.keyboard_groupBox)
        self.kb_options_comboBox.setObjectName(u"kb_options_comboBox")
        sizePolicy2.setHeightForWidth(self.kb_options_comboBox.sizePolicy().hasHeightForWidth())
        self.kb_options_comboBox.setSizePolicy(sizePolicy2)

        self.keyboard_form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kb_options_comboBox)

        self.kb_rules_label = QLabel(self.keyboard_groupBox)
        self.kb_rules_label.setObjectName(u"kb_rules_label")

        self.keyboard_form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.kb_rules_label)

        self.kb_rules_comboBox = QComboBox(self.keyboard_groupBox)
        self.kb_rules_comboBox.setObjectName(u"kb_rules_comboBox")
        sizePolicy2.setHeightForWidth(self.kb_rules_comboBox.sizePolicy().hasHeightForWidth())
        self.kb_rules_comboBox.setSizePolicy(sizePolicy2)

        self.keyboard_form_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.kb_rules_comboBox)


        self.input_row1_hl.addWidget(self.keyboard_groupBox)

        self.input_right_vl = QVBoxLayout()
        self.input_right_vl.setSpacing(16)
        self.input_right_vl.setObjectName(u"input_right_vl")
        self.mouse_groupbox = QGroupBox(self.input_tab)
        self.mouse_groupbox.setObjectName(u"mouse_groupbox")
        self.mouse_form_layout = QFormLayout(self.mouse_groupbox)
        self.mouse_form_layout.setObjectName(u"mouse_form_layout")
        self.mouse_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.mouse_form_layout.setHorizontalSpacing(16)
        self.mouse_form_layout.setVerticalSpacing(12)
        self.mouse_form_layout.setContentsMargins(16, 24, 16, 16)
        self.follow_mouse_label = QLabel(self.mouse_groupbox)
        self.follow_mouse_label.setObjectName(u"follow_mouse_label")

        self.mouse_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.follow_mouse_label)

        self.follow_mouse_comboBox = QComboBox(self.mouse_groupbox)
        self.follow_mouse_comboBox.setObjectName(u"follow_mouse_comboBox")
        sizePolicy2.setHeightForWidth(self.follow_mouse_comboBox.sizePolicy().hasHeightForWidth())
        self.follow_mouse_comboBox.setSizePolicy(sizePolicy2)

        self.mouse_form_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.follow_mouse_comboBox)

        self.mouse_sens_label = QLabel(self.mouse_groupbox)
        self.mouse_sens_label.setObjectName(u"mouse_sens_label")

        self.mouse_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mouse_sens_label)

        self.mouse_sens_doubleSpinBox = QDoubleSpinBox(self.mouse_groupbox)
        self.mouse_sens_doubleSpinBox.setObjectName(u"mouse_sens_doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.mouse_sens_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.mouse_sens_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.mouse_sens_doubleSpinBox.setDecimals(1)
        self.mouse_sens_doubleSpinBox.setMinimum(-1.000000000000000)
        self.mouse_sens_doubleSpinBox.setMaximum(1.000000000000000)
        self.mouse_sens_doubleSpinBox.setSingleStep(0.100000000000000)

        self.mouse_form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.mouse_sens_doubleSpinBox)

        self.mouse_natural_scroll_checkBox = QCheckBox(self.mouse_groupbox)
        self.mouse_natural_scroll_checkBox.setObjectName(u"mouse_natural_scroll_checkBox")

        self.mouse_form_layout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.mouse_natural_scroll_checkBox)


        self.input_right_vl.addWidget(self.mouse_groupbox)

        self.touchpad_groupbox = QGroupBox(self.input_tab)
        self.touchpad_groupbox.setObjectName(u"touchpad_groupbox")
        self.touchpad_inner_vl = QVBoxLayout(self.touchpad_groupbox)
        self.touchpad_inner_vl.setSpacing(12)
        self.touchpad_inner_vl.setObjectName(u"touchpad_inner_vl")
        self.touchpad_inner_vl.setContentsMargins(16, 24, 16, 16)
        self.touchpad_nat_scroll_checkbox = QCheckBox(self.touchpad_groupbox)
        self.touchpad_nat_scroll_checkbox.setObjectName(u"touchpad_nat_scroll_checkbox")

        self.touchpad_inner_vl.addWidget(self.touchpad_nat_scroll_checkbox)


        self.input_right_vl.addWidget(self.touchpad_groupbox)

        self.input_right_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.input_right_vl.addItem(self.input_right_spacer)


        self.input_row1_hl.addLayout(self.input_right_vl)


        self.input_outer_vl.addLayout(self.input_row1_hl)

        self.input_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.input_outer_vl.addItem(self.input_bottom_spacer)

        self.Hyprland_Menu_Settings.addTab(self.input_tab, "")
        self.keybinds_tab = QWidget()
        self.keybinds_tab.setObjectName(u"keybinds_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.keybinds_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keybinds_tabWidget = QTabWidget(self.keybinds_tab)
        self.keybinds_tabWidget.setObjectName(u"keybinds_tabWidget")
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.verticalLayout_8 = QVBoxLayout(self.general_tab)
        self.verticalLayout_8.setSpacing(16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(24, 24, 24, 24)
        self.general_layout = QVBoxLayout()
        self.general_layout.setSpacing(12)
        self.general_layout.setObjectName(u"general_layout")
        self.general_list = QListWidget(self.general_tab)
        self.general_list.setObjectName(u"general_list")

        self.general_layout.addWidget(self.general_list)

        self.general_button_layout = QHBoxLayout()
        self.general_button_layout.setSpacing(8)
        self.general_button_layout.setObjectName(u"general_button_layout")
        self.set_default_general_keybind_button = QPushButton(self.general_tab)
        self.set_default_general_keybind_button.setObjectName(u"set_default_general_keybind_button")
        self.set_default_general_keybind_button.setMinimumSize(QSize(120, 34))

        self.general_button_layout.addWidget(self.set_default_general_keybind_button)

        self.general_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.general_button_layout.addItem(self.general_spacer)

        self.general_add_button = QPushButton(self.general_tab)
        self.general_add_button.setObjectName(u"general_add_button")
        self.general_add_button.setMinimumSize(QSize(80, 34))

        self.general_button_layout.addWidget(self.general_add_button)

        self.delete_keybind_button = QPushButton(self.general_tab)
        self.delete_keybind_button.setObjectName(u"delete_keybind_button")
        self.delete_keybind_button.setMinimumSize(QSize(80, 34))

        self.general_button_layout.addWidget(self.delete_keybind_button)


        self.general_layout.addLayout(self.general_button_layout)


        self.verticalLayout_8.addLayout(self.general_layout)

        self.general_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.general_bottom_spacer)

        self.keybinds_tabWidget.addTab(self.general_tab, "")
        self.movement_tab = QWidget()
        self.movement_tab.setObjectName(u"movement_tab")
        self.verticalLayout_14 = QVBoxLayout(self.movement_tab)
        self.verticalLayout_14.setSpacing(16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(24, 24, 24, 24)
        self.movement_layout = QVBoxLayout()
        self.movement_layout.setSpacing(12)
        self.movement_layout.setObjectName(u"movement_layout")
        self.movement_list = QListWidget(self.movement_tab)
        self.movement_list.setObjectName(u"movement_list")

        self.movement_layout.addWidget(self.movement_list)

        self.movement_button_layout = QHBoxLayout()
        self.movement_button_layout.setSpacing(8)
        self.movement_button_layout.setObjectName(u"movement_button_layout")
        self.set_default_movement_button = QPushButton(self.movement_tab)
        self.set_default_movement_button.setObjectName(u"set_default_movement_button")
        self.set_default_movement_button.setMinimumSize(QSize(120, 34))

        self.movement_button_layout.addWidget(self.set_default_movement_button)

        self.movement_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.movement_button_layout.addItem(self.movement_spacer)

        self.movement_add_button = QPushButton(self.movement_tab)
        self.movement_add_button.setObjectName(u"movement_add_button")
        self.movement_add_button.setMinimumSize(QSize(80, 34))

        self.movement_button_layout.addWidget(self.movement_add_button)

        self.delete_movement_button = QPushButton(self.movement_tab)
        self.delete_movement_button.setObjectName(u"delete_movement_button")
        self.delete_movement_button.setMinimumSize(QSize(80, 34))

        self.movement_button_layout.addWidget(self.delete_movement_button)


        self.movement_layout.addLayout(self.movement_button_layout)


        self.verticalLayout_14.addLayout(self.movement_layout)

        self.movement_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.movement_bottom_spacer)

        self.keybinds_tabWidget.addTab(self.movement_tab, "")
        self.workspaces_tab = QWidget()
        self.workspaces_tab.setObjectName(u"workspaces_tab")
        self.verticalLayout_15 = QVBoxLayout(self.workspaces_tab)
        self.verticalLayout_15.setSpacing(16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(24, 24, 24, 24)
        self.workspace_layout = QVBoxLayout()
        self.workspace_layout.setSpacing(12)
        self.workspace_layout.setObjectName(u"workspace_layout")
        self.workspaces_list = QListWidget(self.workspaces_tab)
        self.workspaces_list.setObjectName(u"workspaces_list")

        self.workspace_layout.addWidget(self.workspaces_list)

        self.workspace_button_layout = QHBoxLayout()
        self.workspace_button_layout.setSpacing(8)
        self.workspace_button_layout.setObjectName(u"workspace_button_layout")
        self.set_default_workspace_button = QPushButton(self.workspaces_tab)
        self.set_default_workspace_button.setObjectName(u"set_default_workspace_button")
        self.set_default_workspace_button.setMinimumSize(QSize(120, 34))

        self.workspace_button_layout.addWidget(self.set_default_workspace_button)

        self.workspace_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.workspace_button_layout.addItem(self.workspace_spacer)

        self.workspace_add_button = QPushButton(self.workspaces_tab)
        self.workspace_add_button.setObjectName(u"workspace_add_button")
        self.workspace_add_button.setMinimumSize(QSize(80, 34))

        self.workspace_button_layout.addWidget(self.workspace_add_button)

        self.delete_workspace_button = QPushButton(self.workspaces_tab)
        self.delete_workspace_button.setObjectName(u"delete_workspace_button")
        self.delete_workspace_button.setMinimumSize(QSize(80, 34))

        self.workspace_button_layout.addWidget(self.delete_workspace_button)


        self.workspace_layout.addLayout(self.workspace_button_layout)


        self.verticalLayout_15.addLayout(self.workspace_layout)

        self.workspace_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.workspace_bottom_spacer)

        self.keybinds_tabWidget.addTab(self.workspaces_tab, "")
        self.multimedia_tab = QWidget()
        self.multimedia_tab.setObjectName(u"multimedia_tab")
        self.verticalLayout_16 = QVBoxLayout(self.multimedia_tab)
        self.verticalLayout_16.setSpacing(16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(24, 24, 24, 24)
        self.multimedia_layout = QVBoxLayout()
        self.multimedia_layout.setSpacing(12)
        self.multimedia_layout.setObjectName(u"multimedia_layout")
        self.multimedia_list = QListWidget(self.multimedia_tab)
        self.multimedia_list.setObjectName(u"multimedia_list")

        self.multimedia_layout.addWidget(self.multimedia_list)

        self.multimedia_button_layout = QHBoxLayout()
        self.multimedia_button_layout.setSpacing(8)
        self.multimedia_button_layout.setObjectName(u"multimedia_button_layout")
        self.set_default_multimedia_button = QPushButton(self.multimedia_tab)
        self.set_default_multimedia_button.setObjectName(u"set_default_multimedia_button")
        self.set_default_multimedia_button.setMinimumSize(QSize(120, 34))

        self.multimedia_button_layout.addWidget(self.set_default_multimedia_button)

        self.multimedia_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.multimedia_button_layout.addItem(self.multimedia_spacer)

        self.multimedia_add_button = QPushButton(self.multimedia_tab)
        self.multimedia_add_button.setObjectName(u"multimedia_add_button")
        self.multimedia_add_button.setMinimumSize(QSize(80, 34))

        self.multimedia_button_layout.addWidget(self.multimedia_add_button)

        self.delete_multimedia_button = QPushButton(self.multimedia_tab)
        self.delete_multimedia_button.setObjectName(u"delete_multimedia_button")
        self.delete_multimedia_button.setMinimumSize(QSize(80, 34))

        self.multimedia_button_layout.addWidget(self.delete_multimedia_button)


        self.multimedia_layout.addLayout(self.multimedia_button_layout)


        self.verticalLayout_16.addLayout(self.multimedia_layout)

        self.multimedia_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.multimedia_bottom_spacer)

        self.keybinds_tabWidget.addTab(self.multimedia_tab, "")

        self.horizontalLayout_2.addWidget(self.keybinds_tabWidget)

        self.Hyprland_Menu_Settings.addTab(self.keybinds_tab, "")
        self.windowrules_tab = QWidget()
        self.windowrules_tab.setObjectName(u"windowrules_tab")
        self.windowrules_outer_vl = QVBoxLayout(self.windowrules_tab)
        self.windowrules_outer_vl.setSpacing(16)
        self.windowrules_outer_vl.setObjectName(u"windowrules_outer_vl")
        self.windowrules_outer_vl.setContentsMargins(24, 24, 24, 24)
        self.windowrules_group = QGroupBox(self.windowrules_tab)
        self.windowrules_group.setObjectName(u"windowrules_group")
        self.windowrules_inner_vl = QVBoxLayout(self.windowrules_group)
        self.windowrules_inner_vl.setSpacing(12)
        self.windowrules_inner_vl.setObjectName(u"windowrules_inner_vl")
        self.windowrules_inner_vl.setContentsMargins(16, 24, 16, 16)
        self.window_rule_listWidget = QListWidget(self.windowrules_group)
        self.window_rule_listWidget.setObjectName(u"window_rule_listWidget")

        self.windowrules_inner_vl.addWidget(self.window_rule_listWidget)

        self.windowrules_btn_hl = QHBoxLayout()
        self.windowrules_btn_hl.setSpacing(8)
        self.windowrules_btn_hl.setObjectName(u"windowrules_btn_hl")
        self.add_window_rule_button = QPushButton(self.windowrules_group)
        self.add_window_rule_button.setObjectName(u"add_window_rule_button")
        self.add_window_rule_button.setMinimumSize(QSize(0, 34))

        self.windowrules_btn_hl.addWidget(self.add_window_rule_button)

        self.windowrules_btn_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.windowrules_btn_hl.addItem(self.windowrules_btn_spacer)

        self.edit_window_rule_button = QPushButton(self.windowrules_group)
        self.edit_window_rule_button.setObjectName(u"edit_window_rule_button")
        self.edit_window_rule_button.setMinimumSize(QSize(0, 34))

        self.windowrules_btn_hl.addWidget(self.edit_window_rule_button)

        self.delete_window_rule_button = QPushButton(self.windowrules_group)
        self.delete_window_rule_button.setObjectName(u"delete_window_rule_button")
        self.delete_window_rule_button.setMinimumSize(QSize(0, 34))

        self.windowrules_btn_hl.addWidget(self.delete_window_rule_button)


        self.windowrules_inner_vl.addLayout(self.windowrules_btn_hl)


        self.windowrules_outer_vl.addWidget(self.windowrules_group)

        self.windowrules_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.windowrules_outer_vl.addItem(self.windowrules_bottom_spacer)

        self.Hyprland_Menu_Settings.addTab(self.windowrules_tab, "")
        self.files_tab = QWidget()
        self.files_tab.setObjectName(u"files_tab")
        self.verticalLayout_10 = QVBoxLayout(self.files_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.config_files_group = QGroupBox(self.files_tab)
        self.config_files_group.setObjectName(u"config_files_group")
        self.configs_form_layout = QFormLayout(self.config_files_group)
        self.configs_form_layout.setObjectName(u"configs_form_layout")
        self.configs_form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.configs_form_layout.setHorizontalSpacing(16)
        self.configs_form_layout.setVerticalSpacing(14)
        self.configs_form_layout.setContentsMargins(20, 24, 20, 20)
        self.current_config_file_label = QLabel(self.config_files_group)
        self.current_config_file_label.setObjectName(u"current_config_file_label")

        self.configs_form_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.current_config_file_label)

        self.config_file_button_layout = QHBoxLayout()
        self.config_file_button_layout.setSpacing(10)
        self.config_file_button_layout.setObjectName(u"config_file_button_layout")
        self.choose_config_file_button = QPushButton(self.config_files_group)
        self.choose_config_file_button.setObjectName(u"choose_config_file_button")

        self.config_file_button_layout.addWidget(self.choose_config_file_button)

        self.current_config_path_label = QLabel(self.config_files_group)
        self.current_config_path_label.setObjectName(u"current_config_path_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.current_config_path_label.sizePolicy().hasHeightForWidth())
        self.current_config_path_label.setSizePolicy(sizePolicy3)

        self.config_file_button_layout.addWidget(self.current_config_path_label)


        self.configs_form_layout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.config_file_button_layout)

        self.cur_hyprlock_label = QLabel(self.config_files_group)
        self.cur_hyprlock_label.setObjectName(u"cur_hyprlock_label")

        self.configs_form_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.cur_hyprlock_label)

        self.hyprlock_button_layout = QHBoxLayout()
        self.hyprlock_button_layout.setSpacing(10)
        self.hyprlock_button_layout.setObjectName(u"hyprlock_button_layout")
        self.choose_hyprlock_button = QPushButton(self.config_files_group)
        self.choose_hyprlock_button.setObjectName(u"choose_hyprlock_button")

        self.hyprlock_button_layout.addWidget(self.choose_hyprlock_button)

        self.cur_hyprlock_file_label = QLabel(self.config_files_group)
        self.cur_hyprlock_file_label.setObjectName(u"cur_hyprlock_file_label")
        sizePolicy3.setHeightForWidth(self.cur_hyprlock_file_label.sizePolicy().hasHeightForWidth())
        self.cur_hyprlock_file_label.setSizePolicy(sizePolicy3)

        self.hyprlock_button_layout.addWidget(self.cur_hyprlock_file_label)


        self.configs_form_layout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.hyprlock_button_layout)

        self.cur_hyprsunset_label = QLabel(self.config_files_group)
        self.cur_hyprsunset_label.setObjectName(u"cur_hyprsunset_label")

        self.configs_form_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.cur_hyprsunset_label)

        self.hyprsunset_button_layout = QHBoxLayout()
        self.hyprsunset_button_layout.setSpacing(10)
        self.hyprsunset_button_layout.setObjectName(u"hyprsunset_button_layout")
        self.choose_hypersunset_button = QPushButton(self.config_files_group)
        self.choose_hypersunset_button.setObjectName(u"choose_hypersunset_button")

        self.hyprsunset_button_layout.addWidget(self.choose_hypersunset_button)

        self.hyprsunset_file_label = QLabel(self.config_files_group)
        self.hyprsunset_file_label.setObjectName(u"hyprsunset_file_label")
        sizePolicy3.setHeightForWidth(self.hyprsunset_file_label.sizePolicy().hasHeightForWidth())
        self.hyprsunset_file_label.setSizePolicy(sizePolicy3)

        self.hyprsunset_button_layout.addWidget(self.hyprsunset_file_label)


        self.configs_form_layout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.hyprsunset_button_layout)

        self.cur_hyprpaper_label = QLabel(self.config_files_group)
        self.cur_hyprpaper_label.setObjectName(u"cur_hyprpaper_label")

        self.configs_form_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.cur_hyprpaper_label)

        self.hyprpaper_button_layout = QHBoxLayout()
        self.hyprpaper_button_layout.setSpacing(10)
        self.hyprpaper_button_layout.setObjectName(u"hyprpaper_button_layout")
        self.choose_hyperpaper_file_button = QPushButton(self.config_files_group)
        self.choose_hyperpaper_file_button.setObjectName(u"choose_hyperpaper_file_button")

        self.hyprpaper_button_layout.addWidget(self.choose_hyperpaper_file_button)

        self.cur_hyprpaper_file_label = QLabel(self.config_files_group)
        self.cur_hyprpaper_file_label.setObjectName(u"cur_hyprpaper_file_label")
        sizePolicy3.setHeightForWidth(self.cur_hyprpaper_file_label.sizePolicy().hasHeightForWidth())
        self.cur_hyprpaper_file_label.setSizePolicy(sizePolicy3)

        self.hyprpaper_button_layout.addWidget(self.cur_hyprpaper_file_label)


        self.configs_form_layout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.hyprpaper_button_layout)

        self.hypridle_label = QLabel(self.config_files_group)
        self.hypridle_label.setObjectName(u"hypridle_label")

        self.configs_form_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.hypridle_label)

        self.hypridle_button_layout = QHBoxLayout()
        self.hypridle_button_layout.setSpacing(10)
        self.hypridle_button_layout.setObjectName(u"hypridle_button_layout")
        self.choose_hypridle_button = QPushButton(self.config_files_group)
        self.choose_hypridle_button.setObjectName(u"choose_hypridle_button")

        self.hypridle_button_layout.addWidget(self.choose_hypridle_button)

        self.cur_hypridle_label = QLabel(self.config_files_group)
        self.cur_hypridle_label.setObjectName(u"cur_hypridle_label")
        sizePolicy3.setHeightForWidth(self.cur_hypridle_label.sizePolicy().hasHeightForWidth())
        self.cur_hypridle_label.setSizePolicy(sizePolicy3)

        self.hypridle_button_layout.addWidget(self.cur_hypridle_label)


        self.configs_form_layout.setLayout(4, QFormLayout.ItemRole.FieldRole, self.hypridle_button_layout)


        self.verticalLayout_5.addWidget(self.config_files_group)

        self.files_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.files_bottom_spacer)


        self.verticalLayout_10.addLayout(self.verticalLayout_5)

        self.Hyprland_Menu_Settings.addTab(self.files_tab, "")

        self.verticalLayout.addWidget(self.Hyprland_Menu_Settings)

        self.stackedWidget.addWidget(self.hyprland_page)
        self.defaul_apps_page = QWidget()
        self.defaul_apps_page.setObjectName(u"defaul_apps_page")
        self.label = QLabel(self.defaul_apps_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 270, 191, 41))
        self.stackedWidget.addWidget(self.defaul_apps_page)
        self.ecosystem_page = QWidget()
        self.ecosystem_page.setObjectName(u"ecosystem_page")
        self.verticalLayout_4 = QVBoxLayout(self.ecosystem_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ecosystem_tabWidget = QTabWidget(self.ecosystem_page)
        self.ecosystem_tabWidget.setObjectName(u"ecosystem_tabWidget")
        self.hyprlock_tab = QWidget()
        self.hyprlock_tab.setObjectName(u"hyprlock_tab")
        self.hyprlock_tab_vl = QVBoxLayout(self.hyprlock_tab)
        self.hyprlock_tab_vl.setObjectName(u"hyprlock_tab_vl")
        self.hyprlock_tab_vl.setContentsMargins(24, 24, 24, 24)
        self.hyprlock_placeholder_label = QLabel(self.hyprlock_tab)
        self.hyprlock_placeholder_label.setObjectName(u"hyprlock_placeholder_label")
        self.hyprlock_placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hyprlock_tab_vl.addWidget(self.hyprlock_placeholder_label)

        self.ecosystem_tabWidget.addTab(self.hyprlock_tab, "")
        self.hypridle_tab = QWidget()
        self.hypridle_tab.setObjectName(u"hypridle_tab")
        self.ecosystem_tabWidget.addTab(self.hypridle_tab, "")
        self.hyprsunset_tab = QWidget()
        self.hyprsunset_tab.setObjectName(u"hyprsunset_tab")
        self.hyprsunset_tab_vl = QVBoxLayout(self.hyprsunset_tab)
        self.hyprsunset_tab_vl.setObjectName(u"hyprsunset_tab_vl")
        self.hyprsunset_tab_vl.setContentsMargins(24, 24, 24, 24)
        self.hyprsunset_placeholder_label = QLabel(self.hyprsunset_tab)
        self.hyprsunset_placeholder_label.setObjectName(u"hyprsunset_placeholder_label")
        self.hyprsunset_placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hyprsunset_tab_vl.addWidget(self.hyprsunset_placeholder_label)

        self.ecosystem_tabWidget.addTab(self.hyprsunset_tab, "")
        self.hyprpaper_tab = QWidget()
        self.hyprpaper_tab.setObjectName(u"hyprpaper_tab")
        self.hyprpaper_tab_vl = QVBoxLayout(self.hyprpaper_tab)
        self.hyprpaper_tab_vl.setObjectName(u"hyprpaper_tab_vl")
        self.hyprpaper_tab_vl.setContentsMargins(24, 24, 24, 24)
        self.hyprpaper_placeholder_label = QLabel(self.hyprpaper_tab)
        self.hyprpaper_placeholder_label.setObjectName(u"hyprpaper_placeholder_label")
        self.hyprpaper_placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hyprpaper_tab_vl.addWidget(self.hyprpaper_placeholder_label)

        self.ecosystem_tabWidget.addTab(self.hyprpaper_tab, "")

        self.verticalLayout_4.addWidget(self.ecosystem_tabWidget)

        self.stackedWidget.addWidget(self.ecosystem_page)
        self.network_page = QWidget()
        self.network_page.setObjectName(u"network_page")
        self.verticalLayout_3 = QVBoxLayout(self.network_page)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, 24, 24, 24)
        self.wifi_group = QGroupBox(self.network_page)
        self.wifi_group.setObjectName(u"wifi_group")
        self.network_layout = QVBoxLayout(self.wifi_group)
        self.network_layout.setSpacing(12)
        self.network_layout.setObjectName(u"network_layout")
        self.network_layout.setContentsMargins(16, 24, 16, 16)
        self.wifi_list = QListWidget(self.wifi_group)
        self.wifi_list.setObjectName(u"wifi_list")

        self.network_layout.addWidget(self.wifi_list)

        self.wifi_btn_hl = QHBoxLayout()
        self.wifi_btn_hl.setSpacing(8)
        self.wifi_btn_hl.setObjectName(u"wifi_btn_hl")
        self.wifi_refresh_button = QPushButton(self.wifi_group)
        self.wifi_refresh_button.setObjectName(u"wifi_refresh_button")

        self.wifi_btn_hl.addWidget(self.wifi_refresh_button)

        self.wifi_btn_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.wifi_btn_hl.addItem(self.wifi_btn_spacer)

        self.wifi_disconnect_button = QPushButton(self.wifi_group)
        self.wifi_disconnect_button.setObjectName(u"wifi_disconnect_button")

        self.wifi_btn_hl.addWidget(self.wifi_disconnect_button)


        self.network_layout.addLayout(self.wifi_btn_hl)


        self.verticalLayout_3.addWidget(self.wifi_group)

        self.network_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.network_bottom_spacer)

        self.stackedWidget.addWidget(self.network_page)
        self.wallpaper_page = QWidget()
        self.wallpaper_page.setObjectName(u"wallpaper_page")
        self.verticalLayout_6 = QVBoxLayout(self.wallpaper_page)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(24, 20, 24, 24)
        self.wallpaper_layout = QVBoxLayout()
        self.wallpaper_layout.setSpacing(12)
        self.wallpaper_layout.setObjectName(u"wallpaper_layout")
        self.choose_folder_layout = QHBoxLayout()
        self.choose_folder_layout.setObjectName(u"choose_folder_layout")
        self.choose_folder_button = QPushButton(self.wallpaper_page)
        self.choose_folder_button.setObjectName(u"choose_folder_button")
        self.choose_folder_button.setMinimumSize(QSize(0, 36))

        self.choose_folder_layout.addWidget(self.choose_folder_button)

        self.folder_label = QLabel(self.wallpaper_page)
        self.folder_label.setObjectName(u"folder_label")

        self.choose_folder_layout.addWidget(self.folder_label)

        self.choose_folder_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.choose_folder_layout.addItem(self.choose_folder_horizontalSpacer)


        self.wallpaper_layout.addLayout(self.choose_folder_layout)

        self.gallery = QListWidget(self.wallpaper_page)
        self.gallery.setObjectName(u"gallery")

        self.wallpaper_layout.addWidget(self.gallery)


        self.verticalLayout_6.addLayout(self.wallpaper_layout)

        self.stackedWidget.addWidget(self.wallpaper_page)
        self.font_cursor_page = QWidget()
        self.font_cursor_page.setObjectName(u"font_cursor_page")
        self.stackedWidget.addWidget(self.font_cursor_page)
        self.plugins_page = QWidget()
        self.plugins_page.setObjectName(u"plugins_page")
        self.verticalLayout_7 = QVBoxLayout(self.plugins_page)
        self.verticalLayout_7.setSpacing(16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(24, 20, 24, 24)
        self.plugins_layout = QVBoxLayout()
        self.plugins_layout.setSpacing(12)
        self.plugins_layout.setObjectName(u"plugins_layout")
        self.plugins_list = QListWidget(self.plugins_page)
        QListWidgetItem(self.plugins_list)
        QListWidgetItem(self.plugins_list)
        QListWidgetItem(self.plugins_list)
        QListWidgetItem(self.plugins_list)
        self.plugins_list.setObjectName(u"plugins_list")

        self.plugins_layout.addWidget(self.plugins_list)

        self.plugins_button_layout = QHBoxLayout()
        self.plugins_button_layout.setObjectName(u"plugins_button_layout")
        self.install_button = QPushButton(self.plugins_page)
        self.install_button.setObjectName(u"install_button")
        self.install_button.setMinimumSize(QSize(0, 36))

        self.plugins_button_layout.addWidget(self.install_button)

        self.uninstall_button = QPushButton(self.plugins_page)
        self.uninstall_button.setObjectName(u"uninstall_button")
        self.uninstall_button.setMinimumSize(QSize(0, 36))

        self.plugins_button_layout.addWidget(self.uninstall_button)

        self.plugins_button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.plugins_button_layout.addItem(self.plugins_button_spacer)

        self.enable_button = QPushButton(self.plugins_page)
        self.enable_button.setObjectName(u"enable_button")
        self.enable_button.setMinimumSize(QSize(0, 36))

        self.plugins_button_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton(self.plugins_page)
        self.disable_button.setObjectName(u"disable_button")
        self.disable_button.setMinimumSize(QSize(0, 36))

        self.plugins_button_layout.addWidget(self.disable_button)


        self.plugins_layout.addLayout(self.plugins_button_layout)


        self.verticalLayout_7.addLayout(self.plugins_layout)

        self.stackedWidget.addWidget(self.plugins_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.verticalLayout_2 = QVBoxLayout(self.update_page)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.update_pushButton = QPushButton(self.update_page)
        self.update_pushButton.setObjectName(u"update_pushButton")
        self.update_pushButton.setMinimumSize(QSize(140, 36))

        self.verticalLayout_2.addWidget(self.update_pushButton)

        self.update_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.update_bottom_spacer)

        self.stackedWidget.addWidget(self.update_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        Widget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Widget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 19))
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
        self.menuTheme.addAction(self.dark_theme_button)
        self.menuTheme.addAction(self.light_theme_button)
        self.menu_Application.addAction(self.actionRestart)
        self.menu_Application.addAction(self.actionHelp)
        self.menu_Application.addAction(self.quit_program)

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)
        self.Hyprland_Menu_Settings.setCurrentIndex(6)
        self.keybinds_tabWidget.setCurrentIndex(0)
        self.ecosystem_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Hyprland Settings", None))
        self.dark_theme_button.setText(QCoreApplication.translate("Widget", u"Dark", None))
        self.light_theme_button.setText(QCoreApplication.translate("Widget", u"Light", None))
        self.quit_program.setText(QCoreApplication.translate("Widget", u"Quit", None))
        self.actionHelp.setText(QCoreApplication.translate("Widget", u"Help", None))
        self.actionRestart.setText(QCoreApplication.translate("Widget", u"Restart", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Widget", u"Hyprland", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Widget", u"Default Apps", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Widget", u"Ecosystem", None))
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Widget", u"Network", None))
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Widget", u"Wallpaper", None))
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Widget", u"Cursor & Fonts", None))
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Widget", u"Plugins", None))
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Widget", u"Update", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.monitor_group.setTitle(QCoreApplication.translate("Widget", u"Display Configuration", None))
        self.monitor_name_label.setText(QCoreApplication.translate("Widget", u"Monitor:", None))
        self.monitor_res_label.setText(QCoreApplication.translate("Widget", u"Resolution:", None))
        self.monitor_pos_label.setText(QCoreApplication.translate("Widget", u"Position:", None))
        self.monitor_scale_label.setText(QCoreApplication.translate("Widget", u"Scale:", None))
        self.mirror_label.setText(QCoreApplication.translate("Widget", u"Mirror:", None))
        self.mirror_comboBox.setItemText(0, QCoreApplication.translate("Widget", u"None", None))

        self.rotation_label.setText(QCoreApplication.translate("Widget", u"Rotation:", None))
        self.set_default_monitor_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.apply_button.setText(QCoreApplication.translate("Widget", u"Apply Settings", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.monitor_tab), QCoreApplication.translate("Widget", u"Monitor", None))
        self.autostart_group.setTitle(QCoreApplication.translate("Widget", u"Autostart Entries", None))
        self.add_program_button.setText(QCoreApplication.translate("Widget", u"Add Program", None))
        self.add_script_button.setText(QCoreApplication.translate("Widget", u"Add Script", None))
        self.del_autostart_button.setText(QCoreApplication.translate("Widget", u"Delete Selected", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.auto_tab), QCoreApplication.translate("Widget", u"Autostart", None))
        self.env_group.setTitle(QCoreApplication.translate("Widget", u"Environment Variables", None))
        self.add_env_button.setText(QCoreApplication.translate("Widget", u"Add Variable", None))
        self.del_env_button.setText(QCoreApplication.translate("Widget", u"Delete Selected", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.env_tab), QCoreApplication.translate("Widget", u"Environment", None))
        self.general_group.setTitle(QCoreApplication.translate("Widget", u"General", None))
        self.gaps_in_label.setText(QCoreApplication.translate("Widget", u"Gaps in:", None))
        self.gaps_out_label.setText(QCoreApplication.translate("Widget", u"Gaps out:", None))
        self.border_size_label.setText(QCoreApplication.translate("Widget", u"Border size:", None))
        self.border_col_1_label.setText(QCoreApplication.translate("Widget", u"Border color 1:", None))
        self.set_color_1_button.setText(QCoreApplication.translate("Widget", u"Pick color\u2026", None))
        self.border_col_2_label.setText(QCoreApplication.translate("Widget", u"Border color 2:", None))
        self.set_color_2_button.setText(QCoreApplication.translate("Widget", u"Pick color\u2026", None))
        self.angle_label.setText(QCoreApplication.translate("Widget", u"Gradient angle:", None))
        self.layout_hyprland_label.setText(QCoreApplication.translate("Widget", u"Layout:", None))
        self.resize_checkbox.setText(QCoreApplication.translate("Widget", u"Resize on border", None))
        self.allow_tearing_checkBox.setText(QCoreApplication.translate("Widget", u"Allow tearing", None))
        self.decoration_group.setTitle(QCoreApplication.translate("Widget", u"Decoration", None))
        self.rounding_label.setText(QCoreApplication.translate("Widget", u"Rounding:", None))
        self.rounding_power_label.setText(QCoreApplication.translate("Widget", u"Rounding power:", None))
        self.active_op_label.setText(QCoreApplication.translate("Widget", u"Active opacity:", None))
        self.inact_op_label.setText(QCoreApplication.translate("Widget", u"Inactive opacity:", None))
        self.shadow_group.setTitle(QCoreApplication.translate("Widget", u"Shadow", None))
        self.shadow_enable_checkbox.setText(QCoreApplication.translate("Widget", u"Enable shadows", None))
        self.shadow_range_label.setText(QCoreApplication.translate("Widget", u"Range:", None))
        self.shadow_render_power_label.setText(QCoreApplication.translate("Widget", u"Render power:", None))
        self.shadow_label_2.setText(QCoreApplication.translate("Widget", u"Color:", None))
        self.shadow_color_button.setText(QCoreApplication.translate("Widget", u"Pick color\u2026", None))
        self.blur_group.setTitle(QCoreApplication.translate("Widget", u"Blur", None))
        self.blur_enable_checkBox.setText(QCoreApplication.translate("Widget", u"Enable blur", None))
        self.blur_size_label.setText(QCoreApplication.translate("Widget", u"Size:", None))
        self.blur_passes_label.setText(QCoreApplication.translate("Widget", u"Passes:", None))
        self.blur_vibrancy_label.setText(QCoreApplication.translate("Widget", u"Vibrancy:", None))
        self.set_default_look_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.look_tab), QCoreApplication.translate("Widget", u"Look / Feel", None))
        self.keyboard_groupBox.setTitle(QCoreApplication.translate("Widget", u"Keyboard", None))
        self.kb_layout_label.setText(QCoreApplication.translate("Widget", u"Layout:", None))
        self.kb_variant_label.setText(QCoreApplication.translate("Widget", u"Variant:", None))
        self.kb_model_label.setText(QCoreApplication.translate("Widget", u"Model:", None))
        self.kb_options_label.setText(QCoreApplication.translate("Widget", u"Options:", None))
        self.kb_rules_label.setText(QCoreApplication.translate("Widget", u"Rules:", None))
        self.mouse_groupbox.setTitle(QCoreApplication.translate("Widget", u"Mouse", None))
        self.follow_mouse_label.setText(QCoreApplication.translate("Widget", u"Follow mouse:", None))
        self.mouse_sens_label.setText(QCoreApplication.translate("Widget", u"Sensitivity:", None))
        self.mouse_natural_scroll_checkBox.setText(QCoreApplication.translate("Widget", u"Natural scroll", None))
        self.touchpad_groupbox.setTitle(QCoreApplication.translate("Widget", u"Touchpad", None))
        self.touchpad_nat_scroll_checkbox.setText(QCoreApplication.translate("Widget", u"Natural scroll", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.input_tab), QCoreApplication.translate("Widget", u"Input", None))
        self.set_default_general_keybind_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.general_add_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.delete_keybind_button.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.keybinds_tabWidget.setTabText(self.keybinds_tabWidget.indexOf(self.general_tab), QCoreApplication.translate("Widget", u"General", None))
        self.set_default_movement_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.movement_add_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.delete_movement_button.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.keybinds_tabWidget.setTabText(self.keybinds_tabWidget.indexOf(self.movement_tab), QCoreApplication.translate("Widget", u"Movement", None))
        self.set_default_workspace_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.workspace_add_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.delete_workspace_button.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.keybinds_tabWidget.setTabText(self.keybinds_tabWidget.indexOf(self.workspaces_tab), QCoreApplication.translate("Widget", u"Workspaces", None))
        self.set_default_multimedia_button.setText(QCoreApplication.translate("Widget", u"Set Default", None))
        self.multimedia_add_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.delete_multimedia_button.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.keybinds_tabWidget.setTabText(self.keybinds_tabWidget.indexOf(self.multimedia_tab), QCoreApplication.translate("Widget", u"Multimedia", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.keybinds_tab), QCoreApplication.translate("Widget", u"Keybindings", None))
        self.windowrules_group.setTitle(QCoreApplication.translate("Widget", u"Window Rules", None))
        self.add_window_rule_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.edit_window_rule_button.setText(QCoreApplication.translate("Widget", u"Edit", None))
        self.delete_window_rule_button.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.windowrules_tab), QCoreApplication.translate("Widget", u"Window Rules", None))
        self.config_files_group.setTitle(QCoreApplication.translate("Widget", u"Config File Paths", None))
        self.current_config_file_label.setText(QCoreApplication.translate("Widget", u"Hyprland:", None))
        self.choose_config_file_button.setText(QCoreApplication.translate("Widget", u"Choose File\u2026", None))
        self.current_config_path_label.setText("")
        self.cur_hyprlock_label.setText(QCoreApplication.translate("Widget", u"Hyprlock:", None))
        self.choose_hyprlock_button.setText(QCoreApplication.translate("Widget", u"Choose File\u2026", None))
        self.cur_hyprlock_file_label.setText("")
        self.cur_hyprsunset_label.setText(QCoreApplication.translate("Widget", u"Hyprsunset:", None))
        self.choose_hypersunset_button.setText(QCoreApplication.translate("Widget", u"Choose File\u2026", None))
        self.hyprsunset_file_label.setText("")
        self.cur_hyprpaper_label.setText(QCoreApplication.translate("Widget", u"Hyprpaper:", None))
        self.choose_hyperpaper_file_button.setText(QCoreApplication.translate("Widget", u"Choose File\u2026", None))
        self.cur_hyprpaper_file_label.setText("")
        self.hypridle_label.setText(QCoreApplication.translate("Widget", u"Hypridle:", None))
        self.choose_hypridle_button.setText(QCoreApplication.translate("Widget", u"Choose File\u2026", None))
        self.cur_hypridle_label.setText("")
        self.Hyprland_Menu_Settings.setTabText(self.Hyprland_Menu_Settings.indexOf(self.files_tab), QCoreApplication.translate("Widget", u"Config Files", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Defaul Apps - coming soon", None))
        self.hyprlock_placeholder_label.setText(QCoreApplication.translate("Widget", u"Hyprlock configuration \u2014 coming soon", None))
        self.ecosystem_tabWidget.setTabText(self.ecosystem_tabWidget.indexOf(self.hyprlock_tab), QCoreApplication.translate("Widget", u"Hyprlock", None))
        self.ecosystem_tabWidget.setTabText(self.ecosystem_tabWidget.indexOf(self.hypridle_tab), QCoreApplication.translate("Widget", u"Hypridle", None))
        self.hyprsunset_placeholder_label.setText(QCoreApplication.translate("Widget", u"Hyprsunset configuration \u2014 coming soon", None))
        self.ecosystem_tabWidget.setTabText(self.ecosystem_tabWidget.indexOf(self.hyprsunset_tab), QCoreApplication.translate("Widget", u"Hyprsunset", None))
        self.hyprpaper_placeholder_label.setText(QCoreApplication.translate("Widget", u"Hyprpaper configuration \u2014 coming soon", None))
        self.ecosystem_tabWidget.setTabText(self.ecosystem_tabWidget.indexOf(self.hyprpaper_tab), QCoreApplication.translate("Widget", u"Hyprpaper", None))
        self.wifi_group.setTitle(QCoreApplication.translate("Widget", u"Wi-Fi", None))
        self.wifi_refresh_button.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.wifi_disconnect_button.setText(QCoreApplication.translate("Widget", u"Disconnect", None))
        self.choose_folder_button.setText(QCoreApplication.translate("Widget", u"Choose Folder", None))
        self.folder_label.setText("")

        __sortingEnabled1 = self.plugins_list.isSortingEnabled()
        self.plugins_list.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.plugins_list.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Widget", u"Hyprbars", None))
        ___qlistwidgetitem9 = self.plugins_list.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Widget", u"Hy3", None))
        ___qlistwidgetitem10 = self.plugins_list.item(2)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Widget", u"Hyprexpo", None))
        ___qlistwidgetitem11 = self.plugins_list.item(3)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Widget", u"Hyprgrass", None))
        self.plugins_list.setSortingEnabled(__sortingEnabled1)

        self.install_button.setText(QCoreApplication.translate("Widget", u"Install", None))
        self.uninstall_button.setText(QCoreApplication.translate("Widget", u"Uninstall", None))
        self.enable_button.setText(QCoreApplication.translate("Widget", u"Enable", None))
        self.disable_button.setText(QCoreApplication.translate("Widget", u"Disable", None))
        self.update_pushButton.setText(QCoreApplication.translate("Widget", u"Check for Updates", None))
        self.menuTheme.setTitle(QCoreApplication.translate("Widget", u"Themes", None))
        self.menu_Application.setTitle(QCoreApplication.translate("Widget", u"Application", None))
    # retranslateUi

