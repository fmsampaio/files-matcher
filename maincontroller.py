import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("gui/mainview.ui", self)

        self.singlePathRadioBtn.setChecked(True)
        self.multiPathRadioBtn.setChecked(False)
        self.handleSinglePathSelection()

        self.singlePathRadioBtn.clicked.connect(self.handleSinglePathSelection)
        self.multiPathRadioBtn.clicked.connect(self.handleMultiPathSelection)

    def handleSinglePathSelection(self):
        print('[DBG] Single path mode was selected!')
        self.path2TextEdit.setText("")
        self.path2TextEdit.setDisabled(True)
        
    def handleMultiPathSelection(self):
        print('[DBG] Multi path mode was selected!')
        self.path2TextEdit.setDisabled(False)
        


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()