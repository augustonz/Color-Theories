import pygame
from ColorTheories.tools import *
from ColorTheories.classes.Color import Color

class Tabela():
    def __init__(self,level):
        columns = level['columns']
        rows = level['rows']
        self.columns = columns
        self.rows = rows
        self.operator = level['arithmetic_operation']
        self.win_condition = level['condition']
        self.win = level['win']
        self.unveiled_cells = level['unveiled_cells']
        self.image=pygame.surface.Surface(((len(columns)+1)*60,(len(rows)+1)*60))
        self.image.fill((255,255,255))
        self.respostas = [[None]*len(columns) for i in range(len(rows))]
        self.rects = [[0]*len(columns) for i in range(len(rows))]
        self.errors = []

        self.putSound = load_sound("put.wav",0.5)
        self.font = load_font("menu.otf", 140)

        self.operator_symbol = self.font.render(level['operation_symbol'],True,pygame.Color("black"))
        if level['operation_symbol']=='≠':
            notEquals=load_img('diferenteMini.png')
            self.image.blit(notEquals, (15,15))
        else:
            self.image.blit(self.operator_symbol, (15,-10))
        
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((60,60))
                surface.fill((255,255,255))
                rect=surface.get_rect(topleft=(60*(j+1)+1,60*(i+1)+1))
                self.image.blit(surface,(60*(i+1),60*(j+1)))
                self.rects[i][j] = rect

        if self.unveiled_cells and self.win_condition == 'arbitrary':
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
                pygame.draw.circle(self.image,pygame.Color('black'),(30,60*(i+1)+30),26)
                pygame.draw.circle(self.image,tuple(rows[i]),(30,60*(i+1)+30),24)

        for i in range(len(rows)+2):
            line = pygame.surface.Surface(((len(columns)+1)*60,1))
            line.fill((0,0,0))
            if i==len(rows)+1:
                self.image.blit(line,(0,i*60-1))
            else:
                self.image.blit(line,(0,i*60))
            if i<len(columns) and columns[i]!=None:
                pygame.draw.circle(self.image,pygame.Color('black'),(60*(i+1)+30,30),26)
                pygame.draw.circle(self.image,tuple(columns[i]),(60*(i+1)+30,30),24)
        
        self.rect=self.image.get_rect()
        
        # ---------------
        # debug_type = 'value'
        # if (level['condition'] == 'math'):
        #     win_condition = [[None]*len(columns) for i in range(len(rows))]
        #     for i in range(len(self.columns)):
        #         for j in range(len(self.rows)):
        #             win_condition[j][i] = self.operator(self.rows[j], self.columns[i])
        #     print("Win: ")
        #     for i in range(len(win_condition)):
        #         for j in range(len(win_condition[0])):
        #             if debug_type == 'value': print(win_condition[i][j].red, win_condition[i][j].green, win_condition[i][j].blue, end=" | ")
        #             else: print(win_condition[i][j].name, end=" | ")
        #         print()
        # else:
        #     print("Win: ")
        #     for i in range(len(self.win)):
        #         for j in range(len(self.win[0])):
        #             if debug_type == 'value': print(self.win[i][j].red, self.win[i][j].green, self.win[i][j].blue, end=" | ")
        #             else: print(self.win[i][j].name, end=" | ")
        #         print()
        # # ---------------
            
    def update(self):
        for i in range(len(self.respostas)):
            for j in range(len(self.respostas[i])):
                surface = pygame.Surface((58,58))
                surface.fill((255,255,255))
                self.image.blit(surface,(60*(j+1)+1,60*(i+1)+1))
                if self.respostas[i][j]!=None:
                    pygame.draw.circle(self.image,pygame.Color('black'),(60*(j+1)+30,60*(i+1)+30),26)
                    self.rects[i][j] = pygame.draw.circle(self.image,tuple(self.respostas[i][j]),(60*(j+1)+30,60*(i+1)+30),24)

                if self.errors.count((i,j))>0:
                    surface = pygame.Surface((58,58),pygame.SRCALPHA)
                    surface.fill((255,0,0,128))
                    self.image.blit(surface,(60*(j+1)+1,60*(i+1)+1))

        self.image.blit(self.operator_symbol, (15,-10))

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
        if self.win_condition == 'math':
            for i in range(len(self.respostas)):
                for j in range(len(self.respostas[0])):
                    if self.respostas[i][j] != self.operator(self.rows[i], self.columns[j]):
                        self.errors.append((i,j))
                        won=False
        else:
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