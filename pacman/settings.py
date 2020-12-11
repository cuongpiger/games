from pygame.math import Vector2 as vec
from pygame import USEREVENT

'''screen settings'''
WIDTH, HEIGHT = 610, 670 # chiều dài và chiều cao của window
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER
FPS = 60

'''color settings'''
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
PACMAN_COLOR = (190, 194, 15)



'''font settings'''
START_TEXT_SIZE = 24
COST_TEXT_SIZE = 16
START_FONT = 'arial black'


'''pacman settings'''
PACMAN_START_POS = vec(1, 1)
MOUTH_EVENT = USEREVENT + 1




'''mob settings'''