import pygame
import tools

class Button(pygame.sprite.Sprite):
    def __init__(self,pos,width,height,text,func):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((width,height))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.update(pos,(width,height))
        self.text = text
        self.func = func
        self.isHover=False

    def isClicked(self,pos):
        if self.rect.collidepoint(pos):
            self.func(0.1)

    def update(self):
        if self.isHover:
            self.image.fill((200,200,200))
        else:
            self.image.fill((100,100,100))
        

    def setHover(self,pos):
        self.isHover = self.rect.collidepoint(pos)
    
