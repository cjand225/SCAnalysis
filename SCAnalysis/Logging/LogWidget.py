import logging

from PyQt5.QtWidgets import QWidget, QStyle, QApplication, QPlainTextEdit, QTabWidget, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

from SCAnalysis.Logging.Log import getLog
from SCAnalysis.Logging.Filters import infoFilter, debugFilter, criticalFilter, warningFilter, errorFilter


class LogWidget(QWidget):

    def __init__(self, uipath, parent=None):
        super().__init__(parent)
        self.UIPath = uipath

        # create widget UI
        self.initUI()

        # get log
        self.log = getLog(__name__)
        self.format = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s')
        self.filterList = [infoFilter, debugFilter, warningFilter, errorFilter, criticalFilter]
        self.filterTabNames = ['Info', 'Debug', 'Warning', 'Error', 'Critical']
        self.handlerAmount = len(self.filterTabNames)
        self.handlerList = [] * self.handlerAmount

        # create tabs to use for handlers output
        self.tabWidget = QTabWidget()
        self.tabsList = [] * self.handlerAmount
        self.tabLayouts = [] * self.handlerAmount

        # iterate through the amount of possible filters for log and add to widget
        for x in range(0, self.handlerAmount):
            handler = QTextEditLogger(self)
            handler.setFormatter(self.format)
            handler.addFilter(self.filterList[x]())
            self.log.addHandler(handler)

            tab = QWidget()
            self.tabWidget.addTab(tab, self.filterTabNames[x])
            tabLayout = QGridLayout(tab)

            tab.setLayout(tabLayout)
            tabLayout.addWidget(handler.widget)

            self.handlerList.append(handler)
            self.tabsList.append(tab)
            self.tabLayouts.append(tabLayout)

        self.ui.logLayout.addWidget(self.tabWidget)
        self.show()

    '''  
        Function: initUI
        Parameters: self
        Return Value: N/A
        Purpose: Initializes, Loads and Adds UI components to LogWidget.
    '''

    def initUI(self):
        self.ui = loadUi(self.UIPath, self)
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignBottom,
                                            self.size(), QApplication.desktop().availableGeometry()))

    def setFormat(self, format):
        self.format = format
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
