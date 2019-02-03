'''

    Holds all graphs

'''


from PyQt5.QtWidgets import QTabWidget


class GraphWindow(QTabWidget):

    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)
