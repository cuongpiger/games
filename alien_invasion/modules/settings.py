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
        self.ship_limit = 3

        # Settings for bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 # số lượng bullet giới hạn

        # Alien settings 
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 represents right, -1 represents left

        # Level up game
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Khởi tạo các setting sẽ thay đổi trong suốt trò chơi
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

