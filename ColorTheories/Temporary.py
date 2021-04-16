import pygame
import tools

class Temporary(pygame.sprite.Sprite):
    def __init__(self,pos,width,height,color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((width,height),pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image,pygame.Color('black'),(int(width/2),int(height/2)),26)
        pygame.draw.circle(self.image,color,(int(width/2),int(height/2)),24)

        self.rect = self.image.get_rect()
        self.pos=pos
        self.selected=False
        self.color = color

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