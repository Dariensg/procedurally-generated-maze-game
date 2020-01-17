import constants
from cell_objects import MazeGrid

import pygame

class HiddenMaze():

    def __init__(self, mazeGrid):

        self.maze_grid = mazeGrid.maze_grid

        self.rectList = []


    def createRectList(self):

        for i, line in enumerate(self.maze_grid):
            for j, char in enumerate(self.maze_grid[i]):

                rect = pygame.Rect([10*j, 10*i, 5, 5])
                    
                self.rectList.append(rect)
                
                if(self.maze_grid[i][j].dirExit == "N"):
                    rect = pygame.Rect([10*j, 10*i - 5, 5, 5])

                    self.rectList.append(rect)
                            
                if(self.maze_grid[i][j].dirExit == "S"):
                    rect = pygame.Rect([10*j, 10*i + 5, 5, 5])

                    self.rectList.append(rect)
                            
                if(self.maze_grid[i][j].dirExit == "E"):
                    rect = pygame.Rect([10*j + 5, 10*i, 5, 5])

                    self.rectList.append(rect)
                            
                if(self.maze_grid[i][j].dirExit == "W"):
                    rect = pygame.Rect([10*j - 5, 10*i, 5, 5])

                    self.rectList.append(rect)
