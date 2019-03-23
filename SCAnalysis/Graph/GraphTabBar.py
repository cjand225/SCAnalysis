'''

    QTabBar class used for Tab bar

'''

from PyQt5.QtWidgets import QTabBar
from PyQt5.QtCore import pyqtSignal, Qt


class GraphTabBar(QTabBar):
    doubleClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QTabBar, self).__init__(parent)
        self.previousIndex = self.count() - 1

    def mouseDoubleClickEvent(self, mouseEvent):
        self.previousIndex = self.tabAt(mouseEvent.pos())
        if mouseEvent.button() == Qt.LeftButton and self.previousIndex == self.count() - 1:
            self.doubleClicked.emit(self.previousIndex)
        QTabBar.mouseDoubleClickEvent(self, mouseEvent)
