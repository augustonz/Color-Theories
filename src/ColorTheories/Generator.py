import pygame
import tools

class Generator():
    def __init__(self,pos,width,height,color):
        self.initialPos=pos
        self.image = pygame.surface.Surface((width,height),pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image,pygame.Color('black'),(int(width/2),int(height/2)),26)
        pygame.draw.circle(self.image,color,(int(width/2),int(height/2)),24)
        
        self.rect = self.image.get_rect()
        self.pos=pos
        self.offsetX=0
        self.offsetY=0

        self.isHover=False
        self.selected=False
        self.color = color
        self.alive=True
        
    def update(self):
        self.rect.update(self.pos,self.rect.size)

    def draw(self,surface):
        surface.blit(self.image,self.initialPos)

    def handleEvent(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.selected=True
                return True