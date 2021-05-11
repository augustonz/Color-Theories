import pygame
from ColorTheories.Button import Button
from ColorTheories.tools import *

class Message():
    def __init__(self,pos,title,text="Base text"):
        self.image = load_img('messageBackground.png')
        self.pos = pos
        self.title = title
        self.text=text
        self.rect=self.image.get_rect()
        self.alive=True
        self.title_font = load_font('menu.otf',120)
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

    def centralized(self, h, text):
        return text.get_rect(center=(pygame.display.Info().current_w/2, h))

    def display(self,surface):
        if (self.alive):
            title_render = self.title_font.render(self.title,True,pygame.Color("black"))
            content_render = self.font.render(self.text,True,pygame.Color("black"))
            content_text: str = self.text
            surface.blit(self.image,self.pos)
            surface.blit(title_render,self.centralized(175, title_render))
            # content_wrapper_width
            # pygame.draw.line(pygame.display.get_surface(), (0,0,0,255), (250, 230), (530, 230))
            rect = pygame.Rect((pygame.display.Info().current_w/2, 230), (280, content_render.get_rect().height))
            offset = 0
            # wrapping
            while content_text:
                i = 1
                while self.font.size(content_text[:i])[0] < rect.width and i < len(content_text):
                    i += 1

                if i < len(content_text): 
                    i = content_text.rfind(" ", 0, i) + 1 
                
                piece_render = self.font.render(content_text[:i], True, pygame.Color("black"))
                surface.blit(piece_render, self.centralized(230+offset, piece_render))
                offset += 30
                content_text = content_text[i:]
            surface.blit(self.okButton.image,self.okButton.pos)

