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
                    saveFile()
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

def saveFile():
    global highlight
    global save1
    
    global save2
    
    global save3
    
    global name

    if highlight == 1:
        if(constants.NEW_GAME):
            changeName(1)
            constants.NEW_GAME = False
        else:
            save1.seek(0)
            save1.write(constants.NAME.rstrip("\n"))
            save1.truncate()

        save1.write("\nLevel " + str(constants.LEVEL + 1))
        save1.truncate()

        save1.seek(0)
        constants.SAVE1TEXT = save1.readlines()
            
    elif highlight == 2:
        if(constants.NEW_GAME):
            changeName(2)
            constants.NEW_GAME = False
        else:
            save2.seek(0)
            save2.truncate()
            save2.write(constants.NAME.rstrip("\n"))

        save2.write("\nLevel " + str(constants.LEVEL + 1))
        save2.truncate()

        save2.seek(0)
        constants.SAVE2TEXT = save2.readlines()
            
    elif highlight == 3:
        if(constants.NEW_GAME):
            changeName(3)
            constants.NEW_GAME = False
        else:
            save3.seek(0)
            save3.write(constants.NAME.rstrip("\n"))
            save3.truncate()

        save3.write("\nLevel " + str(constants.LEVEL + 1))
        save3.truncate()

        save3.seek(0)
        constants.SAVE3TEXT = save3.readlines()

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

def changeName(save):
    global save1
    global save2
    global save3
    global name

    name = name_input.main()

    constants.NAME = name

    
    if save == 1:
        save1.seek(0)
        save1.write(name)
        save1.truncate()
    elif save == 2:
        save2.seek(0)
        save2.write(name)
        save2.truncate()
    elif save == 3:
        save3.seek(0)
        save3.write(name)
        save3.truncate()
    
        
