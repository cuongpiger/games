import pygame
from pygame.sprite import Sprite
from modules.settings import GameSettings, WindowSettings


gameSt = GameSettings()


class Pacman(Sprite):
    def __init__(self, screen, pacman_pos):
        super().__init__()

        self.screen = screen
        self.image = gameSt.pacman_img
        self.rect = self.image[0].get_rect()
        self.mouth_closed = False

        self.rect.x = (pacman_pos.x * gameSt.cell) + gameSt.cell
        self.rect.y = (pacman_pos.y * gameSt.cell) + gameSt.cell

    def toggle_mouth(self):
        self.mouth_closed = not self.mouth_closed

    def rotate(self, img_id, rotate):
        return pygame.transform.rotate(self.image[img_id], rotate)

    def blit(self, rotate):
        if self.mouth_closed:
            self.screen.blit(self.rotate(0, rotate), self.rect)
        else:
            self.screen.blit(self.rotate(1, rotate), self.rect)

