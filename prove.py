import pygame
import random
import time
import math
from pygame.math import Vector2

pygame.init()

display_width = 800
display_height = 650
screen = pygame.display.set_mode((display_width, display_height))
fps = 60
shooting_enemy_image = pygame.image.load('cave-painting.png').convert_alpha()
first_player_spaceship_image = pygame.image.load('spaceship.png').convert_alpha()
gameover_image = pygame.image.load('gameover.png').convert_alpha()
asteroid_boss_image = pygame.image.load('asteroid.png').convert_alpha()
background = pygame.image.load('background.PNG').convert_alpha()
half_life = pygame.image.load('half life.png').convert_alpha()
one_life = pygame.image.load('1 life.png').convert_alpha()
one_life_half = pygame.image.load('1 and half life.png').convert_alpha()
two_life = pygame.image.load('2 life.png').convert_alpha()
two_life_half = pygame.image.load('2 and half life.png').convert_alpha()
three_life = pygame.image.load('3 life.png').convert_alpha()
laser_bullet = pygame.image.load('laser1.png').convert_alpha()
bonus_life_image = pygame.image.load('star.png').convert_alpha()
bonus_laser_image = pygame.image.load('laser-pen.png').convert_alpha()
healthbar_full = pygame.image.load('HealthBarProject.png').convert_alpha()
healthbar_minus_1 = pygame.image.load('HealthBarProject(1).png').convert_alpha()
healthbar_minus_2 = pygame.image.load('HealthBarProject(2).png').convert_alpha()
healthbar_minus_3= pygame.image.load('HealthBarProject(3).png').convert_alpha()
healthbar_minus_4 = pygame.image.load('HealthBarProject(4).png').convert_alpha()
healthbar_minus_5 = pygame.image.load('HealthBarProject(5).png').convert_alpha()
healthbar_minus_6 = pygame.image.load('HealthBarProject(6).png').convert_alpha()
healthbar_minus_7 = pygame.image.load('HealthBarProject(7).png').convert_alpha()
healthbar_minus_8 = pygame.image.load('HealthBarProject(8).png').convert_alpha()
healthbar_minus_9 = pygame.image.load('HealthBarProject(9).png').convert_alpha()
healthbar_minus_10 = pygame.image.load('HealthBarProject(10).png').convert_alpha()
healthbar_minus_11 = pygame.image.load('HealthBarProject(11).png').convert_alpha()
healthbar_minus_12 = pygame.image.load('HealthBarProject(12).png').convert_alpha()
healthbar_minus_13 = pygame.image.load('HealthBarProject(13).png').convert_alpha()
healthbar_minus_14 = pygame.image.load('HealthBarProject(14).png').convert_alpha()
energy_shield_as_bonus_image = pygame.image.load('shield.png').convert_alpha()
energy_shield_number_1 = pygame.image.load('EnergyShield_born_1.png').convert_alpha()
energy_shield_number_2 = pygame.image.load('EnergyShield_born_2.png').convert_alpha()
energy_shield_number_3 = pygame.image.load('EnergyShield_born_3.png').convert_alpha()
energy_shield_number_4 = pygame.image.load('EnergyShield_born_4.png').convert_alpha()
energy_shield_number_5 = pygame.image.load('EnergyShield_born_5.png').convert_alpha()
energy_shield_number_6 = pygame.image.load('EnergyShield_born_6.png').convert_alpha()
energy_shield_number_7 = pygame.image.load('EnergyShield_born_7.png').convert_alpha()
energy_shield_number_8 = pygame.image.load('EnergyShield_born_8.png').convert_alpha()
energy_shield_number_9 = pygame.image.load('EnergyShield_born_9.png').convert_alpha()
energy_shield_number_10 = pygame.image.load('EnergyShield_born_10.png').convert_alpha()
main_spaceship_enemy = pygame.image.load('enemy main spaceship.png').convert_alpha()
enemy_laser_bullet_image = pygame.image.load('laser_rotated2.png').convert_alpha()
kamikaze_enemy_image = pygame.image.load('kamikaze.png').convert_alpha()

def initialize():
    global background_y, shooting_enemy_speed, tick_to_damage_boss, shooting_enemies_list, bullets_list, \
            score, play_again_gameover, pause_bool, stay_menu, player_one_istance, \
            fighting_boss, boss_life, boss_one_istance, boss_present, \
            laser_as_bullet_istance_one, laser_as_bonus_is_active_bool, life_as_bonus_is_active_bool, \
            laser_as_bonus_istance_one, life_as_bonus_istance_one, laser_as_bonus_taken, \
            laser_bonus_taken_tick, life_as_bonus_taken_tick, shield_as_bonus_istance_one, \
            shield_as_bonus_is_active_bool, shield_as_bonus_taken, shield_bonus_taken_tick, shield_as_shield_istance_one,\
            tick_to_animate_shield, tick_immune_after_shield_boss, to_end_shield_animation, enemy_bullets_list, kamikaze_enemy_list, \
            bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_list_removed

    background_y, shooting_enemy_speed, tick_to_damage_boss, boss_life, score, laser_bonus_taken_tick, life_as_bonus_taken_tick, shield_bonus_taken_tick, tick_to_animate_shield, tick_immune_after_shield_boss = 0, 2, 0, 20, 0, 0, 0, 0, 1, 0
    laser_as_bonus_is_active_bool, life_as_bonus_is_active_bool, pause_bool, fighting_boss, boss_present, play_again_gameover, laser_as_bonus_taken, shield_as_bonus_is_active_bool, shield_as_bonus_taken = False, False, False, False, False, False, False, False, False
    stay_menu = True
    to_end_shield_animation = False
    bullets_list, shooting_enemies_list, enemy_bullets_list, kamikaze_enemy_list = [], [], [], []
    bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_list_removed = [], [], [], []
    shooting_enemies_list.append(ShootingEnemy())
    player_one_istance = Player(display_width // 2, display_height//2, first_player_spaceship_image)

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def drawAll():
    drawBackground()
    drawScore()
    drawLife()
    drawPlayer()
    drawBullets()
    drawShootingEnemy()
    drawKamikazeEnemy()
    drawShootingEnemyBullets()
    player_one_istance.drawPlayer()

def drawBackground():
    global background_y
    temp_y = background_y % background.get_rect().height
    screen.blit(background, (0, temp_y - background.get_rect().height))
    if temp_y < display_height:
        screen.blit(background, (0, temp_y))
    background_y -= 1

def deleteCollision():
    global shooting_enemies_list, bullets_list, enemy_bullets_list, kamikaze_enemy_list
    bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_list_removed
    bullets_list = [bullet2 for bullet2 in bullets_list if bullet2 not in bullets_list_removed]
    shooting_enemies_list = [shooting_enemy for shooting_enemy in shooting_enemies_list if shooting_enemy not in shooting_enemies_list_removed]
    enemy_bullets_list = [enemy_bullet for enemy_bullet in enemy_bullets_list if enemy_bullet not in enemy_bullets_list_removed]
    kamikaze_enemy_list = [kamikaze_enemy for kamikaze_enemy in kamikaze_enemy_list if kamikaze_enemy not in kamikaze_enemy_list_removed]

def collideLineLine(l1_p1, l1_p2, l2_p1, l2_p2):
    # normalized direction of the lines and start of the lines
    P = pygame.math.Vector2(*l1_p1)
    line1_vec = pygame.math.Vector2(*l1_p2) - P
    R = line1_vec.normalize()
    Q = pygame.math.Vector2(*l2_p1)
    line2_vec = pygame.math.Vector2(*l2_p2) - Q
    S = line2_vec.normalize()

     # normal vectors to the lines
    RNV = pygame.math.Vector2(R[1], -R[0])
    SNV = pygame.math.Vector2(S[1], -S[0])

    # distance to the intersection point
    QP = Q - P
    t = QP.dot(SNV) / R.dot(SNV)
    u = QP.dot(RNV) / R.dot(SNV)
    return t > 0 and u > 0 and t * t < line1_vec.magnitude_squared() and u * u < line2_vec.magnitude_squared()

def colideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topleft, rect.bottomleft) or
            collideLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collideLineLine(p1, p2, rect.bottomright, rect.topright) or
            collideLineLine(p1, p2, rect.topright, rect.topleft))

def drawPlayer():
    #move and rotate the player
    player_one_istance.movePlayer()
    player_one_istance.rotate()

def drawShootingEnemy():
    #draw shooting enemy
    for shooting_enemy in shooting_enemies_list:
        shooting_enemy.continueMoveShootingEnemy()
        shooting_enemy.rotate()
        shooting_enemy.drawShootingEnemies()

def drawShootingEnemyBullets():
    for bullets_shooting_enemy in enemy_bullets_list:
        bullets_shooting_enemy.update()
        bullets_shooting_enemy.drawBulletEnemyShooting()


def drawKamikazeEnemy():
    #draw kamikaze enemy
    for kamikaze_enemy in kamikaze_enemy_list:
        kamikaze_enemy.moveTrowardsPlayer()
        kamikaze_enemy.rotate()
        kamikaze_enemy.draw()

def drawBullets():
    for bullet2 in bullets_list:
        bullet2.rotate()
        bullet2.continueDrawBullet()

def drawScore():
    font = pygame.font.SysFont('ubuntumono', 20, True)
    score_surface = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_surface, (10,10) )

def drawLife():
    if player_one_istance.life == 6:
        screen.blit( three_life, (display_width - 130, 10) )
    if player_one_istance.life == 5:
        screen.blit( two_life_half, (display_width - 130, 10) )
    if player_one_istance.life == 4:
        screen.blit( two_life, (display_width - 130, 10))
    if player_one_istance.life == 3:
        screen.blit( one_life_half, (display_width - 130, 10) )
    if player_one_istance.life == 2:
        screen.blit( one_life, (display_width - 130, 10) )
    if player_one_istance.life == 1:
        screen.blit( half_life, (display_width - 130, 10) )

class Player:
    #inizialize the player
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.image = first_player_spaceship_image
        self.life = 6
        self.original_player_image = first_player_spaceship_image
        self.angle = 0
        self.rect = self.image.get_rect()

    #move the player
    def movePlayer(self):
        if key[0]:
            self.x -= 10
        elif key[1]:
            self.x += 10
        if key[2]:
            self.y -= 10
        elif key[3]:
            self.y += 10

        #check borders
        if self.x <= 0:
            self.x = 0
        if self.x + shooting_enemy_image.get_width() >= display_width:
            self.x = display_width - first_player_spaceship_image.get_width()
        if self.y <= 0:
            self.y = 0
        if self.y + first_player_spaceship_image.get_height() >= display_height:
            self.y = display_height - first_player_spaceship_image.get_height()

    # rotate the player where the mouse is aiming
    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.original_player_image, int(self.angle))
        orig_center = self.original_player_image.get_rect(topleft=(self.x, self.y)).center
        self.rect = self.image.get_rect(center=orig_center)

    # draw the player
    def drawPlayer(self):
        screen.blit(self.image, self.rect.topleft)

class Bullet:
    #initialize the bullet
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
        self.image = laser_bullet
        self.original_image = laser_bullet
        self.angle = player_one_istance.angle
        self.vel_x = math.cos(self.angle) * 45
        self.vel_y = math.sin(self.angle) * 45
        self.rect = self.image.get_rect()

    #draw the bullet
    def continueDrawBullet(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x < -laser_bullet.get_width() or self.x >= display_width+laser_bullet.get_width()\
                or self.y < -laser_bullet.get_height() or self.y >= display_height + laser_bullet.get_height():
            bullets_list_removed.append(self)

        screen.blit(self.image, (self.x, self.y))

    #rotate the bullet to the new angle
    def rotate(self):
        self.image = pygame.transform.rotate( self.original_image, ((180 / math.pi) * -math.atan2(self.vel_y, self.vel_x) - 90) )
        self.rect = self.image.get_rect()

    #check if the bullet collides with shooting_enemy and in that case increment the score
    def collisionPlayerBulletWithShootingEnemy(self, shooting_enemy, shooting_enemy_image):
        global score
        shooting_enemy_rect = pygame.Rect(shooting_enemy.x, shooting_enemy.y, shooting_enemy_image.get_width(), shooting_enemy_image.get_height() )
        bullet_rect = pygame.Rect(self.x, self.y, laser_bullet.get_width(), laser_bullet.get_height() )
        # check collision
        if shooting_enemy_rect.colliderect(bullet_rect):
            bullets_list_removed.append(self)
            shooting_enemies_list_removed.append(shooting_enemy)
            score += 1

    #check if the bullet collides with kamikaze_enemy and in that case increment the score
    def collisionPlayerBulletWithKamikazeEnemy(self, kamikaze_enemy, kamikaze_enemy_image):
        global score
        kamikaze_enemy_rect = pygame.Rect(kamikaze_enemy.pos.x, kamikaze_enemy.pos.y, kamikaze_enemy_image.get_width(), kamikaze_enemy_image.get_height() )
        bullet_rect = pygame.Rect(self.x, self.y, laser_bullet.get_width(), laser_bullet.get_height() )
        # check collision
        if kamikaze_enemy_rect.colliderect(bullet_rect):
            bullets_list_removed.append(self)
            kamikaze_enemy_list_removed.append(kamikaze_enemy)
            score += 1

    #check if the bullet collides with shooting enemy and in that case increment the score
    def collisionBulletBoss(self, boss_one_istance, asteroid_boss_image):
        global score
        boss_rect_bullet = pygame.Rect(boss_one_istance.x, boss_one_istance.y, asteroid_boss_image.get_width(), asteroid_boss_image.get_height() )
        boss_bullet_rect = pygame.Rect(self.x, self.y, laser_bullet.get_width(), laser_bullet.get_height() )
        # check collision
        if boss_rect_bullet.colliderect(boss_bullet_rect):
            if boss_one_istance.change_boss_healthbar_image_count == 14:
                bullets_list_removed.append(self)
                boss_one_istance.boss_life -= 1
            else:
                boss_one_istance.change_boss_healthbar_image_count += 1
                bullets_list._removed.append(self)
                boss_one_istance.healthbar = eval( 'healthbar_minus_' + str(boss_one_istance.change_boss_healthbar_image_count) )
                boss_one_istance.boss_life -= 1

class ShootingEnemy:
    #inizialize the enemy
    def __init__(self):
        self.image = shooting_enemy_image
        self.new_shooting_enemy_image = shooting_enemy_image
        self.x = display_width//2
        self.y = 0
        self.begin_down = True
        self.choices = 0
        self.timer = 51
        self.left_again = False
        self.right_again = False
        self.up_again = False
        self.down_again = False
        self.rect = shooting_enemy_image.get_rect()
        self.angle = 0
        self.tick_to_shoot_for_enemy = 0

    #draw the shooting enemy
    def continueMoveShootingEnemy(self):
        if self.y < 30:
            self.y += 1
        if self.y == 30:
            self.begin_down = False
            self.y += 1
        else:
            if not self.begin_down and self.timer > 20:
                self.choices = random.choice([1,2,3,4])
                self.timer = 0
            self.timer += 1
            if self.left_again:
                self.x += 1
                self.left_again = False
            if self.right_again:
                self.x -= 1
                self.right_again = False
            if self.up_again:
                self.y += 0
                self.up_again = False
            if self.down_again:
                self.y -= 1
                self.down_again = False
            else:
                if self.choices == 1:
                    if self.x >= display_width:
                        self.timer = 21
                        self.right_again = True
                    else:
                        if self.y < 140 and self.y > 10:
                            self.y += 1
                            self.x += 4
                        else:
                            self.x += 4
                if self.choices == 2:
                    if self.x <= 0:
                        self.timer = 21
                        self.left_again = True
                    else:
                        if self.y < 140 and self.y > 10:
                            self.y += 1
                            self.x -= 4
                        else:
                            self.x -= 4
                if self.choices == 3:
                    if self.y >= 150:
                        self.timer = 21
                        self.down_again = True
                    else:
                        self.y += 2
                if self.choices == 4:
                    if self.y <= 0:
                        self.timer = 21
                        self.up_again = True
                    else:
                        self.y -= 2

    # rotate the shooting enemy where the player is
    def rotate(self):
        temp_x, temp_y = player_one_istance.x - self.x, player_one_istance.y - self.y
        self.angle = (180 / math.pi) * -math.atan2(temp_y, temp_x) - 90
        self.image = pygame.transform.rotate(self.new_shooting_enemy_image, int(self.angle))
        orig_center = self.new_shooting_enemy_image.get_rect(topleft=(self.x, self.y)).center
        self.rect = self.image.get_rect(center=orig_center)

    def drawShootingEnemies(self):
        self.tick_to_shoot_for_enemy += 1
        screen.blit(self.image, (self.x, self.y))

    #check if shooting enemy collides with player and in that case remove 1 life
    def collisionShootingEnemyPlayer(self, player_one_istance, player):
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        #shooting_enemy_rect = pygame.Rect(self.x, self.y, shooting_enemy_image.get_width(), shooting_enemy_image.get_height())
        if player_rect.colliderect(self.rect):
            shooting_enemies_list_removed.append(shooting_enemy)
            player_one_istance.life -= 1
            print(player_one_istance.life)

class BulletEnemyShooting:
    def __init__(self, temp_angle, pos, target):
        self.image = enemy_laser_bullet_image
        self.original_image = enemy_laser_bullet_image
        # The `pos` parameter is the center of the bullet.rect.
        self.rect = self.image.get_rect(center=pos)
        self.position = Vector2(pos)  # The position of the bullet.

        # This vector points from the shooting_enemy position to target position
        direction = target - pos
        # The polar coordinates of the direction vector.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (because the y-axis is flipped).
        self.image = pygame.transform.rotozoom(self.image, -angle, 1)
        #bullet enemy velocity
        self.velocity = direction.normalize() * 11

    def update(self):
        #move the bullet
        self.position += self.velocity  # Update the position vector.
        self.rect.center = self.position  # And the rect.

    def drawBulletEnemyShooting(self):
        screen.blit(self.image, self.rect)

    #check if the enemy shooting bullet collides with player and in that case decrement the life
    def collisionBulletShootingEnemy(self, player_one_istance, player_image):
        global score
        shooting_enemy_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player_image.get_width(), player_image.get_height() )
        #check collision
        if shooting_enemy_rect.colliderect(self.rect):
            enemy_bullets_list_removed.append(self)
            player_one_istance.life -= 1

class KamikazeEnemy:
    #inizialize the enemy
    def __init__(self, pos):
        self.image = kamikaze_enemy_image
        self.original_player_image = kamikaze_enemy_image
        self.rect = self.image.get_rect()
        self.speed = 1
        self.pos = pygame.Vector2(pos[0], pos[1])

    def draw(self):
        self.rect.center = (int(round(self.pos.x)), int(round(self.pos.y)))
        screen.blit(self.image, self.rect)

    #rotate the player where the mouse is aiming
    def rotate(self):
        mouse_x, mouse_y = player_one_istance.x, player_one_istance.y
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.original_player_image, int(self.angle))
        orig_center = self.original_player_image.get_rect(topleft=(self.pos.x, self.pos.y)).center
        self.rect = self.image.get_rect(center=orig_center)

    def moveTrowardsPlayer(self):
        deltaVec = pygame.Vector2(player_one_istance.rect.center) - self.pos
        len = deltaVec.length()
        if len > 0:
            self.pos += deltaVec / len * min(len, self.speed)

    #check if shooting enemy collides with player and in that case remove 1 life
    def collisionKamikazeEnemyWithPlayer(self, player_one_istance, player):
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        if player_rect.colliderect(self.rect):
            kamikaze_enemy_list_removed.append(kamikaze_enemy)
            player_one_istance.life = 0


#inizialize the all game var
initialize()


#temp var
laser_bool = False
key = [False, False, False, False]
mouse = False
temp = False
running = True


#main loop
while running:

    #event loop
    for event in pygame.event.get():

        #move player if keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key[0] = True
            if event.key == pygame.K_d:
                key[1] = True
            if event.key == pygame.K_w:
                key[2] = True
            if event.key == pygame.K_s:
                key[3] = True

            if event.key == pygame.K_SPACE:
                laser_bool = True

        #if mouse is pressed then shoot
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
            temp = True

        # if mouse is not pressed then stop shooting
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False

        #stop player if keys are not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key[0] = False
            if event.key == pygame.K_d:
                key[1] = False
            if event.key == pygame.K_w:
                key[2] = False
            if event.key == pygame.K_s:
                key[3] = False

            if event.key == pygame.K_SPACE:
                laser_bool = False

        #quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    if mouse:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_one_istance.x, mouse_y - player_one_istance.y
        player_one_istance.angle = math.atan2(rel_y, rel_x)
        bullets_list.append( Bullet(player_one_istance.x, player_one_istance.y) )
        mouse = False

    if len(shooting_enemies_list) == 0 or shooting_enemies_list[-1].y > 70:
        shooting_enemies_list.append( ShootingEnemy() )

    if len(shooting_enemies_list) != 0:
        for shooting_enemy in shooting_enemies_list:
            if shooting_enemy.tick_to_shoot_for_enemy % 60 == 0:
                target = Vector2(player_one_istance.x, player_one_istance.y)
                bullet = BulletEnemyShooting(shooting_enemy.angle, (shooting_enemy.x, shooting_enemy.y), target)
                enemy_bullets_list.append(bullet)

            shooting_enemy.collisionShootingEnemyPlayer(player_one_istance, first_player_spaceship_image)

        if len(enemy_bullets_list) != 0:
            for enemy_bullet in enemy_bullets_list:
                enemy_bullet.collisionBulletShootingEnemy(player_one_istance, first_player_spaceship_image)

    if len(kamikaze_enemy_list) == 0 or kamikaze_enemy_list[-1].pos.y > 150:
        dist = 0 - player_one_istance.y
        p_pos = (player_one_istance.rect.centerx, player_one_istance.rect.centery)
        kamikaze_pos = (p_pos[0] + dist * math.sin(0), p_pos[1] + dist * math.cos(0))
        kamikaze_enemy_list.append( KamikazeEnemy(kamikaze_pos) )

    if len(kamikaze_enemy_list) != 0:
        for kamikaze_enemy in kamikaze_enemy_list:
            kamikaze_enemy.collisionKamikazeEnemyWithPlayer(player_one_istance, first_player_spaceship_image)

    for bullet2 in bullets_list:
        for shooting_enemy in shooting_enemies_list:
            bullet2.collisionPlayerBulletWithShootingEnemy(shooting_enemy, shooting_enemy_image)
        for kamikaze_enemy in kamikaze_enemy_list:
             bullet2.collisionPlayerBulletWithKamikazeEnemy(kamikaze_enemy, kamikaze_enemy_image)

    #delete collision
    deleteCollision()
    #draw all things
    drawAll()
    #update all things
    update()