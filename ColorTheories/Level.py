from Button import Button
from tools import *
from Temporary import Temporary
from Generator import Generator
from Pallete import Pallete
from Tabela import Tabela
import Menu
import levelSelect

running = True

def run(val):

    screen = pygame.display.set_mode(screenResolution)

    #Loads images
    background = load_img('background.png')
    
    #Plays the beginning sound
    if (not pygame.mixer.music.get_busy()): 
        play_music('Game-Menu_Looping.wav')

    titleFont=load_font("title.ttf",66)

    #Menu options
    level = pygame.sprite.Group()
    temp = pygame.sprite.Group()
    
    pallete=Pallete()
    tabela = Tabela(val['rows'],val['columns'])

    menuButton = Button((24,24),48,48,text="",font="menu.otf",img="menuBackMini.png",func=backMenu)
    level.add(menuButton)

    #Clock Speed
    clock = pygame.time.Clock()
    global running
    running=True
    selectedColor=None

    while running:
        for event in pygame.event.get():
            for sprite in level.sprites():
                sprite.handleEvent(event)
            
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
        screen.blit(titleFont.render("Level "+val['num'],True,pygame.Color("purple")),(316,0))
        
        pallete.update()
        tabela.update()
        screen.blit(tabela.display(),(100,100))
        screen.blit(pallete.draw(), (500, 100))

        level.update()
        level.draw(screen)

        pygame.display.update()
        clock.tick(60)

def backMenu(val):
    global running
    running=False
    levelSelect.run()