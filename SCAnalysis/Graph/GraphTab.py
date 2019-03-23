'''

    QTabWidget used to "store" graphs in the UI until user is finished.

'''

from PyQt5.QtWidgets import QTabWidget, QWidget, QGridLayout

from SCAnalysis import pkgName
from SCAnalysis.Logging.Log import getLog


class GraphTab(QTabWidget):

    def __init__(self, parent=None):
        super(GraphTab, self).__init__(parent)
        self.log = getLog(pkgName)
        self.graphList = []

    '''

        Function: addGraph
        Parameters: self, graph, graphSettings, currentCount
        Return Value: N/A
        Purpose: Takes parameters for Graph, Graphsettings for current graph, and the current total count of graphs and
                 creates a tab associated with this particular graph within the QTabWidget.

    '''

    def addGraph(self, graph, graphSettings, currentCount):
        nWidget = QWidget()
        nLayout = QGridLayout(nWidget)
        nLayout.addWidget(graph, 0, 0, 4, 4)
        nLayout.addWidget(graphSettings, 4, 0, 1, 1)
        nWidget.setLayout(nLayout)
        if graph.title is '':
            self.insertTab(self.count() - 1, nWidget, "Graph " + str(currentCount + 1))
        else:
            self.insertTab(self.count() - 1, nWidget, graph.title)
        self.graphList.append([nWidget, nLayout, graph, graphSettings])
        self.setCurrentWidget(nWidget)

    '''

        Function: removeGraph
        Parameters: self, index
        Return Value: N/A
        Purpose: 

    '''

    def removeGraph(self, index):
        if index in range(0, self.count() - 1):
            self.widget(index).deleteLater()
            self.removeTab(index)
            self.graphList.remove(self.graphList[index])
