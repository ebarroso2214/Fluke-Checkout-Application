import sys
import datetime
from datetime import timezone
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from FlukeCheckoutUI import Ui_MainWindow


class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.current_user)
        
    def current_user(self):
         user = self.ui.lineEdit.text()
         print(user)
         self.ui.used_by.setText(user)
         print(user)
         dt = datetime.datetime.now()
         date_text = dt.strftime('%m-%d-%Y %H:%M')
         self.ui.date.setText(date_text)
         self.ui.lineEdit.clear()
         
        


    

def app():
        app = QtWidgets.QApplication(sys.argv)
        win = my_app()
        win.show()
        sys.exit(app.exec_())

app()
