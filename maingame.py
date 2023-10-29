import pygame
import sys
import os
from os import listdir
from os.path import isfile, join
import Player
import Enemy

pygame.init()

pygame.display.set_caption("Test game")

background_sfx = pygame.mixer.Sound("Music.mp3")
background_sfx.play()

#Variables for the game window dimensions
screen_w, screen_h = 800, 600
fps = 60
velocity = 5

window = pygame.display.set_mode((screen_w, screen_h))

player = Player.Player()
enemy = Enemy.Enemy()
playerColor = (255, 255, 255)
    
def draw(self, win):
    win.blit(self.image (self.rect.x, self.rect.y))

def set_background(file): 
    #background = (173, 216, 230)
    #ground = (0, 100, 0)
    #window.fill(background)
    image = pygame.image.load(join("assets", file))
    x, y, width, height = image.get_rect()
    tiles = []

    for i in range (screen_w // width + 1):
        for j in range(screen_h // height + 1):
            pos = (i * screen_w, j * height)
            tiles.append(pos)
    return tiles, image 


def draw(window, background, bg_img):
    for tile in background:
        window.blit(bg_img, tile)


#Draw floor
floor = pygame.image.load("assets/Tilesets/TX Tileset Ground.png")
floor_rect = floor.get_rect()
floor_rect.topleft = (0, 515)

def draw_floor():
    window.blit(floor, floor_rect)
    offset = 93
    for i in range(8):
        floor_rect.topleft = (offset, 515)
        window.blit(floor, floor_rect)
        offset += 93
    offset = 93
    floor_rect.topleft = (0, 515)

#Creating the game
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = set_background("testBG.png")

    game = True
    while game:
        clock.tick(fps)
        player_rect = pygame.Rect((player.x, player.y, player.width, player.height))
        #enemy_rect = pygame.Rect((enemy.x, enemy.y, enemy.width, enemy.height))
        enemy.updateRect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        draw(window, background, bg_image)
        player.movement()
        player.jump()
        enemy.walk_towards_player(player.x, player.y)
        draw_floor()

        pygame.draw.rect(window, (0, 0, 255), (enemy.x, enemy.y, enemy.width, enemy.height))
        pygame.draw.rect(window, (enemy.enemy_on_hit(player_rect)), player_rect)

        pygame.display.flip()

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)
