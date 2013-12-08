from PyQt5.QtCore import QObject, pyqtSlot

class Console(QObject): 
    @pyqtSlot("QString") 
    def info(self, string): 
        print(string)

    @pyqtSlot("QString") 
    def debug(self, string): 
        print(string)

    @pyqtSlot("QString") 
    def error(self, string): 
        print(string)

    @pyqtSlot("QString") 
    def log(self, string): 
        print(string)