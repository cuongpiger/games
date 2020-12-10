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
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

##############################################  HELP FUNCTIONS  #############################################

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()

        if centered:
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

        self.draw_text('BFS ALGORITHM', self.screen, (WIDTH//2, HEIGHT//2 - 20), START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True) # remind algorithm
        self.draw_text('PUSH SPACE BAR to START', self.screen, (WIDTH//2, HEIGHT//2 + 20), START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True) # nhấn space-bar để tiến hành chạy
        self.draw_text('High score:', self.screen, (5, 0), START_TEXT_SIZE, (255, 255, 255), START_FONT) # pass
        
        pygame.display.update()


#############################################  PLAYING FUNCTIONS  #############################################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

                


    def playing_update(self):
        pass


    def playing_draw(self):
        self.screen.fill(RED)
        pygame.display.update()