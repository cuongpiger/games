import sys, pygame
import numpy as np
import modules.game_functions as gf
from pygame.sprite import Group
from modules.settings import FOOD, CELL, IMG_FOOD, PACMAN
from modules.util_classes import Coor
from modules.pacman import Pacman


class GameApp:
    def __init__(self, maze, img, path, pacman_speed, algorithm, icon, title, width, height):
        self.maze = maze
        self.background = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.path = path
        self.food = [Coor(x, y) for x, y in zip(*np.where(maze == FOOD))]
        self.clock = pygame.time.Clock()
        self.width = width + 2*CELL
        self.height = height + 2*CELL
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pacman = Pacman(self.screen, path[0], pacman_speed)
        self.algorithm = algorithm 
        self.state = 0
        self.group_food = Group()
        self.img_food = IMG_FOOD
        
        pygame.display.set_icon(pygame.image.load(icon))
        pygame.display.set_caption(title)
        
        for coor in path:
            print(coor)
            
        print()
        
    def run(self):
        i = 1
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT + 1, 333)
        
        gf.initFood(self.screen, self.food, self.group_food, self.img_food)
        
        while True:
            self.state = gf.checkEvents(self.state, self.pacman)
            
            if self.state == 0: # intro is running, waiting to push space to start game
                gf.introDraw(self.screen, self.algorithm, self.width, self.height)
                # gf.screenDraw(self.screen, self.width, self.height, self.background, self.pacman, self.food, self.group_food, self.path[i])
            elif self.state == 1: # game is running
                i += gf.screenDraw(self.screen, self.width, self.height, self.background, self.pacman, self.food, self.group_food, self.path[i])
            
                if i == len(self.path):
                    self.state = -1 # pause game
            elif self.state == 2:
                break
                
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()