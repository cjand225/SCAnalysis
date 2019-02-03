'''
Module: App.py
Purpose: Controller for entire application, used to periodically update project with data to and from the
         model.

'''

import os, sys
from PyQt5.QtWidgets import QApplication

from SCAnalysis.Application.AppWindow import AppWindow
from SCAnalysis.Application import mainUIPath


class App(QApplication):

    def __init__(self):
        super(App, self).__init__(sys.argv)
        self.mainWindow = None

        # Initializing everything
        self.initApplication()

    def initApplication(self):
        self.initMainWindow()

    def initMainWindow(self):
        self.mainWindow = AppWindow(mainUIPath)

    def run(self):
        self.exec_()

    def bindWindowActions(self):
        pass
