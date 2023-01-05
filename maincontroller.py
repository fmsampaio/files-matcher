import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("gui/mainview.ui", self)
        self.setWindowTitle('File Matcher v0.1')
        self.setFixedSize(self.size())

        self.path1 = ''
        self.path2 = ''

        self.singlePathRadioBtn.setChecked(True)
        self.multiPathRadioBtn.setChecked(False)
        self.handleSinglePathSelection()

        self.singlePathRadioBtn.clicked.connect(self.handleSinglePathSelection)
        self.multiPathRadioBtn.clicked.connect(self.handleMultiPathSelection)

        self.openFile1Btn.clicked.connect(self.handleOpenFile1BtnClicked)
        self.openFolder1Btn.clicked.connect(self.handleOpenFolder1BtnClicked)
        self.openFile2Btn.clicked.connect(self.handleOpenFile2BtnClicked)
        self.openFolder2Btn.clicked.connect(self.handleOpenFolder2BtnClicked)


    def handleSinglePathSelection(self):
        print('[DBG] Single path mode was selected!')
        self.path2 = ''
        self.path2TextEdit.setText("")
        self.path2TextEdit.setDisabled(True)
        self.openFile2Btn.setDisabled(True)
        self.openFolder2Btn.setDisabled(True)
        
    def handleMultiPathSelection(self):
        print('[DBG] Multi path mode was selected!')
        self.path2TextEdit.setDisabled(False)
        self.openFile2Btn.setDisabled(False)
        self.openFolder2Btn.setDisabled(False)

    def handleOpenFile1BtnClicked(self):
        self.path1 = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.path1TextEdit.setText(self.path1)
        print(f'[DBG] Selected file for PATH #1: {self.path1}')

    def handleOpenFolder1BtnClicked(self):
        self.path1 = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.path1TextEdit.setText(self.path1)
        print(f'[DBG] Selected folder for PATH #1: {self.path1}')

    def handleOpenFile2BtnClicked(self):
        self.path2 = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.path2TextEdit.setText(self.path2)
        print(f'[DBG] Selected file for PATH #2: {self.path2}')

    def handleOpenFolder2BtnClicked(self):
        self.path2 = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.path2TextEdit.setText(self.path2)
        print(f'[DBG] Selected folder for PATH #2: {self.path2}')


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()