import pygame
from Button import Button
from tools import *

class Message():
    def __init__(self,pos,text="Base text"):
        self.image = load_img('messageBackground.png')
        self.pos = pos
        self.text=text
        self.rect=self.image.get_rect()
        self.alive=True
        self.font= load_font('menu.otf',80)
        self.okButton = Button((360,350),80,80,"","menu.otf",self.close,"nextLevelMini.png")
        

    def close(self,a):
        return False

    def handleEvent(self,event):
        if (event.type==pygame.MOUSEBUTTONUP):
            return self.okButton.handleEvent(event)
        else:
            self.okButton.handleEvent(event)
            return True

    def display(self,surface):
        if (self.alive):
            surface.blit(self.image,self.pos)
            surface.blit(self.font.render(self.text,True,pygame.Color("black")),(300,150))
            surface.blit(self.okButton.image,self.okButton.pos)

