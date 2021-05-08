import pygame
from tools import *
from constants import *
import constants
from classes.Color import Color
from Generator import Generator
from Temporary import Temporary

class Pallete():
    def __init__(self, level):

        level_difficulty = level['difficulty']
        keys = constants.colors
        self.colors = []
        colorList=Color.sorted([getattr(constants, keys[i]) for i in range(len(keys)) if getattr(constants, keys[i]).difficulty <= level_difficulty])        
        palleteHeight=800
        print((len(colorList)+2)//3*85+105)
        self.image = pygame.surface.Surface((700,palleteHeight))
        self.window = pygame.surface.Surface((200,400))
        self.window_rect = self.window.get_rect(topleft=(500,100))
        self.pickSound = load_sound('pick.wav',0.3)

        whiteBackground=pygame.surface.Surface((200,palleteHeight))
        whiteBackground.fill(pygame.Color('white'))
        self.image.blit(whiteBackground,(500,0))

        for i in range(len(colorList)):
            color = Generator((505+(i%3)*65,105+(i//3)*85),60,80,colorList[i])
            self.colors.append(color)

    def update(self):
        for color in self.colors:
            if color.alive:
                color.update()

    def draw(self):
        for color in self.colors:
            if color.alive:
                color.draw(self.image)
    
        subsurf = self.image.subsurface(self.window_rect) 
        return subsurf

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for color in self.colors:
                if (color.handleEvent(event)):
                    newColor = Temporary((event.pos[0]-30,event.pos[1]-30),60,60,color.color)
                    newColor.selected=True
                    self.pickSound.play()
                    return newColor
                    
        if event.type==pygame.MOUSEWHEEL:
                if (self.window.get_rect(topleft=(500,100)).collidepoint(pygame.mouse.get_pos())):
                    if self.window_rect.y>100 and event.y>0:
                        self.window_rect.y+=-10
                        for color in self.colors:
                            color.pos=(color.pos[0],color.pos[1]+10)
                    elif self.window_rect.y<self.image.get_height()-self.window_rect.height and event.y<0:
                        self.window_rect.y+=10
                        for color in self.colors:
                            color.pos=(color.pos[0],color.pos[1]-10)