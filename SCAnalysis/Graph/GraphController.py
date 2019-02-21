"""

    Module: GraphController.py
    Purpose: Controller class for creating and handling graphing objects.


"""

from PyQt5.QtWidgets import QWidget, QGridLayout

from SCAnalysis import pkgName
from SCAnalysis.Graph.Graph import Graph
from SCAnalysis.Graph.GraphTab import GraphTab
from SCAnalysis.Graph.GraphSettings import GraphSettings
from SCAnalysis.Logging.Log import getLog


class GraphController(QWidget):

    def __init__(self, parent=None):
        super(GraphController, self).__init__(parent)

        self.log = getLog(pkgName)

        self.GraphWindow = None
        self.GraphLayout = QGridLayout()
        self.graphCount = 0
        self.GraphList = dict()

        self.initGraphWindow()

    def initGraphWindow(self):
        self.GraphWindow = GraphTab(self)
        self.GraphLayout.addWidget(self.GraphWindow)
        self.setLayout(self.GraphLayout)
        self.GraphWindow.addTab(QWidget(), '+')

    def initGraphSettings(self):
        self.GraphSettings = GraphSettings(self)

    def createGraph(self):
        pass

    def addGraph(self):
        pass

    def removeGraph(self):
        pass

    def updateGraph(self):
        pass

    def switchGraph(self):
        pass
