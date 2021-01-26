from pygame.sprite import Sprite
from modules.settings import CELL

class Food(Sprite):
    def __init__(self, screen, coor, image):
        super().__init__()
        
        self.screen = screen
        self.image = image
        self.rect = image.get_rect()
        
        self.rect.x = (coor.x * CELL) + CELL
        self.rect.y = (coor.y * CELL) + CELL
        
    def blit(self):
        self.screen.blit(self.image, self.rect)