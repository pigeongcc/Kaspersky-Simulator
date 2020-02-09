# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_4


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        
    def setupUi(self, MainWindow_1):
        MainWindow_1.setObjectName("MainWindow_1")
        MainWindow_1.resize(474, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow_1)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 10, 313, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.start_lesson_Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_lesson_Button.sizePolicy().hasHeightForWidth())
        self.start_lesson_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start_lesson_Button.setFont(font)
        self.start_lesson_Button.setCheckable(False)
        self.start_lesson_Button.setAutoDefault(False)
        self.start_lesson_Button.setDefault(False)
        self.start_lesson_Button.setFlat(False)
        self.start_lesson_Button.setObjectName("start_lesson_Button")
        self.verticalLayout.addWidget(self.start_lesson_Button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit_Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_Button.sizePolicy().hasHeightForWidth())
        self.exit_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exit_Button.setFont(font)
        self.exit_Button.setCheckable(False)
        self.exit_Button.setAutoDefault(False)
        self.exit_Button.setDefault(False)
        self.exit_Button.setFlat(False)
        self.exit_Button.setObjectName("exit_Button")
        self.verticalLayout.addWidget(self.exit_Button)
        MainWindow_1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_1)
        self.statusbar.setObjectName("statusbar")
        MainWindow_1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_1)
        self.exit_Button.clicked.connect(MainWindow_1.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)
        MainWindow_1.setTabOrder(self.start_lesson_Button, self.exit_Button)

        self.exit_Button.clicked.connect(self.mainwindow.close)
        self.start_lesson_Button.clicked.connect(self.open_tutor)

    def open_tutor(self):
        self.window_to_open = Ui_4.Ui_MainWindow()
        self.mainwindow.close()

    def retranslateUi(self, MainWindow_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_1.setWindowTitle(_translate("MainWindow_1", "1"))
        self.label.setText(_translate("MainWindow_1", "Тренажер..."))
        self.start_lesson_Button.setText(_translate("MainWindow_1", "Начать обучение"))
        self.exit_Button.setText(_translate("MainWindow_1", "Выход"))


