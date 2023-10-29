import pygame

class Bullet:

    def __init__(self, x, y, direction, width = 15, height = 5, move = 7, bull = False):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = 15
        self.height = 5
        self.move = 7
        self.bull = False
        