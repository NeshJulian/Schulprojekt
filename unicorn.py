#-------------------------------------------------------------------------------
# Name:        module1
# Author:      agoethel
# Created:     07.09.2022
# Copyright:   (c) agoethel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
class Unicorn(pygame.sprite.Sprite):


    def __init__(self, bg_width, screen_width):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/unicorn.png')
        self.image      = pygame.transform.scale2x(image)
        self.BG_WIDTH       = bg_width
        self.SCREEN_WIDTH   = screen_width
        self.camerapos      = [0,0]
        self.frame_index    = 0
        self.rect           = self.image.get_rect()
        self.calc_x         = self.rect.x
        self.direction      = 0
        self.last_direction = self.direction
        self.SINGLESTEP_X   = 4
        self.rect_width     = []


    def update_position(self):
        self.calc_x += (self.SINGLESTEP_X * self.direction)
        if self.calc_x < 0 :
            self.calc_x=0
        elif  self.calc_x >= 800 - self.rect.width:
            self.calc_x = 800 - self.rect.width
        self.rect.x = self.calc_x


