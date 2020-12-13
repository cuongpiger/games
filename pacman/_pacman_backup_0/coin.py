import pygame
from pygame.sprite import Sprite
from settings import CoinSetting

coin_st = CoinSetting()

class Coin(Sprite):
    def __init__(self, background, pos):
        super().__init__()

        self.background = background
        self.pos = pos
        
        # self.rect = 

    def draw(self):
        pygame.draw.circle(self.background, coin_st.color, pos, coin_st.size, 0)