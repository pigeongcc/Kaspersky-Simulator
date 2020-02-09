# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\block_attempt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import block_1_rc
import Ui_block_attempt_3


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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 181, 21))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 131, 21))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(780, 520, 361, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_extra = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_extra.setEnabled(True)
        self.lineEdit_extra.setGeometry(QtCore.QRect(715, 540, 482, 23))
        self.lineEdit_extra.setFont(font)
        self.lineEdit_extra.setFrame(True)
        self.lineEdit_extra.setReadOnly(False)
        self.lineEdit_extra.setClearButtonEnabled(False)
        self.lineEdit_extra.setObjectName("lineEdit_extra")
        self.lineEdit_extra.hide()
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(990, 570, 71, 20))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setText("")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 200, 141, 20))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setText("")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 80, 141, 31))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setText("")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(260, 220, 201, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 250, 331, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 280, 201, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_e1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_e1.setGeometry(QtCore.QRect(700, 440, 21, 20))
        self.radioButton_e1.setObjectName("radioButton_e1")
        self.radioButton_e2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_e2.setGeometry(QtCore.QRect(700, 460, 21, 20))
        self.radioButton_e2.setObjectName("radioButton_e2")
        self.radioButton_e3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_e3.setGeometry(QtCore.QRect(260, 250, 331, 20))
        self.radioButton_e3.setObjectName("radioButton_e3")
        self.radioButton_e4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_e4.setGeometry(QtCore.QRect(260, 250, 331, 20))
        self.radioButton_e4.setObjectName("radioButton_e4")
        self.radioButton_e5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_e5.setGeometry(QtCore.QRect(260, 250, 331, 20))
        self.radioButton_e5.setObjectName("radioButton_e5")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(260, 350, 381, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 380, 421, 20))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_e1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e1.setGeometry(QtCore.QRect(707, 408, 21, 20)) # plus 18
        self.checkBox_e1.setObjectName("checkBox_e1")
        
        self.checkBox_e2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e2.setGeometry(QtCore.QRect(707, 426, 21, 20))
        self.checkBox_e2.setObjectName("checkBox_e2")
        
        self.checkBox_e3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e3.setGeometry(QtCore.QRect(707, 444, 21, 20))
        self.checkBox_e3.setObjectName("checkBox_e3")
        
        self.checkBox_e4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e4.setGeometry(QtCore.QRect(707, 462, 21, 20))
        self.checkBox_e4.setObjectName("checkBox_e4")
        
        self.checkBox_e5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e5.setGeometry(QtCore.QRect(707, 480, 21, 20))
        self.checkBox_e5.setObjectName("checkBox_e5")
        
        self.checkBox_e6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e6.setGeometry(QtCore.QRect(707, 498, 21, 20))
        self.checkBox_e6.setObjectName("checkBox_e6")
        
        self.checkBox_e7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e7.setGeometry(QtCore.QRect(707, 516, 21, 20))
        self.checkBox_e7.setObjectName("checkBox_e7")
        
        self.checkBox_e8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e8.setGeometry(QtCore.QRect(703, 642, 21, 20))
        self.checkBox_e8.setObjectName("checkBox_e8")
        
        self.checkBox_e9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e9.setGeometry(QtCore.QRect(703, 664, 21, 20))
        self.checkBox_e9.setObjectName("checkBox_e9")
        

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 120, 151, 21))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setText("")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 150, 171, 16))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setText("")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 170, 141, 21))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setText("")
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 199, 111, 16))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setText("")
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 195, 121, 21))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setText("")
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setGeometry(QtCore.QRect(1760, 200, 21, 20))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setText("")
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 130, 141, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setPixmap(QtGui.QPixmap(":/4/19.0.jpg"))
        self.lineEdit_4.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.checkBox_e1.hide()
        self.checkBox_e2.hide()
        self.checkBox_e3.hide()
        self.checkBox_e4.hide()
        self.checkBox_e5.hide()
        self.checkBox_e6.hide()
        self.checkBox_e7.hide()
        self.checkBox_e8.hide()
        self.checkBox_e9.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.radioButton_e1.hide()
        self.radioButton_e2.hide()
        self.radioButton_e3.hide()
        self.radioButton_e4.hide()
        self.radioButton_e5.hide()
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.clicked.connect(self.click_4_1)
    
    def click_4_1(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.next(":/extra/20NEW.jpg")
        self.lineEdit_extra.show()
        self.change(1062, 748, 72, 19)
        self.connect(self.click_4_2)
    
    def click_4_2(self):
        self.next(":/extra/21yesNEW.jpg")
        self.lineEdit_extra.hide()
        self.radioButton_e1.show()
        self.radioButton_e2.show()
        #self.change(1062, 748, 72, 19) the same click! 'Далее'
        self.connect(self.click_4_3)
    
    def click_4_3(self):
        if self.radioButton_e1.isChecked():
            self.next(":/extra/22yesNEW.jpg")
            self.radioButton_e1.hide()
            self.radioButton_e2.hide()
            self.checkBox_e1.show()
            self.checkBox_e2.show()
            self.checkBox_e3.show()
            self.checkBox_e4.show()
            self.checkBox_e5.show()
            self.checkBox_e6.show()
            self.checkBox_e7.show()
            self.checkBox_e8.show()
            self.checkBox_e9.show()
            self.change(1062, 748, 72, 19)
            self.connect(self.click_4_4)


    def click_4_4(self):
        shouldNotBeChecked = self.checkBox_e4.isChecked() or self.checkBox_e5.isChecked() or self.checkBox_e6.isChecked() or self.checkBox_e7.isChecked()
        shouldBeChecked = self.checkBox_e1.isChecked() and self.checkBox_e2.isChecked() and self.checkBox_e3.isChecked() and self.checkBox_e8.isChecked() and self.checkBox_e9.isChecked()
        if shouldBeChecked and not shouldNotBeChecked:
            self.next(":/extra/23yesNEW.jpg")
            self.checkBox_e1.hide()
            self.checkBox_e2.hide()
            self.checkBox_e3.hide()
            self.checkBox_e4.hide()
            self.checkBox_e5.hide()
            self.checkBox_e6.hide()
            self.checkBox_e7.hide()
            self.checkBox_e8.hide()
            self.checkBox_e9.hide()
            self.radioButton_e1.setGeometry(QtCore.QRect(700, 669, 21, 20))
            self.radioButton_e1.show()
            self.radioButton_e2.setGeometry(QtCore.QRect(700, 690, 21, 20))
            self.radioButton_e2.show()
            self.connect(self.click_4_5)
    
    def click_4_5(self):
        if self.radioButton_e1.isChecked():
            self.next(":/extra/24yesNEW.jpg")
            self.radioButton_e1.setGeometry(QtCore.QRect(724, 484, 21, 20))
            self.radioButton_e1.show()
            self.radioButton_e2.setGeometry(QtCore.QRect(724, 510, 21, 20))
            self.radioButton_e2.show()
            self.radioButton_e3.setGeometry(QtCore.QRect(724, 536, 21, 20))
            self.radioButton_e3.show()
            self.connect(self.click_4_6)

    def click_4_6(self):
        if self.radioButton_e1.isChecked():
            self.next(":/extra/26NEW.jpg")
            self.radioButton_e1.hide()
            self.radioButton_e2.hide()
            self.radioButton_e3.hide()
            self.change(420, 380, 141, 21)
            self.connect(self.click_4_8)

    def click_4_8(self):
        self.pushButton.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/4/26_new_начало_настройки_политики.jpg")) #это всё из-за пробелов в названии скрина!11
        self.pushButton_8.setEnabled(True)
        self.checkBox.show()
        self.checkBox_2.show()
        self.radioButton.show()
        self.radioButton_2.show()
        self.radioButton_3.show()
        self.checkBox.show()
        self.checkBox_2.show()
        self.radioButton.show()
        self.radioButton_2.show()
        self.radioButton_3.show()
        self.radioButton.clicked.connect(self.radioListener)
        self.checkBox.clicked.connect(self.radioListener)
        self.checkBox_2.clicked.connect(self.radioListener)
        #while(1):
        #    if self.radioButton.isChecked() and self.checkBox.isChecked() and not self.checkBox_2.isChecked():
        #        self.pushButton_8.clicked.connect(self.click_4_9)
        #        break
    
    def radioListener(self):
        if self.radioButton.isChecked() and self.checkBox.isChecked() and not self.checkBox_2.isChecked():
            self.pushButton_8.clicked.connect(self.click_4_9)

    def click_4_9(self):
        self.pushButton_8.setEnabled(False)
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.label.setPixmap(QtGui.QPixmap(":/4/27.jpg"))
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.clicked.connect(self.click_4_10)

    def click_4_10(self):
        self.pushButton_9.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/4/28.jpg"))
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.clicked.connect(self.click_4_11)

    def click_4_11(self):
        self.pushButton_10.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/4/29.jpg"))
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.clicked.connect(self.click_5_1)

    """
    def click_4_12(self):
        self.pushButton_11.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/5/30_контроль_устройств.jpg"))
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.clicked.connect(self.click_5_2)
    """

    def click_5_1(self):
        self.pushButton_12.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/5/30_контроль_устройств.jpg"))
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.clicked.connect(self.click_5_2)

    def click_5_2(self):
        self.pushButton_13.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/5/30.1.jpg"))
        self.pushButton.setEnabled(True)
        self.change(361, 132, 144, 21)
        self.connect(self.click_5_3)

    # и тут до меня допёрло...
    def click_5_3(self):
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.radioButton_e1.hide()
        self.radioButton_e2.hide()
        self.pushButton.setEnabled(True)
        self.next(":/5/30.2.jpg")
        self.change(20, 220, 81, 21)
        self.connect(self.click_5_4)

    def click_5_4(self):
        self.next(":/5/31.jpg")
        self.change(20, 270, 151, 16)
        self.connect(self.click_5_5)

    def click_5_5(self):
        self.next(":/5/32.jpg")
        self.change(20, 291, 121, 20)
        self.connect(self.click_5_6)

    def click_5_6(self):
        self.next(":/5/33.1.jpg")
        self.change(1800, 131, 101, 31)
        self.connect(self.click_5_7)

    def click_5_7(self):
        self.next(":/5/33.2.jpg")
        self.change(910, 210, 41, 16)
        self.connect(self.click_5_8)

    def click_5_8(self):
        self.next(":/5/33.3.jpg")
        self.change(960, 206, 111, 20)
        self.connect(self.click_5_9)

    def click_5_9(self):
        self.next(":/5/33.5.jpg")
        self.change(1170, 532, 81, 20)
        self.connect(self.click_5_10)

    def click_5_10(self):
        self.next(":/5/33.1.jpg")
        self.change(20, 317, 121, 20)
        self.connect(self.click_6_1)

    def click_6_1(self):
        self.next(":/6/34.jpg")
        self.change(20, 340, 81, 20)
        self.connect(self.click_6_2)

    def click_6_2(self):
        self.next(":/6/35.jpg")
        self.change(20, 361, 81, 20)
        self.connect(self.click_6_3)

    def click_6_3(self):
        self.next(":/6/36.jpg")
        self.change(20, 385, 111, 20)
        self.connect(self.open_window_3)

    def open_window_3(self):
        self.pushButton.setEnabled(False)
        self.window_to_open = Ui_block_attempt_3.Ui_MainWindow()
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
        self.radioButton.setText(_translate("MainWindow", "Активная политика"))
        self.radioButton_2.setText(_translate("MainWindow", "Политика для автономных пользователей"))
        self.radioButton_3.setText(_translate("MainWindow", "Неактивная политика"))
        self.radioButton_e1.setText(_translate("MainWindow", ""))
        self.radioButton_e2.setText(_translate("MainWindow", ""))
        self.radioButton_e3.setText(_translate("MainWindow", ""))
        self.radioButton_e4.setText(_translate("MainWindow", ""))
        self.radioButton_e5.setText(_translate("MainWindow", ""))
        self.checkBox.setText(_translate("MainWindow", "Наследовать параметры из политики верхнего уровня"))
        self.checkBox_2.setText(_translate("MainWindow", "Форсировать наследование параметров дочерними политиками"))
