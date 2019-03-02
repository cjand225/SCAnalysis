'''

    Individual Widget to store Figure within a figure canvas on itself.

'''

import random
from PyQt5.Qt import QWidget, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from SCAnalysis import pkgName
from SCAnalysis.Logging.Log import getLog


class Graph(QWidget):

    def __init__(self, graphFigure=None, parent=None):
        super(Graph, self).__init__(parent)

        self.log = getLog(pkgName)

        self.figure = None
        if graphFigure is None:
            self.figure = Figure()
            self.title = ''
        else:
            self.figure = graphFigure
            self.title = self.figure.get_axes()[0].get_title()

        self.canvas = FigureCanvas(self.figure)
        self.figure.tight_layout()

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # self.canvas.draw()

    '''

        Function:
        Parameters:
        Return Value:
        Purpose:

    '''

    def plot(self):
        # clear plot if its already been populated
        self.figure.clf()
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        # Set title for figure
        self.figure.suptitle(self.title)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    '''

        Function: createFigure
        Parameters: self
        Return Value: N/A
        Purpose:

    '''

    def createFigure(self):
        pass

    '''

        Function: setFigure
        Parameters: self, figure
        Return Value: N/A
        Purpose:

    '''

    def setFigure(self, figure):
        self.canvas.figure = figure
        self.canvas.draw()

    '''

        Function: getFigure
        Parameters: self
        Return Value: self.figure (Figure from matplotlib.figure)
        Purpose:

    '''

    def getFigure(self):
        return self.figure

    '''

        Function: getCanvas
        Parameters: self
        Return Value: FigureCanvasQTAgg
        Purpose:

    '''

    def getCanvas(self):
        return self.canvas

    '''

        Function: updateFigure
        Parameters: self, data
        Return Value: N/A
        Purpose:

    '''

    def updateFigure(self, data):
        pass
