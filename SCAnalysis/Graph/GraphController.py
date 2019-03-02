"""

    Module: GraphController.py
    Purpose: Controller class for creating and handling graphing objects.


"""
import os

from PyQt5.QtWidgets import QWidget, QGridLayout, QDialog

from SCAnalysis import pkgName
from SCAnalysis.Graph.GraphDialog import GraphDialog
from SCAnalysis.Graph.Graph import Graph
from SCAnalysis.Graph.GraphTab import GraphTab
from SCAnalysis.Graph.GraphSettings import GraphSettings
from SCAnalysis.Graph.GraphTabBar import GraphTabBar
from SCAnalysis.Logging.Log import getLog
from SCAnalysis.ParsePlot.plot import speed_time, voltage_time, motor_current_time, motor_temp_time, battery_temp_time


class GraphController(QWidget):

    def __init__(self, parent=None):
        super(GraphController, self).__init__(parent)

        self.parsePlotList = [speed_time, voltage_time, motor_current_time, motor_temp_time, battery_temp_time]
        self.GraphTabWidget = None
        self.graphCount = 0
        self.maxGraphCount = 20
        self.log = getLog(pkgName)
        self.GraphLayout = QGridLayout()
        self.addTab = QWidget()

        self.GraphList = []

        self.initGraphWindow()

    '''

        Function: initGraphWindow
        Parameters: self
        Return Value: N/A
        Purpose:

    '''

    def initGraphWindow(self):
        self.GraphTabWidget = GraphTab(self)

        self.GraphTabBar = GraphTabBar(self)

        self.GraphTabWidget.setTabBar(self.GraphTabBar)
        self.GraphTabWidget.setTabsClosable(True)
        self.GraphTabWidget.setMovable(True)

        self.GraphLayout.addWidget(self.GraphTabWidget)
        self.setLayout(self.GraphLayout)
        self.GraphTabWidget.addTab(self.addTab, '+')
        self.addTabIndex = self.GraphTabWidget.count() - 1

        # connect signals to functions for creating and removing graphs
        self.GraphTabBar.doubleClicked.connect(self.createGraphDialog)
        self.GraphTabWidget.tabCloseRequested.connect(self.removeGraph)

    '''

        Function: createGraphDialog
        Parameters: self
        Return Value: N/A
        Purpose: 

    '''

    def createGraphDialog(self):
        dialog = GraphDialog()
        retVal = dialog.exec()
        if retVal == QDialog.Accepted:
            self.handleDialogPath(dialog.getPath())
        elif retVal == QDialog.Rejected:
            pass

    '''

        Function: addGraph
        Parameters: self, graphFigure
        Return Value: 
        Purpose:

    '''

    def addGraph(self, graphFigure):
        nGraph = Graph(graphFigure)
        nSettings = GraphSettings(nGraph.getFigure(), nGraph.getCanvas(), self)
        self.GraphList.append((nGraph, nSettings))
        self.GraphTabWidget.addGraph(self.GraphList[self.graphCount][0], self.GraphList[self.graphCount][1],
                                     self.graphCount)
        self.graphCount += 1

    '''

        Function: removeGraph
        Parameters: self, index
        Return Value: 
        Purpose:

    '''

    def removeGraph(self, index):
        self.graphCount -= 1
        self.GraphList.remove(self.GraphList[index])
        self.GraphTabWidget.removeGraph(index)

    '''

        Function: createGraph
        Parameters: self
        Return Value: 
        Purpose:

    '''

    def createGraph(self):
        # create the graph and it's settings.
        nGraph = Graph()
        nSettings = GraphSettings(nGraph.getFigure(), nGraph.getCanvas(), self)
        self.GraphList.append((nGraph, nSettings))
        self.GraphTabWidget.addGraph(self.GraphList[self.graphCount][0], self.GraphList[self.graphCount][1],
                                     self.graphCount)
        self.graphCount += 1

    '''

        Function: handleDialogPath
        Parameters: self, path
        Return Value: 
        Purpose:

    '''

    def handleDialogPath(self, path):
        if os.path.isdir(path):
            for plot in self.parsePlotList:
                self.addGraph(plot(path))
        elif os.path.isfile(path):
            pass
        else:
            pass
