import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow

from modules.mainwindow import Ui_MainWindow
from modules.settings import WindowSetting


windowSt = WindowSetting()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.cb_mazes.addItems([item['name'] for item in windowSt.cb_mazes])


        self.setWindowIcon(QIcon(windowSt.icon))
        self.setWindowTitle(windowSt.title)
        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setFixedWidth(windowSt.width)
        self.setFixedHeight(windowSt.height)

