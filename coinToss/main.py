from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

import sys
import os
import pygame
import time
import random


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #USER INTERFACE
        self.setWindowTitle("Coin Flip")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'coin.png')))
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        hbox = QHBoxLayout()
        
        #FLIP BUTTON CUSTOMIZATION
        bFlip = QPushButton("Flip")
        bFlip.setToolTip("Click to simulate coin toss!")
        bFlip.clicked.connect(self.onClick)
        hbox.addWidget(bFlip)


        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox)
    

        #DEFAULT MYSTERY IMAGE
        self.labelImage = QLabel(self)
        pixmap = QPixmap(os.path.join(os.path.dirname(__file__), 'mystery.png'))
        self.labelImage.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.vbox.addWidget(self.labelImage, alignment = Qt.AlignCenter)


        self.setLayout(self.vbox)
        self.show()
    

    #METHOD FOR CLICKING MAIN BUTTON
    def onClick(self):
        audioDir = os.path.join(os.path.dirname(__file__), 'toss.mp3')
        pygame.init()
        pygame.mixer.music.load(audioDir)
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()
        
        
        pixmap = QPixmap(self.randomSide())
        self.labelImage.setPixmap(pixmap.scaled(150,150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.vbox.addWidget(self.labelImage, alignment = Qt.AlignCenter)
        
    #GENERATE RANDOM SIDE FROM TWO SELECTIONS
    def randomSide(self):
        headsDir = os.path.join(os.path.dirname(__file__), 'heads.png')
        tailsDir = os.path.join(os.path.dirname(__file__), 'tails.png')
        selections = [headsDir, tailsDir]
        
        return random.choice(selections)
    



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())