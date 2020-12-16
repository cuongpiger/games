import pygame
from pygame.sprite import Sprite
from modules.settings import GameSettings, WindowSettings
from modules.utility_classes import Pos, Location


gameSt = GameSettings()


class Pacman(Sprite):
    def __init__(self, screen, pacman_pos):
        super().__init__()

        self.screen = screen
        self.image = gameSt.pacman_img
        self.rect = self.image[0].get_rect()
        self.mouth_closed = False
        self.pacman_pos = pacman_pos.swap()

        self.rect.x = (pacman_pos.x * gameSt.cell) + gameSt.cell
        self.rect.y = (pacman_pos.y * gameSt.cell) + gameSt.cell

        self.location = Location(self.rect.x, self.rect.y)

    def toggle_mouth(self):
        self.mouth_closed = not self.mouth_closed

    def rotate(self, img_id, angel):
        return pygame.transform.rotate(self.image[img_id], angel)

    def blit(self, angel):
        if self.mouth_closed:
            self.screen.blit(self.rotate(0, angel), self.rect)
        else:
            self.screen.blit(self.rotate(1, angel), self.rect)

    def update(self, direc_pos, speed):
        self.location = self.location.move(direc_pos.swap(), speed)
        self.rect.x, self.rect.y = self.location.x, self.location.y

    def check_move(self, direc_pos):
        new_pacman_pos = (self.pacman_pos + direc_pos).swap()
        future_location = Location(new_pacman_pos.x*gameSt.cell + gameSt.cell, new_pacman_pos.y*gameSt.cell + gameSt.cell)
        # future_pos = Pos((self.rect.x - gameSt.cell)//gameSt.cell, (self.rect.y - gameSt.cell)//gameSt.cell)

        if future_location == Location(self.rect.x, self.rect.y):
        # if future_pos == new_pacman_pos:
            self.pacman_pos = new_pacman_pos.swap()
            return True

        return False
