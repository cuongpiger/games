import sys
from time import sleep

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
def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color) # tô lại màu nền

    # Vẽ lại tất cả các bullet sau ship và aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() # vẽ ship
    aliens.draw(screen) # vẽ 1 dòng alien

    # Vẽ ra play_button nếu game is inactive
    if not stats.game_active:
        play_button.draw_button()

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

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    # Update location của những bullet và xóa những bullet cũ
    bullets.update()

    # Loại bỏ những bullet đã biến mất
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

        
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Check for any bullets that have hit aliens, if so => remove this alien and this bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # phương thức này sẽ kiểm tra từng bullet và alien có va chạm ko
        # nếu có thì sẽ trả về 1 dictionary chứa các bullet và alien đã bị va chạm, 2 tham số True True tức cho pygame biết nếu có
        # va chạm thì xóa 2 đối tượng bullet và alien va chạm này

    # Làm mới lại hạm đội nếu bị tiêu diệt hết
    if len(aliens) == 0:
        # Destroy existing bullets and creat new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens) 


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

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # Check if the fleet is at an edge and then update the positions of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    # Update the position of all alines in the fleet 
    aliens.update() # tự dộng gọi cho từng sprite trong group

    # Kiểm tra giữa ship và alien có va chạm ko
    if pygame.sprite.spritecollideany(ship, aliens): # method này nhận vào 2 tham số, 1 sprite và 1 group, phương thức này sẽ tìm kiếm bất
        # kì member nào của group mà va chạm vs sprite và sẽ dừng tìm kiếm ngay khi phát hiện và trả về alien đầu tiên mà va chạm vs ship
        # , trong trường hợp ko có bất kì va chạm nào thì method này trả về None và khối if này sẽ ko bao h xảy ra
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Kiểm tra xem có alien nào dưới màn hình ko
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        # Nếu có va chạm trừ mạng đi 1
        stats.ships_left -= 1

        # Destroy aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause 0.5s
        sleep(0.5)
    else:
        stats.game_active = False

def change_fleet_direction(ai_settings, aliens):
    # Drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # Check if any aliens have reached the bottom of the screen
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: # nếu có alien chạm bottom thì ship cũng bị mất đi 1 mạng
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
