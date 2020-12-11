from settings import *
from math import radians
import pygame

class Pacman:
    closed_angles = radians(0), radians(360)
    opened_angles = ((radians(135), radians(45)), (radians(45), radians(315)), (radians(315), radians(225)), (radians(225), radians(135))) # top right bot left

    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.mouth_closed = False
        self.pix_pos = self.get_pix_pos()
        self.go = 0
        self.direction = vec(1, 0)


    def toggle_mouth(self):
        self.mouth_closed = not self.mouth_closed

    def draw_pacman(self):
        if self.mouth_closed:
            pygame.draw.arc(self.app.screen, PACMAN_COLOR,
                           (int(self.pix_pos.x), int(self.pix_pos.y), self.app.cell_width - 2, self.app.cell_height - 2),
                            self.closed_angles[0], self.closed_angles[1], 60)
        else:
            pygame.draw.arc(self.app.screen, PACMAN_COLOR,
                           (int(self.pix_pos.x), int(self.pix_pos.y), self.app.cell_width - 2, self.app.cell_height - 2),
                            self.opened_angles[self.go][0], self.opened_angles[self.go][1], 60)


    def update(self):
        self.pix_pos += self.direction

    
    def draw(self):
        # pygame.draw.circle(self.app.screen, PACMAN_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width // 2 - 2)
        self.draw_pacman()

    
    def move(self, direction, go):
        self.direction = direction
        self.go = go


    def get_pix_pos(self):
        # self.pix_pos = vec(self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2, self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2)
        return vec(self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER//2 + 2, self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER//2 + 2)