import sys
import pygame

from modules.settings import WindowSettings
from modules.game_stats import GameStats
import modules.game_functions as gf

windowSt = WindowSettings()

class GameApp:
    def __init__(self, board, feed_pos, pacman_pos, path, maze_img, maze_width, maze_height, title):
        self.board = board
        self.feed_pos = feed_pos
        self.pacman_pos = pacman_pos
        self.path = path
        self.maze_img = maze_img
        self.width = maze_width
        self.height = maze_height
        self.title = title
        self.stats = GameStats(len(path))
        self.screen = pygame.display.set_mode((maze_width + windowSt.padding, maze_height + windowSt.padding))

        pygame.display.set_icon(pygame.image.load(windowSt.icon))
        pygame.display.set_caption(windowSt.title)


    def run(self):
        # pygame.time.set_timer(self.)
        pygame.init()

        while True:
            gf.check_events(self.stats)

            if self.stats.game_active:
                pass
            else:
                gf.intro_draw(self.screen, self.title, self.width + windowSt.padding, self.height + windowSt.padding)

            gf.update_screen(self.screen)


    # def start_event