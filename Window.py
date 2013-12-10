from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from os import getcwd


class Window(QWidget):
    webview = None

    def __init__(self, url, width, height, controller=None):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(width, height)

        self.webview = QWebView(self)
        self.webview.setGeometry(1, 1, width - 2, height - 2)
        self.webview.page().mainFrame().javaScriptWindowObjectCleared.connect(self.javaScriptWindowObject)
        self.controller = controller
        # webview.page().mainFrame().evaluateJavaScript("alert(1);")
        self.webview.load(QUrl.fromLocalFile(getcwd() + url))

    def javaScriptWindowObject(self):
        self.webview.page().mainFrame().addToJavaScriptWindowObject('application', self)
        if self.controller:
            self.webview.page().mainFrame().addToJavaScriptWindowObject("controller", self.controller)

    @pyqtSlot()
    def quit(self):
        self.close()

    @pyqtSlot("int", "int")
    def moveTo(self, offsetX, offsetY):
        self.move(offsetX, offsetY)

    @pyqtSlot()
    def minimize(self):
        self.showMinimized()

    @pyqtSlot("QString")
    def info(self, string):
        print(string)
