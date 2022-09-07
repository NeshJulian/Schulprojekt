#-------------------------------------------------------------------------------
# Name:        main
# Author:      jnowak
# Created:     07.09.2022
# Copyright:   (c) jnowak 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, unicorn

Screen_WIDTH = 800
Screen_HEIGHT = 600

#Initialisierung
pygame.init()
screen = pygame.display.set_mode( (Screen_HEIGHT, Screen_WIDTH))
pygame.display.set_caption("Pink Fluffy Spaceinvaders, dancing on Spaceships")
#Hintergrund
#TODO Mehrphaser Hintergrund, bis jetzt nur 1
backImage = pygame.image.load('background/corona_lf.png').convert()
camera_pos = [0, 0]
#Unicorn
unicorn1 = unicorn.Unicorn(bg_width = 10, screen_width = 10);
unicorn_group = pygame.sprite.GroupSingle()
unicorn_group.add(unicorn1)
#Enemy
#Items
#Laser

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

##    print ("test")

    screen.blit(backImage, (0, 0))
    unicorn_group.draw(screen)
    pygame.display.update()

pygame.quit()
