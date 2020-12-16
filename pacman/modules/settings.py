import pygame
from json import load

CELL = 30

def read_json_file(path):

    try:
        with open(path) as reader:
            return load(reader)
    except:
        return None

class WindowSettings:
    def __init__(self):
        self.width = 811
        self.height = 355
        self.padding = CELL
        self.title = 'Pacman'
        self.icon = r'data/images/pacman.ico'
        self.feed_density = (0.01, 1.)
        self.pacman_speed = (1, 5)
        self.cb_mazes = read_json_file(r'data/text/maze_info.json')
        self.cb_algorithms = read_json_file(r'data/text/algorithms_info.json')


class GameSettings:
    def __init__(self):
        self.wall = 0
        self.path = 1
        self.pacman = 2
        self.speed = 1.0
        self.feed = 3
        self.cell = CELL
        self.feed_img = pygame.transform.scale(pygame.image.load(r'data/images/feed.png'), (self.cell, self.cell))
        self.pacman_img = [pygame.transform.scale(pygame.image.load(r'data/images/pacman_close.png'), (self.cell, self.cell)), 
                           pygame.transform.scale(pygame.image.load(r'data/images/pacman_open.png'), (self.cell, self.cell))]
        

class ColorSettings:
    PURPLE = (66, 54, 107)
    ORANGE = (156, 118, 54)
    DARK_BLUE = (36, 112, 117)
    GREY = (57, 64, 64)

class FontSettings:
    SIZE_24 = 24
    SIZE_16 = 16
    SIZE_18 = 18
    FONT_ARIAL_BLACK = 'arial black'