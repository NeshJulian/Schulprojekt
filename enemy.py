import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/aliensprite.png')
        self.image = pygame.transform.scale2x(img)
        self.enemyX = x
        self.enemyY = y
        self.rect = (100,100)

    #def createEnemy(self, x,y):
