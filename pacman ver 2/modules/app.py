import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QKeySequence, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QShortcut

from modules.ui import Ui_MainWindow
from modules.settings import WindowSettings, GameParameters
from modules.game import Game
# from modules.parameters import GameParameters
# from modules.utility_functions import load_qpixmap
# from modules.game_app import GameApp


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.windowSt = WindowSettings()

        '''Settings for combobox selecting mazes'''
        self.cb_mazes.addItems([item['title'] for item in self.windowSt.mazes])
        self.cb_mazes.currentIndexChanged.connect(self.cb_mazes_index_changed)

        '''Settings for combobox selecting algorithms'''
        self.cb_algorithms.addItems([item['title']
                                     for item in self.windowSt.algorithms])
        self.cb_algorithms.currentIndexChanged.connect(
            self.cb_algorithms_index_changed)

        '''Settings for comboxbox selecting heuristics'''
        self.cb_heuristic.setEnabled(False)

        '''Settings for slider feed density'''
        self.sld_feed_density.setRange(
            self.windowSt.feed_density[0]*100, self.windowSt.feed_density[1]*100)
        self.sld_feed_density.setSingleStep(10)
        self.sld_feed_density.valueChanged.connect(
            self.feed_density_value_changed)

        '''Settings for spinbox feed density'''
        self.sb_feed_density.setRange(
            self.windowSt.feed_density[0]*100, self.windowSt.feed_density[1]*100)
        self.sb_feed_density.setSuffix('%')
        self.sb_feed_density.setSingleStep(10)
        self.sb_feed_density.valueChanged.connect(
            self.feed_density_value_changed)

        '''Settings for slider pacman's speed'''
        self.sld_pacman_speed.setRange(
            self.windowSt.pacman_speed[0], self.windowSt.pacman_speed[1])
        self.sld_pacman_speed.setSingleStep(1)
        self.sld_pacman_speed.valueChanged.connect(
            self.pacman_speed_value_changed)

        '''Settings for spinbox pacman's speed'''
        self.sb_pacman_speed.setRange(
            self.windowSt.pacman_speed[0], self.windowSt.pacman_speed[1])
        self.sb_pacman_speed.setSingleStep(1)
        self.sb_pacman_speed.valueChanged.connect(
            self.pacman_speed_value_changed)

        '''Settings for label used to display maze'''
        self.box_maze.setPixmap(QPixmap(self.windowSt.mazes[0]['path']))

        '''Settings for button run'''
        self.btn_run.clicked.connect(self.btn_run_clicked)
        self.btn_run_shortcut = QShortcut(QKeySequence('Return'), self)
        self.btn_run_shortcut.activated.connect(self.btn_run_clicked)

        '''Settings for main window'''
        self.setWindowIcon(QIcon(self.windowSt.icon))
        self.setWindowTitle(self.windowSt.title)
        self.setWindowFlags(self.windowFlags() & Qt.CustomizeWindowHint)
        self.setFixedWidth(self.windowSt.width)
        self.setFixedHeight(self.windowSt.height)

    def cb_mazes_index_changed(self, idx):
        self.box_maze.setPixmap(QPixmap(self.windowSt.mazes[idx]['path']))

    def cb_algorithms_index_changed(self, idx):
        if self.windowSt.algorithms[idx]['heuristic']:
            self.cb_heuristic.setEnabled(True)
            self.cb_heuristic.addItems(
                [item for item in self.windowSt.algorithms[idx]['heuristic']])
        else:
            self.cb_heuristic.setEnabled(False)
            self.cb_heuristic.clear()

    def feed_density_value_changed(self, val):
        self.sld_feed_density.setValue(val)
        self.sb_feed_density.setValue(val)

    def pacman_speed_value_changed(self, val):
        self.sld_pacman_speed.setValue(val)
        self.sb_pacman_speed.setValue(val)

    def btn_run_clicked(self):
        maze = self.windowSt.mazes[self.cb_mazes.currentIndex()]['mask']
        algorithm = self.windowSt.algorithms[self.cb_algorithms.currentIndex(
        )]['name']
        heuristic = self.cb_heuristic.currentText()
        pacman_speed = self.sb_pacman_speed.value()
        feed_density = self.sb_feed_density.value()/100.
        game_params = GameParameters(
            maze, algorithm, heuristic, pacman_speed, feed_density)
        game = Game(game_params)
        # game = Game(self.game_params)
        # board = game.board
        # feed_pos = game.feed_pos
        # pacman_pos = game.pacman_pos
        # maze_img = self.game_params.maze_img
        # maze_width = self.game_params.maze_width
        # maze_height = self.game_params.maze_height
        # pacman_speed = self.game_params.pacman_speed

        # if self.game_params.algorithm == 'bfs':
        #     path = game.bfs()
        #     game_app = GameApp(board, feed_pos, pacman_pos, pacman_speed, path, maze_img, maze_width, maze_height, self.algo_title + ',' + self.hue_title)
        #     game_app.run()
