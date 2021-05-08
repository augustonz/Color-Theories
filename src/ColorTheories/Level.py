import pickle
from Button import Button
from Temporary import Temporary
from Generator import Generator
from Pallete import Pallete
from Tabela import Tabela
from Message import Message
from tools import *
import Menu
import levelSelect
import constants

running = True
level =""
end = True
Val=None
lives=3#Sistema de vida
def run(val):
    global Val
    Val=val
    screen = pygame.display.set_mode(screenResolution)

    #Loads resources
    background = load_img('background.png')
    fullHeart = load_img('heartFullMini.png')
    emptyHeart = load_img('heartEmptyMini.png')
    #Plays the beginning sound
    if (not pygame.mixer.music.get_busy()): 
        play_music('Game-Menu_Looping.wav')
    titleFont=load_font("title.ttf",66)
    textFont=load_font("menu.otf",48)
    mistake=load_sound('mistake.wav',0.2)
    failLevel=load_sound('failLevel.wav',0.2)
    completeLevel=load_sound('completeLevel.wav',0.2)
    
    #Menu options
    global level
    level = pygame.sprite.Group()
    temp = pygame.sprite.Group()

    pallete=Pallete(val)
    tabela = Tabela(val)
    winButton = Button((96,24),48,48,text="",font="menu.otf",img="menuBackMini.png",func=winLevel,args=int(val["num"])+1)
    level.add(winButton)

    def checkWin(val):
        global lives
        global Val
        global winLevel
        pygame.mixer.stop()
        if (tabela.checkWin()):
            completeLevel.play()
            winLevel(int(Val["num"])+1)
        else:
            lives-=1
            if lives>0:
                mistake.play()
            else:
                failLevel.play()

    checkWinButton = Button((150,470),300,92,text="Verificar resposta",font="menu.otf",img="menuButtonMini.png",func=checkWin)
    level.add(checkWinButton)
    menuButton = Button((24,24),48,48,text="",font="menu.otf",img="menuBackMini.png",func=backMenu)
    level.add(menuButton)

    def displayLives():
        for i in range(3):
            if (i+1)<=lives:
                screen.blit(fullHeart,(96+52*i,24))
            else:
                screen.blit(emptyHeart,(96+52*i,24))

    #Clock Speed
    clock = pygame.time.Clock()
    global running
    running=True
    selectedColor=None

    if "msg" in val:
        paused=True
        msg = Message((180,100),val['msg']['title'],val['msg']['content'])

        while paused:
            for event in pygame.event.get():
                paused = msg.handleEvent(event)
                if paused==None:paused=True
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            screen.blit(background,(0,0))
            displayLives()
            screen.blit(titleFont.render("Nível "+val['num'],True,pygame.Color("purple")),(316,0))
            screen.blit(tabela.display(),(100,100))
            screen.blit(pallete.draw(), (500, 100))
            level.update()
            level.draw(screen)
            msg.display(screen)

            pygame.display.update()
            
            clock.tick(60)
    
    while running:
        for event in pygame.event.get():
            for sprite in level.sprites():
                sprite.handleEvent(event)
            if "msg" in val: msg.handleEvent(event)
            pallete.handleEvent(event)
            tabela.handleEvent(event,selectedColor)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pallete.handleEvent(event)):
                    newColor=pallete.handleEvent(event)
                    selectedColor=newColor.color
                    level.add(newColor)
                        
            if event.type == pygame.MOUSEBUTTONUP:
                selectedColor=None

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        #Display objects on screen
        screen.blit(background,(0,0))
        screen.blit(titleFont.render("Nível "+val['num'],True,pygame.Color("purple")),(316,0))
        
        pallete.update()
        tabela.update()
        
        displayLives()

        screen.blit(tabela.display(),(100,100))
        screen.blit(pallete.draw(), (500, 100))

        level.update()
        level.draw(screen)

        pygame.display.update()
        
        clock.tick(60)

    global end
    end=True
    level.remove(checkWinButton)
    while True:
        for event in pygame.event.get():
            for sprite in level.sprites():
                sprite.handleEvent(event)

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        #Display objects on screen
        screen.blit(background,(0,0))
        screen.blit(titleFont.render("Nível "+val['num'],True,pygame.Color("purple")),(316,0))

        screen.blit(tabela.display(),(100,100))
        screen.blit(pallete.draw(), (500, 100))

        newBlock = load_img("square_mini.png")
        newBlock.blit(titleFont.render("Parabéns!",True,pygame.Color("purple")),(80,25))
        newBlock.blit(textFont.render("Revise sua resposta ou vá para o próximo nível.",True,pygame.Color("black")),(60,115))
        
        if end:
            screen.blit(newBlock, (200, 150))
        

        level.update()
        level.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

def winLevel(num):
    global running
    running=False
    global lives
    lives=3
    global level
    global Val
    with open(pickle_path(), 'rb') as fi:
        openLevels = pickle.load(fi)
    if (openLevels.count(Val['num'])==0):
        openLevels.append(int(Val['num']))
    
    with open(pickle_path(), 'wb') as fi:
        # dump your data into the file
        pickle.dump(openLevels, fi)
    
    def closeEnd(notUsed):
        global end
        end=False
        nextLevelButton.kill()
        stopButton.kill()
    
    nextLevelButton = Button((425,325),80,80,img="nextLevelMini.png",text="",font="menu.otf",func=goToLevel,args=num)
    stopButton = Button((275,325),80,80,img="stopButtonMini.png",text="",font="menu.otf",func=closeEnd,args=None)
    
    level.add(nextLevelButton)
    level.add(stopButton)



def backMenu(val):
    global running
    running=False
    global lives
    lives=3
    levelSelect.run()


def goToLevel(lvl):
    run(constants.levels[lvl-1])