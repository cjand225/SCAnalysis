import logging

from PyQt5.QtWidgets import QWidget, QStyle, QApplication, QPlainTextEdit, QTabWidget, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

from SCAnalysis import pkgName
from SCAnalysis.Resources import logUIPath
from SCAnalysis.Logging import logDefaultFormat
from SCAnalysis.Logging.Log import getLog
from SCAnalysis.Logging.Filters import infoFilter, debugFilter, criticalFilter, warningFilter, errorFilter


class LogWidget(QWidget):

    def __init__(self, uipath, parent=None):
        super(LogWidget, self).__init__(parent)
        self.UIPath = logUIPath

        # create widget UI
        self.initUI()

        # get log
        self.log = getLog(pkgName)
        self.filterList = [infoFilter, debugFilter, warningFilter, errorFilter, criticalFilter]
        self.filterTabNames = ['Info', 'Debug', 'Warning', 'Error', 'Critical']
        self.handlerAmount = len(self.filterTabNames)
        self.handlerList = [] * self.handlerAmount

        # create QTabWidget and lists for dynamically creating handlers
        self.tabWidget = QTabWidget()
        self.tabsList = [] * self.handlerAmount
        self.tabLayouts = [] * self.handlerAmount

        # create tabs, add to tabwidget, add tabwidget to logWidget
        self.initTabs()
        self.ui.logLayout.addWidget(self.tabWidget)

    '''  
        Function: initUI
        Parameters: self
        Return Value: N/A
        Purpose: Initializes, Loads and Adds UI components to logWidget.
    '''

    def initUI(self):
        self.ui = loadUi(self.UIPath, self)
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignBottom,
                                            self.size(), QApplication.desktop().availableGeometry()))

    '''  
        Function: setFormat
        Parameters: self format
        Return Value: N/A
        Purpose: Changes the format in which log message records are displayed.
    '''

    def initTabs(self):
        # iterate through the amount of possible filters for log and add to widget
        for x in range(0, self.handlerAmount):
            handler = QTextEditLogger(self)
            handler.setFormatter(logDefaultFormat)
            handler.addFilter(self.filterList[x]())
            self.log.addHandler(handler)

            # create a tab and its layout, add it to the tab widget
            tab = QWidget()
            self.tabWidget.addTab(tab, self.filterTabNames[x])
            tabLayout = QGridLayout(tab)

            tab.setLayout(tabLayout)
            tabLayout.addWidget(handler.widget)

            # add the recently created objects to a list in case of need later.
            self.handlerList.append(handler)
            self.tabsList.append(tab)
            self.tabLayouts.append(tabLayout)

    '''  
        Function: setFormat
        Parameters: self format
        Return Value: N/A
        Purpose: Changes the format in which log message records are displayed.
    '''

    def setFormat(self, format):
        # sets the format within the logwidget class
        self.format = format
        # sets format for every handler within the logwidget tabs
        for x in range(0, self.handlerAmount):
            self.handlerList[x].setFormatter(self.format)


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    '''  
        Function: emit
        Parameters: self, record
        Return Value: N/A
        Purpose: Emits records that can be attached and filtered via filtering classes.
    '''

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
