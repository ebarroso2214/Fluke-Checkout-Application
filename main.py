import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon


class app_window(QMainWindow):
    def __init__(self):
        super(app_window, self).__init__()
        self.setGeometry(1200,300,700,700)
        self.setWindowTitle("Fluke Checkout")
        self.setToolTip("Fluke Checkout")
        self.setWindowIcon(QIcon("checkmark.jpg"))
        self.app_UI()
    
    def app_UI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Enter name : ")
        self.lbl_name.move(50,50)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200,50)
        self.txt_name.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Checkout")
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200,100)

        self.lbl_checked_out_by = QtWidgets.QLabel(self)
        self.lbl_checked_out_by.setText("Not Checked Out")
        self.lbl_checked_out_by.move(50,80)
        self.lbl_checked_out_by.resize(200,180)

    def clicked(self):
        self.lbl_checked_out_by.setText("Checked out by : " + self.txt_name.text())



def window():
    app = QApplication(sys.argv)
    win = app_window()
    win.show()
    sys.exit(app.exec_())

window()