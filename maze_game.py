import pygame

import maze_generator, constants, main_menu, save_menu, pause_menu

from player import Player
from hidden_player import HiddenPlayer
from hidden_maze import HiddenMaze

def drawPlayer(player, width, height):
    global screen
    
    pygame.draw.rect(screen, constants.PINK, [player.rectX, player.rectY, width, height])
    pygame.display.update(player)

def createLevel():
    global mazeGrid
    global screen
    global newWidth, newHeight
    global hiddenMaze
    global hiddenPlayer
    global player
    global screenHeight, screenWidth
    
    maze_generator.main()

    mazeGrid = maze_generator.mazeGrid
    width = maze_generator.width
    height = maze_generator.height

    
    if(len(mazeGrid.maze_grid[0])*width * 2 < 1920 and len(mazeGrid.maze_grid)*height * 2 < 1080):
        newWidth = width
        newHeight = height
       
        screenHeight = len(mazeGrid.maze_grid)*height * 2
        screenWidth = len(mazeGrid.maze_grid[0])*width * 2
        
        screen = pygame.display.set_mode([len(mazeGrid.maze_grid[0])*width * 2, len(mazeGrid.maze_grid)*height * 2 + 20], pygame.FULLSCREEN)

    else:
        newWidth = 2000/(width*4)
        newHeight = 2000/(height*4)

        screenHeight = 1000
        screenWidth = 1000
        
        screen = pygame.display.set_mode([1000, 1020], pygame.FULLSCREEN)
    
    hiddenMaze = HiddenMaze(mazeGrid)
    hiddenMaze.createRectList()
    
    hiddenPlayer = HiddenPlayer(hiddenMaze)
    player = Player(hiddenPlayer, newWidth, newHeight)

    

def checkWin(hiddenPlayer):
    global screenHeight, screenWidth
    
    if hiddenPlayer.checkWin(screenWidth, screenHeight):
        createLevel()


def main():
    global screen
    global mazeGrid
    global newWidth, newHeight
    global hiddenMaze
    global hiddenPlayer
    global player

    pygame.init()

    done = False

    clock = pygame.time.Clock()

    done = main_menu.drawMenu()

    createLevel()
    
    
    while not done:
        clock.tick(20)

        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = pause_menu.drawMenu()
                    createLevel()

                    
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_up()
            pygame.display.update(player)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.move_down()
            pygame.display.update(player)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move_right()
            pygame.display.update(player)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move_left()
            pygame.display.update(player)


        screen.fill(constants.BLACK)
        
        maze_generator.drawMaze(screen)
        drawPlayer(player, newWidth, newHeight)

        checkWin(hiddenPlayer)


        pygame.display.flip()


    
    
    pygame.quit()


if __name__ == "__main__":
    main()
