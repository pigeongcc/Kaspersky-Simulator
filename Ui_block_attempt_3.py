# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\block_attempt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import block_1_rc
import Ui_1


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        self.mainwindow.showMaximized()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setWhatsThis("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/1/7.jpg"))
        QtGui.QPixmapCache.setCacheLimit(2147483647)
        self.label.setObjectName("label")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setEnabled(True)
        self.lineEdit_1.setGeometry(QtCore.QRect(1020, 364, 151, 21))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(1020, 391, 151, 21))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(1020, 418, 151, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setReadOnly(False)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(360, 130, 141, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setPixmap(QtGui.QPixmap(":/6/37.jpg"))
        self.lineEdit_1.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.change(20, 410, 91, 20)
        self.connect(self.click_6_5)
        

    def click_6_5(self):
        self.next(":/6/39.jpg")
        self.change(20, 433, 81, 20)
        self.connect(self.click_6_6)

    def click_6_6(self):
        self.next(":/6/40.jpg")
        self.change(10, 460, 141, 20)
        self.connect(self.click_6_7)

    def click_6_7(self):
        self.next(":/6/41.jpg")
        self.change(20, 509, 121, 16)
        self.connect(self.click_6_8)

    def click_6_8(self):
        self.next(":/6/42.1.jpg")
        self.change(260, 250, 101, 21)
        self.connect(self.click_6_9)

    def click_6_9(self):
        self.next(":/6/42.2.jpg")
        self.change(742, 320, 17, 17)
        self.connect(self.click_6_10)

    def click_6_10(self):
        self.next(":/6/42.3.jpg")
        self.lineEdit_1.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.change(1035, 692, 73, 21)
        self.connect(self.click_6_11)

    def click_6_11(self):
        self.next(":/6/42.6.jpg")
        self.lineEdit_1.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.change(20, 532, 111, 18)
        self.connect(self.click_7_1)

    def click_7_1(self):
        self.next(":/7/43.jpg")
        self.change(20, 556, 85, 18)
        self.connect(self.click_7_2)

    def click_7_2(self):
        self.next(":/7/44.jpg")
        self.change(20, 580, 62, 18)
        self.connect(self.click_7_3)

    def click_7_3(self):
        self.next(":/7/45.jpg")
        self.change(20, 604, 110, 18)
        self.connect(self.click_7_4)

    def click_7_4(self):
        self.next(":/7/46.jpg")
        self.change(5, 629, 111, 18)
        self.connect(self.click_7_5)

    def click_7_5(self):
        self.next(":/7/47.jpg")
        self.connect(self.open_menu)

    def open_menu(self):
        self.window_to_open = Ui_1.Ui_MainWindow()
        self.mainwindow.close()

    def change(self, a, b, c, d):
        self.pushButton.setGeometry(QtCore.QRect(a, b, c, d))

    def next(self, pic):
        self.label.setPixmap(QtGui.QPixmap(pic))

    def connect(self, method):
        self.pushButton.clicked.connect(method)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "block"))
        self.centralwidget.setStatusTip(_translate("MainWindow", "Шаг 1: найти верную кнопку"))