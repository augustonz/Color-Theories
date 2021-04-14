import pygame
import tools

class Coins(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tools.load_img('background.png')
        self.rect = self.image.get_rect()