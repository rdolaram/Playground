'''
Rakesh Dolaram
Python Painting Application
'''

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.initCanvas()
    
    def initUI(self):
        #INIT USER INTERFACE
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setWindowTitle("pyPainter")
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'paintbrush.png')))
        
        self.show()

       
    def initCanvas(self):
        #CREATE DEFAULT CANVAS
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)

        self.drawing = False
        self.brushSize = 5
        self.brushColor = QtCore.Qt.black

        self.lastPoint = QtCore.QPoint()

        #CREATE MENUBAR
        menuBar = self.menuBar()
        
        #FILE MENU
        fileMenu = menuBar.addMenu("File")

        saveAction = QAction(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'save.png')), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'clear.png')), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)


        #BRUSH SIZE MENU
        brushMenu = menuBar.addMenu("Brush Size")

        threepxAction = QAction("3px", self)
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threepx)

        fivepxAction = QAction("5px", self)
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivepx)

        sevenpxAction = QAction("7px", self)
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenpx)

        ninepxAction = QAction("9px", self)
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninepx)

        selectSizeAction = QAction("Select Brush Size", self)
        brushMenu.addAction(selectSizeAction)
        selectSizeAction.triggered.connect(self.selectSize)


        #BRUSH COLOR MENU
        brushColor = menuBar.addMenu("Brush Color")

        blackAction = QAction(QtGui.QIcon(""), "Black", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.black)    

        redAction = QAction(QtGui.QIcon(""), "Red", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.red)

        greenAction = QAction(QtGui.QIcon(""), "Green", self)
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.green)

        blueAction = QAction(QtGui.QIcon(""), "Blue", self)
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blue)

        selectColorAction = QAction(QtGui.QIcon(""), "Select Color", self)
        brushColor.addAction(selectColorAction)
        selectColorAction.triggered.connect(self.selectColor)



    #PAINT FUNCTIONALITY    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            
    
    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) & self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.brushColor, self.brushSize, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            print(self.lastPoint)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == QtCore.Qt.LeftButton:
            self.drawing = False
    
    def paintEvent(self, event):
        canvasPainter = QtGui.QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())



    #FILE FUNCTIONS
    def save(self):
        filePath,  _= QFileDialog.getSaveFileName(self, 'Save Image', "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)") 
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(QtCore.Qt.white)
        self.update()
    

    #BRUSH SIZE FUNCTIONS
    def threepx(self):
        self.brushSize = 3
    def fivepx(self):
        self.brushSize = 5
    def sevenpx(self):
        self.brushSize = 7
    def ninepx(self):
        self.brushSize = 9    
    def selectSize(self):
        size, ok = QInputDialog.getInt(self, "Size", "Select Brush Size")
        if ok:
            self.brushSize = size


    #BRUSH COLOR FUNCTIONS
    def black(self):
        self.brushColor = QtCore.Qt.black
    def green(self):
        self.brushColor = QtCore.Qt.green
    def blue(self):
        self.brushColor = QtCore.Qt.blue
    def red(self):
        self.brushColor = QtCore.Qt.red
    def selectColor(self):
        color = QColorDialog.getColor()
        self.brushColor = color



if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyle("Fusion")
    window = Window()
    sys.exit(App.exec())