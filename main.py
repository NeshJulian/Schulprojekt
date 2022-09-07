import pygame
import enemy

clock = pygame.time.Clock()
Screen_WIDTH = 800
Screen_HEIGHT = 600

#Initialisierung
pygame.init()
screen1 = pygame.display.set_mode((Screen_WIDTH, Screen_HEIGHT))
pygame.display.set_caption("Pink Fluffy Spaceinvaders, dancing on Spaceships")
#Hintergrund
backImage = pygame.transform.scale(pygame.image.load('background/corona_lf.png'), (Screen_WIDTH, Screen_HEIGHT))

camera_pos = [0, 0]
#Player
#Enemy
enemy1 = enemy.Enemy(200, 100)
enemy_group = pygame.sprite.GroupSingle
enemy_group.add(enemy1)
#Items
#Laser

running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen1.blit(backImage, (0, 0))
    enemy_group.draw(screen1)
    #enemy_group.draw(screen)
    pygame.display.update()

pygame.quit()