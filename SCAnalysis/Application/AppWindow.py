'''
Module: AppWindow.py
Purpose: View for entire application, used as a means to convey information to and from user.

'''

from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QStyle, QLayout
from PyQt5.uic import loadUi

from SCAnalysis import pkgName
from SCAnalysis.Logging.Log import getLog


class AppWindow(QMainWindow):

    def __init__(self, uipath):
        super(AppWindow, self).__init__()
        # initialize Window
        self.uiPath = uipath
        self.log = getLog(pkgName)
        self.logWidget = None

        self.initWindow()

    '''
        Function: initWindow
        Parameters: self
        Return Value: N/A
        Purpose: Initializes the Main Window widget for the Application and displays it to user.
        
    '''

    def initWindow(self):
        self.mainWindowUI = loadUi(self.uiPath, self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignHCenter,
                                            self.size(), QApplication.desktop().availableGeometry()))
        self.show()

    ''' 

        Function: toggleWidget
        Parameters: widget, e
        Return Value: N/A
        Purpose: static method that involves toggling any of the widgets bound to the main app window, allowing
                 reduction of repetitious code for different widgets

    '''

    @staticmethod
    def toggleWidget(widget, e):
        if widget.isVisible():
            widget.hide()
        else:
            widget.show()

    def connectActions(self):
        if self.logWidget is not None:
            self.actionLogs.triggered.connect(lambda e: type(self).toggleWidget(self.logWidget, e))

    def addLogWidget(self, widget):
        self.logWidget = widget
