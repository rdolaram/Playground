'''
Rakesh Dolaram
To do application
'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("To Do Application")

        #INPUT TASK
        self.lineEdit = QLineEdit(self)
        self.lineEdit.returnPressed.connect(self.enterPressed)

        #ADD BUTTON
        button = QPushButton("Add task", self)
        button.clicked.connect(self.buttonClicked)

        #LIST
        self.list = QListWidget()


        #LAYOUT MANAGEMENT        
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.list)
        self.setLayout(vbox)


        self.show()

    def buttonClicked(self):
        text = self.lineEdit.text()
        self.list.addItem(text)
    
    #DEBATING ON WHETHER ENTER FUNCTIONALITY WILL BE IMPLEMENTED.
    '''
    def enterPressed(self):
        text = self.lineEdit.text()
        self.list.addItem(text)
    '''




#START THE APPLICATION
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Window()
    sys.exit(App.exec())