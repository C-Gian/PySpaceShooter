import pygame

pygame.init()

display_width = 950
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))

ostacolo = pygame.image.load('laser.png').convert_alpha()
ostacolo_mask = pygame.mask.from_surface(ostacolo)
ostacolo_rect = ostacolo.get_rect()
ox = 950//2 - ostacolo_rect.center[0]
oy = 700//2 - ostacolo_rect.center[1]

laser = pygame.image.load('kamikaze.png').convert_alpha()
laser_mask = pygame.mask.from_surface(laser)
laser_rect = laser.get_rect()


running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        pass

    mx, my = pygame.mouse.get_pos()

    offset = (mx-ox, my-oy)

    result = ostacolo_mask.overlap(laser_mask, offset)

    if result:
        print('aooo')
    else:
        print('eyyyyy')

    screen.blit(ostacolo, (ox, oy))
    screen.blit(laser, (mx, my))

    pygame.display.update()
