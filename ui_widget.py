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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(743, 564)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Menu_settings = QTabWidget(Widget)
        self.Menu_settings.setObjectName(u"Menu_settings")
        self.Menu_settings.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu_settings.sizePolicy().hasHeightForWidth())
        self.Menu_settings.setSizePolicy(sizePolicy)
        self.Menu_settings.setMaximumSize(QSize(751, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 301, 291))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.monitors_box = QComboBox(self.widget)
        self.monitors_box.setObjectName(u"monitors_box")

        self.horizontalLayout.addWidget(self.monitors_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.resolution_box = QComboBox(self.widget)
        self.resolution_box.setObjectName(u"resolution_box")

        self.horizontalLayout_2.addWidget(self.resolution_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.position_box = QComboBox(self.widget)
        self.position_box.setObjectName(u"position_box")

        self.horizontalLayout_3.addWidget(self.position_box)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.scale_box = QComboBox(self.widget)
        self.scale_box.setObjectName(u"scale_box")

        self.horizontalLayout_4.addWidget(self.scale_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.Menu_settings.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Menu_settings.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.Menu_settings.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Menu_settings.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.Menu_settings.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.Menu_settings.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.Menu_settings.addTab(self.tab_7, "")

        self.verticalLayout_2.addWidget(self.Menu_settings)


        self.retranslateUi(Widget)

        self.Menu_settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Monitor: ", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Resolution", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Position", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Scale", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab), QCoreApplication.translate("Widget", u"Monitor", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Environment", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Autostart", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"Look and Feel", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"Input", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_6), QCoreApplication.translate("Widget", u"Keybindings", None))
        self.Menu_settings.setTabText(self.Menu_settings.indexOf(self.tab_7), QCoreApplication.translate("Widget", u"Window Rules", None))
    # retranslateUi

