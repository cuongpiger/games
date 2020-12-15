import sys
import pygame
from pygame.sprite import Group
from modules.settings import WindowSettings, GameSettings
from modules.game_stats import GameStats
from modules.pacman import Pacman
from modules.feed import Feed
from modules.utility_classes import Pos
import modules.game_functions as gf

windowSt = WindowSettings()

class GameApp:
    def __init__(self, board, feed_pos, pacman_pos, path, maze_img, maze_width, maze_height, title):
        self.board = board
        self.feed_pos = feed_pos
        self.path = path # cái đường đi của bfs
        self.background = pygame.transform.scale(pygame.image.load(maze_img), (maze_width, maze_height))
        self.width = maze_width + 2*windowSt.padding
        self.height = maze_height + 2*windowSt.padding
        self.title = title
        self.stats = GameStats(len(path))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pacman = Pacman(self.screen, pacman_pos.swap())
        self.feed = Group()
        self.clock = pygame.time.Clock()

        pygame.display.set_icon(pygame.image.load(windowSt.icon))
        pygame.display.set_caption(windowSt.title)


    def run(self):
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT + 1, 333)

        gf.feed_draw(self.screen, self.feed, self.feed_pos)

        while True:
            gf.check_events(self.pacman, self.stats)

            if self.stats.game_active:
                gf.background_draw(self.screen, self.background, self.feed, self.pacman)
            else:
                gf.intro_draw(self.screen, self.title, self.width, self.height)

            pygame.display.flip()
            self.clock.tick(60)