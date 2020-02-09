# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

import Ui_1, Ui_4, main


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 192)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 150, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.next_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_Button.setObjectName("next_Button")
        self.horizontalLayout_2.addWidget(self.next_Button)
        self.back_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.back_Button.setObjectName("back_Button")
        self.horizontalLayout_2.addWidget(self.back_Button)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 476, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_rank = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_rank.setObjectName("lineEdit_rank")
        self.verticalLayout.addWidget(self.lineEdit_rank)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.lineEdit_studygroup = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_studygroup.setObjectName("lineEdit_studygroup")
        self.verticalLayout.addWidget(self.lineEdit_studygroup)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.back_Button.clicked.connect(self.open_menu)
        self.next_Button.clicked.connect(self.open_lesson_choosing_with_save)

    def open_menu(self):
        self.window_to_open = Ui_1.Ui_MainWindow()
        self.mainwindow.close()

    def get_lineEdit_texts(self, list_to_save):
        list_to_save[1] = self.lineEdit_rank.text()
        list_to_save[2] = self.lineEdit_name.text()
        list_to_save[3] = self.lineEdit_studygroup.text()
        list_to_save[4] = datetime.today().strftime('%d.%m.%Y')

    def open_lesson_choosing_with_save(self):
        self.list_info = [None for i in range(5)]
        self.get_lineEdit_texts(self.list_info)
        main.callback_save_info(main, self.list_info)

        self.window_to_open = Ui_4.Ui_MainWindow()
        self.mainwindow.close()
    
    def save_info(self, list_to_save, number):
        #0 0-number 1-rank 2-name 3-studyGroup 4-dateOfTest 5-mark 6-mistakes 7-time 8-numberOfLesson
        list_to_save[number][0] = number + 1
        list_to_save[number][1] = self.lineEdit_rank.text()
        list_to_save[number][2] = self.lineEdit_name.text()
        list_to_save[number][3] = self.lineEdit_studygroup.text()
        list_to_save[number][4] = datetime.today().strftime('%d.%m.%Y')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2"))
        self.next_Button.setText(_translate("MainWindow", "Далее"))
        self.back_Button.setText(_translate("MainWindow", "Назад"))
        self.label_4.setText(_translate("MainWindow", "Введите данные о курсанте, проходящем тестирование"))
        self.label.setText(_translate("MainWindow", "Воинское звание:"))
        self.label_2.setText(_translate("MainWindow", "Фамилия и инициалы:"))
        self.label_3.setText(_translate("MainWindow", "Учебная группа:"))
