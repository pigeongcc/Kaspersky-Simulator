import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import Ui_1, Ui_2

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_1.Ui_MainWindow()
    sys.exit(app.exec_())