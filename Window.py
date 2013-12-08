from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

    @pyqtSlot()
    def quit(self):
        self.close()

    @pyqtSlot("int", "int")
    def moveTo(self, offsetX, offsetY):
        self.move(offsetX, offsetY)

    @pyqtSlot()
    def minSize(self):
        self.showMinimized()
