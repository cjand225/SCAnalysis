'''
Module: AppWindow.py
Purpose: View for entire application, used as a means to convey information to and from user.

'''

import os
from pathlib import Path

from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QStyle, QLayout
from PyQt5.uic import loadUi

from SCAnalysis import pkgName
from SCAnalysis.Resources import quitDialogUIPath, helpDialogUIPath, aboutDocPath, adminDocPath, userDocPath
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
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter,
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

    '''
        Function: connectActions
        Parameters: self
        Return Value: N/A
        Purpose: connects various functions with Actions on AppWindow form, used typically to toggle some child widget.
    
    '''

    def connectActions(self):

        # File
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionOpen_Directory.triggered.connect(self.openDirectory)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveAsFile)
        self.actionClose.triggered.connect(self.closeGraph)
        self.actionExit.triggered.connect(self.close)

        # View
        if self.logWidget is not None:
            self.actionLogs.triggered.connect(lambda e: type(self).toggleWidget(self.logWidget, e))

        # help
        self.actionAbout.triggered.connect(self.createAboutDialog)
        self.actionUser_Manual.triggered.connect(self.createAdminDialog)
        self.actionAdmin_Manual.triggered.connect(self.createUserDialog)

    ''' 

        Function: addLog
        Parameters: self, logwid(QWidget)
        Return Value: N/A
        Purpose: Adds a QWidget from Logging Module, when function is invoked by App Class, which is then
                 handled primarily by AppWindow and Interfaced with the User through text updates within Widget.

    '''

    def addLogWidget(self, widget):
        self.logWidget = widget

    ''' 

        Function: openFileDialog(self)
        Parameters: self
        Return Value: fileName(String) or None
        Purpose: Opens a fileDialog to get input from the user on where the file they are
                 wanting to open happens to exist. if the file doesn't exist it'll return nothing,
                 otherwise it'll return the name of the file prepended with its directory.

    '''

    def openFileDialog(self):
        fileDialog = QFileDialog()
        return fileDialog.getOpenFileName(self, 'Open')

    ''' 
        Function: saveFileDialog(self)
        Parameters: self
        Return Value: FileName(String) or None
        Purpose: Opens a fileDialog to get input from the user on where they would like to save
                 their current session to. If Nothing is pressed on return, it'll return None,
                 otherwise it'll return the name and place of where they would like to save their
                 file.
    '''

    def saveFileDialog(self):
        fileDialog = QFileDialog()
        return fileDialog.getSaveFileName(self, 'Save As')

    ''' 

        Function: closeEvent(self, a0: QCloseEvent)
        Parameters: self, a0: QCloseEvent(QAction)
        Return Value: N/A
        Purpose: Overloads closeEvent Function for AppWindow(QMainWindow), such that it will
                 make sure the user actually intended on closing the program, as well as ensuring
                 its' children gui components have closed as well via handleWidgetClosing() called/
                 within handleClose() function

    '''

    def closeEvent(self, a0: QCloseEvent):
        retVal = self.createDecisionDialog(quitDialogUIPath)
        self.handleClose(retVal, a0)

    '''
        Function: handleClose
        Parameters: self, Return Value, QCloseEven
        Return Value: N/A
        Purpose: Function that handles all closing based on user's choice of wanting to exit the program 
                 or not. 
    '''

    def handleClose(self, retVal, a0: QCloseEvent):
        if retVal == 1:  # if OK clicked - Close
            a0.accept()
            self.handleWidgetClosing()
        # if Cancel or MessageBox is closed - Ignore the signal
        if retVal == 0:
            a0.ignore()

    ''' 

        Function: handleWidgetClosing(self)
        Parameters: self
        Return Value: N/A
        Purpose: Function used to check if a widget exists and if it does, makes sure its close event is called
                 before calling the AppWindow close event.

    '''

    def handleWidgetClosing(self):
        if self.logWidget is not None:
            self.logWidget.close()

    '''

        Function: createAboutDialog
        Parameters: self
        Return Value: N/A
        Purpose: Binds the buttonbox to the close event allowing the ok/close buttons to close the dialog
                 and then executes the dialog to display out to the user.


    '''

    def createAboutDialog(self):
        self.createBrowserDialog(helpDialogUIPath, aboutDocPath)

    '''

        Function: createAdminDialog
        Parameters: self
        Return Value: N/A
        Purpose: Binds the buttonbox to the close event allowing the ok/close buttons to close the dialog
                 and then executes the dialog to display out to the user.


    '''

    def createAdminDialog(self):
        self.createBrowserDialog(helpDialogUIPath, adminDocPath)

    '''

        Function: createUserDialog
        Parameters: self
        Return Value: N/A
        Purpose: Binds the buttonbox to the close event allowing the ok/close buttons to close the dialog
                 and then executes the dialog to displ  ay out to the user.


    '''

    def createUserDialog(self):
        self.createBrowserDialog(helpDialogUIPath, userDocPath)

    '''
    
        Function: createBrowserDialog
        Parameters: self, uiPath, filePath
        Return Value: return value of execution
        Purpose: Creates a general purpose brower dialog used to load any document from a file, mostly used for easy
                 streaming of manuals and other documention to the program itself.
    '''

    def createBrowserDialog(self, uiPath, filePath):
        # create and loadui for QDialog instance
        browserDialog = QDialog()
        browserDialog.ui = loadUi(uiPath, browserDialog)
        # if filePath is specified, create it, otherwise, return Rejected Enum
        if os.path.isfile(filePath):
            # open as a file stream
            file = QFile(filePath)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            # direct stream as HTML, connect close button, execute and return value after close.
            browserDialog.ui.textBrowser.setHtml(stream.readAll())
            browserDialog.ui.buttonBox.clicked.connect(browserDialog.close)
            return browserDialog.exec()
        else:
            return QDialog.Rejected

    '''
        Function: createDecisionDialog
        Parameters: self, uiPath, filePath
        Return Value: return value of execution
        Purpose: creates a general purpose binary decision making Dialog that the user can load from ui file
                 or choose to add programatically.
    '''

    def createDecisionDialog(self, uiPath):
        decisionDialog = QDialog()
        decisionDialog.ui = loadUi(uiPath, decisionDialog)
        return decisionDialog.exec()

    '''
    
        Function: newFile
        Parameters: self
        Return Value: N/A
        Purpose: 
        
    '''

    def newFile(self):
        newLoc = QFileDialog().getSaveFileUrl(self, "New File", str(Path.home()))

    '''

        Function: openDirectory
        Parameters: self
        Return Value: str of chosen directory
        Purpose:

    '''

    def openDirectory(self):
        dirLoc = QFileDialog().getExistingDirectory(self, "Select Directory", str(Path.home()))

    '''

        Function: openFile
        Parameters: self
        Return Value: str of file location
        Purpose:

    '''

    def openFile(self):
        openLoc = QFileDialog().getOpenFileNames(self, "Open File", str(Path.home()))

    '''

        Function: saveAs
        Parameters: self
        Return Value: str of file location
        Purpose:

    '''

    def saveFile(self):
        saveLoc = QFileDialog().getSaveFileUrl(self, "Save File", str(Path.home()))

    '''

        Function: saveAsFile
        Parameters: self
        Return Value:str of file location
        Purpose:

    '''

    def saveAsFile(self):
        saveLoc = QFileDialog().getSaveFileUrl(self, "Save As File", str(Path.home()))

    '''

        Function: closeGraph
        Parameters: self
        Return Value: N/A
        Purpose:

    '''

    def closeGraph(self):
        pass
