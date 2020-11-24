import pygame
from pygame.sprite import Sprite


# Class dùng để điều khiển bullet bắn ra từ ship
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        # Tạo ra bullet object từ ship's current location
        super().__init__()
        self.screen = screen

        # Tạo ra bullet có rect tại (0, 0) và sau đó chỉnh cho chính xác lại sau
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # do ta ko dùng image để xây dựng hình ảnh, nên ta dùng class Rect của pygame
        self.rect.centerx = ship.rect.centerx # vị trí của viên đạn phụ thuộc vào vị trí của đầu tàu
        self.rect.top = ship.rect.top

        # Lưu vị trí của bullet vào một biến số thực
        self.y = float(self.rect.y)

        # Fill color for bullet
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # Di chuyển bullet lên trên screen
        self.y -= self.speed_factor

        # Update lại bullet's location cho viên đạn
        self.rect.y = self.y

    # Vẽ bullet lên màn hình
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)