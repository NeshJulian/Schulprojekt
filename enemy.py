import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/alien.png')
        self.image = pygame.transform.rotozoom(img, 90, 1.5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def enemyMove(self):

        if self.rect.y >= 750:
            self.rect.y = 10
            self.rect.x -= 50

        if self.rect.y < 750:
            self.rect.y += 3

    def update(self):
        self.enemyMove()
