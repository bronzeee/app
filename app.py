# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from Window import Window
from os import getcwd

class LoginController(QObject):

    @pyqtSlot("QString", "QString", "bool") 
    def login(self, username, password, remember_me):
        if remember_me :
            pass
        print('username : %s, password : %s, remember_me : %s' % (username , password , remember_me))

        if True :
            form.load('main')

        return True;

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = LoginController()
    form = Window("login", 250, 600, controller)
    form.show()
    sys.exit(app.exec_())
