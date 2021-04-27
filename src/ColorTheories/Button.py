import pygame
from tools import *

class Button(pygame.sprite.Sprite):
    def __init__(self,pos,width,height,text="Base text",font=None,func=None,img=None,args=None):
        pygame.sprite.Sprite.__init__(self)
        if (img):
            self.image=load_img(img)
        else:
            self.image = pygame.surface.Surface((width,height))
            self.image.fill((100,100,100))
        menuFont = load_font(font,height+20)
        self.text=text
        textWidth,textHeight=menuFont.size(text)
        self.image.blit(menuFont.render(text,True,pygame.Color("black")),(int((width-textWidth)/2),8))
        
        self.pos=pos
        self.rect = self.image.get_rect()
        self.rect.update(self.pos,(width,height))

        self.func = func
        self.isHover=False
        self.start=False
        self.args=args
        
    def update(self):
        if self.isHover:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(200)
        
    def handleEvent(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos) and self.func:
                self.start=True
            else:
                self.start=False
        elif event.type==pygame.MOUSEMOTION:
            self.isHover = self.rect.collidepoint(event.pos)
        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
            if self.rect.collidepoint(event.pos) and self.func:
                if self.start:
                    return self.func(self.args)
        else:
            pass