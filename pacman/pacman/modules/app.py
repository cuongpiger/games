import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow

from modules.mainwindow import Ui_MainWindow
from modules.settings import WindowSettings
from modules.parameters import GameParameters


windowSt = WindowSettings()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        '''Settings for combobox selecting mazes'''
        self.cb_mazes.addItems([item['name'] for item in windowSt.cb_mazes])
        self.cb_mazes.currentIndexChanged.connect(self.cb_mazes_index_changed)

        '''Settings for main window'''
        self.setWindowIcon(QIcon(windowSt.icon))
        self.setWindowTitle(windowSt.title)
        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setFixedWidth(windowSt.width)
        self.setFixedHeight(windowSt.height)

        '''Object to store all parameters of the game'''
        self.game_params = GameParameters(windowSt.cb_mazes[0]['path']) # path to current maze's map

    def cb_mazes_index_changed(self, idx):
        self.box_maze.setPixmap(QPixmap(windowSt.cb_mazes[idx]['path']))
        self.game_params.maze = windowSt.cb_mazes[idx]['path']