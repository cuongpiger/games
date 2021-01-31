import pygame
from pygame.sprite import Sprite
from modules.settings import IMG_PACMAN, CELL
from modules.util_classes import Coor, Location


class Pacman(Sprite):
    def __init__(self, screen, coor, pacman_speed):
        super().__init__()

        self.screen = screen
        self.image = IMG_PACMAN
        self.rect = self.image[0].get_rect()
        self.mouth_closed = False
        self.coor = coor
        self.rect.x = (coor.x * CELL) + CELL
        self.rect.y = (coor.y * CELL) + CELL
        self.location = Location(self.rect.x, self.rect.y)
        self.speed = pacman_speed

    def toggleMouth(self):
        self.mouth_closed = not self.mouth_closed

    def rotate(self, angel):
        return pygame.transform.rotate(self.image[int(self.mouth_closed)], angel)

    def draw(self, angel):
        self.screen.blit(self.rotate(angel), self.rect)

    def update(self, target_coor):
        self.location = self.location.move(
            (target_coor - self.coor), self.speed)
        self.rect.y, self.rect.x = self.location.get()

    def checkMove(self, target_coor):
        if self.checkMoveHit(target_coor):
            self.coor = target_coor
            return True

        return False

    def checkMoveHit(self, target_coor):
        direc = target_coor - self.coor
        hor_bar = target_coor.x * CELL + CELL

        if direc.x < 0 and self.rect.top <= hor_bar:  # go top
            return True

        if direc.x > 0 and self.rect.top >= hor_bar:  # go down
            return True

        ver_bar = target_coor.y * CELL + CELL

        if direc.y < 0 and self.rect.left <= ver_bar:
            return True

        if direc.y > 0 and self.rect.left >= ver_bar:
            return True

        return False
