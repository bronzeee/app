from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from os import getcwd


class Window(QWidget):

    def __init__(self, url, width, height, controller=None):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(width, height)

        webview = QWebView(self)
        webview.setGeometry(1, 1, width - 2, height - 2)
        webview.page().mainFrame().addToJavaScriptWindowObject(
            "application", self)

        if controller:
            webview.page().mainFrame().addToJavaScriptWindowObject(
                "controller", controller)

        # webview.page().mainFrame().evaluateJavaScript("alert(1);")
        webview.load(QUrl.fromLocalFile(getcwd() + url))

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
