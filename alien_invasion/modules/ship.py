import pygame


class Ship():
    def __init__(self, ai_settings, screen): # tham chiếu đến screen object
        # Tạo ra ship và location bắt đầu của nó
        self.screen = screen
        self.ai_settings = ai_settings

        # Tải file `ship.bmp` lên
        self.image = pygame.image.load(r'images/ship.bmp')
        self.rect = self.image.get_rect() # lấy ra chiều dài và chiều cao của ship (bao gồm cả transparent background)
        self.screen_rect = screen.get_rect() # lấy ra chiều dài và chiều cao của screen

        # Thiết lập vị trí bắt đầu của ship là ở trung tâm - dưới cùng của screen
        self.rect.centerx = self.screen_rect.centerx # lấy ra trung tâm theo chiều ngang
        self.rect.bottom = self.screen_rect.bottom

        # Do hàm `centerx` chỉ trả giá trị int, nhưng `ship_speed_factor` lại có type là float nên ta cần 1 vài biến đổi \n
            # đó là lấy giá trị từ `self.rect.centerx` và ép kiểu nó thành float
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update location của ship dựa vào `movement_flag`
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor # di chuyển ship qua phải theo `ship_speed_factor`

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor # di chuyển ship qua trái theo `ship_speed_factor`

        # Gán location mới về lại cho `self.rect.centerx`
        self.rect.centerx = self.center

    def blitme(self):
        # Vẽ ship ở vị trí hiện tại của nó lên trên screen
        self.screen.blit(self.image, self.rect)