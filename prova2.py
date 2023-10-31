import pygame
import turtle
import time
import math
import random
import sys
import os
pygame.init()

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

BGColor = (96,128,56)
ZColor = (225,0,0)
PColor = (0,0,255)

MOVE = 10

size = (800, 800)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zombie Game")

shooting_enemy_image = pygame.image.load('cave-painting.png').convert_alpha()
first_player_spaceship_image = pygame.image.load('spaceship.png').convert_alpha()
laser_bullet = pygame.image.load('laser1.png').convert_alpha()
enemy_laser_bullet_image = pygame.image.load('laser_rotated2.png').convert_alpha()
kamikaze_enemy_image = pygame.image.load('kamikaze.png').convert_alpha()

class Char(pygame.sprite.Sprite):
    def __init__(self, color, pos, radius, width):
        super().__init__()
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, [radius, radius], radius, width)
        self.rect = self.image.get_rect()

    def moveRightP(self, pixels):
        self.rect.x += pixels
        pass

    def moveLeftP(self, pixels):
        self.rect.x -= pixels
        pass

    def moveUpP(self, pixels):
        self.rect.y -= pixels
        pass

    def moveDownP(self, pixels):
        self.rect.y += pixels
        pass


class Zombie(pygame.sprite.Sprite):
    def __init__(self2, color, pos, radius, width):
        super().__init__()
        self2.image = kamikaze_enemy_image
        self2.original_player_image = kamikaze_enemy_image
        self2.rect = self2.image.get_rect()
        self2.speed = 4
        self2.pos = pygame.Vector2(pos[0], pos[1])

    def draw(self2):
        self2.rect.center = (int(round(self2.pos.x)), int(round(self2.pos.y)))
        screen.blit(self2.image, self2.rect)

    # rotate the player where the mouse is aiming
    def rotate(self2):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self2.pos.x, mouse_y - self2.pos.y
        self2.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self2.image = pygame.transform.rotate(self2.original_player_image, int(self2.angle))
        orig_center = self2.original_player_image.get_rect(topleft=(self2.pos.x, self2.pos.y)).center
        self2.rect = self2.image.get_rect(center=orig_center)

    def move_towards_Char(self2, Char):
        deltaVec = pygame.Vector2(Char.rect.center) - self2.pos
        len = deltaVec.length()
        if len > 0:
            self2.pos += deltaVec / len * min(len, self2.speed)


all_sprites_list = pygame.sprite.Group()

playerChar = Char(PColor, [0, 0], 15, 0)
playerChar.rect.x = 400
playerChar.rect.y = 400

all_sprites_list.add(playerChar)

carryOn = True
clock = pygame.time.Clock()

zombie_list = []
zombie_rad = 15
zombie_dist = (200, 900)
next_zombie_time = pygame.time.get_ticks() + 10000

zombie_list = []
zombie_rad = 15
zombie_dist = (200, 900)
next_zombie_time = 10000

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerChar.moveLeftP(MOVE)
    if keys[pygame.K_d]:
        playerChar.moveRightP(MOVE)
    if keys[pygame.K_w]:
        playerChar.moveUpP(MOVE)
    if keys[pygame.K_s]:
        playerChar.moveDownP(MOVE)

    current_time = pygame.time.get_ticks()
    if current_time > next_zombie_time:
        next_zombie_time = current_time + 2000

        dist  = 0 - playerChar.rect.y
        angle = 0
        p_pos = (playerChar.rect.centerx, playerChar.rect.centery)
        zombie_pos = (p_pos[0] + dist * math.sin(angle), p_pos[1] + dist * math.cos(angle))

        #new_pos = (random.randrange(0, size[0]), 0)
        new_zombie = Zombie(RED, zombie_pos, zombie_rad, 0)
        zombie_list.append(new_zombie)

    # update all the positions of the zombies
    for zombie in zombie_list:
        zombie.move_towards_Char(playerChar)

    screen.fill(BGColor)
    screen.blit(playerChar.image,playerChar.rect)

    # draw all the zombies
    for zombie in zombie_list:
        zombie.rotate()
        zombie.draw()


    pygame.display.flip()
    clock.tick(60)
pygame.quit()