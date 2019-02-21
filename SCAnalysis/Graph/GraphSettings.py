"""

    Module: GraphSettings.py
    Purpose: Sidebar widget used to get settings from the user for graph creation, etc.

"""

from PyQt5.QtWidgets import QWidget, QDockWidget
from PyQt5.uic import loadUi

from SCAnalysis.Graph.GraphTypes import GraphTypes
from SCAnalysis.Logging.Log import getLog


class GraphSettings(QDockWidget):

    def __init__(self, path, figure, parent=None):
        super(GraphSettings, self).__init__(parent)
        self.uiPath = path
        self.figReference = figure

        self.initUI()

    def initUI(self):
        self.settingsUi = loadUi(self.uiPath)

    def connectActions(self):
        pass

