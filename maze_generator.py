import pygame

import constants

from cell_objects import MazeTracer, MazeGrid, MazeCell


def drawMaze(screen):
    global mazeGrid
    global width, height
    global firstDraw

    i = 0
    j = 0
    
    if(len(mazeGrid.maze_grid[0])*width * 2 < 1920 and len(mazeGrid.maze_grid)*height * 2 < 1080):
        for i, line in enumerate(mazeGrid.maze_grid):
                for j, char in enumerate(mazeGrid.maze_grid[i]):
                    pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height + height/2, width, height])

                    if i == len(mazeGrid.maze_grid) - 1 and j == len(mazeGrid.maze_grid[i]) - 1:
                        pygame.draw.rect(screen, constants.GREEN, [2*j*width + width/2, 2*i*height + height/2, width, height])

                    if(mazeGrid.maze_grid[i][j].dirExit == "N"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height - height/2, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "S"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2, 2*i*height + height/2 + height, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "E"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width + width/2 + width, 2*i*height + height/2, width, height])
                    if(mazeGrid.maze_grid[i][j].dirExit == "W"):
                        pygame.draw.rect(screen, constants.WHITE, [2*j*width - width/2, 2*i*height + height/2, width, height])

                    if i == len(mazeGrid.maze_grid) - 1 and j == len(mazeGrid.maze_grid[i]) - 1:
                        levelText = pygame.font.Font(None, 20)
                        levelTextSurface = levelText.render("Level " + str(constants.LEVEL + 1), True, constants.GREEN)
                        screen.blit(levelTextSurface, [(2*j*width + width/2)/2 - levelTextSurface.get_rect()[2], 2*i*height + height/2 + 20])
                    
    else:
        newWidth = width*4
        newHeight = height*4
        
        for i, line in enumerate(mazeGrid.maze_grid):
                for j, char in enumerate(mazeGrid.maze_grid[i]):

                    rect = pygame.Rect([2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2, 2000/newWidth, 2000/newHeight])
                    
                    pygame.draw.rect(screen, constants.WHITE, rect)

                    if i == len(mazeGrid.maze_grid) - 1 and j == len(mazeGrid.maze_grid[i]) - 1:
                        pygame.draw.rect(screen, constants.GREEN, [2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2, 2000/newWidth, 2000/newHeight])
                    
                    if(mazeGrid.maze_grid[i][j].dirExit == "N"):
                        rect = pygame.Rect([2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) - (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
                        
                        pygame.draw.rect(screen, constants.WHITE, rect)
                            
                    if(mazeGrid.maze_grid[i][j].dirExit == "S"):
                        rect = pygame.Rect([2*j*(2000/newWidth) + (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2 + (2000/newHeight), (2000/newWidth), (2000/newHeight)])
                        
                        pygame.draw.rect(screen, constants.WHITE, rect)
                            
                    if(mazeGrid.maze_grid[i][j].dirExit == "E"):
                        rect = pygame.Rect([2*j*(2000/newWidth) + (2000/newWidth)/2 + (2000/newWidth), 2*i*(2000/newHeight) + (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
                        
                        pygame.draw.rect(screen, constants.WHITE, rect)
                            
                    if(mazeGrid.maze_grid[i][j].dirExit == "W"):
                        rect = pygame.Rect([2*j*(2000/newWidth) - (2000/newWidth)/2, 2*i*(2000/newHeight) + (2000/newHeight)/2, (2000/newWidth), (2000/newHeight)])
                        
                        pygame.draw.rect(screen, constants.WHITE, rect)

                    
                    if i == len(mazeGrid.maze_grid) - 1 and j == len(mazeGrid.maze_grid[i]) - 1:
                        levelText = pygame.font.Font(None, 20)
                        levelTextSurface = levelText.render("Level " + str(constants.LEVEL + 1), True, constants.GREEN)
                        screen.blit(levelTextSurface, [480, 1000])



def main():
    global mazeGrid
    global width, height
    
    mazeGrid = MazeGrid()

    if constants.LEVEL < 5:
        width, height = 10, 10
    elif constants.LEVEL < 10:
        width, height = 20, 20
    elif constants.LEVEL < 20:
        width, height = 50, 50
    else:
        width, height = 100, 100

    mazeGrid.gridMaze(width, height)

    mazeTracer = MazeTracer()

    mazeTracer.chooseStartCell(mazeGrid)
    
    while not mazeGrid.checkComplete():
        mazeTracer.update(mazeGrid)


if __name__ == "__main__":
    main()




