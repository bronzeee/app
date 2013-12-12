from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from jinja2 import Environment, PackageLoader
from os import getcwd
from Console import Console


class Window(QWidget):
    webview = None

    def __init__(self, url, width, height, controller=None):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.webview = QWebView(self)
        self.webview.page().mainFrame().javaScriptWindowObjectCleared.connect(self.javaScriptWindowObject)
        self.controller = controller
        # webview.page().mainFrame().evaluateJavaScript("alert(1);")
        self.load(url, width, height)
        # self.webview.load(QUrl.fromLocalFile(getcwd() + url))

    def load(self, page, width=None, height=None):
        if width != None and height != None:
            self.resize(width, height)
            self.webview.setGeometry(1, 1, width - 2, height - 2)
        env = Environment(loader=PackageLoader('app', 'templates'))
        template = env.get_template('Window.html')
        self.webview.setHtml(template.render(container=page), QUrl.fromLocalFile(getcwd() + '/'))

    def javaScriptWindowObject(self):
        console = Console();
        self.webview.page().mainFrame().addToJavaScriptWindowObject('application', self)
        self.webview.page().mainFrame().addToJavaScriptWindowObject('console', console)
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
