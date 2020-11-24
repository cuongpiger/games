# Class chứa tất cả các settings cho Alien Invasion
class Settings():
    def __init__(self):
        # Khởi tạo các settings cho trò chơi

        # Settings cho screen
        self.screen_width = 1200 # chiều dài màn hình
        self.screen_height = 800 # chiều cao
        self.bg_color = (230, 230, 230) # chuẩn màu RGB, combination này là ra màu xám nhạt, tổng cộng có hơn 16tr combination về màu
        
        # Settings for ship
        self.ship_speed_factor = 1.5 # tốc độ di chuyển của ship, di chuyển 1.5px

        # Settings for bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 # số lượng bullet giới hạn


