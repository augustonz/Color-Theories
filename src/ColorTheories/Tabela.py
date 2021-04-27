import pygame
from tools import *

class Tabela():
    def __init__(self,level):
        columns = level['columns']
        rows = level['rows']
        self.columns = columns
        self.rows = rows
        self.operator = level['arithmetic_operation']
        self.win_condition = level['condition']
        self.win = level['win']
        self.image=pygame.surface.Surface(((len(columns)+1)*60,(len(rows)+1)*60))
        self.image.fill((255,255,255))
        self.respostas = [[None]*len(rows) for i in range(len(columns))]
        self.rects = [[0]*len(rows) for i in range(len(columns))]
        self.putSound = load_sound("put.wav",0.5)

        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((60,60))
                surface.fill((255,255,255))
                rect=surface.get_rect(topleft=(60*(j+1)+1,60*(i+1)+1))
                self.image.blit(surface,(60*(i+1),60*(j+1)))
                self.rects[i][j] = rect

        for i in range(len(columns)+2):
            line = pygame.surface.Surface((1,(len(rows)+1)*60))
            line.fill((0,0,0))
            if i==len(columns)+1:
                self.image.blit(line,(i*60-1,0))
            else:
                self.image.blit(line,(i*60,0))
            
            if i<len(columns) and rows[i]!=None:
                pygame.draw.circle(self.image,pygame.Color('black'),(30,60*(i+1)+30),26)
                pygame.draw.circle(self.image,tuple(rows[i]),(30,60*(i+1)+30),24)

        for i in range(len(rows)+2):
            line = pygame.surface.Surface(((len(rows)+1)*60,1))
            line.fill((0,0,0))
            if i==len(rows)+1:
                self.image.blit(line,(0,i*60-1))
            else:
                self.image.blit(line,(0,i*60))
            if i<len(rows) and columns[i]!=None:
                pygame.draw.circle(self.image,pygame.Color('black'),(60*(i+1)+30,30),26)
                pygame.draw.circle(self.image,tuple(columns[i]),(60*(i+1)+30,30),24)
        
        self.rect=self.image.get_rect()

        # DEBUG: Show win condition in console
        # ---------------
        if (level['condition'] == 'math'):
            win_condition = [[None]*len(rows) for i in range(len(columns))]
            for i in range(len(self.columns)):
                for j in range(len(self.rows)):
                    win_condition[i][j] = self.operator(self.columns[j], self.rows[i])
            print("Win: ")
            for i in range(len(win_condition)):
                for j in range(len(win_condition)):
                    print(win_condition[i][j].red, win_condition[i][j].green, win_condition[i][j].blue, end=" | ")
                print()
        else:
            print("Win: ")
            for i in range(len(self.win)):
                for j in range(len(self.win[0])):
                    print(self.win[i][j].red, self.win[i][j].green, self.win[i][j].blue, end=" | ")
                print()
        # ---------------
            
    def update(self):
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                if self.respostas[i][j]!=None:
                    pygame.draw.circle(self.image,pygame.Color('black'),(60*(j+1)+30,60*(i+1)+30),26)
                    self.rects[i][j] = pygame.draw.circle(self.image,tuple(self.respostas[i][j]),(60*(j+1)+30,60*(i+1)+30),24)
                else:
                    surface = pygame.Surface((58,58))
                    surface.fill((255,255,255))
                    self.image.blit(surface,(60*(j+1)+1,60*(i+1)+1))

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
        if self.win_condition == 'math':
            for i in range(len(self.respostas)):
                for j in range(len(self.respostas[0])):
                    won = won and (self.respostas[i][j] == self.operator(self.rows[i], self.columns[j]))
        else:
            won = self.respostas == self.win
        return won

    def handleEvent(self,event,selected):
        if event.type==pygame.MOUSEBUTTONUP:
            for i in range(len(self.respostas)):
                for j in range(len(self.respostas[0])):
                    if self.rects[i][j].collidepoint((event.pos[0]-100,event.pos[1]-100)):
                        self.putSound.play()
                        self.respostas[i][j]=selected
        else:
            pass