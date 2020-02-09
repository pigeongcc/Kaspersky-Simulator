# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\tutor_n.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Ui_1


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 141)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 135, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 450, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 229, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.menu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_Button.setGeometry(QtCore.QRect(520, 80, 94, 28))
        self.menu_Button.setObjectName("menu_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menu_Button.clicked.connect(self.open_menu)

    def open_menu(self):
        self.window_to_open = Ui_1.Ui_MainWindow()
        self.mainwindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tutor-n"))
        self.centralwidget.setStatusTip(_translate("MainWindow", "Обучение завершено"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Время выполнения:</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>(таймер будет засекать время с момента начала обучения)</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Обучение завершено!"))
        self.menu_Button.setStatusTip(_translate("MainWindow", "Приступить к занятию"))
        self.menu_Button.setText(_translate("MainWindow", "Главное меню"))
