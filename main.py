import pygame
import random
import pygame.mixer

pygame.init()
#Screen initialisierung
screen = pygame.display.set_mode( (800,600) )
#Hintergrund
bgimage = pygame.image.load('.idea/img/Background/starBackground.png').convert()
#Player
player = pygame.image.load('.idea/img/player.png').convert_alpha()
playerPosx = 350
playerPosy = 500
playerDeltax = 0
#Laser
laserimg = pygame.image.load('.idea/img/laserRed.png').convert_alpha()
isShooting = False
laserPosx = -100
laserPosy = 0
laserDeltay = -10
trefferAnzahl = 0
laser_sound = pygame.mixer.Sound('.idea/snd/laser3.ogg')
#Enemy
enemy = pygame.image.load('.idea/img/enemyShip.png').convert_alpha()
enemyPosx = random.randint(50, 550)
enemyPosy = 50
enemyDeltax = 50
enemyDeltay = 50
enemyCounter = random.randint(50,150)
explosion_sound = pygame.mixer.Sound('.idea/snd/explosion5.ogg')
#Schriftart
trefferfont = pygame.font.SysFont('Arial', 30)
trefferimg = trefferfont.render("Treffer: " +str(0), True, (255,255,255))

running = True

while running:
    #eingabe
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerDeltax += 3
            if event.key == pygame.K_LEFT:
                playerDeltax -= 3
            if event.key == pygame.K_SPACE and not isShooting:
                isShooting = True
                laser_sound.play()
                laserPosx = playerPosx+46
                laserPosy = playerPosy-38

        if event.type == pygame.KEYUP:
            playerDeltax = 0

    #update
    #enemyPosy += enemyDeltay
    if enemyPosy > 550:
        enemyPosy = 550

    enemyPosx += enemyDeltax

    if enemyPosx < 0:
        enemyPosx = 0
        enemyDeltax *= -1
        enemyPosy += enemyDeltay

    if enemyPosx > 702:
        enemyPosx = 702
        enemyDeltax *= -1
        enemyPosy += enemyDeltay

    if enemyPosx + 98 > playerPosx and enemyPosx < playerPosx + 99:
        if enemyPosy + 50 > playerPosy and enemyPosy < playerPosy + 75:
            enemyPosx -= enemyDeltax

    playerPosx += playerDeltax
    if playerPosx < 0:
        playerPosx = 0

    if playerPosx > 701:
        playerPosx = 701

    if isShooting:
        laserPosy = laserPosy + laserDeltay

    if enemyPosx + 98 > laserPosx and enemyPosx < laserPosx + 33:
        if enemyPosy + 50 > laserPosy and enemyPosy < laserPosy + 9:
            trefferAnzahl += 1
            print("Trefferanzahl: " , trefferAnzahl)
            trefferimg = trefferfont.render("Treffer: " +str(trefferAnzahl), True, (255,255,255))
            enemyCounter -= 1
            enemyPosx = random.randint(50, 550)
            enemyPosy = 10
            laserPosx = -100
            isShooting = False
            explosion_sound.play()

    if laserPosy < -30:
        print("oben")
        laserPosx = -100
        laserPosy = 1000
        isShooting = False

    for i in range ((int) (800/bgimage.get_width()) +1):
        for j in range ((int) (600/bgimage.get_height()) +1):
            screen.blit(bgimage, (i*254, j*256))

    screen.blit(player,(playerPosx, playerPosy))
    screen.blit(laserimg, (laserPosx, laserPosy))
    screen.blit(enemy, (enemyPosx, enemyPosy))
    screen.blit(trefferimg, (10,10))

    pygame.display.update()

pygame.quit()

