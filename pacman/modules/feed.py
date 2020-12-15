import pygame
from pygame.sprite import Sprite
from modules.settings import GameSettings


gameSt = GameSettings()


class Feed(Sprite):
    def __init__(self, screen, feed_pos):
        super().__init__()

        self.screen = screen
        self.image = gameSt.feed_img
        self.rect = self.image.get_rect()

        self.rect.x = (feed_pos.x * gameSt.cell) + gameSt.cell
        self.rect.y = (feed_pos.y * gameSt.cell) + gameSt.cell


    def blit(self):
        self.screen.blit(self.image, self.rect)

        
