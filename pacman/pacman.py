from settings import *
from math import radians
import pygame
from maze import mazes

class Pacman:
    closed_angles = radians(0), radians(360)
    opened_angles = ((radians(135), radians(45)), (radians(45), radians(315)), (radians(315), radians(225)), (radians(225), radians(135))) # top right bot left

    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.mouth_closed = False
        self.pix_pos = self.get_pix_pos()
        self.go = 1
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.maze = mazes[0]


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
        if self.able_to_move:
            self.pix_pos += self.direction # pacman move

        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction

            self.able_to_move = self.can_move()

        '''Update new grid position'''
        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_BUFFER//2 - 2 + self.app.cell_width//2) // self.app.cell_width
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_BUFFER//2 - 2 + self.app.cell_height//2) // self.app.cell_height


        # self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_BUFFER + self.app.cell_width//2) // self.app.cell_width + 1
        # self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_BUFFER + self.app.cell_height//2) // self.app.cell_height + 1

    
    def draw(self):
        # pygame.draw.circle(self.app.screen, PACMAN_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width // 2 - 2)
        self.draw_pacman()
        pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*self.app.cell_width + TOP_BOTTOM_BUFFER//2, self.grid_pos[1]*self.app.cell_height + TOP_BOTTOM_BUFFER//2, 
                                                self.app.cell_width, self.app.cell_height), 1)


    
    def move(self, direction, go):
        self.stored_direction = direction
        self.go = go


    def get_pix_pos(self):
        # self.pix_pos = vec(self.grid_pos.x * self.app.cell_width + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2, self.grid_pos.y * self.app.cell_height + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2)
        return vec(self.grid_pos[0] * self.app.cell_width + TOP_BOTTOM_BUFFER//2 + 2, self.grid_pos[1] * self.app.cell_height + TOP_BOTTOM_BUFFER//2 + 2)

    
    def time_to_move(self,):
        if int(self.pix_pos[0] - TOP_BOTTOM_BUFFER//2 - 1) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0): # right or left
                return True

        if int(self.pix_pos[1] - TOP_BOTTOM_BUFFER//2 - 1) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1): # down or up
                return True

        return False

    
    def can_move(self):
        pos = vec(self.grid_pos + self.direction)
        j, i = int(pos.x), int(pos.y)

        if i < 28 and i >= 0 and j < 30 and j >= 0:
            return self.maze[i][j] == 1

        return False
