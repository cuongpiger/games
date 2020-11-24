import sys

import pygame

from modules.bullet import Bullet
from modules.alien import Alien


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
def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color) # tô lại màu nền

    # Vẽ lại tất cả các bullet sau ship và aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() # vẽ ship
    aliens.draw(screen) # vẽ 1 dòng alien

    # Hiển thị screen dc refresh gần đây nhất
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT: # nếu nhấn phím mũi tên qua phải
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # nếu nhấn phím mũi tên qua trái
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: # nếu bắn bullet
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: # nếu nhấn phím Q thì thoát game luôn
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    # Update location của những bullet và xóa những bullet cũ
    bullets.update()

    # Loại bỏ những bullet đã biến mất
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Bắn ra một bullet nếu như chưa vượt quá giới hạn số bullet cho 1 lần bắn
    if len(bullets) < ai_settings.bullets_allowed: # nếu số bullet bắn ra nhỏ hơn giới hạn bullet cho phép
        # Tạo ra một bullet mới và thả nó vào bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    # Tạo ra một hạm đội alien 
    alien = Alien(ai_settings, screen) # tạo ra một alien object và tìm ra số lượng alien có thể có trên 1 dòng
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        # Tạo ra từng dòng của các alien
        for alien_number in range(number_aliens_x):
            # Tạo ra một alien và đặt nó vào dòng hiện tại
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width # tìm ko gian trống theo chiều ngang (có trừ 2 biên)
    number_aliens_x = int(available_space_x / (2*alien_width)) # tìm số lượng alien có thể có trên 1 dòng

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Tạo ra một alien và đặt nó vào dòng hiện tại
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    # Xác định số dòng alien mà có thể bỏ vào màn hình
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y / (2*alien_height))

    return number_rows

