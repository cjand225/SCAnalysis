"""

    Module: GraphSettings.py
    Purpose: Sidebar widget used to get settings from the user for graph creation, etc.

"""

from PyQt5.QtWidgets import QWidget


class GraphSettings(QWidget):

    def __init__(self, parent):
        super(GraphSettings, self).__init__(parent)
