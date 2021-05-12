from typing import List
import pygame
from ColorTheories.tools import *
from ColorTheories.constants import *
from ColorTheories import constants
from ColorTheories.Generator import Generator
from ColorTheories.Temporary import Temporary

class Pallete():
    def __init__(self, level):

        level_difficulty = level['difficulty']
        keys = constants.entities
        self.entities: list[Generator] = []
        entity_list: list[Entity] = [getattr(constants, keys[i]) for i in range(len(keys)) if getattr(constants, keys[i]).difficulty <= level_difficulty]
        palleteHeight=800
        self.image = pygame.surface.Surface((700,palleteHeight))
        self.window = pygame.surface.Surface((200,400))
        self.window_rect = self.window.get_rect(topleft=(500,100))
        self.pickSound = load_sound('pick.wav',0.3)

        whiteBackground=pygame.surface.Surface((200,palleteHeight))
        whiteBackground.fill(pygame.Color('white'))
        self.image.blit(whiteBackground,(500,0))

        for i in range(len(entity_list)):
            entity = Generator((505+(i%3)*65,105+(i//3)*85),60,80,entity_list[i])
            self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            if entity.alive:
                entity.update()

    def draw(self):
        for entity in self.entities:
            if entity.alive:
                entity.draw(self.image)
    
        subsurf = self.image.subsurface(self.window_rect) 
        return subsurf

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for entity in self.entities:
                if (entity.handleEvent(event)):
                    newEntity = Temporary((event.pos[0]-30,event.pos[1]-30),60,60,entity.entity)
                    newEntity.selected=True
                    self.pickSound.play()
                    return newEntity
                    
        if event.type==pygame.MOUSEWHEEL:
                if (self.window.get_rect(topleft=(500,100)).collidepoint(pygame.mouse.get_pos())):
                    if self.window_rect.y>100 and event.y>0:
                        self.window_rect.y+=-10
                        for entity in self.entities:
                            entity.pos=(entity.pos[0],entity.pos[1]+10)
                    elif self.window_rect.y<self.image.get_height()-self.window_rect.height and event.y<0:
                        self.window_rect.y+=10
                        for entity in self.entities:
                            entity.pos=(entity.pos[0],entity.pos[1]-10)