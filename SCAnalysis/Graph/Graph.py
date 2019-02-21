'''

    Individual Widget to store graph in as a pixmap type object

'''

import random
from PyQt5.Qt import QWidget, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from SCAnalysis import pkgName
from SCAnalysis.Logging.Log import getLog


class Graph(QWidget):

    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)

        self.log = getLog(pkgName)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.title = ''

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot()

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

    def editTitle(self, title):
        self.title = title

    def editAxisX(self, xTitle):
        self.axisTitleX = xTitle

    def editAxisY(self, yTitle):
        self.axisTitleY = yTitle

    def editAxisScaleX(self, scale):
        self.scaleValueX = scale

    def editAxisScaleY(self, scale):
        self.scaleValueY = scale

    def saveFigure(self, path):
        self.figure.savefig(path)

    def zoom(self):
        pass
