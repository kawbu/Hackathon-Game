import pygame
import random

class Enemy:

    def __init__(self, x = 200, y = 455, width = 40, height = 60, speed = 3):
        #Enemy Details
        self.enemiesKilled = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.jumping = False
        self.jumpCount = 9
        self.distance = 9
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.image = pygame.image.load('assets/enemyAnimation/tile000_scaled_2x_pngcrushed.png')
        self.death_sfx = pygame.mixer.Sound("monsterdeath.wav")
        self.walkRight = [pygame.image.load('assets/enemyAnimation/tile000_scaled_2x_pngcrushed.png'), pygame.image.load('assets/enemyAnimation/tile001_scaled_2x_pngcrushed.png'), pygame.image.load('assets/enemyAnimation/tile002_scaled_2x_pngcrushed.png'),
             pygame.image.load('assets/enemyAnimation/tile003_scaled_2x_pngcrushed.png'), pygame.image.load('assets/enemyAnimation/tile004_scaled_2x_pngcrushed.png'), pygame.image.load('assets/enemyAnimation/tile005_scaled_2x_pngcrushed.png')]

        self.walkLeft = [pygame.image.load('assets/enemyAnimation/tile000_scaled_2x_pngcrushedLeft.png'), pygame.image.load('assets/enemyAnimation/tile001_scaled_2x_pngcrushedLeft.png'), pygame.image.load('assets/enemyAnimation/tile002_scaled_2x_pngcrushedLeft.png'),
             pygame.image.load('assets/enemyAnimation/tile003_scaled_2x_pngcrushedLeft.png'), pygame.image.load('assets/enemyAnimation/tile004_scaled_2x_pngcrushedLeft.png'), pygame.image.load('assets/enemyAnimation/tile005_scaled_2x_pngcrushedLeft.png')]
        self.walkCount = 0

    #Enemy will always move in the direction of the player.
    def walk_towards_player(self, player_x, player_y):
        if player_x > self.x:
            self.x += self.speed
            self.walkCount += 1
            self.image = self.get_next_image(self.walkRight, self.walkCount)
        else:
            self.walkCount += 1
            self.image = self.get_next_image(self.walkLeft, self.walkCount)
            self.x -= self.speed


    def get_next_image(self, image_list, current_index):
        return image_list[current_index % len(image_list)]


    #Updates position of enemy rectangle for collision detection
    def updateRect(self):
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))

    def respawn(self):
        self.enemiesKilled += 1
        self.death_sfx.play()
        deathAnimation = pygame.Rect((self.x, self.y, self.width, self.height))
        respawn_pos = random.choice([1000, -100, 1100, -200])
        self.x = respawn_pos

    #Enemy resets when hit and turns player icon red indicating a hit
    def enemy_on_hit(self, playerRect, playerObj):
        collide = playerRect.collidepoint(self.rect.center)
        if collide:
            self.respawn()
            playerObj.health -= 1
            return (255, 0, 0)
        return (255, 255, 255)
    
    def enemy_on_bullet(self, bulletRect):
        collide = bulletRect.collidepoint(self.rect.topleft) or bulletRect.collidepoint(self.rect.center)
        if collide:
            self.respawn()
            return 1000
        else:
            return 0

    #Enemy Jumps on Random Intervals
    def jump_on_random(self):
        temp_int = random.randint(0, 60)

        if temp_int == self.speed:
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