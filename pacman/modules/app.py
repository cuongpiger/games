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

        '''Settings for combobox selecting algorithms'''
        self.cb_algorithms.addItems([item['title'] for item in windowSt.cb_algorithms])
        self.cb_algorithms.currentIndexChanged.connect(self.cb_algorithms_index_changed)

        '''Settings for slider feed density'''
        self.sld_feed_density.setRange(0, 100)
        self.sld_feed_density.setSingleStep(10)
        self.sld_feed_density.valueChanged.connect(self.feed_density_value_changed)

        '''Settings for spinbox feed density'''
        self.sb_feed_density.setRange(0, 100)
        self.sb_feed_density.setSingleStep(10)
        self.sb_feed_density.valueChanged.connect(self.feed_density_value_changed)

        '''Settings for slider pacman's feed'''
        self.sld_pacman_speed.setRange(0, 5)
        self.sld_pacman_speed.setSingleStep(1)
        self.sld_pacman_speed.valueChanged.connect(self.pacman_speed_value_changed)

        '''Settings for spinbox pacman's feed'''
        self.sb_pacman_speed.setRange(0, 5)
        self.sb_pacman_speed.setSingleStep(1)
        self.sb_pacman_speed.valueChanged.connect(self.pacman_speed_value_changed)

        '''Settings for label used to display maze'''
        self.box_maze.setPixmap(first_maze)

        '''Settings for main window'''
        self.setWindowIcon(QIcon(windowSt.icon))
        self.setWindowTitle(windowSt.title)
        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setFixedWidth(windowSt.width)
        self.setFixedHeight(windowSt.height)

        '''Object to store all parameters of the game'''
        self.game_params = GameParameters(windowSt.cb_mazes[0]['path'], first_maze.rect().width(), first_maze.rect().height(), windowSt.cb_algorithms[0]['name']) # a game's infos


    def cb_mazes_index_changed(self, idx):
        changed_maze = load_qpixmap(windowSt.cb_mazes[idx]['path'])

        self.box_maze.setPixmap(changed_maze)
        self.game_params.update_maze(windowSt.cb_mazes[idx]['path'], changed_maze.rect().width(), changed_maze.rect().height()) # update changed maze's infos


    def cb_algorithms_index_changed(self, idx):
        self.game_params.algorithm = windowSt.cb_algorithms[idx]['name']


    def feed_density_value_changed(self, val):
        self.sld_feed_density.setValue(val)
        self.sb_feed_density.setValue(val)
        self.game_params.feed_density = val/100


    def pacman_speed_value_changed(self, val):
        self.sld_pacman_speed.setValue(val)
        self.sb_pacman_speed.setValue(val)
        self.game_params.pacman_speed = val