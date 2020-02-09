# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\results_list.ui'
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
        MainWindow.resize(562, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 182, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.menu_Button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_Button.setGeometry(QtCore.QRect(440, 320, 94, 28))
        self.menu_Button.setObjectName("menu_Button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 50, 531, 251))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menu_Button.clicked.connect(self.open_menu)

    def open_menu(self):
        self.window_to_open = Ui_1.Ui_MainWindow()
        self.mainwindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "results_list"))
        self.label.setText(_translate("MainWindow", "Список результатов"))
        self.menu_Button.setStatusTip(_translate("MainWindow", "Приступить к занятию"))
        self.menu_Button.setText(_translate("MainWindow", "Главное меню"))
