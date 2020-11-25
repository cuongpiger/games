import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        # Khởi tạo các thuộc tính của button
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Setup các thuộc tính và hướng cho button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Bỏ msg vào button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # biến vân bản dc lưu trữ trong msg thành hình ảnh
            # và sau đó lưu hình ảnh này vào `msg_image_rect`, tham số True tức là bật khử răng cưa khiến cho các cạnh của văn bản nhìn
            # mịn hơn, 2 đối số cuối là phông chữ và màu nền cho button
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Vẽ ra một blank button trước
        self.screen.fill(self.button_color, self.rect)
        # Sau đó mới bỏ msg vô
        self.screen.blit(self.msg_image, self.msg_image_rect)