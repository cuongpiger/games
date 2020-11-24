import sys

import pygame

from modules.bullet import Bullet


# Theo dõi các event keyboard và mouse
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # khi click vào nút đóng của sổ
            sys.exit() # đóng window
        elif event.type == pygame.KEYDOWN: # nếu bắt dc event 1 phím dc nhấn xuống
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # nếu bắt dc event thả 1 phím
            check_keyup_events(event, ship)

# Vẽ lại màn hình qua mỗi lần lặp
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color) # tô lại màu nền

    # Vẽ lại tất cả các bullet sau ship và aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() # vẽ ship

    # Hiển thị screen dc refresh gần đây nhất
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT: # nếu nhấn phím mũi tên qua phải
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # nếu nhấn phím mũi tên qua trái
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Tạo ra một bullet mới và thả nó vào bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False