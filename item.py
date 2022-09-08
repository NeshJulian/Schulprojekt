import random

import pygame

class Item(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Rainbow_Poop.png')
        self.image = pygame.transform.scale(img, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def itemMove(self):
        self.rect.x -= 1

    def respawnPoop(self, itemUsed):
        if self.rect.x <= 0 and itemUsed:
            self.rect.x = random.randint(300, 500)
            self.rect.y = random.randint(50, 700)

    def update(self, itemUsed):
        self.respawnPoop(itemUsed)
        self.itemMove()
