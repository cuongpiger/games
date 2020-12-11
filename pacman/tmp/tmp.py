from math import radians
import pygame, sys
from pygame.locals import *

FPS = 30  # frames per second
MOUTH_EVENT = USEREVENT+1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Point(object):
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class PacMan(object):
    closed_angles = radians(0), radians(360)
    opened_angles = radians(45), radians(315)
    color = YELLOW
    thickness = 100

    def __init__(self, x=0, y=0, width=1, height=1):
        self.pos = Point(x, y)
        self.width, self.height = width, height
        self.mouth_closed = False

    def toggle_mouth(self):
        self.mouth_closed = not self.mouth_closed

    def draw(self, surface):
        if self.mouth_closed:
            pygame.draw.arc(surface, self.color,
                            (int(self.pos.x), int(self.pos.y),
                             self.width, self.height),
                            self.closed_angles[0], self.closed_angles[1],
                            self.thickness)
        else:
           pygame.draw.arc(surface, self.color,
                            (int(self.pos.x), int(self.pos.y),
                             self.width, self.height),
                            self.opened_angles[0], self.opened_angles[1],
                            self.thickness)

def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    screen = pygame.display.set_mode((500,400), 0, 32)
    screen.fill(BLACK)

    pacman = PacMan(250-25, 200-25, 30, 30)
    pygame.time.set_timer(MOUTH_EVENT, 333)

    while True:  # display update loop
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == MOUTH_EVENT:
                pacman.toggle_mouth()
                continue
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pacman.draw(screen)

        pygame.display.update()
        fpsclock.tick(FPS)

main()