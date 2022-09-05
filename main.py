import pygame

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
#Player
#Enemy
#Items
#Laser

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print ("test")

    screen.blit(backImage, (0, 0))
    pygame.display.update()

pygame.quit()