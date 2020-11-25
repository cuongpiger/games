# Class dùng để theo dõi số liệu thống kê cho trò chơi
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        # Khởi tạo các số liệu thống kê có thể có trong trò chơi
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0