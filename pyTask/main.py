'''
Rakesh Dolaram
To do application
'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import sys

items = {}

selectText = ''

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.dialogFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
        self.font = QtGui.QFont("Arial", 15)
        
        self.initUI()


    def initUI(self):
        self.setGeometry(1000,500,500,300)
        self.setWindowTitle("To Do")

        #INPUT TASK
        self.lineEdit = QLineEdit(self)
        self.lineEdit.returnPressed.connect(self.addTask)

        #BUTTONS
        addButton = QPushButton("Add", self)
        addButton.clicked.connect(self.addTask)

        removeButton = QPushButton("Remove", self)
        removeButton.clicked.connect(self.removeTask)

        #LIST
        self.list = []
        self.listWidget = QListWidget()
        self.listWidget.itemDoubleClicked.connect(self.doubleClickedItem)

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
        global items

        text = self.lineEdit.text()
        if text in self.list:
            self.duplicateError()
        else:
            #Add it to the list of taken names
            self.list.append(text)
            
            #Add it to the dictionary with default desc
            
            items.update({text:'No notes associated with task.'})
            print(items)
            
            #CREATE THE ITEM
            curItem = QListWidgetItem()
            curItem.setText(text)
            curItem.setFont(self.font)
            curItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            print(curItem.text())
            self.listWidget.addItem(curItem)
    

    def removeTask(self):
        selected = self.listWidget.selectedItems()
        if not selected: return
        for item in selected:
            self.listWidget.takeItem(self.listWidget.row(item))


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

    def doubleClickedItem(self):
        global selectedText
        selectedText = self.listWidget.currentItem().text()
        
        #CREATE NEW WIDGET CLASS OBJECT
        self.secondWindow = SecondWindow()   



class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setWindowTitle("Info")
        self.setFixedHeight(500)
        self.setFixedWidth(300)

        self.initUI()

    def initUI(self):
        global items
        global selectedText

        
        #LAYOUT
        hbox = QHBoxLayout()
        
        nameEdit = QLineEdit()
        nameEdit.setAlignment(QtCore.Qt.AlignHCenter)
        nameEdit.setText(selectedText)
        hbox.addWidget(nameEdit)
        
        descEdit = QTextEdit()
        descEdit.setText(items.get(selectedText))



        hbox2 = QHBoxLayout()
        okButton = QPushButton("Ok")
        cancelButton = QPushButton("Cancel")
        hbox2.addWidget(cancelButton)
        hbox2.addWidget(okButton)


        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox)
        vbox.addWidget(descEdit)
        vbox.addLayout(hbox2)
       
        
        self.setLayout(vbox)

        self.show()



#START THE APPLICATION
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Window()
    sys.exit(App.exec())