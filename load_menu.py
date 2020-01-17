import pygame, sys, os

import constants
import name_input

global highlight


global save1
global save2
global save3

highlight = 1

path = os.path.join(os.path.split('save_menu')[0], 'saves')

save1 = open(os.path.join(path, 'save1.txt'), 'r+')
save2 = open(os.path.join(path, 'save2.txt'), 'r+')
save3 = open(os.path.join(path, 'save3.txt'), 'r+')


constants.SAVE1TEXT = save1.readlines()
constants.SAVE2TEXT = save2.readlines()
constants.SAVE3TEXT = save3.readlines()


def drawMenu():
    global save1Button
    
    global save2Button
    
    global save3Button
    
    
    global selected
    global done
    
    selected = False
    done = False

    screen = pygame.display.set_mode([1000, 1000], pygame.FULLSCREEN)
    
    titleText = pygame.font.Font(None, 50)
    
    while not selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return done
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    moveCursor("d")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    moveCursor("u")
                elif event.key == pygame.K_RETURN:
                    loadFile()
                    return done
                    break

        save1Button = titleText.render(constants.SAVE1TEXT[0] + "\n" + constants.SAVE1TEXT[1], True, constants.WHITE)
        save2Button = titleText.render(constants.SAVE2TEXT[0] + "\n" + constants.SAVE2TEXT[1], True, constants.WHITE)
        save3Button = titleText.render(constants.SAVE3TEXT[0] + "\n" + constants.SAVE3TEXT[1], True, constants.WHITE)

        screen.fill(constants.BLACK)

        drawButtons(screen)
        pygame.display.flip()
        

def drawButtons(screen):
    global highlight
    global save1Button
    global save2Button
    global save3Button
    
    if highlight == 1:
        pygame.draw.rect(screen, constants.WHITE, [500 - (save1Button.get_rect()[2]/2) - 10, 290, save1Button.get_rect()[2] + 20, save1Button.get_rect()[3] + 20], 2)
    elif highlight == 2:
        pygame.draw.rect(screen, constants.WHITE, [500 - (save2Button.get_rect()[2]/2) - 10, 490, save2Button.get_rect()[2] + 20, save2Button.get_rect()[3] + 20], 2)
    elif highlight == 3:
        pygame.draw.rect(screen, constants.WHITE, [500 - (save3Button.get_rect()[2]/2) - 10, 690, save3Button.get_rect()[2] + 20, save3Button.get_rect()[3] + 20], 2)

    screen.blit(save1Button, [500 - (save1Button.get_rect()[2]/2), 300])
    screen.blit(save2Button, [500 - (save2Button.get_rect()[2]/2), 500])
    screen.blit(save3Button, [500 - (save3Button.get_rect()[2]/2), 700])


def moveCursor(direction):
    global highlight
    
    if direction == "u" and highlight > 1:
        highlight -= 1
    elif direction == "d" and highlight < 3:
        highlight += 1


def selectMenu():
    global highlight
    global selected
    global done

    if(highlight == 1):
        selected = True
        return
    elif(highlight == 2):
        selected = True
        return
    elif(highlight == 3):
        selected = True
        return

def loadFile():
    global highlight
    
    if highlight == 1:
        levelText = constants.SAVE1TEXT[1].split(" ")
        level = int(levelText[len(levelText) - 1])
        constants.LEVEL = level - 1
        constants.NAME = constants.SAVE1TEXT[0]
    elif highlight == 2:
        levelText = constants.SAVE2TEXT[1].split(" ")
        level = int(levelText[len(levelText) - 1])
        constants.LEVEL = level - 1
        constants.NAME = constants.SAVE2TEXT[0]
    elif highlight == 3:
        levelText = constants.SAVE3TEXT[1].split(" ")
        level = int(levelText[len(levelText) - 1])
        constants.LEVEL = level - 1
        constants.NAME = constants.SAVE3TEXT[0]
