import sys
import pygame
from modules.settings import ColorSettings, FontSettings, CELL
from modules.util_classes import Coor
from modules.food import Food

colorSt = ColorSettings()
fontSt = FontSettings()


def checkEvents(state, pacman):
    flag = state
    
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            pacman.toggleMouth()
        elif event.type == pygame.QUIT:
            flag = 2
        elif event.type == pygame.KEYDOWN:
            flag = checkKeydownEvents(state, event)
            
    return flag

def screenDraw(screen, width, height, background, pacman, food, group_food):
    screen.fill(colorSt.GREY)
    screen.blit(background, (CELL, CELL))
    group_food.draw(screen)
    pacman.blit(90)


def introDraw(screen, title, width, height):
    screen.fill(colorSt.GREY)
    title_1, title_2 = title.split(',')

    if title_2 == '':
        drawText(screen, title_1, fontSt.FONT_ARIAL_BLACK,
                  fontSt.SIZE_24, colorSt.ORANGE, Coor(width//2, height//2 - 20))
    else:
        drawText(screen, title_1, fontSt.FONT_ARIAL_BLACK,
                  fontSt.SIZE_24, colorSt.ORANGE, Coor(width//2, height//2 - 50))
        drawText(screen, title_2, fontSt.FONT_ARIAL_BLACK, fontSt.SIZE_18,
                  colorSt.RED, Coor(width//2, height//2 - 20))

    drawText(screen, 'push SPACE BAR to START', fontSt.FONT_ARIAL_BLACK,
              fontSt.SIZE_20, colorSt.DARK_BLUE, Coor(width//2, height//2 + 20))
    
def foodDraw(screen, food, group_food, img_food):
    for coor in food:
        f = Food(screen, coor.swap(), img_food)
        group_food.add(f)


# utility functions down

def checkKeydownEvents(state, event):
    if event.key == pygame.K_SPACE:
        if state <= 0:
            return 1
        elif state == 1: # game is running
            return 0 # pause game

def drawText(screen, content, font_name, size, color, coor, align='center'):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(content, False, color)
    text_size = text.get_size()

    if align == 'center':
        coor.set(coor.x - text_size[0]//2, coor.y - text_size[1]//2)

    screen.blit(text, coor.get())
    
def updateFood(screen, food, group_food):
    pass
    
        
