import pygame
import tools

class Dragable():
    def __init__(self,pos,width,height,color):
        self.initialPos=pos
        self.image = pygame.surface.Surface((width,height),pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image,color,(int(width/2),int(height/2)),25)

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
                self.pos=(event.pos[0]-self.rect.width//2,event.pos[1]-self.rect.height//2)
                return True
        elif event.type==pygame.MOUSEMOTION:
            if self.selected==False:   
                self.isHover = self.rect.collidepoint(event.pos)
            else:
                self.pos=(event.pos[0]-self.rect.width//2,event.pos[1]-self.rect.height//2)
        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.rect=pygame.Rect((0,0,0,0))
                self.alive=False