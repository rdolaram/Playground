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
        selectText = text
        self.lineEdit.clear()
        if text in self.list:
            self.duplicateError()
        else:
            #ADD TEXT TO THE LIST OF TAKEN NAMES
            self.list.append(text)
            
            #ADD TEXT TO DICTIONAIRY AND SET DEFAULT VALUE
            items.update({text:'No notes associated with task.'})
                        
            #CREATE THE ITEM
            curItem = QListWidgetItem()
            curItem.setText(text)
            curItem.setFont(self.font)
            curItem.setTextAlignment(QtCore.Qt.AlignHCenter)
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
        global selectText
        selectText = self.listWidget.currentItem().text()
        self.listWidget.currentItem().setText(selectText)
        self.secondWindow = SecondWindow()

        
        
        

    

class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setWindowTitle("Info")
        self.setFixedHeight(400)
        self.setFixedWidth(300)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        
        self.initUI()

    def initUI(self):
        global items
        global selectText

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        

        #DESCRIPTION EDIT
        self.descEdit = QTextEdit()
        self.descEdit.setText(items.get(selectText))

        
        #BUTTONS
        okButton = QPushButton("Ok")
        okButton.clicked.connect(self.ok)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancel)
        
        hbox2.addWidget(cancelButton)
        hbox2.addWidget(okButton)


        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.descEdit)
        vbox.addLayout(hbox2)
       
        self.setLayout(vbox)

        self.show()


    
    def ok(self):
        global items
        global selectText
    
        descText = self.descEdit.toPlainText()

        #PUSH VALUES INTO DICTIONAIRY
        items[selectText] = descText # WORKS
 
        self.close()

    def cancel(self):
        self.close()


#START THE APPLICATION
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Window()
    sys.exit(App.exec())