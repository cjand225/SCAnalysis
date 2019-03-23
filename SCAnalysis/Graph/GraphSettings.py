"""

    Module: GraphSettings.py
    Purpose: Sidebar widget used to get settings from the user for graph creation, etc.

"""

from PyQt5.QtWidgets import QWidget, QToolBox, QToolButton, QGridLayout, QToolBar
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.uic import loadUi

from SCAnalysis.Logging.Log import getLog


class GraphSettings(QToolBox):

    def __init__(self, figure, canvas, parent=None):
        super(GraphSettings, self).__init__(parent)
        self.figReference = figure
        self.navBar = NavigationToolbar(canvas, parent)
        self.insertItem(0, self.navBar, "Nav")

    '''

        Function: initUI
        Parameters: self
        Return Value: N/A
        Purpose:

    '''

    def initUI(self):
        pass

    '''

        Function: connectActions
        Parameters: self
        Return Value: N/A
        Purpose:

    '''

    def connectActions(self):
        pass
