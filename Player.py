import pygame

class Player:

    def __init__(self, x = 400, y = 485, width = 30, height = 30, move = 5, jumping = False, distance = 8, jumpCount = 8):
        #Player Details
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = move
        self.playSound = 0
        self.walking = pygame.mixer.Sound("walk.mp3")

        # Jumping
        self.jumping = jumping
        self.distance = distance
        self.jumpCount = jumpCount
    
    # Left and Right movement
    def movement(self):
        keys = pygame.key.get_pressed()
        self.direction: int

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.move
            self.direction = 0
            if self.playSound % 20 == 0 and (not (keys[pygame.K_UP] or keys[pygame.K_w])):
                self.walking.play()
                self.playSound += 1
            else:
                self.playSound += 1
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < 800-self.width:
            self.x += self.move 
            self.direction = 1
            if self.playSound % 20 == 0 and (not (keys[pygame.K_UP] or keys[pygame.K_w])):
                self.walking.play()
                self.playSound += 1
            else:
                self.playSound += 1
        
    # Jumping
    def jump(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
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