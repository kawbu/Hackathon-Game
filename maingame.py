import pygame
import sys
import os
from os import listdir
from os.path import isfile, join
import Player
import Enemy
import shooting
import random

pygame.init()

#Background Music and Caption
pygame.display.set_caption("Skeletal Skirmish")
background_sfx = pygame.mixer.Sound("Music.mp3")
background_sfx.set_volume(0.2)
background_sfx.play()
pygame.font.init()

#Global variables for the game
screen_w, screen_h = 800, 600
fps = 60
velocity = 5
window = pygame.display.set_mode((screen_w, screen_h))
player = Player.Player()
enemy = Enemy.Enemy()
enemy2 = Enemy.Enemy(x = 800)
playerColor = (255, 255, 255)

#Drawing background
def draw(self, win):
    win.blit(self.image (self.rect.x, self.rect.y))

#Creating the background
def set_background(file): 
    image = pygame.image.load(join("assets", file))
    x, y, width, height = image.get_rect()
    tiles = []

    for i in range (screen_w // width + 1):
        for j in range(screen_h // height + 1):
            pos = (i * screen_w, j * height)
            tiles.append(pos)
    return tiles, image 


#Draw background
def draw(window, background, bg_img):
    for tile in background:
        window.blit(bg_img, tile)


#Displays current score (total enemies killed)
def display_score(enemies_killed):
    tempFont = pygame.font.Font(pygame.font.get_default_font(), 50)
    return tempFont.render(f"Points: {enemies_killed}", False, (0, 0, 0))

titleFont = pygame.font.Font(pygame.font.get_default_font(), 70)
titleRect = titleFont.render("Skeletal Skirmish", False, (255, 255, 255))

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
    isNight = True
    pressed = False
    clock = pygame.time.Clock()
    background, bg_image = set_background("nightBG.png")
    bullet_rect = None
    enemies_killed = 0
    bgCycle = 0
    bg_list = [pygame.image.load("assets/potentialBG.png"), pygame.image.load("assets/nightBG.png")]

    game = True
    game_started = False

    play_button = pygame.image.load("assets/playButton.png")
    button_rect = play_button.get_rect()
    loading_screen = pygame.image.load("assets/titleScreen.jpg")
    screen_rect = loading_screen.get_rect()

    button_rect.center = (screen_w // 2, screen_h // 2 - 200)
    screen_rect.center = (screen_w // 2, screen_h // 2 - 150)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if not game_started:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button_rect.collidepoint(x, y):
                        game_started = True
                window.blit(loading_screen, screen_rect)
                window.blit(play_button, button_rect)
                window.blit(titleRect, (100, 200))
        
        if game_started:
            clock.tick(fps)
            draw(window, background, bg_image)
            
            keys = pygame.key.get_pressed()
            player_rect = pygame.Rect((player.x, player.y, player.width, player.height))
            if keys[pygame.K_SPACE]:
                pressed = True
                bullet = shooting.Bullet(player.x, player.y + 30, player.direction)

            if pressed:
                pygame.draw.rect(window, (155, 149, 149), (bullet.x, bullet.y, bullet.width, bullet.height))
                if bullet.direction == 1 and bullet.x < 900:
                    bullet.x += bullet.move
                elif bullet.direction == 0 and bullet.x > -50:
                    bullet.x -= bullet.move
                bullet_rect = pygame.Rect((bullet.x, bullet.y, bullet.width, bullet.height))

            #enemy_rect = pygame.Rect((enemy.x, enemy.y, enemy.width, enemy.height))
            enemy.updateRect()
            enemy2.updateRect()
            if bullet_rect:
                bullet.y += enemy.enemy_on_bullet(bullet_rect)
                bullet.y += enemy2.enemy_on_bullet(bullet_rect)
            enemy.jump_on_random()
            enemy2.jump_on_random()
            enemies_killed = enemy.enemiesKilled + enemy2.enemiesKilled

            player.movement()
            player.jump()
            enemy.walk_towards_player(player.x, player.y)
            enemy2.walk_towards_player(player.x, player.y)
            draw_floor()
            #isNight, bg_image = day_night_cycle(enemies_killed, isNight, bg_image)

            score = display_score(enemies_killed)
            window.blit(score, score.get_rect())
            window.blit(player.image, player.rect)
            window.blit(enemy.image, enemy.rect)
            window.blit(enemy2.image, enemy2.rect)
            window.blit(player.weaponImage, player.weaponRect)
            player.draw_health_bar(window)
            enemy.enemy_on_hit(player.rect, player)
            enemy2.enemy_on_hit(player.rect, player)

            # Reset game at 0 health, also cycles between backgrounds.
            if player.health == 0:
                bg_image = bg_list[bgCycle % len(bg_list)]
                bgCycle += 1
                game_started = False
                player.health = 5
                player.x = 400
                enemy.enemiesKilled = 0
                enemy2.enemiesKilled = 0

        pygame.display.flip()

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)
