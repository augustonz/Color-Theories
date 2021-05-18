import pygame
from ColorTheories.classes.Entity import Entity
from ColorTheories.tools import *

class Tabela():
    def __init__(self,level):
        columns: list[Entity] = level['columns']
        rows: list[Entity] = level['rows']
        self.columns = columns
        self.rows = rows
        self.win = level['win']
        self.unveiled_cells = level['unveiled_cells']
        self.image=pygame.surface.Surface(((len(columns)+1)*60,(len(rows)+1)*60))
        self.image.fill((255,255,255))
        self.respostas = [[None]*len(columns) for i in range(len(rows))]
        self.rects = [[0]*len(columns) for i in range(len(rows))]
        self.errors = []

        self.putSound = load_sound("put.wav",0.5)
        self.font = load_font("menu.otf", 140)
        
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((60,60))
                surface.fill((255,255,255))
                rect=surface.get_rect(topleft=(60*(j+1)+1,60*(i+1)+1))
                self.image.blit(surface,(60*(i+1),60*(j+1)))
                self.rects[i][j] = rect

        if self.unveiled_cells:
            for cell in self.unveiled_cells:
                self.respostas[cell[0]][cell[1]] = self.win[cell[0]][cell[1]]

        for i in range(len(columns)+2):
            line = pygame.surface.Surface((1,(len(rows)+1)*60))
            line.fill((0,0,0))
            if i==len(columns)+1:
                self.image.blit(line,(i*60-1,0))
            else:
                self.image.blit(line,(i*60,0))
            
            if i<len(rows) and rows[i]!=None:
                rows[i].render(self.image, 0,60*(i+1))

        for i in range(len(rows)+2):
            line = pygame.surface.Surface(((len(columns)+1)*60,1))
            line.fill((0,0,0))
            if i==len(rows)+1:
                self.image.blit(line,(0,i*60-1))
            else:
                self.image.blit(line,(0,i*60))
            if i<len(columns) and columns[i]!=None:
                columns[i].render(self.image, 60*(i+1),0)
        
        self.rect=self.image.get_rect()
        operation = load_font('FiraCode-Retina.ttf', 30)
        self.image.blit(operation.render('*', True, 'black'), (24, 15))
        
        # ---------------
        print("Win: ")
        for i in range(len(self.win)):
            for j in range(len(self.win[0])):
                print(self.win[i][j].name, end=" | ")
            print()
        # # ---------------
            
    def update(self):
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((58,58))
                surface.fill((255,255,255))
                self.image.blit(surface,(60*(j+1)+1,60*(i+1)+1))
                if self.respostas[i][j]!=None:
                    self.rects[i][j] = self.respostas[i][j].render(self.image, 60*(j+1),60*(i+1))

                if self.errors.count((i,j))>0:
                    surface = pygame.Surface((58,58),pygame.SRCALPHA)
                    surface.fill((255,0,0,128))
                    self.image.blit(surface,(60*(j+1)+1,60*(i+1)+1))

    def resetErrors(self):
        self.errors=[]

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
        won = True
        self.resetErrors()
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[0])):
                if self.respostas[i][j] != self.win[i][j]:
                    self.errors.append((i,j))
                    won=False
        return won

    def handleEvent(self,event,selected):
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            for i in range(len(self.respostas)):
                for j in range(len(self.respostas[0])):
                    if self.rects[i][j].collidepoint((event.pos[0]-100,event.pos[1]-100)):
                        self.putSound.play()
                        self.respostas[i][j]=selected
        else:
            pass