import sys

import pygame
from settings import *


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            else:
                pass

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

##############################################  HELP FUNCTIONS  #############################################

    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()

        pos = (pos[0] - text_size[0] // 2, pos[1] - text_size[1] // 2)

        screen.blit(text, pos) # vẽ ra màn hình



#############################################  INTRO FUNCTIONS  #############################################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'


    def start_update(self):
        pass



    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, (WIDTH//2, HEIGHT//2), START_TEXT_SIZE, (170, 132, 58), START_FONT) # lời chào mới vô game
        pygame.display.update()