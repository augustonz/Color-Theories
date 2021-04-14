import pygame
import tools

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

    def click(self,target):
        pos = pygame.mouse.get_pos()
