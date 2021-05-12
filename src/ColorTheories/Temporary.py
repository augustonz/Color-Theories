import pygame
from ColorTheories.classes.Entity import Entity

class Temporary(pygame.sprite.Sprite):
    def __init__(self,pos,width,height,entity: Entity):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((width,height),pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        entity.render(self.image,int(width/2),int(height/2))

        self.rect = self.image.get_rect()
        self.pos=pos
        self.selected=False
        self.entity = entity

    def update(self):
        self.rect.update(self.pos,self.rect.size)

    def handleEvent(self,event):
        if event.type==pygame.MOUSEMOTION:
            if self.selected==True:   
                self.pos=(event.pos[0]-self.rect.width//2,event.pos[1]-self.rect.height//2)
        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.rect=pygame.Rect((0,0,0,0))
                self.kill()