'''
Module: App.py
Purpose: Controller for entire application, used to periodically update project with data to and from the
         model.

'''

import os, sys
from PyQt5.QtWidgets import QApplication

from SCAnalysis.Application.AppWindow import AppWindow


class App():
    def __init__(self):
        self.Application = None
        self.mainWindow = None
        self.running = False

        # Initializing everything
        self.initApplication()
        self.initMainWindow()

    def initApplication(self):
        self.Application = QApplication(sys.argv)

    def initMainWindow(self):
        self.mainWindow = AppWindow()

    def run(self):
        self.running = True
        self.Application.exec_()

    def exit(self):
        self.running = False
        self.Application.exit(0)
