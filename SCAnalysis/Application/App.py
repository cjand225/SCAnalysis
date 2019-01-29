'''
Module: App.py
Purpose: Controller for entire application, used to periodically update project with data to and from the
         model.

'''

import os, sys
from PyQt5.QtWidgets import QApplication


class App():
    def __init__(self):
        self.Application = None
        self.mainWindow = None
        self.running = False

        self.graph = None

        # Initializing everything
        self.initApplication()

    def initApplication(self):
        self.Application = QApplication(sys.argv)

    def initMainWindow(self):
        print("")
