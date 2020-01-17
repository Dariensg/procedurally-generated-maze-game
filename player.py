import pygame

import constants, cell_objects, maze_generator
from hidden_player import HiddenPlayer


class Player(pygame.Rect):

    def __init__(self, hiddenPlayer, startX, startY):

        self.moveX = int(startX)
        self.moveY = int(startY)
        
        self.rectX = int(startX/2)
        self.rectY = int(startY/2)

        self.width = int(startX)
        self.height = int(startY)

        self.hidden_player = hiddenPlayer

    def move_left(self):
        if self.hidden_player.check_move("l"):
            self.rectX -= self.moveX 

    def move_right(self):
        if self.hidden_player.check_move("r"):
            self.rectX += self.moveX

    def move_up(self):
        if self.hidden_player.check_move("u"):
            self.rectY -= self.moveY

    def move_down(self):
        if self.hidden_player.check_move("d"):
            self.rectY += self.moveY

 

