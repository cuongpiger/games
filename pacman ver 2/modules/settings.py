from modules.util_functions import readJson
import pygame
CELL = 30
WALL = 0
PATH = 1
FOOD = 2
PACMAN = 3
TRACE = ((253, 235, 238), (250, 205, 210), (239, 154, 155), (229, 115, 115), (239,
                                                                              83, 80), (243, 67, 54), (229, 57, 53), (211, 47, 47), (198, 40, 40), (183, 28, 28))

IMG_FLAG = pygame.transform.scale(
    pygame.image.load(r'data/images/flag.png'), (CELL, CELL))
IMG_FOOD = pygame.transform.scale(
    pygame.image.load(r'data/images/food.png'), (CELL, CELL))
IMG_PACMAN = [
    pygame.transform.scale(pygame.image.load(
        r'data/images/pacman_close.png'), (CELL, CELL)),
    pygame.transform.scale(pygame.image.load(r'data/images/pacman_open.png'), (CELL, CELL))]


class WindowSettings:
    def __init__(self):
        ''' Settings for startup window'''
        self.width = 811
        self.height = 355
        self.title = 'Pacman'
        self.icon = r'data/images/pacman.ico'
        self.mazes = readJson(r'data/json/mazes.json')
        self.algorithms = readJson(r'data/json/algorithms.json')
        self.feed_density = (0.01, 1.)
        self.pacman_speed = (1, 6)


class GameParameters:
    def __init__(self, maze, algorithm, heuristic, pacman_speed, feed_density):
        ''' Settings for running game'''
        self.maze = maze
        self.algorithm = algorithm
        self.heuristic = heuristic
        self.pacman_speed = pacman_speed
        self.feed_density = feed_density


class ColorSettings:
    PURPLE = (66, 54, 107)
    ORANGE = (156, 118, 54)
    DARK_BLUE = (36, 112, 117)
    GREY = (57, 64, 64)
    WHITE = (255, 255, 255),
    RED = (235, 64, 52)


class FontSettings:
    SIZE_24 = 24
    SIZE_20 = 20
    SIZE_16 = 16
    SIZE_18 = 18
    FONT_ARIAL_BLACK = 'Arial Black'
