# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\6n.ui'
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
        MainWindow.resize(642, 217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 161, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 259, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 135, 48))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 90, 8, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 120, 450, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 272, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.menu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_Button.setGeometry(QtCore.QRect(510, 150, 94, 28))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "6-n"))
        self.centralwidget.setStatusTip(_translate("MainWindow", "Тестирование завершено"))
        self.label.setText(_translate("MainWindow", "Ваш результат:"))
        self.label_2.setText(_translate("MainWindow", "(здесь будет оценка)"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Ошибок:</p><p>Время выполнения:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>0</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>(таймер будет засекать время с момента начала тестирования)</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Тестирование завершено!"))
        self.menu_Button.setStatusTip(_translate("MainWindow", "Приступить к занятию"))
        self.menu_Button.setText(_translate("MainWindow", "Главное меню"))
