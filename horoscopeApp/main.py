'''
Rakesh Dolaram
Displays daily horoscope & quote.
'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
import sys
import requests 
from bs4 import BeautifulSoup

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.getHoroscope()
        self.sendUI()

        #Vertical Layout Configuration
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox2.setAlignment(QtCore.Qt.AlignHCenter)
        vbox2.addStretch()
        hbox = QHBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)
        #Horizontal Layout Configuration
        vbox.addLayout(hbox)
        hbox.addWidget(self.nameLabel)
        hbox.addWidget(self.numLabel)
        #Send Button
        vbox.addLayout(vbox2)
        vbox2.addWidget(self.sendButton)
        
        self.setLayout(vbox)

        self.show()

    def initUI(self):
        self.setWindowTitle("Horoscopes")
        self.setFixedWidth(1000)
        self.setFixedHeight(350)
        
        #Credit Label
        self.label = QLabel() 
        self.setFont(QtGui.QFont("Times", 15, QFont.Bold))
        self.label.setWordWrap(True)

        #Selection Box
        self.combo = QComboBox()
        self.combo.addItem("Aries")
        self.combo.addItem("Taurus")
        self.combo.addItem("Gemini")
        self.combo.addItem("Cancer")
        self.combo.addItem("Leo")
        self.combo.addItem("Virgo")
        self.combo.addItem("Libra")
        self.combo.addItem("Scorpio")
        self.combo.addItem("Sagittarius")
        self.combo.addItem("Capricorn")
        self.combo.addItem("Aquarius")
        self.combo.addItem("Pisces")

        self.combo.currentTextChanged.connect(self.getHoroscope)


    def sendUI(self):
        #Name LineEdit
        self.nameLabel = QLineEdit()
        self.nameLabel.setFixedWidth(300)
        self.nameLabel.setPlaceholderText("Recipient's name")
        #Num Line Edit
        self.numLabel = QLineEdit()
        self.numLabel.setFixedWidth(300)
        self.numLabel.setPlaceholderText("Recipient's number")
        self.numLabel.setMaxLength(10)
        #Send Button
        self.sendButton = QPushButton()
        self.sendButton.setText("Send")
        #Send Button StyleSheet    
        self.sendButton.setStyleSheet('QPushButton {background-color: #0a6cff; color: white; font: bold; font-size: 25px; height: 30px; width: 20px;}')
        self.sendButton.setFixedWidth(150)
        self.sendButton.clicked.connect()
        

    def getHoroscope(self):
        text = self.combo.currentText()
        
        if text == 'Aries':
            number = '1'
        elif text == "Taurus":
            number = '2'
        elif text == "Gemini":
            number = '3'
        elif text == "Cancer":
            number = '4'
        elif text == "Leo":
            number = '5'
        elif text == "Virgo":
            number = '6'
        elif text == "Libra":
            number = '7'
        elif text == "Scorpio":
            number = '8'
        elif text == "Sagittarius":
            number = '9'
        elif text == "Capricorn":
            number = '10'
        elif text == "Aquarius":
            number = '11'
        elif text == "Pisces":
            number = '12'
        
        result = requests.get("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + number)
        src = result.content
        soup = BeautifulSoup(src)
        page = soup.find("p").getText()
       
        self.label.setText(page + "\n\nHoroscope from: https://www.horoscope.com/us/index.aspx")


    def confirmPrompt(self):
        pass

                

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Window()
    sys.exit(App.exec())