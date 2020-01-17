import hidden_maze, constants

import pygame

class HiddenPlayer():

    def __init__(self, hiddenMaze):

        self.rectX = 0
        self.rectY = 0

        self.moveX = 5
        self.moveY = 5

        self.rectList = hiddenMaze.rectList

    def check_move(self, direction):
        if direction == "r":
            if pygame.Rect([self.rectX + self.moveX, self.rectY, 5, 5]).collidelist(self.rectList) != -1:
                self.moveRight()
                return True
        elif direction == "l":
            if pygame.Rect([self.rectX - self.moveX, self.rectY, 5, 5]).collidelist(self.rectList) != -1:
                self.moveLeft()
                return True
        elif direction == "d":
            if pygame.Rect([self.rectX, self.rectY + self.moveY, 5, 5]).collidelist(self.rectList) != -1:
                self.moveDown()
                return True
        elif direction == "u":
            if pygame.Rect([self.rectX, self.rectY - self.moveY, 5, 5]).collidelist(self.rectList) != -1:
                self.moveUp()
                return True

        return False

    def moveLeft(self):
        self.rectX -= self.moveX

    def moveRight(self):
        self.rectX += self.moveX

    def moveUp(self):
        self.rectY -= self.moveY

    def moveDown(self):
        self.rectY += self.moveY

    def checkWin(self, width, height):
        if self.rectX == width/2 - 10 and self.rectY == height/2 - 10 and constants.LEVEL < 5:
            constants.LEVEL += 1
            return True
        elif self.rectX == width/4 - 10 and self.rectY == height/4 - 10 and 5 <= constants.LEVEL < 10:
            constants.LEVEL += 1
            return True
        elif self.rectX == width/2 - 10 and self.rectY == height/2 - 10 and 10 <= constants.LEVEL < 20:
            constants.LEVEL += 1
            return True
        elif self.rectX == width - 10 and self.rectY == height - 10 and constants.LEVEL >= 20:
            constants.LEVEL += 1
            return True

        return False
