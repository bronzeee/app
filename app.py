# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from Console import Console
from Window import Window
from os import getcwd


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Window()
    form.setWindowFlags(Qt.FramelessWindowHint)
    # bmp = QBitmap(form.size())
    # p = QPainter()
    # p.begin(bmp)
    # p.fillRect(bmp.rect(), Qt.white)
    # p.setBrush(QColor(0,0,0))
    # p.drawRoundedRect(bmp.rect(), 5, 5)
    # p.setPen(QColor(255,255,255,255))
    # p.drawPoints(QPointF(form.width()-2,form.height()-1), QPointF(form.width()-1,form.height()-2))
    # p.setPen(QColor(0,0,0))
    # p.drawPoints(QPointF(0,2),QPointF(3,0),QPointF(2,0),QPointF(1,1))1
    # p.end()
    # form.setMask(bmp)
    form.resize(250, 600)
    webview = QWebView(form)
    console = Console()
    webview.setGeometry(1, 1, form.width() - 2, form.height() - 2)
    webview.page().mainFrame().addToJavaScriptWindowObject("console", console)
    webview.page().mainFrame().addToJavaScriptWindowObject("application", form)
    webview.load(QUrl.fromLocalFile(getcwd() + "/page/index.html"))
    form.show()
   # webview.page().mainFrame().evaluateJavaScript("alert(1);") 
    sys.exit(app.exec_())
