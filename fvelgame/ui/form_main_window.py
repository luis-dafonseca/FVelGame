# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 561)
        self.action_Run = QAction(MainWindow)
        self.action_Run.setObjectName(u"action_Run")
        icon = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Run.setIcon(icon)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Exit.setIcon(icon1)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        icon2 = QIcon()
        iconThemeName = u"help-about"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_About.setIcon(icon2)
        self.action_Contents = QAction(MainWindow)
        self.action_Contents.setObjectName(u"action_Contents")
        icon3 = QIcon()
        iconThemeName = u"help-contents"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Contents.setIcon(icon3)
        self.action_Undo = QAction(MainWindow)
        self.action_Undo.setObjectName(u"action_Undo")
        icon4 = QIcon()
        iconThemeName = u"edit-undo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Undo.setIcon(icon4)
        self.action_Redo = QAction(MainWindow)
        self.action_Redo.setObjectName(u"action_Redo")
        icon5 = QIcon()
        iconThemeName = u"edit-redo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Redo.setIcon(icon5)
        self.action_Reset = QAction(MainWindow)
        self.action_Reset.setObjectName(u"action_Reset")
        icon6 = QIcon()
        iconThemeName = u"document-revert"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Reset.setIcon(icon6)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        icon7 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_New.setIcon(icon7)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon8 = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Open.setIcon(icon8)
        self.action_Save = QAction(MainWindow)
        self.action_Save.setObjectName(u"action_Save")
        icon9 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save.setIcon(icon9)
        self.action_Build = QAction(MainWindow)
        self.action_Build.setObjectName(u"action_Build")
        icon10 = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Build.setIcon(icon10)
        self.action_Save_as = QAction(MainWindow)
        self.action_Save_as.setObjectName(u"action_Save_as")
        icon11 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.action_Save_as.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        self.gridLayout_2 = QGridLayout(self.tabMain)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tabMain)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tabMain)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.tabMain)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.tabMain)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(64, 64))
        self.label_5.setBaseSize(QSize(64, 64))
        self.label_5.setFrameShape(QFrame.Panel)
        self.label_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.label_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton = QPushButton(self.tabMain)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.label_27 = QLabel(self.tabMain)
        self.label_27.setObjectName(u"label_27")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setIndent(7)

        self.verticalLayout_10.addWidget(self.label_27)


        self.horizontalLayout.addLayout(self.verticalLayout_10)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.label_2 = QLabel(self.tabMain)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tabMain)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.label_3 = QLabel(self.tabMain)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tabMain)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tabMain, "")
        self.tabDynamics = QWidget()
        self.tabDynamics.setObjectName(u"tabDynamics")
        self.gridLayout_3 = QGridLayout(self.tabDynamics)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.tabDynamics)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.label_7 = QLabel(self.tabDynamics)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_9 = QLabel(self.tabDynamics)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_8 = QLabel(self.tabDynamics)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox = QDoubleSpinBox(self.tabDynamics)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.tabDynamics)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tabDynamics)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.tabDynamics)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 5, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.doubleSpinBox_2 = QDoubleSpinBox(self.tabDynamics)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)

        self.tabWidget.addTab(self.tabDynamics, "")
        self.tabDisplay = QWidget()
        self.tabDisplay.setObjectName(u"tabDisplay")
        self.gridLayout_4 = QGridLayout(self.tabDisplay)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.tabDisplay)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMargin(5)
        self.label_13.setIndent(-3)

        self.gridLayout_4.addWidget(self.label_13, 0, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.tabDisplay)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(128, 128))
        self.label_16.setFrameShape(QFrame.Panel)
        self.label_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_7 = QPushButton(self.tabDisplay)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_20.addWidget(self.pushButton_7)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.label_40 = QLabel(self.tabDisplay)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setIndent(5)

        self.verticalLayout_8.addWidget(self.label_40)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_17)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 3, 1, 1)

        self.label_11 = QLabel(self.tabDisplay)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMargin(5)
        self.label_11.setIndent(-3)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.tabDisplay)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(128, 128))
        self.label_17.setFrameShape(QFrame.Panel)
        self.label_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_16)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_6 = QPushButton(self.tabDisplay)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_19.addWidget(self.pushButton_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.label_39 = QLabel(self.tabDisplay)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setIndent(5)

        self.verticalLayout_7.addWidget(self.label_39)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_15)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_18 = QLabel(self.tabDisplay)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(128, 128))
        self.label_18.setFrameShape(QFrame.Panel)
        self.label_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_5 = QPushButton(self.tabDisplay)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_18.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.label_38 = QLabel(self.tabDisplay)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setIndent(5)

        self.verticalLayout_6.addWidget(self.label_38)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_14)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.label_12 = QLabel(self.tabDisplay)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMargin(5)
        self.label_12.setIndent(-3)

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.tabDisplay)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(128, 128))
        self.label_15.setFrameShape(QFrame.Panel)
        self.label_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_8 = QPushButton(self.tabDisplay)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_21.addWidget(self.pushButton_8)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.label_41 = QLabel(self.tabDisplay)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setIndent(5)

        self.verticalLayout_9.addWidget(self.label_41)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_19)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 3, 1, 1)

        self.label_14 = QLabel(self.tabDisplay)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMargin(5)
        self.label_14.setIndent(-3)

        self.gridLayout_4.addWidget(self.label_14, 1, 2, 1, 1)

        self.label_10 = QLabel(self.tabDisplay)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)
        self.label_10.setIndent(-3)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_19 = QLabel(self.tabDisplay)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(128, 128))
        self.label_19.setFrameShape(QFrame.Panel)
        self.label_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.label_19)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_4 = QPushButton(self.tabDisplay)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_15.addWidget(self.pushButton_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.label_26 = QLabel(self.tabDisplay)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setIndent(5)

        self.verticalLayout_2.addWidget(self.label_26)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tabDisplay, "")
        self.tabSounds = QWidget()
        self.tabSounds.setObjectName(u"tabSounds")
        self.gridLayout_5 = QGridLayout(self.tabSounds)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_10 = QPushButton(self.tabSounds)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_5.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.label_21 = QLabel(self.tabSounds)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_23 = QLabel(self.tabSounds)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setIndent(2)

        self.gridLayout_5.addWidget(self.label_23, 0, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.tabSounds)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_5.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 311, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.tabSounds)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_5.addWidget(self.pushButton_12, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.tabSounds)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_5.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.label_24 = QLabel(self.tabSounds)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setIndent(2)

        self.gridLayout_5.addWidget(self.label_24, 1, 3, 1, 1)

        self.pushButton_11 = QPushButton(self.tabSounds)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_5.addWidget(self.pushButton_11, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.tabSounds)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_5.addWidget(self.pushButton_14, 2, 2, 1, 1)

        self.label_25 = QLabel(self.tabSounds)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setIndent(2)

        self.gridLayout_5.addWidget(self.label_25, 2, 3, 1, 1)

        self.label_20 = QLabel(self.tabSounds)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_22 = QLabel(self.tabSounds)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabSounds, "")
        self.tabVelocity = QWidget()
        self.tabVelocity.setObjectName(u"tabVelocity")
        self.gridLayout_6 = QGridLayout(self.tabVelocity)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_28 = QLabel(self.tabVelocity)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(0, 264))
        self.label_28.setFrameShape(QFrame.Panel)
        self.label_28.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.label_28, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_29 = QLabel(self.tabVelocity)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(30, 0))
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_30 = QLabel(self.tabVelocity)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(30, 0))
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_30, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout_7.addWidget(self.doubleSpinBox_4, 0, 1, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.tabVelocity)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout_7.addWidget(self.doubleSpinBox_5, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabVelocity, "")
        self.tabMargins = QWidget()
        self.tabMargins.setObjectName(u"tabMargins")
        self.gridLayout_9 = QGridLayout(self.tabMargins)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_31 = QLabel(self.tabMargins)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(0, 264))
        self.label_31.setFrameShape(QFrame.Panel)
        self.label_31.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.label_31, 0, 4, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton = QRadioButton(self.tabMargins)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.groupBox = QGroupBox(self.tabMargins)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(30, 0))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_32, 0, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_10.addWidget(self.doubleSpinBox_7, 1, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(30, 0))
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_33, 1, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_10.addWidget(self.doubleSpinBox_6, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabMargins)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_11 = QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(30, 0))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_35, 0, 0, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout_11.addWidget(self.doubleSpinBox_9, 0, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(30, 0))
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_34, 1, 0, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout_11.addWidget(self.doubleSpinBox_8, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tabMargins, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_Save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)
        self.menuHelp.addAction(self.action_Contents)
        self.menuHelp.addAction(self.action_About)
        self.menuEdit.addAction(self.action_Undo)
        self.menuEdit.addAction(self.action_Redo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_Reset)
        self.menuGame.addAction(self.action_Run)
        self.menuGame.addAction(self.action_Build)
        self.toolBar.addAction(self.action_New)
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.action_Save_as)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Undo)
        self.toolBar.addAction(self.action_Redo)
        self.toolBar.addAction(self.action_Reset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Run)
        self.toolBar.addAction(self.action_Build)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Run.setText(QCoreApplication.translate("MainWindow", u"&Run Game", None))
#if QT_CONFIG(statustip)
        self.action_Run.setStatusTip(QCoreApplication.translate("MainWindow", u"Run game", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Run.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(statustip)
        self.action_Exit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit game editor", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_Contents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
#if QT_CONFIG(statustip)
        self.action_Contents.setStatusTip(QCoreApplication.translate("MainWindow", u"Help contents", None))
#endif // QT_CONFIG(statustip)
        self.action_Undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(statustip)
        self.action_Undo.setStatusTip(QCoreApplication.translate("MainWindow", u"Undo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_Redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(statustip)
        self.action_Redo.setStatusTip(QCoreApplication.translate("MainWindow", u"Redo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Redo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
#if QT_CONFIG(statustip)
        self.action_New.setStatusTip(QCoreApplication.translate("MainWindow", u"Create new game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
#if QT_CONFIG(statustip)
        self.action_Open.setStatusTip(QCoreApplication.translate("MainWindow", u"Open game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(statustip)
        self.action_Save.setStatusTip(QCoreApplication.translate("MainWindow", u"Save game definition", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Build.setText(QCoreApplication.translate("MainWindow", u"Build", None))
#if QT_CONFIG(statustip)
        self.action_Build.setStatusTip(QCoreApplication.translate("MainWindow", u"Build game executable", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Build.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_Save_as.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.tabMain.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabMain.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game properties", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Game name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Game description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), QCoreApplication.translate("MainWindow", u"Main", None))
#if QT_CONFIG(statustip)
        self.tabDynamics.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game dynamics", None))
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scroll direction", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Player speed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Treasure frequency", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Obstac\u00e7e frequency", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Horizontal", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Vertical", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDynamics), QCoreApplication.translate("MainWindow", u"Dynamics", None))
#if QT_CONFIG(statustip)
        self.tabDisplay.setStatusTip(QCoreApplication.translate("MainWindow", u"Define visual elements", None))
#endif // QT_CONFIG(statustip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.label_16.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Obstacle image", None))
        self.label_17.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_18.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Treasure image", None))
        self.label_15.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Track", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Player image", None))
        self.label_19.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDisplay), QCoreApplication.translate("MainWindow", u"Display", None))
#if QT_CONFIG(tooltip)
        self.tabSounds.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabSounds.setStatusTip(QCoreApplication.translate("MainWindow", u"Define game sounds", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.tabSounds.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Crash with obstacle", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Catch the treasure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSounds), QCoreApplication.translate("MainWindow", u"Sounds", None))
#if QT_CONFIG(statustip)
        self.tabVelocity.setStatusTip(QCoreApplication.translate("MainWindow", u"Define scrolling velocity", None))
#endif // QT_CONFIG(statustip)
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVelocity), QCoreApplication.translate("MainWindow", u"Velocity", None))
#if QT_CONFIG(statustip)
        self.tabMargins.setStatusTip(QCoreApplication.translate("MainWindow", u"Define track margins", None))
#endif // QT_CONFIG(statustip)
        self.label_31.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Symmetrical", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rigth", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMargins), QCoreApplication.translate("MainWindow", u"Margins", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

