import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow

from modules.mainwindow import Ui_MainWindow
from modules.settings import WindowSettings
from modules.parameters import GameParameters
from modules.ultility_functions import load_qpixmap



windowSt = WindowSettings()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        first_maze = load_qpixmap(windowSt.cb_mazes[0]['path'])

        self.setupUi(self)

        '''Settings for combobox selecting mazes'''
        self.cb_mazes.addItems([item['title'] for item in windowSt.cb_mazes])
        self.cb_mazes.currentIndexChanged.connect(self.cb_mazes_index_changed)

        '''Setting for label used to display maze'''
        self.box_maze.setPixmap(first_maze)

        '''Settings for main window'''
        self.setWindowIcon(QIcon(windowSt.icon))
        self.setWindowTitle(windowSt.title)
        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setFixedWidth(windowSt.width)
        self.setFixedHeight(windowSt.height)

        '''Object to store all parameters of the game'''
        self.game_params = GameParameters(windowSt.cb_mazes[0]['path'], first_maze.rect().width(), first_maze.rect().height()) # current maze's infos

    def cb_mazes_index_changed(self, idx):
        changed_maze = load_qpixmap(windowSt.cb_mazes[idx]['path'])

        self.box_maze.setPixmap(changed_maze)
        self.game_params.update(windowSt.cb_mazes[idx]['path'], changed_maze.rect().width(), changed_maze.rect().height()) # update changed maze's infos