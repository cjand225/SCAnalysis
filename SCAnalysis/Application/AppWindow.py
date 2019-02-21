'''
Module: AppWindow.py
Purpose: View for entire application, used as a means to convey information to and from user.

'''

from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QStyle, QLayout
from PyQt5.uic import loadUi

from SCAnalysis import pkgName
from SCAnalysis.Resources import quitDialogUIPath, helpDialogUIPath
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
        # Initialize Dialogs
        self.initFileDialog()
        self.initHelpDialog(helpDialogUIPath)
        self.initAboutDialog(helpDialogUIPath)
        self.initCloseDialog(quitDialogUIPath)
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
        if self.logWidget is not None:
            self.actionLogs.triggered.connect(lambda e: type(self).toggleWidget(self.logWidget, e))

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

        Function: initFileDialog(self)
        Parameters: self
        Return Value: N/A
        Purpose: Initializes a QFileDialog used primarily for getting input from the user on where they 
                 would like to read or write a file. Needs to be called before openFileDialog, saveAsFileDialog,
                 and saveFileDialog

    '''

    def initFileDialog(self):
        self.fileDialog = QFileDialog(self)

    '''

        Function: initAboutDialog
        Parameters: uiPath, filePath
        Return Value: N/A
        Purpose: Instances a QDialog given a filepath in UIpath parameter and a file containing data to display
                 given by filePath, loads file into a text stream that then is set as html for the textbrowser
                 built into the Dialog's ui file. If no file path is given, it'll just return none 

    '''

    def initAboutDialog(self, uiPath, filePath=None):
        self.aboutDialog = QDialog()
        self.aboutDialog.ui = loadUi(uiPath, self.aboutDialog)
        if filePath is not None:
            file = QFile(filePath)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            self.aboutDialog.ui.textBrowser.setHtml(stream.readAll())

    '''

        Function: initHelpDialog
        Parameters: uiPath, filePath
        Return Value: N/A
        Purpose: Instances a QDialog given a filepath in UIpath parameter and a file containing data to display
                 given by filePath, loads file into a text stream that then is set as html for the textbrowser
                 built into the Dialog's ui file. If no file path is given, it'll just return none


    '''

    def initHelpDialog(self, uiPath, filePath=None):
        self.helpDialog = QDialog()
        self.helpDialog.ui = loadUi(uiPath, self.helpDialog)
        if filePath is not None:
            file = QFile(filePath)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            self.helpDialog.ui.textBrowser.setHtml(stream.readAll())

    ''' 

        Function: openFileDialog(self)
        Parameters: self
        Return Value: fileName(String) or None
        Purpose: Opens a fileDialog to get input from the user on where the file they are
                 wanting to open happens to exist. if the file doesn't exist it'll return nothing,
                 otherwise it'll return the name of the file prepended with its directory.

    '''

    def openFileDialog(self):
        filename = self.fileDialog.getOpenFileName(self, 'Open File')
        if filename:
            return filename[0]
        else:
            return None

    ''' 
        Function: saveAsFileDialog(self)
        Parameters: self
        Return Value: FileName(String) or None
        Purpose: Opens a fileDialog to get input from the user on where they would like to save
                 their current session to. If Nothing is pressed on return, it'll return None,
                 otherwise it'll return the name and place of where they would like to save their
                 file.
    '''

    def saveAsFileDialog(self):
        filename = self.fileDialog.getSaveFileName(self, 'Save File')
        if filename != '':
            return filename[0]
        else:
            return None

    def initCloseDialog(self, uipath):
        self.QuitMsg = QDialog()
        self.QuitMsg.ui = loadUi(uipath, self.QuitMsg)

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
        retVal = self.QuitMsg.exec()  # grabs event code from Message box execution
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
        self.close()

    '''

        Function: handleAboutDialog
        Parameters: self
        Return Value: N/A
        Purpose: Binds the buttonbox to the close event allowing the ok/close buttons to close the dialog
                 and then executes the dialog to display out to the user.


    '''

    def handleAboutDialog(self):
        self.aboutDialog.ui.buttonBox.clicked.connect(self.aboutDialog.close)
        self.aboutDialog.exec()

    '''

        Function: handleHelpDialog
        Parameters: self
        Return Value: N/A
        Purpose: Binds the buttonbox to the close event allowing the ok/close buttons to close the dialog
                 and then executes the dialog to display out to the user.


    '''

    def handleHelpDialog(self):
        self.helpDialog.ui.buttonBox.clicked.connect(self.helpDialog.close)
        self.helpDialog.exec()
