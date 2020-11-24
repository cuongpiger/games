import pygame
from pygame.sprite import Sprite

# Class đại diện cho 1 alien
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # Khởi tạo alien object và thiết lập vị trí bắt đầu cho nó
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load hình ảnh alien lên và thiết lập rect cho nó
        self.image = pygame.image.load(r'images/alien.bmp')
        self.rect = self.image.get_rect()

        # Với mỗi alien dc tạo ra, location của nó sẽ trên - góc trái màn hình
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Lưu trữ tọa độ theo hệ số thực của alien
        self.x = float(self.rect.x)

    # Dùng để vẽ alien ở vị trí hiện tại của nó
    def blitme(self):
        self.screen.blit(self.image, self.rect)