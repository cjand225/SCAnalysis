from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QStyle
from PyQt5.uic import loadUi


class AppWindow():
    def __int__(self):
        self.window = None
        self.initWindow()

    def initWindow(self):
        self.window = QMainWindow()
