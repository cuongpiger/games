import sys

import pygame
import numpy as np
from maze import mazes
from settings import *
from pacman import *


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH // 28
        self.cell_height = MAZE_HEIGHT // 30
        self.pacman = Pacman(self, PACMAN_START_POS)
        self.walls = None

        self.load()

    def run(self):
        pygame.time.set_timer(MOUTH_EVENT, 333)

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

    
    '''Load cái map lên'''
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        
        tmp = mazes[0]
        maze = np.array(tmp)
        walls_pos = np.where(maze == 0)
        self.walls = [vec(j, i) for i, j in zip(walls_pos[0], walls_pos[1])]
        


    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))

        for y in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, y*self.cell_height), (WIDTH, y*self.cell_height))

        for wall in self.walls:
            pygame.draw.rect(self.background, (112, 55, 163), (int(wall.x*self.cell_width), int(wall.y*self.cell_height), self.cell_width, self.cell_height))


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
        
        pygame.display.update()


#############################################  PLAYING FUNCTIONS  #############################################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == MOUTH_EVENT:
                self.pacman.toggle_mouth()
                continue

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pacman.move(vec(0, -PACMAN_SPEED), 0)

                if event.key == pygame.K_RIGHT:
                    self.pacman.move(vec(PACMAN_SPEED, 0), 1)

                if event.key == pygame.K_DOWN:
                    self.pacman.move(vec(0, PACMAN_SPEED), 2)

                if event.key == pygame.K_LEFT:   
                    self.pacman.move(vec(-PACMAN_SPEED, 0), 3)
                

    def playing_update(self):
        self.pacman.update()


    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2)) # đưa cái maze.png lên màn hình
        self.draw_grid()
        self.draw_text('COST: {}'.format('143/372'), self.screen, (5, 0), COST_TEXT_SIZE, WHITE, START_FONT)
        self.draw_text('{}'.format('BFS Algorithm'), self.screen, (WIDTH // 2 + 170, 0), COST_TEXT_SIZE, WHITE, START_FONT)
        self.pacman.draw() # vẽ pacman
        
        pygame.display.update()