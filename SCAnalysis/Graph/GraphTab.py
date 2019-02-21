'''

    QTabWidget used to "store" graphs in the UI until user is finished.

'''

from PyQt5.QtWidgets import QTabWidget, QWidget

from SCAnalysis import pkgName
from SCAnalysis.Graph import Graph
from SCAnalysis.Graph import GraphSettings
from SCAnalysis.Logging.Log import getLog


class GraphTab(QTabWidget):

    def __init__(self, parent=None):
        super(GraphTab, self).__init__(parent)
        self.log = getLog(pkgName)

        self.graphList = []

    def addGraph(self, graph):
        if graph.__class__ is QWidget.__class__:
            # make graph settings
            self.insertTab(self.count() - 2, graph, graph.title)
            self.graphList.append([graph])

    def removeGraph(self, index):
        # make sure index is within range of the tab count,
        # except last tab since we use that as a means to add more graphs
        if index in range(0, self.count() - 1):
            # remove settings and graph tab
            self.removeTab(index)
