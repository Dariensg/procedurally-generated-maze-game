import pygame, sys

import constants
import load_menu

global highlight

highlight = 1

def drawMenu():
    global playTextSurface
    global quitTextSurface
    global loadTextSurface
    global selected
    global done
    global screen
    
    selected = False
    done = False

    screen = pygame.display.set_mode([1000, 1000], pygame.FULLSCREEN)
    
    titleText = pygame.font.Font(None, 50)

    playTextSurface = titleText.render("New Game", True, constants.WHITE)
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

        screen.fill(constants.BLACK)

        drawButtons()
        drawTitle()
        
        pygame.display.flip()
        

def drawButtons():
    global screen
    global highlight
    global playTextSurface
    global loadTextSurface
    global quitTextSurface
    
    if highlight == 1:
        pygame.draw.rect(screen, constants.WHITE, [500 - (playTextSurface.get_rect()[2]/2) - 10, 290, playTextSurface.get_rect()[2] + 20, playTextSurface.get_rect()[3] + 20], 2)
    elif highlight == 2:
        pygame.draw.rect(screen, constants.WHITE, [500 - (loadTextSurface.get_rect()[2]/2) - 10, 490, loadTextSurface.get_rect()[2] + 20, loadTextSurface.get_rect()[3] + 20], 2)
    elif highlight == 3:
        pygame.draw.rect(screen, constants.WHITE, [500 - (quitTextSurface.get_rect()[2]/2) - 10, 690, quitTextSurface.get_rect()[2] + 20, quitTextSurface.get_rect()[3] + 20], 2)

    screen.blit(playTextSurface, [500 - (playTextSurface.get_rect()[2]/2), 300])
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
        constants.NEW_GAME = True
    elif(highlight == 2):
        selected = True
        load_menu.drawMenu()
    elif(highlight == 3):
        done = True

def drawTitle():
    global screen
    
    titleImage = pygame.image.load("maze_game_title.png")

    screen.blit(pygame.Surface.convert_alpha(titleImage), [500 - titleImage.get_rect()[2]/2, 15])
        
