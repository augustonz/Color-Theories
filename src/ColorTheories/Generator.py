import pygame
from ColorTheories.tools import *

class Generator():
    def __init__(self,pos,width,height,color):
        self.initialPos=pos
        self.image = pygame.surface.Surface((width,height),pygame.SRCALPHA)
        self.image.fill((0,0,0,0))

        smallFont = load_font('Roboto-Thin.ttf',10)
        mediumFont = load_font('Roboto-Thin.ttf',15)
        bigFont = load_font('Roboto-Thin.ttf',20)
        
        smallWidth=smallFont.size(color.name)[0]
        mediumWidth=mediumFont.size(color.name)[0]
        bigWidth=bigFont.size(color.name)[0]
        
        if bigWidth<60:
            self.image.blit(bigFont.render(color.name,False,pygame.Color('black')),(30-bigWidth//2,0))
        elif mediumWidth<60:
            self.image.blit(mediumFont.render(color.name,False,pygame.Color('black')),(30-mediumWidth//2,5))
        else:
            self.image.blit(smallFont.render(color.name,False,pygame.Color('black')),(30-smallWidth//2,10))
        
        pygame.draw.circle(self.image,pygame.Color('black'),(int(width/2),50),26)
        pygame.draw.circle(self.image,tuple(color),(int(width/2),50),24)
        
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