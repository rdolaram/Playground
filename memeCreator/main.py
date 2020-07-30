'''
Python Meme Creator
Rakesh Dolaram
'''
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Meme Creator")
        self.setStyleSheet("background-color: gray;")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'resources/trollface.png')))
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.show()

    def createLayout(self):
        gridlayout = QGridLayout()
        












if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


