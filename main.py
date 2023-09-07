import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200,300,700,700)
    win.setWindowTitle("Fluke Checkout")
    win.setWindowIcon(QIcon("checkmark.jpg"))
    win.setToolTip("Fluke Checkout")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Enter name : ")
    lbl_name.move(50,50)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200,50)

    def clicked(self):
        print('button clicked')
        print('name :' + txt_name.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.clicked.connect(clicked)
    btn_save.move(200,130)

    win.show()
    sys.exit(app.exec_())

window()