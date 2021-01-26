import pygame
from pygame.sprite import Sprite
from modules.settings import IMG_PACMAN, CELL
from modules.util_classes import Coor, Location

class Pacman(Sprite):
    def __init__(self, screen, pacman_coor, pacman_speed):
        super().__init__()
        
        self.screen = screen
        self.image = IMG_PACMAN
        self.rect = self.image[0].get_rect()
        self.mouth_closed = False
        self.pacman_coor = pacman_coor.swap()
        self.rect.x = (pacman_coor.x * CELL) + CELL
        self.rect.y = (pacman_coor.y * CELL) + CELL
        self.location = Location(self.rect.x, self.rect.y)
        self.speed = pacman_speed
        
    def toggleMouth(self):
        self.mouth_closed = not self.mouth_closed

    def rotate(self, angel):
        return pygame.transform.rotate(self.image[int(self.mouth_closed)], angel)
    
    def blit(self, angel):
        self.screen.blit(self.rotate(angel), self.rect)
        
    def update(self, direc):
        pass