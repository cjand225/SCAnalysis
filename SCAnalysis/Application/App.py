'''
Module: App.py
Purpose: Controller for entire application, used to periodically update project with data to and from the
         model.

'''

import os, sys
from PyQt5.QtWidgets import QApplication

from SCAnalysis import pkgName
from SCAnalysis.Resources import mainUIPath, logUIPath

from SCAnalysis.Application.AppWindow import AppWindow
from SCAnalysis.Graph.GraphController import GraphController
from SCAnalysis.Logging.Log import getLog
from SCAnalysis.Logging.LogWidget import LogWidget


class App(QApplication):

    def __init__(self):
        super(App, self).__init__(sys.argv)

        self.log = getLog(pkgName)

        self.mainWindow = None
        self.GraphMod = None

        # Initializing everything
        self.initApplication()

    def initApplication(self):
        self.initMainWindow()
        self.initLogModule()
        self.initGraphModule()
        self.bindWindowActions()

    def initMainWindow(self):
        self.mainWindow = AppWindow(mainUIPath)
        self.log.debug('Initializing main window.')

    def initGraphModule(self):
        self.GraphMod = GraphController(self.mainWindow)
        self.log.debug('Initializing graphing module.')

    def initLogModule(self):
        self.logWidget = LogWidget(self.mainWindow)

    def run(self):
        self.log.debug('Executing application.')
        self.exec_()

    def bindWindowActions(self):
        self.log.debug('Binding main window actions.')
        self.mainWindow.setCentralWidget(self.GraphMod)
        self.mainWindow.addLogWidget(self.logWidget)
        self.mainWindow.connectActions()
