import pygame
import random

class Enemy:
    health = 1
    speed = 0

    def __init__(self, x = 200, y = 485, width = 30, height = 30, speed = 3):
        #Enemy Details
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.jumping = False
        self.jumpCount = 8
        self.distance = 8
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
    
    def walk_towards_player(self, player_x, player_y):
        if player_x > self.x:
            self.x += self.speed
        else:
            self.x -= self.speed
    
    def updateRect(self):
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))

    def enemy_on_hit(self, playerRect):
        collide = playerRect.collidepoint(self.rect.center)
        if collide:
            self.x = -200
            return (255, 0, 0)
        return (255, 255, 255)
        
    def jump_on_random(self):
        temp_int = random.randint(0, 60)

        if temp_int == 3:
            self.jumping = True
        if self.jumping:
            if self.jumpCount >= -1*self.distance:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.jumping = False
                self.jumpCount = self.distance