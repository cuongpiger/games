from PySide2.QtGui import QIcon
from modules.util_functions import readJson
CELL = 30
WALL = 0
PATH = 1
FOOD = 2
PACMAN = 3

class WindowSettings:
    def __init__(self):
        ''' Settings for startup window'''
        self.width = 811
        self.height = 355
        self.title = 'Pacman'
        self.icon = QIcon(r'data/images/pacman.ico')
        self.mazes = readJson(r'data/json/mazes.json')
        self.algorithms = readJson(r'data/json/algorithms.json')
        self.feed_density = (0.01, 1.)
        self.pacman_speed = (1, 7)


class GameParameters:
    def __init__(self, maze, algorithm, heuristic, pacman_speed, feed_density):
        ''' Settings for running game'''
        self.maze = maze
        self.algorithm = algorithm
        self.heuristic = heuristic
        self.pacman_speed = pacman_speed
        self.feed_density = feed_density
