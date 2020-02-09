# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_4


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 10, 231, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.task1_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.task1_Button.setFont(font)
        self.task1_Button.setCheckable(False)
        self.task1_Button.setFlat(False)
        self.task1_Button.setObjectName("task1_Button")
        self.verticalLayout.addWidget(self.task1_Button)
        self.task2_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.task2_Button.setFont(font)
        self.task2_Button.setCheckable(False)
        self.task2_Button.setFlat(False)
        self.task2_Button.setObjectName("task2_Button")
        self.verticalLayout.addWidget(self.task2_Button)
        self.task3_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.task3_Button.setFont(font)
        self.task3_Button.setCheckable(False)
        self.task3_Button.setFlat(False)
        self.task3_Button.setObjectName("task3_Button")
        self.verticalLayout.addWidget(self.task3_Button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.task1_Button.clicked.connect(self.open_lesson, 1)

    def open_lesson(self, number):
        self.window_to_open = Ui_4.Ui_MainWindow()
        self.mainwindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "Выберите занятие:"))
        self.task1_Button.setStatusTip(_translate("MainWindow", "Приступить к занятию"))
        self.task1_Button.setText(_translate("MainWindow", "Занятие №1\n"
"Тема занятия: \"Тест программы (клик сюда)\""))
        self.task2_Button.setText(_translate("MainWindow", "Занятие №2\n"
"Тема занятия: \"Программы тест\""))
        self.task3_Button.setText(_translate("MainWindow", "Занятие №3\n"
"Тема занятия: \"Программный тест\""))
