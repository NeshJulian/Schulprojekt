import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self, imgpath):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imgpath)
        self.image = pygame.transform.scale(image, (image.get_width(), 1500))
        self.rect = self.image.get_rect()

        if imgpath == 'background/Hintergrund3.png':
            self.rect.center = (-550, 0)
        else:
            self.rect.center = (-550, 0)

    def update(self):
        if self.rect.x < self.image.get_rect().x:
            self.rect.x += 1


