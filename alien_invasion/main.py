import pygame
from pygame.sprite import Group

from modules.settings import Settings
from modules.game_stats import GameStats
from modules.scoreboard import Scoreboard
from modules.button import Button
from modules.ship import Ship
import modules.game_functions as gf

def run_game():
    # Khởi tạo pygame, settings và screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # screen object vs chiều dài và chiều cao trong settings.py
    pygame.display.set_caption('Alien Invasion') # title for window

    # Tạo ra button play game
    play_button = Button(ai_settings, screen, 'Play') 

    # Khởi tạo đối tượng dùng để thống kê dữ liệu trong trò chơi
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Tạo ra một ship object
    ship = Ship(ai_settings, screen)
    # Tạo một Group để chứa các bullet
    bullets = Group()
    # Tạo một Group để chứa các alien
    aliens = Group()

    # Tạo ra một hàng chứa các alien
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Bắt đầu main loop của trò chơi
    while True:
        # Theo dõi các event keyboard và mouse 
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            # Update bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) 

            # update aline
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Vẽ lại screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
       


run_game()