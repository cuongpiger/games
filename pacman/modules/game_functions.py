import sys
import pygame

from modules.settings import GameSettings, ColorSettings, FontSettings, WindowSettings
from modules.utility_classes import Pos
from modules.pacman import Pacman
from modules.feed import Feed


gameSt = GameSettings()
colorSt = ColorSettings()
fontSt = FontSettings()


def check_events(path, pacman, stats):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            pacman.toggle_mouth()
        elif event.type == pygame.QUIT: # click vào button close window trên title bar
            stats.game_active = 2
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(path, stats, event)




def intro_draw(screen, title, width, height):
    screen.fill(colorSt.GREY)
    title_1, title_2 = title.split(',')

    if title_2 == '':
        draw_text(screen, title_1, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_24, colorSt.ORANGE, Pos(width//2, height//2 - 20))
    else:
        draw_text(screen, title_1, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_24, colorSt.ORANGE, Pos(width//2, height//2 - 50))
        draw_text(screen, title_2, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_16, colorSt.DARK_BLUE, Pos(width//2, height//2 - 20))

    draw_text(screen, 'push SPACE BAR to START', fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_18, colorSt.DARK_BLUE, Pos(width//2, height//2 + 20))


def screen_draw(screen, width, height, background, feed, pacman, speed, direc_pos, cost, total_cost):
    screen.fill(colorSt.GREY)
    screen.blit(background, (gameSt.cell, gameSt.cell))
    pacman.update(direc_pos, speed)
    update_feed(screen, feed, pacman)
    feed.draw(screen)
    pacman.blit(direc_pos.get_angel())
    draw_text(screen, f'COST: {cost}/{total_cost}', fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_18, colorSt.WHITE, Pos(5, 2), 'left')
    draw_text(screen, 'SPACE: stop/play', fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_18, colorSt.WHITE, Pos(2, height - 30), 'left')

    return pacman.check_move(direc_pos)


def feed_draw(screen, feed, feed_pos):
    for pos in feed_pos:
        food = Feed(screen, pos.swap())
        feed.add(food)


def update_feed(screen, feed, pacman):
    food = pygame.sprite.spritecollideany(pacman, feed)

    if food:
        feed.remove(food)


    

###################################################################################################### utility functions down

def draw_text(screen, content, font_name, size, color, pos, align='center'):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(content, False, color)
    text_size = text.get_size()

    if align == 'center':
        pos = (pos.x - text_size[0]//2, pos.y - text_size[1]//2)
    elif align == 'left':
        pos = (pos.x, pos.y)

    screen.blit(text, pos)


def check_keydown_events(path, stats, event):
    if event.key == pygame.K_SPACE:
        if stats.game_active <= 0 and path:
            stats.game_active = 1
        elif stats.game_active == 1:
            stats.game_active = 0