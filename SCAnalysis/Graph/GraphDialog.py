'''

    Dialog used to create graph
    https://www.tutorialspoint.com/pyqt/pyqt_qcheckbox_widget.htm
'''
import os

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout, QLabel, QLineEdit, \
    QComboBox, QCheckBox, QButtonGroup, QFileDialog, QRadioButton, QPushButton
from PyQt5.uic import loadUi


class GraphDialog(QDialog):

    def __init__(self, parent=None):
        super(GraphDialog, self).__init__(parent)
        self.chosenPath = ''
        self.createBaseForm()
        self.fDialog = QFileDialog()
        self.setWindowTitle("Create Graph(s)")
        self.connectActions()

    def connectActions(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.fileButton.clicked.connect(self.handleRadioSelection)
        self.dirButton.clicked.connect(self.handleRadioSelection)
        self.pushButton.clicked.connect(self.handleDirExecution)
        self.textField.textChanged.connect(self.checkTextField)

    def initUI(self):
        self.mLayout.addWidget(self.buttonBox)
        pass

    def createBaseForm(self):
        # initalize objects for form
        self.mLayout = QVBoxLayout()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.baseForm = QGroupBox("Graph Settings")
        self.baseFormLayout = QFormLayout()
        self.dirButton = QRadioButton("Directory")
        self.fileButton = QRadioButton("File")
        self.textField = QLineEdit()
        self.pushButton = QPushButton("Open")

        # set attributes
        self.setMinimumWidth(500)
        self.setMinimumHeight(100)
        self.textField.setMinimumWidth(int(self.width() / 2))
        self.pushButton.setMaximumWidth(int(self.width() / 6))
        self.dirButton.setChecked(True)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        # add to layout
        self.baseFormLayout.addRow(self.dirButton)
        self.baseFormLayout.addRow(self.fileButton)
        self.baseFormLayout.addRow(self.textField, self.pushButton)

        # set layout
        self.baseForm.setLayout(self.baseFormLayout)

        # add to main layout of dialog
        self.mLayout.addWidget(self.baseForm)
        self.mLayout.addWidget(self.buttonBox)

        # set layout for entire Qdialog
        self.setLayout(self.mLayout)

    def done(self, a0: int):
        return super(GraphDialog, self).done(a0)

    def handleDirExecution(self):
        directory = self.fDialog.getExistingDirectory()
        self.textField.setText(directory)
        self.checkPath(self.textField.text())

    def handleFileExecution(self):
        files = self.fDialog.getOpenFileNames()

    def handleRadioSelection(self):
        if self.dirButton.isChecked():
            self.fileButton.setChecked(False)
            self.textField.clear()
            if self.pushButton.receivers(self.pushButton.clicked) > 0:
                self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(self.handleDirExecution)
        elif self.fileButton.isChecked():
            self.dirButton.setChecked(False)
            self.textField.clear()
            if self.pushButton.receivers(self.pushButton.clicked) > 0:
                self.pushButton.clicked.disconnect()
            self.pushButton.clicked.connect(self.handleFileExecution)

    def checkPath(self, path):
        if os.path.isdir(path) or os.path.isfile(path):
            self.chosenPath = os.path.abspath(path)

    def getPath(self):
        return self.chosenPath

    def checkTextField(self):
        if os.path.isfile(self.textField.text()) or os.path.isdir(self.textField.text()):
            self.textField.setStyleSheet("QLineEdit {background: rgba(0, 255, 0,0.6);}")
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        elif self.textField.text() == '':
            self.textField.setStyleSheet("QLineEdit {background: rgba(255, 255, 255,0.6);}")
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.textField.setStyleSheet("QLineEdit {background: rgba(255, 0, 0,0.6);}")
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
