from modules.settings import CELL, IMG_FLAG

class Flag:
    def __init__(self, screen, pacman_coor):
        super().__init__()
        
        self.screen = screen
        self.image = IMG_FLAG
        self.rect = IMG_FLAG.get_rect()
        
        self.rect.x = (pacman_coor.x * CELL) + CELL
        self.rect.y = (pacman_coor.y * CELL) + CELL
        
    def draw(self):
        self.screen.blit(self.image, self.rect)