'''
Rakesh Dolaram
To do application
'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import random
import sys

#CODE TO IMPLEMENT
#WHEN WE CLICK A TASK (QLISTWIDGET OBJECT)
# WE ARE BROUGHT WITH A MENU OPTION SUCH AS RENAME
# NOTES
# ETC


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.dialogFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
        self.font = QtGui.QFont("Arial", 15)
        
        self.initUI()


    def initUI(self):
        self.setGeometry(1000,500,500,300)
        self.setWindowTitle("To Do Application")

        #INPUT TASK
        self.lineEdit = QLineEdit(self)
        self.lineEdit.returnPressed.connect(self.enterPressed)

        #BUTTONS
        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.addTask)

        removeButton = QPushButton("Remove", self)
        removeButton.clicked.connect(self.removeTask)

        #LIST
        self.list = []
        self.listWidget = QListWidget()


        #LAYOUT MANAGEMENT        
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(addButton)
        hbox.addWidget(removeButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)

        self.show()

    def addTask(self):
        text = self.lineEdit.text()
        if text in self.list:
            self.duplicateError()
        else:
            self.list.append(text)
            #CREATE THE ITEM
            x = QListWidgetItem()
            x.setText(text)
            x.setFont(self.font)
            x.setTextAlignment(QtCore.Qt.AlignHCenter)
            
            self.listWidget.addItem(x)

    def removeTask(self):
        selected = self.listWidget.selectedItems()
        if not selected: return
        for item in selected:
            self.listWidget.takeItem(self.listWidget.row(item))

    def enterPressed(self):
        text = self.lineEdit.text()
        self.listWidget.addItem(text)

    def duplicateError(self):
        dialog = QDialog()

        duplicateLabel = QLabel("Duplicate task", dialog)
        duplicateLabel.setAlignment(QtCore.Qt.AlignCenter)
        duplicateLabel.setFont(self.dialogFont)

        dialog.setWindowTitle("WARNING")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.setFixedHeight(100)
        dialog.setFixedWidth(250)

        vbox = QVBoxLayout()        
        vbox.addWidget(duplicateLabel)
    
        dialog.setLayout(vbox)
        dialog.exec_()

#START THE APPLICATION
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Window()
    sys.exit(App.exec())