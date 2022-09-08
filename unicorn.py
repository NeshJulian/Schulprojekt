#-------------------------------------------------------------------------------
# Name:        module1
# Author:      agoethel
# Created:     07.09.2022
# Copyright:   (c) agoethel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
class Unicorn(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.fullimage = pygame.image.load('img/unicorn.png')
        self.image = self.fullimage
        self.image_right = []

        for i in range(4):
            if i == 0:
                self.image_right.append(pygame.transform.scale(self.fullimage.subsurface(i, 0, 16, 16), (64, 64)))
            elif i == 3:
                self.image_right.append(pygame.transform.scale(self.fullimage.subsurface((i*16)+2, 0, 17, 16), (64, 64)))
            else:
                self.image_right.append(pygame.transform.scale(self.fullimage.subsurface((i*16)+1, 0, 17, 16), (64, 64)))

        self.frame_index = 0
        self.image = self.image_right[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.cal_y = self.rect.y
        self.step_Distance = 5
        self.direction = 0
        self.last_direction = self.direction
        self.clock = pygame.time.Clock()

    def updateImage(self):

        if self.frame_index != 4:
            self.image = self.image_right[self.frame_index]
            self.frame_index += 1
            if self.frame_index == 4:
                self.frame_index = 0

    def updatePosition(self):
        self.cal_y = self.cal_y + self.step_Distance * self.direction

        if self.cal_y >= 720:
            self.cal_y = 710

        if self.cal_y <= 30:
            self.cal_y = 35

        self.rect.y = self.cal_y

    def fly(self, upDown):
        self.direction = upDown
        self.last_direction = self.direction

    def update(self, zaehler):
        self.updatePosition()
        if zaehler >= 20:
            self.updateImage()






