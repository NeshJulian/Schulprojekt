import random
import pygame
import enemy
import item
import laser
import map
import unicorn

clock = pygame.time.Clock()
Screen_WIDTH = 1000
Screen_HEIGHT = 750

#Initialisierung
pygame.init()
screen = pygame.display.set_mode((Screen_WIDTH, Screen_HEIGHT))
pygame.display.set_caption("Pink Fluffy Spaceinvaders, dancing on Spaceships")
level_counter = 2
#Farben
white = (0, 0, 0)
pink = (255, 0, 255)
#Hintergrund
backImage1 = map.Map('background/Hintergrund1.png')
backImage2 = map.Map('background/Hintergrund2.png')
map_group1 = pygame.sprite.GroupSingle(backImage1)
map_group2 = pygame.sprite.GroupSingle(backImage2)
#Player
playerX = 60
playerY = random.randint(100, 750)
unicorn1 = unicorn.Unicorn(playerX, playerY)
unicorn_group = pygame.sprite.Group(unicorn1)
zaehler = 0
#Enemy
enemyX = 970
enemyY = 30
enemy_group = pygame.sprite.Group()
gameGoOn = True
enemy_counter = 0
killedEnemys = enemy_counter
newEnemys = True

for i in range(5):
    for j in range(10):
        enemy_group.add(enemy.Enemy(enemyX, enemyY))
        enemyY += 75
        enemy_counter += 1
    enemyX -= 100
    enemyY = 30

#Items
itemX = random.randint(300, 500)
itemY = random.randint(50, 700)
item_group = pygame.sprite.GroupSingle(item.Item(itemX, itemY))
itemUsed = False
#Laser
laserX = -50
laserY = -50
laser1 = laser.Laser(laserX, laserY)
laser_group = pygame.sprite.GroupSingle(laser1)
isShooting = True

#Fonts
font = pygame.font.SysFont("Arial", 60)
font_small = pygame.font.SysFont("Arial", 20)
game_end = font.render("Spiel gewonnen", True, pink)
game_over = font.render("Game Over", True, pink)
next_level = font.render("Level 2", True, pink)
score_board = font_small.render("Sie haben: " + str(enemy_counter) + " Gegner getötet", True, pink)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                unicorn1.fly(-1)
            if event.key == pygame.K_s:
                unicorn1.fly(1)
        if event.type == pygame.KEYUP:
            unicorn1.fly(0)

    if pygame.sprite.spritecollide(unicorn1, item_group, True):
        laser1.boost = True
        itemUsed = True

    if pygame.sprite.spritecollide(unicorn1, enemy_group, False):
        gameGoOn = False
        screen.blit(game_over, (400, 300))
        screen.blit(score_board, (400, 300))
        isShooting = False

    if pygame.sprite.spritecollide(laser1, enemy_group, True):
        laser1.rect.x = -100
        isShooting = True
        enemy_counter -= 1
        killedEnemys += 1

    zaehler += 1

    if gameGoOn:
        enemy_group.update()
        unicorn_group.update(zaehler)

    if isShooting and laser1.rect.x < -50:
        laser1.rect.x = unicorn1.rect.x + 30
        laser1.rect.y = unicorn1.rect.y
        isShooting = False

    if laser1.rect.x > Screen_WIDTH:
        laser1.rect.x = unicorn1.rect.x +30
        laser1.rect.y = unicorn1.rect.y

    if not isShooting and gameGoOn:
        laser1.movement()

    if zaehler >= 20:
        zaehler = 0

    if not gameGoOn and enemy_counter != 0:
        screen.blit(game_over, (500, 200))

    if level_counter ==2:
        backImage1.update()
        map_group1.draw(screen)

    if enemy_counter == 0:
        if level_counter == 2:
            level_counter -= 1
            screen.blit(next_level, (500, 300))
        elif level_counter == 1:
            level_counter -= 1
        elif level_counter == 0:
            screen.blit(score_board, (500, 100))
            screen.blit(game_end, (500, 200))
            gameGoOn = False

    if level_counter == 1:
        print(level_counter)
        print(gameGoOn)
        enemyX = 900
        enemyY = 30
        if newEnemys:
            print(newEnemys)
            for i in range(5):
                for j in range(10):
                    enemy_group.add(enemy.Enemy(enemyX, enemyY))
                    enemyY += 75
                    enemy_counter += 1
                enemyX -= 100
                enemyY = 30
            itemUsed = False
            item_group.add(item.Item(itemX, itemY))
        newEnemys = False
        backImage2.update()
        map_group2.draw(screen)
        print(enemy_counter)

    item_group.update(itemUsed)

    if gameGoOn:
        laser_group.draw(screen)
        unicorn_group.draw(screen)


    item_group.draw(screen)
    enemy_group.draw(screen)
    pygame.display.update()

pygame.quit()