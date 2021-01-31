import pygame
from modules.settings import TRACE, CELL
from pygame.sprite import Sprite

class Trace(Sprite):
    def __init__(self, screen, pacman, maze):
        super().__init__()
        
        self.screen = screen
        self.rect = pygame.Rect(pacman.coor.y * CELL + CELL, pacman.coor.x * CELL + CELL, CELL, CELL)
        self.maze = maze
        self.coor = pacman.coor
        
    def draw(self):
        pygame.draw.rect(self.screen, TRACE[min(self.maze[self.coor.get()], len(TRACE) - 1)], self.rect)