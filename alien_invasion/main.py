import pygame
from pygame.sprite import Group

from modules.settings import Settings
from modules.ship import Ship
import modules.game_functions as gf

def run_game():
    # Khởi tạo pygame, settings và screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # screen object vs chiều dài và chiều cao trong settings.py
    pygame.display.set_caption('Alien Invasion') # title for window

    # Tạo ra một ship object
    ship = Ship(ai_settings, screen)
    # Tạo một Group để chứa các bullet
    bullets = Group()

    # Bắt đầu main loop của trò chơi
    while True:
        # Theo dõi các event keyboard và mouse
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        bullets.update()

        # Vẽ lại screen
        gf.update_screen(ai_settings, screen, ship, bullets)
       


run_game()