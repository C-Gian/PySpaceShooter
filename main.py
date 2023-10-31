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
first_player_spaceship_image = pygame.image.load('spaceship3.png').convert_alpha()
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
enemy_laser_bullet_image = pygame.image.load('prova.png').convert_alpha()
kamikaze_enemy_image = pygame.image.load('kamikaze.png').convert_alpha()
kamikaze_explosion_1 = pygame.image.load('kamikaze_0.png').convert_alpha()
kamikaze_explosion_2 = pygame.image.load('kamikaze_1.png').convert_alpha()
kamikaze_explosion_3 = pygame.image.load('kamikaze_2.png').convert_alpha()
kamikaze_explosion_4 = pygame.image.load('kamikaze_3.png').convert_alpha()
kamikaze_explosion_5 = pygame.image.load('kamikaze_4.png').convert_alpha()
kamikaze_explosion_6 = pygame.image.load('kamikaze_5.png').convert_alpha()
kamikaze_explosion_7 = pygame.image.load('kamikaze_6.png').convert_alpha()
main_enemy_boss_image = pygame.image.load('prova2.png').convert_alpha()
main_enemy_boss_image_damage = pygame.image.load('prova2-damage.png').convert_alpha()
explosion_boss_missile_1 = pygame.image.load('explosion_boss_missile_.png').convert_alpha()
explosion_boss_missile_2 = pygame.image.load('explosion_boss_missile_2.png').convert_alpha()
explosion_boss_missile_3 = pygame.image.load('explosion_boss_missile_3.png').convert_alpha()
explosion_boss_missile_4 = pygame.image.load('explosion_boss_missile_4.png').convert_alpha()
explosion_boss_missile_5 = pygame.image.load('explosion_boss_missile_5.png').convert_alpha()
explosion_boss_missile_6 = pygame.image.load('explosion_boss_missile_6.png').convert_alpha()
explosion_boss_missile_7 = pygame.image.load('explosion_boss_missile_7.png').convert_alpha()
explosion_boss_missile_8 = pygame.image.load('explosion_boss_missile_8.png').convert_alpha()
explosion_boss_missile_9 = pygame.image.load('explosion_boss_missile_9.png').convert_alpha()
missile_animation_1 = pygame.image.load('missile_animation_1.png').convert_alpha()
missile_animation_2 = pygame.image.load('missile_animation_2.png').convert_alpha()

def initialize():
    global background_y, shooting_enemy_speed, tick_to_damage_boss, shooting_enemies_list, bullets_list, \
            score, play_again_gameover, pause_bool, stay_menu, player_one_istance, \
            fighting_boss, boss_present, laser_as_bullet_istance_one, laser_as_bonus_is_active_bool, life_as_bonus_is_active_bool, \
            laser_as_bonus_istance_one, life_as_bonus_istance_one, laser_as_bonus_taken, \
            laser_bonus_taken_tick, life_as_bonus_taken_tick, shield_as_bonus_istance_one, \
            shield_as_bonus_is_active_bool, shield_as_bonus_taken, shield_bonus_taken_tick, shield_as_shield_istance_one,\
            tick_to_animate_shield, tick_immune_after_shield_boss, to_end_shield_animation, enemy_bullets_list, kamikaze_enemy_list, \
            bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_removed, tick_to_animate_kamikaze_explosion, \
            boss_list, boss_list_removed, boss_missile_list, boss_missile_removed

    background_y, shooting_enemy_speed, tick_to_damage_boss, boss_life, score, laser_bonus_taken_tick, life_as_bonus_taken_tick, shield_bonus_taken_tick, tick_to_animate_shield, tick_immune_after_shield_boss = 0, 2, 0, 20, 0, 0, 0, 0, 1, 0
    laser_as_bonus_is_active_bool, life_as_bonus_is_active_bool, pause_bool, fighting_boss, boss_present, play_again_gameover, laser_as_bonus_taken, shield_as_bonus_is_active_bool, shield_as_bonus_taken = False, False, False, False, False, False, False, False, False
    stay_menu = True
    to_end_shield_animation = False
    tick_to_animate_kamikaze_explosion = 1
    bullets_list, shooting_enemies_list, enemy_bullets_list, kamikaze_enemy_list, boss_list, boss_missile_list = [], [], [], [], [], []
    bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_removed, boss_list_removed, boss_missile_removed = [], [], [], [], [], []
    shooting_enemies_list.append(ShootingEnemy())
    player_one_istance = Player(display_width // 2, display_height//2, first_player_spaceship_image)
    laser_as_bullet_istance_one = Laser(player_one_istance.x, player_one_istance.y)
    shield_as_bonus_istance_one = EnergyShieldAsBonus()
    shield_as_shield_istance_one = EnergyShield(player_one_istance)
    laser_as_bonus_istance_one = LaserAsBonus()
    life_as_bonus_istance_one = LifeAsBonus()

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def drawAll():
    gameIntro()
    gamePause()
    gameOver()
    drawBackground()
    drawScore()
    drawLife()
    drawPlayer()
    drawShootingEnemy()
    drawKamikazeEnemy()
    drawShootingEnemyBullets()
    drawBullets()
    drawBossMissile()
    drawBoss()
    drawLaserBonus()
    drawLifeBonus()
    drawShieldBonus()
    drawLaser()
    player_one_istance.drawPlayer()
    drawShield()

def checkAll():
    checkBoss()
    checkLaserBonus()
    checkLifeBonus()
    checkShieldBonus()

def drawBackground():
    global background_y
    temp_y = background_y % background.get_rect().height
    screen.blit(background, (0, temp_y - background.get_rect().height))
    if temp_y < display_height:
        screen.blit(background, (0, temp_y))
    background_y -= 1

def deleteCollision():
    global shooting_enemies_list, bullets_list, enemy_bullets_list, kamikaze_enemy_list, explosion_list, boss_missile_list
    bullets_list_removed, shooting_enemies_list_removed, enemy_bullets_list_removed, kamikaze_enemy_removed
    bullets_list = [bullet2 for bullet2 in bullets_list if bullet2 not in bullets_list_removed]
    shooting_enemies_list = [shooting_enemy for shooting_enemy in shooting_enemies_list if shooting_enemy not in shooting_enemies_list_removed]
    enemy_bullets_list = [enemy_bullet for enemy_bullet in enemy_bullets_list if enemy_bullet not in enemy_bullets_list_removed]
    kamikaze_enemy_list = [kamikaze_enemy for kamikaze_enemy in kamikaze_enemy_list if kamikaze_enemy not in kamikaze_enemy_removed]
    boss_missile_list = [boss_missilee for boss_missilee in boss_missile_list if boss_missilee not in boss_missile_removed]

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

def drawBossMissile():
    #draw boss missile
    for boss_missilee in boss_missile_list:
        boss_missilee.moveTrowardsPlayer()
        boss_missilee.rotate()
        boss_missilee.draw()

def drawBullets():
    for bullet2 in bullets_list:
        bullet2.rotate()
        bullet2.continueDrawBullet()

def drawLaser():
    global laser_as_bonus_is_active_bool
    if laser_bool and laser_as_bonus_taken:
        laser_as_bullet_istance_one.rotate()
        laser_as_bullet_istance_one.continueDrawLaser()

def drawShield():
    global shield_as_bonus_is_active_bool, shield_as_bonus_taken
    if shield_as_bonus_taken:
        shield_as_shield_istance_one.continueDrawEnergyShield()

def drawBoss():
    global boss_list
    if len(boss_list) != 0:
        boss_list[0].draw()

def drawLaserBonus():
    global laser_as_bonus_is_active_bool
    if laser_as_bonus_is_active_bool:
        laser_as_bonus_istance_one.continueDrawLaserBonus()

def drawLifeBonus():
    global life_as_bonus_is_active_bool
    if life_as_bonus_is_active_bool:
        life_as_bonus_istance_one.continueDrawLifeBonus()

def drawShieldBonus():
    global shield_as_bonus_is_active_bool, shield_as_bonus_taken
    if shield_as_bonus_is_active_bool and not shield_as_bonus_taken:
        shield_as_bonus_istance_one.continueDrawShieldBonus()

def drawScore():
    font = pygame.font.SysFont('ubuntumono', 20, True)
    if not player_one_istance.life <= 0:
        score_surface = font.render("Score : " + str(score), True, (255, 255, 255))
        screen.blit(score_surface, (10,10) )
    else:
        score_surface = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_surface, (295, 242))

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

def buttonIntro(messaggio, x, y, w, h, colore_chiaro, colore_scuro, action=None):
    global stay_menu
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, colore_scuro, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                stay_menu = False
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, colore_chiaro, (x, y, w, h))

    testo_green_button = pygame.font.SysFont('ubuntumono', 20, True)
    green_button_surface = testo_green_button.render(messaggio, True, (0, 0, 0))
    green_button_rect = green_button_surface.get_rect()
    green_button_rect.center = (x + (w // 2), (y + (h // 2)))

    screen.blit(green_button_surface, green_button_rect)

def gameIntro():
    global stay_menu
    while stay_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit( background, (0, 0) )
        testo_menu = pygame.font.SysFont('comicsans', 70, True)
        menu_surface = testo_menu.render( 'MENÙ', True, (255,255,255) )
        menu_rect = menu_surface.get_rect()
        menu_rect.center = ( display_width//2, 165 )
        screen.blit(menu_surface, menu_rect)

        #creo il bottone verde con scritto start
        buttonIntro( 'start', (display_width // 2) - 125 // 2, 200, 125, 25, (255,0,0), (200,0,0), "play")
        #creo il bottone rosso con scritto quit
        buttonIntro('quit', (display_width // 2) - 125 // 2, 230, 125, 25, (0, 255, 0), (0, 200, 0), "quit")

        pygame.display.update()
        pygame.time.Clock().tick(fps//2)

def gamePause():
    global pause_bool
    while pause_bool:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                pause_bool = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                global stay_menu
                stay_menu = True
                pause_bool = False
                initialize()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill( (255, 255, 255) )

        testo_pausa = pygame.font.SysFont('comicsans', 70, True)
        pausa_surface = testo_pausa.render( 'PAUSA', True, (0,0,0) )
        pausa_rect = pausa_surface.get_rect()
        pausa_rect.center = ( (display_width//2), (display_height//2) )
        screen.blit(pausa_surface, pausa_rect)

        pygame.display.update()
        pygame.time.Clock().tick(fps//2)

def gameOver():
    global stay_menu
    if player_one_istance.life <= 0:
        screen.blit( gameover_image, (0, 0) )
        drawScore()
        update()
        play_again_gameover = False
        while not play_again_gameover:
            for event in pygame.event.get():

                #if key pressed is space than start new game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    initialize()
                    play_again_gameover = True
                    stay_menu = False

                #if key pressed is esc then go to menu
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    stay_menu = True
                    play_again_gameover = True
                    initialize()

                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

def checkBoss():
    global fighting_boss, boss_present
    if score == 1000:   #condition to active the boss
        boss_present = True
        fighting_boss = True

def checkLaserBonus():
    global score, laser_as_bonus_is_active_bool, laser_as_bonus_taken
    if score == 1 and not laser_as_bonus_taken:    # condition to active the bonus
        laser_as_bonus_is_active_bool = True

def checkLifeBonus():
    global score, life_as_bonus_is_active_bool
    if player_one_istance.life < 6 and (score == 10 or player_one_istance.life == 1):   #condition to active the bonus
        life_as_bonus_is_active_bool = True

def checkShieldBonus():
    global score, shield_as_bonus_is_active_bool, shield_as_bonus_taken
    if score == 1 and not shield_as_bonus_taken:     #condition to active the bonus
        shield_as_bonus_is_active_bool = True

class EnergyShield:
    #initialize the shield
    def __init__(self, player_one_istance):
        self.x = player_one_istance.x
        self.y = player_one_istance.y
        self.image = energy_shield_number_1
        self.tick = 0

    def continueDrawEnergyShield(self):
        global tick_to_animate_shield
        self.image = eval('energy_shield_number_' + str(tick_to_animate_shield))
        self.x = player_one_istance.x - first_player_spaceship_image.get_width()//2
        self.y = (player_one_istance.y - first_player_spaceship_image.get_height()//2)+2
        screen.blit( self.image, (self.x, self.y) )

    def collideShootingEnemy(self):
        shooting_enemy_rect = pygame.Rect( shooting_enemy.x, shooting_enemy.y, shooting_enemy_image.get_width(), shooting_enemy_image.get_height() )
        shield_as_bonus_rect = pygame.Rect( self.x, self.y, energy_shield_number_5.get_width(), energy_shield_number_5.get_height() )
        if shield_as_bonus_rect.colliderect(shooting_enemy_rect):
            shooting_enemies_list_removed.add(shooting_enemy)

    def collideKamikazeEnemy(self):
        global shield_bonus_taken_tick
        kamikaze_enemy_rect = pygame.Rect( kamikaze_enemy.pos.x, kamikaze_enemy.pos.y, kamikaze_enemy_image.get_width(), kamikaze_enemy_image.get_height() )
        shield_as_bonus_rect = pygame.Rect( self.x, self.y, energy_shield_number_5.get_width(), energy_shield_number_5.get_height() )
        if shield_as_bonus_rect.colliderect(kamikaze_enemy_rect):
            kamikaze_enemy_removed.append(kamikaze_enemy)
            shield_bonus_taken_tick = 300

    def collideBossMissile(self):
        global shield_bonus_taken_tick
        boss_missile_rect = pygame.Rect( boss_missilee.pos.x, boss_missilee.pos.y, missile_animation_1.get_width(), missile_animation_1.get_height() )
        shield_as_bonus_rect = pygame.Rect( self.x, self.y, energy_shield_number_5.get_width(), energy_shield_number_5.get_height() )
        if shield_as_bonus_rect.colliderect(boss_missile_rect):
            boss_missile_removed.append(boss_missilee)
            shield_bonus_taken_tick = 300

    def collideBoss(self):
        global tick_immune_after_shield_boss, shield_bonus_taken_tick
        boss_Rect = pygame.Rect( bosss.x, bosss.y, bosss.image.get_width(), bosss.image.get_height() )
        shield_as_bonus_rect = pygame.Rect( self.x, self.y, energy_shield_number_5.get_width(), energy_shield_number_5.get_height() )
        if shield_as_bonus_rect.colliderect(boss_Rect):
            tick_immune_after_shield_boss = 30
            shield_bonus_taken_tick = 300

class EnergyShieldAsBonus:
    #initialize the bonus
    def __init__(self):
        self.image = energy_shield_as_bonus_image
        self.x = random.randint(10, display_width - self.image.get_width()-100)
        self.y = random.randint(10, display_height - self.image.get_height()+50)
        self.time = 0

    #draw the bonus
    def continueDrawShieldBonus(self):
        screen.blit(self.image, (self.x, self.y))

    #after x second it will change its position, where x is number/60
    def updatePos(self):
        self.time += 1
        if self.time%150 == 0:
            self.x = random.randint(10, display_width - self.image.get_width()-100)
            self.y = random.randint(10, display_height - self.image.get_height()+50)

    #check if the bullet collides with the shield bonus and in that case activate the shield
    def collisionBulletShieldBonus(self, bullet2, laser_bullet):
        global shield_as_bonus_is_active_bool, shield_as_bonus_taken
        bullet_rect = pygame.Rect(bullet2.x, bullet2.y, laser_bullet.get_width(), laser_bullet.get_height() )
        shield_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() )
        # check collision
        if shield_bonus_rect.colliderect(bullet_rect):
            bullets_list_removed.append(bullet2)
            self.x = 5000
            shield_as_bonus_is_active_bool = False
            shield_as_bonus_taken = True

    #check if shield_as_bonus collides with player and in that case get the bonus
    def collisionShieldAsBonusPlayer(self, player_one_istance, player):
        global shield_as_bonus_is_active_bool, shield_as_bonus_taken
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        shield_as_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if player_rect.colliderect(shield_as_bonus_rect):
            shield_as_bonus_is_active_bool = False
            shield_as_bonus_taken = True

class LifeAsBonus:
    #initialize the bonus
    def __init__(self):
        self.image = bonus_life_image
        self.x = random.randint(10, display_width - self.image.get_width()-100)
        self.y = random.randint(10, display_height - self.image.get_height()+50)
        self.time = 0

    #draw the bonus
    def continueDrawLifeBonus(self):
        screen.blit(self.image, (self.x, self.y))

    #after x second it will change its position, where x is number/60
    def updatePos(self):
        self.time += 1
        if self.time%150 == 0:
            self.x = random.randint(10, display_width - self.image.get_width()-100)
            self.y = random.randint(10, display_height - self.image.get_height()+50)

    #check if the bullet collides with the laser bonus and in that case activate the laser beam
    def collisionBulletLifeBonus(self, bullet2, laser_bullet):
        global life_as_bonus_is_active_bool
        bullet_rect = pygame.Rect(bullet2.x, bullet2.y, laser_bullet.get_width(), laser_bullet.get_height() )
        life_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() )
        # check collision
        if life_bonus_rect.colliderect(bullet_rect):
            player_one_istance.life += 1
            bullets_list_removed.append(bullet2)
            self.x = 5000
            life_as_bonus_is_active_bool = False
            return True
        return False

    #check if life_as_bonus collides with player and in that case get the bonus
    def collisionLifeAsBonusPlayer(self, player_one_istance, player):
        global life_as_bonus_is_active_bool
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        life_as_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if player_rect.colliderect(life_as_bonus_rect):
            player_one_istance.life += 1
            life_as_bonus_is_active_bool = False
            return True
        return False

class LaserAsBonus:
    #initialize the bonus
    def __init__(self):
        self.image = bonus_laser_image
        self.x = random.randint(10, display_width-self.image.get_width()-100)
        self.y = random.randint(10, display_height-self.image.get_height()+50)
        self.time = 0

    #draw the bonus
    def continueDrawLaserBonus(self):
        screen.blit(self.image, (self.x, self.y))

    #after x second it will change its position, where x is number/60
    def updatePos(self):
        self.time += 1
        if self.time%150 == 0:
            self.x = random.randint(10, display_width - self.image.get_width()-100)
            self.y = random.randint(10, display_height - self.image.get_height()+50)

    #check if the bullet collides with the laser bonus and in that case activate the laser beam
    def collisionBulletLaserBonus(self, bullet2, laser_bullet):
        global laser_as_bonus_is_active_bool, laser_as_bonus_taken
        bullet_rect = pygame.Rect(bullet2.x, bullet2.y, laser_bullet.get_width(), laser_bullet.get_height() )
        laser_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height() )
        # check collision
        if laser_bonus_rect.colliderect(bullet_rect):
            bullets_list_removed.append(bullet2)
            self.x = 5000
            laser_as_bonus_taken = True
            laser_as_bonus_is_active_bool = False

    #check if laser_as_bonus collides with player and in that case get the bonus
    def collisionLaseAsBonusPlayer(self, player_one_istance, player):
        global laser_as_bonus_is_active_bool, laser_as_bonus_taken
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        laser_as_bonus_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if player_rect.colliderect(laser_as_bonus_rect):
            laser_as_bonus_taken = True
            laser_as_bonus_is_active_bool = False

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
            score += 1
            kamikaze_enemy.shooted = True

    #check if the bullet collides with shooting enemy and in that case increment the score
    def collisionPlayerBulletWithBoss(self, boss_one_istance):
        global score
        boss_rect = pygame.Rect(boss_one_istance.x, boss_one_istance.y, main_enemy_boss_image.get_width(), main_enemy_boss_image.get_height() )
        bullet_rect = pygame.Rect(self.x, self.y, laser_bullet.get_width(), laser_bullet.get_height() )
        # check collision
        if bullet_rect.colliderect(boss_rect):
            boss_one_istance.bool_damage = True
            bullets_list_removed.append(self)
            boss_one_istance.life -= 1

    #check if the bullet collides with shooting enemy and in that case increment the score
    def collisionPlayerBulletWithBossMissile(self, boss_missilee):
        global score
        boss_missile_rect = pygame.Rect(boss_missilee.pos.x, boss_missilee.pos.y, boss_missilee.image.get_width(), boss_missilee.image.get_height() )
        bullet_rect = pygame.Rect(self.x, self.y, laser_bullet.get_width(), laser_bullet.get_height() )
        # check collision
        if bullet_rect.colliderect(boss_missile_rect):
            score += 1
            bullets_list_removed.append(self)
            boss_missilee.shooted = True

class ShootingEnemy:
    #inizialize the enemy
    def __init__(self):
        self.image = shooting_enemy_image
        self.new_shooting_enemy_image = shooting_enemy_image
        self.x = random.uniform( shooting_enemy_image.get_width(), display_width - shooting_enemy_image.get_width() )
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
        global score, shield_as_bonus_taken
        shooting_enemy_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player_image.get_width(), player_image.get_height() )
        #check collision
        if shooting_enemy_rect.colliderect(self.rect):
            enemy_bullets_list_removed.append(self)
            if not shield_as_bonus_taken:
                player_one_istance.life -= 1

class Boss:
    #inizialize the boss
    def __init__(self):
        self.x = display_width//2-main_enemy_boss_image.get_width()//2
        self.y = -(main_enemy_boss_image.get_height()+50)
        self.image = main_enemy_boss_image
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.life = 500
        self.timer_damage = 0
        self.bool_damage = False

    def draw(self):
        if self.bool_damage:
            self.timer_damage += 1
            self.image = main_enemy_boss_image_damage
            if self.timer_damage == 5:
                self.bool_damage = False
                self.timer_damage = 0
                self.image = main_enemy_boss_image
        if self.y >= -(self.h//2):
            screen.blit(self.image, (self.x, self.y))

        else:
            self.y += 1
            screen.blit(self.image, (self.x, self.y))

    #check if boss collides with player and in that case remove 50 life
    def collisionPlayerWithBoss(self, player_one_istance, player):
        global shield_bonus_taken_tick
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        boss_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if player_rect.colliderect(boss_rect):
            if shield_as_bonus_taken:
                shield_bonus_taken_tick = 300
            else:
                player_one_istance.life -= 50

    def bossDefeat(self):
        global score, fighting_boss, boss_present
        if boss_present and self.boss_life <= 0:
            score += 50
            boss_present = False
            fighting_boss = False
            return True

class Laser:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
        self.original_image = pygame.Surface((2, 1100))
        self.original_image.set_colorkey( (0,0,0) )
        self.original_image.fill( (255,0,0) )
        self.copy_image = self.original_image.copy()
        self.copy_image.set_colorkey( (0,0,0) )
        self.rect = self.copy_image.get_rect()
        self.new_image = pygame.Surface((2, 1100))
        self.angle = 0

    def continueDrawLaser(self):
        if laser_bool:
            screen.blit(self.new_image, self.rect)

    def rotate(self):
        # get rectangle of player and laser, as if the angle would be 0
        player_rect = player_one_istance.original_player_image.get_rect(topleft=(player_one_istance.x, player_one_istance.y))
        laser_rect = self.original_image.get_rect(midbottom=player_rect.midtop)
        self.angle = player_one_istance.angle
        pivotPos = [player_rect.centerx - laser_rect.x, player_rect.centery - laser_rect.y]
        # calcaulate the axis aligned bounding box of the rotated image
        w, h = self.original_image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        # calculate the translation of the pivot
        pivot = pygame.math.Vector2(pivotPos[0], -pivotPos[1])
        pivot_rotate = pivot.rotate(self.angle)
        pivot_move = pivot_rotate - pivot
        # calculate the upper left origin of the rotated image
        origin = (laser_rect.x + min_box[0] - pivot_move[0], laser_rect.y - max_box[1] + pivot_move[1])
        # get a rotated image
        self.new_image = pygame.transform.rotate(self.original_image, self.angle)
        # get new rectangle
        self.rect = self.new_image.get_rect(topleft=origin)

    def collide(self):
        global score, fighting_boss, tick_to_damage_boss, boss_list
        shooting_enemy_rect = pygame.Rect( shooting_enemy.x, shooting_enemy.y, shooting_enemy_image.get_width(), shooting_enemy_image.get_height() )
        kamikaze_enemy_rect = pygame.Rect(kamikaze_enemy.pos.x, kamikaze_enemy.pos.y, kamikaze_enemy_image.get_width(), kamikaze_enemy_image.get_height())
        boss_missile_rect = pygame.Rect(boss_missilee.pos.x, boss_missilee.pos.y, boss_missilee.image.get_width(), boss_missilee.image.get_height())
        angle = player_one_istance.angle
        if angle < 0:
            angle += 360
        if angle < 90 or (angle > 180 and angle < 270):
            laserline = [laser_as_bullet_istance_one.rect.topleft, laser_as_bullet_istance_one.rect.bottomright]
        else:
            laserline = [laser_as_bullet_istance_one.rect.bottomleft, laser_as_bullet_istance_one.rect.topright]

        if not fighting_boss:
            if shooting_enemy.y > shooting_enemy_image.get_height():
                collide_shooting_enemy = colideRectLine(shooting_enemy_rect, *laserline)
                if collide_shooting_enemy:
                    shooting_enemies_list_removed.append(shooting_enemy)
                    score += 1
            if kamikaze_enemy.pos.y > kamikaze_enemy_image.get_height():
                collide_kamikaze_enemy = colideRectLine(kamikaze_enemy_rect, *laserline)
                if collide_kamikaze_enemy:
                    kamikaze_enemy_removed.append(kamikaze_enemy)
                    score += 1
        if fighting_boss:
            if tick_to_damage_boss < 150:
                if shooting_enemy.y > shooting_enemy_image.get_height():
                    collide_shooting_enemy = colideRectLine(shooting_enemy_rect, *laserline)
                    if collide_shooting_enemy:
                        shooting_enemies_list_removed.append(shooting_enemy)
                        score += 1
                if kamikaze_enemy.pos.y > kamikaze_enemy_image.get_height():
                    collide_kamikaze_enemy = colideRectLine(kamikaze_enemy_rect, *laserline)
                    if collide_kamikaze_enemy:
                        kamikaze_enemy_removed.append(kamikaze_enemy)
                        score += 1
            else:
                if shooting_enemy.y > shooting_enemy_image.get_height():
                    collide_shooting_enemy = colideRectLine(shooting_enemy_rect, *laserline)
                    if collide_shooting_enemy:
                        shooting_enemies_list_removed.append(shooting_enemy)
                        score += 1
                if kamikaze_enemy.pos.y > kamikaze_enemy_image.get_height():
                    collide_kamikaze_enemy = colideRectLine(kamikaze_enemy_rect, *laserline)
                    if collide_kamikaze_enemy:
                        kamikaze_enemy_removed.append(kamikaze_enemy)
                        score += 1
                if boss_missilee.pos.y > boss_missilee.image.get_height():
                    collide_boss_missile = colideRectLine(boss_missile_rect, *laserline)
                    if collide_boss_missile:
                        boss_missile_removed.append(boss_missilee)

class KamikazeEnemy:
    #inizialize the enemy
    def __init__(self, pos):
        self.image = kamikaze_enemy_image
        self.original_player_image = kamikaze_enemy_image
        self.rect = self.image.get_rect()
        self.speed = 3
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.shooted = False
        self.tick_to_animate_kamikaze_explosion = 1

    def draw(self):
        if self.shooted:
            self.rect.center = (int(round(self.pos.x)), int(round(self.pos.y)))
            self.image = eval( 'kamikaze_explosion_' + str(self.tick_to_animate_kamikaze_explosion) )
            if self.tick_to_animate_kamikaze_explosion == 7:
                kamikaze_enemy_removed.append(self)
            else:
                self.tick_to_animate_kamikaze_explosion += 1
            screen.blit(self.image, self.rect)
        else:
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
        global shield_as_bonus_taken, shield_bonus_taken_tick
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        if player_rect.colliderect(self.rect):
            if shield_as_bonus_taken:
                kamikaze_enemy_removed.append(kamikaze_enemy)
                shield_bonus_taken_tick = 300
            else:
                kamikaze_enemy_removed.append(kamikaze_enemy)
                player_one_istance.life -= 3

class BossMissile:
    #inizialize the boss missile
    def __init__(self, pos):
        self.image = missile_animation_1
        self.original_missile_image = missile_animation_1
        self.rect = self.image.get_rect()
        self.speed = 3
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.shooted = False
        self.tick_to_animate_missile_explosion = 1
        self.tick_to_animate_missile_fire = 1

    def draw(self):
        if self.shooted:
            self.rect.center = (int(round(self.pos.x-150)), int(round(self.pos.y)))
            self.image = eval( 'explosion_boss_missile_' + str(self.tick_to_animate_missile_explosion) )
            if self.tick_to_animate_missile_explosion == 9:
                boss_missile_removed.append(self)
            else:
                self.tick_to_animate_missile_explosion += 1
            screen.blit(self.image, self.rect)
        else:
            self.rect.center = (int(round(self.pos.x)), int(round(self.pos.y)))
            screen.blit(self.image, self.rect)

    #rotate the player where the mouse is aiming
    def rotate(self):
        mouse_x, mouse_y = player_one_istance.x, player_one_istance.y
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        self.image = pygame.transform.rotate(self.original_missile_image, int(self.angle))
        orig_center = self.original_missile_image.get_rect(topleft=(self.pos.x, self.pos.y)).center
        self.rect = self.image.get_rect(center=orig_center)

    def moveTrowardsPlayer(self):
        deltaVec = pygame.Vector2(player_one_istance.rect.center) - self.pos
        len = deltaVec.length()
        if len > 0:
            self.pos += deltaVec / len * min(len, self.speed)

    #check if the boss missile collide with player and in that case gameover
    def collisionBossMissileWithPlayer(self, player_one_istance, player):
        global shield_as_bonus_taken, shield_bonus_taken_tick
        player_rect = pygame.Rect(player_one_istance.x, player_one_istance.y, player.get_width(), player.get_height())
        if player_rect.colliderect(self.rect):
            if shield_as_bonus_taken:
                boss_missile_removed.append(boss_missilee)
                shield_bonus_taken_tick = 300
            else:
                boss_missile_removed.append(boss_missilee)
                player_one_istance.life -= 50


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

            #if key pressed is esc then go to menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                global stay_menu
                stay_menu = True
                initialize()

            #if key pressed is c then pause
            if event.key == pygame.K_c:
                global pause_bool
                pause_bool = True

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

    if not boss_present and (len(shooting_enemies_list) == 0 or shooting_enemies_list[-1].y > 70):
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

    if not boss_present and (len(kamikaze_enemy_list) == 0 or kamikaze_enemy_list[-1].pos.y > 150):
        dist = 0 - player_one_istance.y
        p_pos = (player_one_istance.rect.centerx, player_one_istance.rect.centery)
        kamikaze_pos = (p_pos[0] + dist * math.sin(0), p_pos[1] + dist * math.cos(0))
        kamikaze_enemy_list.append( KamikazeEnemy(kamikaze_pos) )

    if len(kamikaze_enemy_list) != 0:
        for kamikaze_enemy in kamikaze_enemy_list:
            kamikaze_enemy.collisionKamikazeEnemyWithPlayer(player_one_istance, first_player_spaceship_image)

    if len(boss_missile_list) == 0 or boss_missile_list[-1].pos.y > 150:
        dist = 0 - player_one_istance.y
        p_pos = (random.uniform(266,534), random.uniform(-224, 0)) #(player_one_istance.rect.centerx, player_one_istance.rect.centery)
        boss_missile_pos = (p_pos[0] + dist * math.sin(0), p_pos[1] + dist * math.cos(0))
        boss_missile_list.append( BossMissile(boss_missile_pos) )

    if len(boss_missile_list) != 0:
        for boss_missilee in boss_missile_list:
            boss_missilee.collisionBossMissileWithPlayer(player_one_istance, first_player_spaceship_image)

    for bullet2 in bullets_list:
        for shooting_enemy in shooting_enemies_list:
            bullet2.collisionPlayerBulletWithShootingEnemy(shooting_enemy, shooting_enemy_image)
        for kamikaze_enemy in kamikaze_enemy_list:
            bullet2.collisionPlayerBulletWithKamikazeEnemy(kamikaze_enemy, kamikaze_enemy_image)
        for boss_missilee in boss_missile_list:
            bullet2.collisionPlayerBulletWithBossMissile(boss_missilee)

    if boss_present:
        tick_to_damage_boss += 1
        boss_istance_one = Boss()
        boss_list.append(boss_istance_one)
        for bosss in boss_list:
            bosss.collisionPlayerWithBoss(player_one_istance, first_player_spaceship_image)
            for bullet2 in bullets_list:
                bullet2.collisionPlayerBulletWithBoss(bosss)

    #if the laser_as_bonus is active
    if laser_as_bonus_is_active_bool:
        #if the laser_as_bonus is on the screen,then if the spaceship collides with it,active the laser beam
        laser_as_bonus_istance_one.collisionLaseAsBonusPlayer(player_one_istance, first_player_spaceship_image)
        #every x second the bonus change its position
        laser_as_bonus_istance_one.updatePos()
        #for each laser(bullet) shooted
        for bullet2 in bullets_list:
            #check if the bullet collides with the laser_as_bonus
            laser_as_bonus_istance_one.collisionBulletLaserBonus(bullet2, laser_bullet)

    #if the player took the laser_as_bonus
    if laser_as_bonus_taken:
        #increment the tick to calculate how much time the bonus still active
        laser_bonus_taken_tick += 1
        #if this tick is greater then 300 it will turn off
        if laser_bonus_taken_tick == 300:
            laser_as_bonus_taken = False
            laser_as_bonus_is_active_bool = False
        #if i'm pressing space then use the laser and check collisions
        if laser_bool:
            for shooting_enemy in shooting_enemies_list:
                laser_as_bullet_istance_one.collide()
            for kamikaze_enemy in kamikaze_enemy_list:
                laser_as_bullet_istance_one.collide()
            for bosss in boss_list:
                laser_as_bullet_istance_one.collide()
            for boss_missilee in boss_missile_list:
                laser_as_bullet_istance_one.collide()

    #if life_bonus is active
    if life_as_bonus_is_active_bool:
        if life_as_bonus_istance_one.collisionLifeAsBonusPlayer(player_one_istance, first_player_spaceship_image):
            life_as_bonus_is_active_bool = False

        # every x second the bonus change its position
        life_as_bonus_istance_one.updatePos()
        # for each laser(bullet) shooted
        for bullet2 in bullets_list:
            # check if the bullet collides with the life_as_bonus
            if life_as_bonus_istance_one.collisionBulletLifeBonus(bullet2, laser_bullet):
                life_as_bonus_is_active_bool = False
                break

    #if the shield_as_bonus is active
    if shield_as_bonus_is_active_bool:
        #if the shield_as_bonus is on the screen,then if the spaceship collides with it,active the laser beam
        shield_as_bonus_istance_one.collisionShieldAsBonusPlayer(player_one_istance, first_player_spaceship_image)

        #every x second the bonus change its position
        shield_as_bonus_istance_one.updatePos()
        #for each laser(bullet) shooted
        for bullet2 in bullets_list:
            #check if the bullet collides with the shield_as_bonus
            shield_as_bonus_istance_one.collisionBulletShieldBonus(bullet2, laser_bullet)

    if shield_as_bonus_taken and not to_end_shield_animation:
        if tick_to_animate_shield == 5:
            for shooting_enemy in shooting_enemies_list:
                shield_as_shield_istance_one.collideShootingEnemy()
            for kamikaze_enemy in kamikaze_enemy_list:
                shield_as_shield_istance_one.collideKamikazeEnemy()
            for boss_missilee in boss_missile_list:
                shield_as_shield_istance_one.collideBossMissile()
        else:
            tick_to_animate_shield += 1
            for shooting_enemy in shooting_enemies_list:
                shield_as_shield_istance_one.collideShootingEnemy()
            for kamikaze_enemy in kamikaze_enemy_list:
                shield_as_shield_istance_one.collideKamikazeEnemy()
            for boss_missilee in boss_missile_list:
                shield_as_shield_istance_one.collideBossMissile()

    #if the player took the shield_as_bonus
    if shield_as_bonus_taken:
        #increment the tick to calculate how much time the bonus still active
        shield_bonus_taken_tick += 1
        #if this tick is greater then 300 it will turn off
        if shield_bonus_taken_tick >= 300:
            to_end_shield_animation = True
            if tick_to_animate_shield == 10:
                shield_as_bonus_taken = False
                shield_as_bonus_is_active_bool = False
                tick_to_animate_shield = 1
                to_end_shield_animation = False
                shield_bonus_taken_tick = 0
            else:
                tick_to_animate_shield += 1

    #delete collision
    deleteCollision()
    #check all things
    checkAll()
    #draw all things
    drawAll()
    #update all things
    update()