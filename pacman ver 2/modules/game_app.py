import sys, pygame
import numpy as np
import modules.game_functions as gf
from pygame.sprite import Group
from modules.settings import FOOD, CELL, IMG_FOOD, PACMAN
from modules.util_classes import Coor
from modules.pacman import Pacman
from modules.flag import Flag
from modules.trace import Trace


class GameApp:
    def __init__(self, maze, img, path, trace, pacman_speed, algorithm, icon, title, width, height):
        self.maze = maze
        self.background = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.path = path
        self.food = [Coor(x, y) for x, y in zip(*np.where(maze == FOOD))]
        self.clock = pygame.time.Clock()
        self.width = width + 2*CELL
        self.height = height + 2*CELL
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pacman = Pacman(self.screen, path[0], pacman_speed)
        self.flag = Flag(self.screen, self.pacman.coor.swap())
        self.algorithm = algorithm 
        self.state = 0
        self.group_food = Group()
        self.group_trace = Group()
        self.img_food = IMG_FOOD
        self.trace = trace
        
        pygame.display.set_icon(pygame.image.load(icon))
        pygame.display.set_caption(title)
        
    def run(self):
        i = 1
        maze = np.full(self.maze.shape, -1)
        maze[self.path[0].get()] += 1
        
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT + 1, 333)
        
        gf.initFood(self.screen, self.food, self.group_food, self.img_food)
        
        while True:
            self.state = gf.checkEvents(self.state, self.pacman)
            
            if self.state == 0: # intro is running, waiting to push space to start game
                gf.introDraw(self.screen, self.algorithm, self.width, self.height)
                self.state = 3
            elif self.state == 1: # game is running
                if not len(self.group_trace.sprites()):
                    self.group_trace.add(Trace(self.screen, self.pacman, maze))
                
                self.flag.draw()
                if gf.screenDraw(self.screen, self.width, self.height, self.background, self.pacman, self.flag, self.food, self.group_food, self.group_trace, maze, self.path[i], i, len(self.path) - 1, self.trace):
                    maze[self.path[i].get()] += 1
                    i += 1
                
                if i == len(self.path):
                    self.state = -1 # pause game
            elif self.state == 3:
                gf.screenDraw(self.screen, self.width, self.height, self.background, self.pacman, None, self.food, self.group_food, self.group_trace, maze, self.pacman.coor, 0, len(self.path) - 1, False)
                self.state = -1
            elif self.state == 4: # quit game
                self.state = 0
                break
                
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()