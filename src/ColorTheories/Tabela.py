import pygame
from tools import *


class Tabela():
    def __init__(self,level):
        columns = level['columns']
        rows = level['rows']
        self.win = level['win']
        self.image=pygame.surface.Surface(((len(columns)+1)*60,(len(rows)+1)*60))
        self.image.fill((255,255,255))
        self.respostas = [[None]*len(rows) for i in range(len(columns))]
        self.rects = [[0]*len(rows) for i in range(len(columns))]

        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((60,60))
                surface.fill((255,255,255))
                rect=surface.get_rect(topleft=(60*(i+1)+1,60*(j+1)+1))
                self.image.blit(surface,(60*(i+1),60*(j+1)))
                self.rects[i][j] = rect

        for i in range(len(columns)+2):
            line = pygame.surface.Surface((1,(len(rows)+1)*60))
            line.fill((0,0,0))
            if i==len(columns)+1:
                self.image.blit(line,(i*60-1,0))
            else:
                self.image.blit(line,(i*60,0))
            
            if i<len(columns):
                pygame.draw.circle(self.image,columns[i],(30,60*(i+1)+30),25)

        for i in range(len(rows)+2):
            line = pygame.surface.Surface(((len(columns)+1)*60,1))
            line.fill((0,0,0))
            if i==len(rows)+1:
                self.image.blit(line,(0,i*60-1))
            else:
                self.image.blit(line,(0,i*60))
            if i<len(rows):
                pygame.draw.circle(self.image,rows[i],(60*(i+1)+30,30),25)
        
        self.rect=self.image.get_rect()

    def update(self):
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                if self.respostas[i][j]!=None:
                    pygame.draw.circle(self.image,pygame.Color('black'),(60*(i+1)+30,60*(j+1)+30),26)
                    self.rects[i][j] = pygame.draw.circle(self.image,self.respostas[i][j],(60*(i+1)+30,60*(j+1)+30),24)
                else:
                    surface = pygame.Surface((58,58))
                    surface.fill((255,255,255))
                    self.image.blit(surface,(60*(i+1)+1,60*(j+1)+1))

    def display(self):
        return self.image

    def getTabela(self):
        Str=""
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[0])):
                Str+=str(self.respostas[i][j])
            Str+="\n"
        return Str
        
    def checkWin(self):
        return self.respostas==self.win
    def handleEvent(self,event,selected):
        if event.type==pygame.MOUSEBUTTONUP:
            for i in range(len(self.respostas)):
                for j in range(len(self.respostas[i])):
                    if (self.rects[i][j]!=None):
                        if self.rects[i][j].collidepoint((event.pos[0]-100,event.pos[1]-100)):
                            self.respostas[i][j]=selected
        else:
            pass