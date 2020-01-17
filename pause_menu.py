import pygame, sys

import constants
import load_menu
import save_menu

global highlight

highlight = 1

def drawMenu():
    global saveTextSurface
    global quitTextSurface
    global loadTextSurface
    global selected
    global done
    
    selected = False
    done = False

    screen = pygame.display.set_mode([1000, 1000], pygame.FULLSCREEN)
    
    titleText = pygame.font.Font(None, 50)

    saveTextSurface = titleText.render("Save", True, constants.WHITE)
    loadTextSurface = titleText.render("Load", True, constants.WHITE)
    quitTextSurface = titleText.render("Quit", True, constants.WHITE)
    
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
                    selectMenu()
                    return done
                    break
                elif event.key == pygame.K_ESCAPE:
                    selected = True
                    done = True
                    return done

        screen.fill(constants.BLACK)

        drawButtons(screen)
        pygame.display.flip()
        

def drawButtons(screen):
    global highlight
    global saveTextSurface
    global loadTextSurface
    global quitTextSurface
    
    if highlight == 1:
        pygame.draw.rect(screen, constants.WHITE, [500 - (saveTextSurface.get_rect()[2]/2) - 10, 290, saveTextSurface.get_rect()[2] + 20, saveTextSurface.get_rect()[3] + 20], 2)
    elif highlight == 2:
        pygame.draw.rect(screen, constants.WHITE, [500 - (loadTextSurface.get_rect()[2]/2) - 10, 490, loadTextSurface.get_rect()[2] + 20, loadTextSurface.get_rect()[3] + 20], 2)
    elif highlight == 3:
        pygame.draw.rect(screen, constants.WHITE, [500 - (quitTextSurface.get_rect()[2]/2) - 10, 690, quitTextSurface.get_rect()[2] + 20, quitTextSurface.get_rect()[3] + 20], 2)

    screen.blit(saveTextSurface, [500 - (saveTextSurface.get_rect()[2]/2), 300])
    screen.blit(loadTextSurface, [500 - (loadTextSurface.get_rect()[2]/2), 500])
    screen.blit(quitTextSurface, [500 - (quitTextSurface.get_rect()[2]/2), 700])

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
        save_menu.drawMenu()
    elif(highlight == 2):
        selected = True
        load_menu.drawMenu()
    elif(highlight == 3):
        done = True
        
