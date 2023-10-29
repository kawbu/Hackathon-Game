import pygame

class Player:

    def __init__(self, x = 400, y = 455, width = 40, height = 60, move = 5, jumping = False, distance = 8, jumpCount = 8):
        #Player Details
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = move
        self.playSound = 0
        self.walking = pygame.mixer.Sound("walk.mp3")
        self.image = pygame.image.load("assets/playerAnimation/IdleLeft.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.walkRight = [pygame.image.load('assets/playerAnimation/R1_inPixio.png'), pygame.image.load('assets/playerAnimation/R2_inPixio.png'), pygame.image.load('assets/playerAnimation/R3_inPixio.png'),
             pygame.image.load('assets/playerAnimation/R4_inPixio.png'), pygame.image.load('assets/playerAnimation/R5_inPixio.png'), pygame.image.load('assets/playerAnimation/R6_inPixio.png')]

        self.walkLeft = [pygame.image.load('assets/playerAnimation/L1_inPixio.png'), pygame.image.load('assets/playerAnimation/L2_inPixio.png'), pygame.image.load('assets/playerAnimation/L3_inPixio.png'),
            pygame.image.load('assets/playerAnimation/L4_inPixio.png'), pygame.image.load('assets/playerAnimation/L5_inPixio.png'), pygame.image.load('assets/playerAnimation/L6_inPixio.png')]
        self.walkCount = 0
        self.direction = 0

        #Player Weapon
        self.weaponAnimations = [pygame.image.load("assets/playerAnimation/playerBowRight.png"), pygame.image.load("assets/playerAnimation/playerBowLeft.png")]
        self.weaponImage = self.weaponAnimations[0]
        self.weaponRect = self.weaponImage.get_rect()
        self.weaponOffset = 20
        self.weaponRect.topleft = (self.x - self.weaponOffset, self.y)

        # Jumping
        self.jumping = jumping
        self.distance = distance
        self.jumpCount = jumpCount
    
    def get_next_image(self, image_list, current_index):
        return image_list[current_index % len(image_list)]
    
    # Left and Right movement
    def movement(self):
        keys = pygame.key.get_pressed()
        self.direction: int

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.move
            self.direction = 0
            self.walkCount += 1
            self.image = self.get_next_image(self.walkLeft, self.walkCount)
            if self.playSound % 20 == 0 and (not (keys[pygame.K_UP] or keys[pygame.K_w])):
                self.walking.play()
                self.playSound += 1
            else:
                self.playSound += 1
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < 800-self.width:
            self.x += self.move 
            self.direction = 1
            self.walkCount += 1
            self.image = self.get_next_image(self.walkRight, self.walkCount)
            if self.playSound % 20 == 0 and (not (keys[pygame.K_UP] or keys[pygame.K_w])):
                self.walking.play()
                self.playSound += 1
            else:
                self.playSound += 1
        else:
            if self.direction == 1:
                self.image = pygame.image.load('assets/playerAnimation/IdleRight.png')
            else:
                self.image = pygame.image.load('assets/playerAnimation/IdleLeft.png')
        self.rect.topleft = (self.x, self.y)
        self.weaponRect.topleft = (self.x + self.weaponOffset, self.y) if self.direction == 1 else (self.x - self.weaponOffset, self.y)
        self.weaponImage = self.weaponAnimations[0] if self.direction == 1 else self.weaponAnimations[1]

    # Jumping
    def jump(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.walkCount = 0
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
        self.weaponRect.topleft = (self.x + self.weaponOffset, self.y) if self.direction == 1 else (self.x - self.weaponOffset, self.y)
        