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
        self.pacman_pos = pacman_pos.swap() # original

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
        print('ok')
        if self.check_move_hit(new_pacman_pos.swap(), direc_pos):
            self.pacman_pos = new_pacman_pos.swap()
            return True

        return False

    def check_move_hit(self, new_pacman_pos, direc_pos):
        hor_bar = new_pacman_pos.x*gameSt.cell + gameSt.cell
        ver_bar = new_pacman_pos.y*gameSt.cell + gameSt.cell

        if direc_pos.x < 0 and self.rect.top <= hor_bar: # go top
            return True
        elif direc_pos.x > 0 and self.rect.top >= hor_bar: # go bottom
            return True
        elif direc_pos.y < 0 and self.rect.left <= ver_bar: # go left
            return True
        elif direc_pos.y > 0 and self.rect.left >= ver_bar: # go right
            return True

        return False

            

