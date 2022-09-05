import pygame
import unicorn, item, enemy

Screen_WIDTH = 800
Screen_HEIGHT = 600

pygame.init()
#Initialisierung Screen / Fenster
screen = pygame.display.set_mode( (Screen_HEIGHT, Screen_WIDTH))
#Hintergrund
#TODO Mehrphaser Hintergrund, bis jetzt nur 1
backImage = pygame.image.load()
#Player
#Enemy
#Items
#Laser

running = True

while running:

    pygame.display.update()

pygame.quit()