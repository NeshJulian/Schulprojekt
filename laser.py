import pygame

class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Rainbow.png').convert_alpha()
        self.image = pygame.transform.scale(img, (32, 16))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.distance = 5
        self.boost = False
        self.zaehler = 0

    def movement(self):

        if self.boost:
            self.distance = 10

            if self.zaehler >= 83:
                self.boost = False
        else:
            self.distance = 5

        self.rect.x += self.distance