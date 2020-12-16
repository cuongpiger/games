import sys
import pygame

from modules.settings import GameSettings, ColorSettings, FontSettings, WindowSettings
from modules.utility_classes import Pos
from modules.pacman import Pacman
from modules.feed import Feed


gameSt = GameSettings()
colorSt = ColorSettings()
fontSt = FontSettings()


def check_events(pacman, stats):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            pacman.toggle_mouth()
        elif event.type == pygame.QUIT: # click vào button close window trên title bar
            # pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(stats, event)




def intro_draw(screen, title, width, height):
    screen.fill(colorSt.GREY)
    title_1, title_2 = title.split(',')

    if title_2 == '':
        draw_text(screen, title_1, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_24, colorSt.ORANGE, Pos(width//2, height//2 - 20))
    else:
        draw_text(screen, title_1, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_24, colorSt.ORANGE, Pos(width//2, height//2 - 50))
        draw_text(screen, title_2, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_16, colorSt.DARK_BLUE, Pos(width//2, height//2 - 20))

    draw_text(screen, 'push SPACE BAR to START', fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_18, colorSt.DARK_BLUE, Pos(width//2, height//2 + 20))


def screen_draw(screen, background, feed, pacman, speed, direc_pos):
    screen.blit(background, (gameSt.cell, gameSt.cell))
    pacman.update(direc_pos, speed)
    feed.draw(screen)
    pacman.blit(direc_pos.get_angel())

    return pacman.check_move(direc_pos)


def feed_draw(screen, feed, feed_pos):
    for pos in feed_pos:
        food = Feed(screen, pos.swap())
        feed.add(food)


def update_feed(screen, pacman, feed):
    pass


    

###################################################################################################### utility functions down

def draw_text(screen, content, font_name, size, color, pos, align='center'):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(content, False, color)
    text_size = text.get_size()

    if align == 'center':
        pos = (pos.x - text_size[0]//2, pos.y - text_size[1]//2)

    screen.blit(text, pos)


def check_keydown_events(stats, event):
    if event.key == pygame.K_SPACE:
        if stats.game_active <= 0:
            stats.game_active = 1
        elif stats.game_active == 1:
            stats.game_active = 0